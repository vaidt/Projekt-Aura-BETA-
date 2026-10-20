#!/usr/bin/env python3

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

BETA = Path(__file__).resolve().parents[1]
SOURCE = BETA.parent / "aura-specification"

GENESIS_COMMIT = "89de18afc41e79afc0259116df861928dfae8cba"
RELATED_COMMIT = "991274eed57d5b3308b0607feeb4d01e6a485974"

MANIFEST_PATH = BETA / "docs/governance/KEY_PROVENANCE_MANIFEST.json"
RECORD_PATH = BETA / "evidence/registry/EVID-KEY-PROVENANCE-001.json"

ARTIFACTS = [
    ("GENESIS_DECLARATION", GENESIS_COMMIT, "GENESIS_DECLARATION.txt"),
    ("GENESIS_SIGNATURE", GENESIS_COMMIT, "GENESIS_DECLARATION.txt.sig"),
    ("AUTHORITY_BINDING_RECORD", RELATED_COMMIT,
     "AUTHORITY_BINDING_RECORD_v1.1.md"),
    ("AUTHORITY_BINDING_SIGNATURE", RELATED_COMMIT,
     "AUTHORITY_BINDING_RECORD_v1.1.md.sig"),
    ("P008_RATIFICATION_RECORD", RELATED_COMMIT,
     "AURA_P008_RATIFICATION_RECORD_v1.0.md"),
    ("P008_SIGNATURE", RELATED_COMMIT,
     "AURA_P008_RATIFICATION_RECORD_v1.0.md.sig"),
    ("M1_CLOSURE_RECORD", RELATED_COMMIT,
     "AURA_M1_CLOSURE_RECORD_v1.0.md"),
    ("M1_CLOSURE_SIGNATURE", RELATED_COMMIT,
     "AURA_M1_CLOSURE_RECORD_v1.0.md.sig"),
]

EXPECTED = {
    "GENESIS_DECLARATION": {
        "sha256": (
            "6b5a4c4eaa258eef27452fe6a2f2d752"
            "484ae6c88968a039b0b40ca0ac8f2bb6"
        ),
        "git_blob_sha1": "9c19e97270a4539ea7788a0553db2a800a573c44",
    },
    "GENESIS_SIGNATURE": {
        "git_blob_sha1": "82f114a695c5b30094500452c8770cb4d6d572f5",
    },
}

def git(*args, binary=False):
    result = subprocess.run(
        ["git", "-C", str(SOURCE), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    if binary:
        return result.stdout
    return result.stdout.decode("utf-8").strip()

def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def main():
    if not SOURCE.is_dir():
        fail(f"Source repository not found: {SOURCE}")

    if not (SOURCE / ".git").exists():
        fail(f"Not a Git working copy: {SOURCE}")

    # Verify both pinned commits before reading any artifact.
    for commit in (GENESIS_COMMIT, RELATED_COMMIT):
        git("cat-file", "-e", f"{commit}^{{commit}}")

    # Refuse to overwrite either output.
    for path in (MANIFEST_PATH, RECORD_PATH):
        if path.exists():
            fail(f"Refusing to overwrite existing file: {path}")

    entries = []

    for artifact_id, commit, source_path in ARTIFACTS:
        data = git("show", f"{commit}:{source_path}", binary=True)
        blob_sha1 = git("rev-parse", f"{commit}:{source_path}")
        sha256 = hashlib.sha256(data).hexdigest()

        expected = EXPECTED.get(artifact_id, {})
        if expected.get("sha256") and sha256 != expected["sha256"]:
            fail(f"Genesis SHA-256 mismatch: got {sha256}")

        if (expected.get("git_blob_sha1")
                and blob_sha1 != expected["git_blob_sha1"]):
            fail(f"Git blob ID mismatch for {artifact_id}: {blob_sha1}")

        entries.append({
            "artifact_id": artifact_id,
            "source_commit": commit,
            "source_path": source_path,
            "byte_length": len(data),
            "sha256": sha256,
            "git_blob_sha1": blob_sha1,
        })

    manifest = {
        "manifest_id": "AURA-KEY-PROVENANCE-MANIFEST-001",
        "status": "NON_NORMATIVE",
        "source_repository": "https://github.com/vaidt/aura-specification",
        "source_commits": {
            "genesis": GENESIS_COMMIT,
            "related_records": RELATED_COMMIT,
        },
        "digest_definitions": {
            "sha256": "SHA-256 of the raw file bytes returned by git show",
            "git_blob_sha1": "Git object ID resolved by git rev-parse COMMIT:PATH",
        },
        "artifacts": entries,
        "limitations": [
            "This is a byte and Git-object inventory, not a trust-anchor determination.",
            "Signature files are hashed but their SSH signatures are not verified by this script.",
            "Signer identity, authority continuity, constitutional validity and ratification are not established.",
            "The inventory is limited to the eight explicitly pinned artifacts and commits.",
        ],
    }

    manifest_bytes = (
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    manifest_sha256 = hashlib.sha256(manifest_bytes).hexdigest()

    record = {
        "evidence_id": "EVID-KEY-PROVENANCE-001",
        "claim_id": (
            "Byte-level SHA-256 and Git blob inventory for eight pinned "
            "AURA authority-related source artifacts"
        ),
        "source_uri": "https://github.com/vaidt/aura-specification",
        "source_revision": {
            "revision_type": "git_commit",
            "revision_id": (
                f"GENESIS={GENESIS_COMMIT}; RELATED={RELATED_COMMIT}"
            ),
            "repository": "vaidt/aura-specification",
            "path": None,
        },
        "content_digest": {
            "algorithm": "SHA-256",
            "value": manifest_sha256,
            "scope": "Generated docs/governance/KEY_PROVENANCE_MANIFEST.json bytes",
        },
        "evidence_availability": "PRESENT",
        "verification_result": "PASS",
        "verification_method": {
            "name": "Pinned Git object and raw-byte digest inventory",
            "version": "1.0",
            "command_or_procedure": (
                "git show COMMIT:PATH; git rev-parse COMMIT:PATH; "
                "Python hashlib.sha256; verify pinned Genesis values"
            ),
            "environment": "Local Termux; Python 3",
        },
        "scope_coverage": {
            "included": [entry["artifact_id"] for entry in entries],
            "excluded": [
                "SSH signature verification",
                "Signer identity and competence",
                "Authority continuity and constitutional validity",
                "Normative ratification or implementation authorization",
            ],
            "coverage_status": "EXHAUSTED_WITHIN_SCOPE",
        },
        "observed_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        ).replace("+00:00", "Z"),
        "reviewer": "NOT_INDEPENDENTLY_REVIEWED",
        "limitations": manifest["limitations"] + [
            "PASS applies only to the declared byte-hashing and Git-object checks.",
            "The manifest and record are non-constitutive engineering evidence.",
        ],
        "normative_effect": "NONE",
        "verification_artifact_uri": None,
        "notes": (
            "Manifest path: docs/governance/KEY_PROVENANCE_MANIFEST.json. "
            "No SSH signature validation or governance-authority determination "
            "was performed."
        ),
    }

    record_bytes = (
        json.dumps(record, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")

    # Exclusive creation: never overwrite pre-existing files.
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECORD_PATH.parent.mkdir(parents=True, exist_ok=True)

    try:
        with MANIFEST_PATH.open("xb") as f:
            f.write(manifest_bytes)
        with RECORD_PATH.open("xb") as f:
            f.write(record_bytes)
    except FileExistsError:
        fail("An output appeared during generation; inspect both paths manually.")

    print("PASS: pinned commit checks and Genesis value checks.")
    print(f"Manifest: {MANIFEST_PATH}")
    print(f"Manifest SHA-256: {manifest_sha256}")
    print(f"Evidence record: {RECORD_PATH}")
    print("LIMIT: no SSH signature or constitutional authority verification.")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print("ERROR: Git command failed. Do not bypass the pinned-source checks.",
              file=sys.stderr)
        if exc.stderr:
            print(exc.stderr.decode("utf-8", errors="replace"), file=sys.stderr)
        raise SystemExit(1)
