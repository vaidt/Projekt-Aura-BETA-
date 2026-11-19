#!/usr/bin/env python3
"""Offline SSHSIG exact-byte gate candidate. NON-CONSTITUTIVE. No network."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys

RECORD = "AURA-M1-SSHSIG-POSITIVE-GATE-CANDIDATE/1"
HEXDIGEST = re.compile(r"[0-9a-f]{64}\Z")
SHA1 = re.compile(r"[0-9a-f]{40}\Z")
MAX_MANIFEST = 32768
MAX_MESSAGE = 8 * 1024 * 1024
MAX_CONTROL = 32768
MAX_STDERR = 1200


class GateError(Exception):
    pass


def must_sha256(value: str, label: str) -> str:
    if not isinstance(value, str) or not HEXDIGEST.fullmatch(value):
        raise GateError(f"{label}: expected exact lowercase SHA-256")
    return value


def strict_pairs(pairs: list[tuple[str, object]]) -> dict:
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise GateError(f"duplicate JSON key: {key}")
        obj[key] = value
    return obj


def strict_constant(value: str):
    raise GateError(f"non-finite JSON number: {value}")


def read_bounded(path: Path, limit: int) -> bytes:
    if path.is_symlink():
        raise GateError(f"symlink prohibited: {path.name}")
    s = path.lstat()
    if not stat.S_ISREG(s.st_mode):
        raise GateError(f"non-regular input: {path.name}")
    if s.st_size > limit:
        raise GateError(f"input too large: {path.name}")
    with path.open("rb") as f:
        a = os.fstat(f.fileno())
        out = f.read(limit + 1)
        b = os.fstat(f.fileno())
    if len(out) > limit or a.st_size != len(out) or (a.st_dev, a.st_ino, a.st_mtime_ns, a.st_size) != (b.st_dev, b.st_ino, b.st_mtime_ns, b.st_size):
        raise GateError(f"unstable or oversized read: {path.name}")
    return out


def confined(root: Path, rel: str) -> Path:
    if not isinstance(rel, str) or not rel or "\\" in rel or "\x00" in rel:
        raise GateError("invalid manifest relative path")
    posix = PurePosixPath(rel)
    if posix.is_absolute() or any(p in ("", ".", "..") for p in posix.parts) or str(posix) != rel:
        raise GateError("non-canonical manifest relative path")
    candidate = root
    for part in posix.parts:
        candidate = candidate / part
        if candidate.is_symlink():
            raise GateError("symlink in input path")
    if not candidate.resolve().is_relative_to(root):
        raise GateError("path escapes root")
    return candidate


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def load_manifest(root: Path, relpath: str, trusted_hash: str) -> dict:
    p = confined(root, relpath)
    raw = read_bounded(p, MAX_MANIFEST)
    if hashlib.sha256(raw).hexdigest() != trusted_hash:
        raise GateError("external manifest pin mismatch")
    try:
        data = json.loads(raw.decode("utf-8"), object_pairs_hook=strict_pairs, parse_constant=strict_constant)
    except (UnicodeError, ValueError) as exc:
        raise GateError("manifest is not valid strict UTF-8 JSON") from exc
    if not isinstance(data, dict) or data.get("record_id") != "BETA-M1-SSHSIG-VERIFICATION-MANIFEST-2026-10-20":
        raise GateError("unexpected M1 fixture manifest contract")
    return data


def load_entry(root: Path, obj: dict) -> tuple[dict, bytes, Path, Path]:
    if not isinstance(obj, dict):
        raise GateError("invalid fixture entry")
    field_names = (
        ("message_path", "message_blob_sha", MAX_MESSAGE),
        ("signature_path", "signature_blob_sha", MAX_CONTROL),
        ("allowed_signers_path", "allowed_signers_blob_sha", MAX_CONTROL),
    )
    info: dict = {}
    got = {}
    paths = {}
    for pfield, hashfield, maximum in field_names:
        pin = obj.get(hashfield)
        if not isinstance(pin, str) or not SHA1.fullmatch(pin):
            raise GateError(f"invalid pinned Git blob SHA: {hashfield}")
        relative_path = obj.get(pfield)
        path = confined(root, relative_path)
        content = read_bounded(path, maximum)
        if git_blob_sha1(content) != pin:
            raise GateError(f"Git blob pin mismatch: {pfield}")
        info[pfield] = {"path": relative_path, "git_blob_sha1": pin, "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}
        got[pfield] = content
        paths[pfield] = path
    return info, got["message_path"], paths["signature_path"], paths["allowed_signers_path"]


def openssh_verify(message: bytes, signature: Path, signers: Path, identity: str, namespace: str) -> tuple[bool, str]:
    if not shutil.which("ssh-keygen"):
        raise GateError("OpenSSH ssh-keygen is unavailable")
    args = ["ssh-keygen", "-Y", "verify", "-f", str(signers), "-I", identity, "-n", namespace, "-s", str(signature)]
    process = subprocess.run(args, input=message, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=12, check=False)
    if process.returncode == 0:
        return True, "OpenSSH SSHSIG verification succeeded"
    return False, f"OpenSSH SSHSIG verification failed (exit={process.returncode})"


def evaluate(args: argparse.Namespace) -> dict:
    root = Path(args.root).resolve(strict=True)
    if not root.is_dir() or not root.is_absolute():
        raise GateError("invalid root directory")
    trusted = {k: must_sha256(getattr(args, k), k) for k in (
        "trusted_manifest_sha256",
        "trusted_historical_message_sha256",
        "trusted_current_message_sha256",
        "trusted_historical_signers_sha256",
        "trusted_current_signers_sha256",
    )}
    if args.expected_source_repository != "vaidt/aura-specification":
        raise GateError("unrecognized source repository identity")
    if args.expected_source_commit != "991274eed57d5b3308b0607feeb4d01e6a485974":
        raise GateError("unrecognized pinned M1 source commit")
    if args.expected_namespace != "aura-governance" or args.expected_identity != "kontakt.vaidt@gmail.com":
        raise GateError("unrecognized SSHSIG namespace/identity policy")
    manifest = load_manifest(root, args.manifest, trusted["trusted_manifest_sha256"])
    if manifest.get("source_repository") != args.expected_source_repository or manifest.get("source_current_commit") != args.expected_source_commit:
        raise GateError("source repository or commit mismatch")
    if manifest.get("namespace") != args.expected_namespace or manifest.get("identity") != args.expected_identity:
        raise GateError("manifest SSHSIG identity/namespace mismatch")
    historical, h_msg, h_sig, h_signers = load_entry(root, manifest.get("historical"))
    current, c_msg, c_sig, c_signers = load_entry(root, manifest.get("current"))
    comparisons = [
        (historical["message_path"]["sha256"], trusted["trusted_historical_message_sha256"], "historical message"),
        (current["message_path"]["sha256"], trusted["trusted_current_message_sha256"], "current message"),
        (historical["allowed_signers_path"]["sha256"], trusted["trusted_historical_signers_sha256"], "historical signers"),
        (current["allowed_signers_path"]["sha256"], trusted["trusted_current_signers_sha256"], "current signers"),
    ]
    for actual, expected, label in comparisons:
        if actual != expected:
            raise GateError(f"externally supplied SHA-256 pin mismatch: {label}")
    h_ok, h_result = openssh_verify(h_msg, h_sig, h_signers, args.expected_identity, args.expected_namespace)
    result = {"schema": RECORD, "mode": args.mode, "scope": "EXACT_BYTES_SSHSIG_TECHNICAL_ONLY", "normative_effect": "NONE", "manifest_sha256": trusted["trusted_manifest_sha256"], "source_repository": args.expected_source_repository, "source_commit": args.expected_source_commit, "historical": {"signature_valid": h_ok, "message_sha256": historical["message_path"]["sha256"], "result": h_result}, "current": {"verification_performed": False, "message_sha256": current["message_path"]["sha256"]}, "status": "FAIL"}
    if not h_ok:
        result["reason"] = "historical positive-control signature failed"
        return result
    if args.mode == "historical-reference":
        result["status"] = "PASS_HISTORICAL_SSHSIG_BOUNDED"
        return result
    c_ok, c_result = openssh_verify(c_msg, c_sig, c_signers, args.expected_identity, args.expected_namespace)
    result["current"].update({"verification_performed": True, "signature_valid": c_ok, "result": c_result})
    result["status"] = "PASS_CRYPTO_ONLY_NON_CONSTITUTIVE" if c_ok else "BLOCKED_CURRENT_EXACTBYTE_SIGNATURE_MISMATCH"
    return result


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", required=True)
    p.add_argument("--manifest", default="tests/fixtures/m1/SSHSIG_INPUT_MANIFEST.json")
    p.add_argument("--mode", choices=("historical-reference", "current-strict"), required=True)
    for key in ("trusted-manifest-sha256", "trusted-historical-message-sha256", "trusted-current-message-sha256", "trusted-historical-signers-sha256", "trusted-current-signers-sha256", "expected-source-repository", "expected-source-commit", "expected-namespace", "expected-identity"):
        p.add_argument("--"+key, required=True)
    return p


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    try:
        result = evaluate(args)
    except (GateError, OSError, subprocess.TimeoutExpired) as e:
        result = {"schema": RECORD, "status": "FAIL_CLOSED", "normative_effect": "NONE", "reason": str(e)[:MAX_STDERR]}
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=True))
    return 0 if result["status"] in ("PASS_CRYPTO_ONLY_NON_CONSTITUTIVE", "PASS_HISTORICAL_SSHSIG_BOUNDED") else 2


if __name__ == "__main__":
    sys.exit(main())
