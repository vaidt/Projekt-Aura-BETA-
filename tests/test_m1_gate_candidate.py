#!/usr/bin/env python3
"""Independent negative/positive controls for lab-only M1 SSHSIG candidate."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "pinned_source"
SCRIPT = BASE / "scripts" / "m1_real_sshsig_gate_candidate.py"
MANIFEST = "tests/fixtures/m1/SSHSIG_INPUT_MANIFEST.json"
IDENTITY = "kontakt.vaidt@gmail.com"
NS = "aura-governance"


def hash256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


class VerifyM1Gate(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="aura-m1-lab-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        shutil.copytree(SRC, self.root)
        self.manifest_path = self.root / MANIFEST
        self.m = json.loads(self.manifest_path.read_text())

    def params(self, mode="current-strict"):
        m = self.m
        b = self.root
        return [
            "--root", str(b),
            "--mode", mode,
            "--trusted-manifest-sha256", hash256(self.manifest_path),
            "--trusted-historical-message-sha256", hash256(b / m["historical"]["message_path"]),
            "--trusted-current-message-sha256", hash256(b / m["current"]["message_path"]),
            "--trusted-historical-signers-sha256", hash256(b / m["historical"]["allowed_signers_path"]),
            "--trusted-current-signers-sha256", hash256(b / m["current"]["allowed_signers_path"]),
            "--expected-source-repository", "vaidt/aura-specification",
            "--expected-source-commit", "991274eed57d5b3308b0607feeb4d01e6a485974",
            "--expected-namespace", NS,
            "--expected-identity", IDENTITY,
        ]

    def run_gate(self, mode="current-strict", params=None):
        if params is None:
            params = self.params(mode)
        p = subprocess.run([sys.executable, str(SCRIPT)] + params, capture_output=True, text=True, timeout=16)
        try:
            doc = json.loads(p.stdout)
        except json.JSONDecodeError as exc:
            raise AssertionError("Verifier must always emit machine-readable JSON: " + p.stdout + "\n" + p.stderr) from exc
        return p.returncode, doc

    def replace_file(self, label, filefield, hashfield, data):
        entry = self.m[label]
        target = self.root / entry[filefield]
        target.write_bytes(data)
        entry[hashfield] = blob(data)

    def write_manifest(self):
        self.manifest_path.write_text(json.dumps(self.m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def assert_block(self, params=None):
        rc, d = self.run_gate(params=params)
        self.assertEqual(rc, 2, d)
        self.assertNotIn(d["status"], ("PASS_CRYPTO_ONLY_NON_CONSTITUTIVE", "PASS_HISTORICAL_SSHSIG_BOUNDED"))

    def create_signed_current_fixture(self):
        # A lab-only private key is generated under TemporaryDirectory and never exported.
        key = Path(self.temp.name) / "LAB_KEY_DO_NOT_DISTRIBUTE"
        p = subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", str(key)], capture_output=True, timeout=15)
        self.assertEqual(p.returncode, 0, p.stderr)
        current_path = self.root / self.m["current"]["message_path"]
        current_path.with_name(current_path.name + ".sig").unlink()  # Never reuse the historical signature during synthetic re-signing.
        s = subprocess.run(["ssh-keygen", "-Y", "sign", "-f", str(key), "-n", NS, str(current_path)], capture_output=True, timeout=15)
        self.assertEqual(s.returncode, 0, s.stderr)
        sig = current_path.with_name(current_path.name + ".sig").read_bytes()
        self.replace_file("current", "signature_path", "signature_blob_sha", sig)
        pub = key.with_suffix(".pub").read_bytes()
        signers = (IDENTITY + " ").encode("ascii") + pub
        self.replace_file("current", "allowed_signers_path", "allowed_signers_blob_sha", signers)
        self.write_manifest()

    def test_01_historical_control_true_positive(self):
        rc, d = self.run_gate(mode="historical-reference")
        self.assertEqual(rc, 0)
        self.assertEqual(d["status"], "PASS_HISTORICAL_SSHSIG_BOUNDED")
        self.assertTrue(d["historical"]["signature_valid"])
        self.assertEqual(d["normative_effect"], "NONE")

    def test_02_real_current_exact_bytes_fail(self):
        rc, d = self.run_gate()
        self.assertEqual(rc, 2)
        self.assertEqual(d["status"], "BLOCKED_CURRENT_EXACTBYTE_SIGNATURE_MISMATCH")
        self.assertTrue(d["historical"]["signature_valid"])
        self.assertFalse(d["current"]["signature_valid"])

    def test_03_valid_synthetic_new_current_signature_positive_path(self):
        self.create_signed_current_fixture()
        rc, d = self.run_gate()
        self.assertEqual(rc, 0, d)
        self.assertTrue(d["current"]["signature_valid"])
        self.assertEqual(d["status"], "PASS_CRYPTO_ONLY_NON_CONSTITUTIVE")
        self.assertEqual(d["normative_effect"], "NONE")

    def test_04_external_manifest_pin_wrong(self):
        a = self.params()
        at = a.index("--trusted-manifest-sha256") + 1
        a[at] = "0" * 64
        self.assert_block(a)

    def test_05_manifest_modified_without_external_repin(self):
        a = self.params()
        self.manifest_path.write_bytes(self.manifest_path.read_bytes() + b" ")
        self.assert_block(a)

    def test_06_current_message_changed_without_repin(self):
        a = self.params()
        path = self.root / self.m["current"]["message_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        self.assert_block(a)

    def test_07_current_message_changed_and_manifest_rehashed_but_signature_invalid(self):
        path = self.root / self.m["current"]["message_path"]
        self.replace_file("current", "message_path", "message_blob_sha", path.read_bytes() + b"\n")
        self.write_manifest()
        rc, d = self.run_gate()
        self.assertEqual(rc, 2)
        self.assertEqual(d["status"], "BLOCKED_CURRENT_EXACTBYTE_SIGNATURE_MISMATCH")

    def test_08_current_signature_modified_without_repin(self):
        a = self.params()
        path = self.root / self.m["current"]["signature_path"]
        path.write_bytes(path.read_bytes().replace(b"SSHSIG", b"NONSGN", 1))
        self.assert_block(a)

    def test_09_current_signature_changed_and_rehashed_is_not_pass(self):
        sig = self.root / self.m["current"]["signature_path"]
        self.replace_file("current", "signature_path", "signature_blob_sha", sig.read_bytes()[:-10] + b"X" * 10)
        self.write_manifest()
        self.assert_block()

    def test_10_signer_allowlist_change_without_repin(self):
        a = self.params()
        p = self.root / self.m["current"]["allowed_signers_path"]
        p.write_bytes(p.read_bytes() + b"# invalid extra\n")
        self.assert_block(a)

    def test_11_signer_allowlist_change_and_manifest_repin_still_blocked(self):
        p = self.root / self.m["current"]["allowed_signers_path"]
        self.replace_file("current", "allowed_signers_path", "allowed_signers_blob_sha", b"someone@else.invalid ssh-ed25519 AAAA\n")
        self.write_manifest()
        self.assert_block()

    def test_12_namespace_substitution(self):
        a = self.params()
        a[a.index("--expected-namespace") + 1] = "file"
        self.assert_block(a)

    def test_13_identity_substitution(self):
        a = self.params()
        a[a.index("--expected-identity") + 1] = "attacker@example.invalid"
        self.assert_block(a)

    def test_14_source_commit_substitution(self):
        a = self.params()
        a[a.index("--expected-source-commit") + 1] = "0" * 40
        self.assert_block(a)

    def test_15_source_repo_substitution(self):
        a = self.params()
        a[a.index("--expected-source-repository") + 1] = "evil/fork"
        self.assert_block(a)

    def test_16_manifest_duplicate_key_rejected(self):
        raw = self.manifest_path.read_text()
        raw = raw.replace('{', '{ "source_repository": "evil/repo", ', 1)
        self.manifest_path.write_text(raw)
        self.assert_block()

    def test_17_manifest_nan_rejected(self):
        raw = self.manifest_path.read_text()
        raw = raw.replace('"status": "NON_NORMATIVE_TEST_FIXTURES"', '"status": NaN', 1)
        self.manifest_path.write_text(raw)
        self.assert_block()

    def test_18_manifest_bad_utf8_rejected(self):
        self.manifest_path.write_bytes(b"\xff{" + self.manifest_path.read_bytes())
        self.assert_block()

    def test_19_git_blob_reference_mismatch_rejected(self):
        self.m["historical"]["signature_blob_sha"] = "0" * 40
        self.write_manifest()
        self.assert_block()

    def test_20_symlink_to_external_current_message_rejected(self):
        p = self.root / self.m["current"]["message_path"]
        keep = Path(self.temp.name) / "message-copy"
        keep.write_bytes(p.read_bytes())
        p.unlink()
        p.symlink_to(keep)
        self.assert_block()

    def test_21_path_traversal_rejected(self):
        a = self.params()  # External pins are independently captured before hostile input.
        self.m["current"]["message_path"] = "../outside.md"
        self.write_manifest()
        a[a.index("--trusted-manifest-sha256") + 1] = hash256(self.manifest_path)
        self.assert_block(a)

    def test_22_absolute_path_rejected(self):
        a = self.params()
        self.m["current"]["message_path"] = "/tmp/escape.md"
        self.write_manifest()
        a[a.index("--trusted-manifest-sha256") + 1] = hash256(self.manifest_path)
        self.assert_block(a)

    def test_23_missing_historical_message_rejected(self):
        a = self.params()
        (self.root / self.m["historical"]["message_path"]).unlink()
        self.assert_block(a)

    def test_24_historical_signature_corrupted_after_manifest_pin_update(self):
        p = self.root / self.m["historical"]["signature_path"]
        self.replace_file("historical", "signature_path", "signature_blob_sha", b"INVALID\n")
        self.write_manifest()
        self.assert_block()

    def test_25_historical_reference_cannot_succeed_with_bad_control(self):
        p = self.root / self.m["historical"]["signature_path"]
        self.replace_file("historical", "signature_path", "signature_blob_sha", b"INVALID\n")
        self.write_manifest()
        rc, d = self.run_gate(mode="historical-reference")
        self.assertEqual(rc, 2)
        self.assertEqual(d["reason"], "historical positive-control signature failed")

    def test_26_current_signers_external_pin_mismatch(self):
        a = self.params()
        a[a.index("--trusted-current-signers-sha256") + 1] = "0" * 64
        self.assert_block(a)

    def test_27_message_crlf_rewrite_rejected_even_with_repin(self):
        p = self.root / self.m["current"]["message_path"]
        self.replace_file("current", "message_path", "message_blob_sha", p.read_bytes().replace(b"\n", b"\r\n"))
        self.write_manifest()
        rc, d = self.run_gate()
        self.assertEqual(rc, 2)
        self.assertEqual(d["status"], "BLOCKED_CURRENT_EXACTBYTE_SIGNATURE_MISMATCH")

    def test_28_current_signers_different_from_history_is_not_implicitly_prohibited(self):
        self.create_signed_current_fixture()
        self.assertNotEqual((self.root / self.m["current"]["allowed_signers_path"]).read_bytes(), (self.root / self.m["historical"]["allowed_signers_path"]).read_bytes())
        rc, d = self.run_gate()
        self.assertEqual(rc, 0, d)

    def test_29_current_signature_may_differ_after_proper_new_signing(self):
        self.create_signed_current_fixture()
        self.assertNotEqual((self.root / self.m["current"]["signature_path"]).read_bytes(), (self.root / self.m["historical"]["signature_path"]).read_bytes())
        self.assertEqual(self.run_gate()[0], 0)

    def test_30_missing_openssh_is_fail_closed(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("candidate_m1", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        old = mod.shutil.which
        mod.shutil.which = lambda binary: None
        try:
            with self.assertRaises(mod.GateError):
                mod.openssh_verify(b"test", Path("/dev/null"), Path("/dev/null"), IDENTITY, NS)
        finally:
            mod.shutil.which = old


if __name__ == "__main__":
    unittest.main(verbosity=2)
