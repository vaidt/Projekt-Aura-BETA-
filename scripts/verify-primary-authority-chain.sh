#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
WORK_DIR="${RUNNER_TEMP:-$(mktemp -d)}/aura-primary-authority-observation"
mkdir -p "$WORK_DIR"
REPORT="$WORK_DIR/authority-source-signature-observation.json"
SUMMARY="${GITHUB_STEP_SUMMARY:-/dev/null}"

fetch_pinned() {
  local repo="$1" rev="$2" path="$3" expected_blob="$4" output="$5"
  local url="https://raw.githubusercontent.com/$repo/$rev/$path"
  curl --fail --silent --show-error --location "$url" -o "$output"
  local actual
  actual="$(git -C "$REPO_ROOT" hash-object --no-filters "$output")"
  if [[ "$actual" != "$expected_blob" ]]; then
    echo "::error title=Source blob mismatch::$repo@$rev:$path expected $expected_blob but got $actual"
    exit 1
  fi
  printf 'PINNED %s@%s:%s blob=%s\n' "$repo" "$rev" "$path" "$actual"
}

verify_observation() {
  local label="$1" identity="$2" namespace="$3" signers="$4" signature="$5" message="$6" log="$7"
  local rc=0 outcome="FAIL"
  set +e
  ssh-keygen -Y verify -f "$signers" -I "$identity" -n "$namespace" -s "$signature" < "$message" > "$log" 2>&1
  rc=$?
  set -e
  if [[ "$rc" -eq 0 ]]; then outcome="PASS"; fi
  printf '%s\t%s\t%s\n' "$label" "$outcome" "$rc" >> "$WORK_DIR/results.tsv"
  printf '%s outcome=%s exit=%s\n' "$label" "$outcome" "$rc"
  cat "$log"
}

echo "== AURA primary authority source signature observation (NON-CONSTITUTIVE) =="
echo "OpenSSH: $(ssh -V 2>&1)"
echo "BETA checked-out revision: $(git -C "$REPO_ROOT" rev-parse HEAD)"
echo "The signature outcomes are observations. This job PASS does not mean all signatures PASS or that authority is established."

mkdir -p "$WORK_DIR/genesis" "$WORK_DIR/binding" "$WORK_DIR/p008"

# Candidate Genesis act, pinned to the commit where the signed declaration was added.
fetch_pinned "vaidt/aura-specification" "89de18afc41e79afc0259116df861928dfae8cba" "GENESIS_DECLARATION.txt" "9c19e97270a4539ea7788a0553db2a800a573c44" "$WORK_DIR/genesis/GENESIS_DECLARATION.txt"
fetch_pinned "vaidt/aura-specification" "89de18afc41e79afc0259116df861928dfae8cba" "GENESIS_DECLARATION.txt.sig" "82f114a695c5b30094500452c8770cb4d6d572f5" "$WORK_DIR/genesis/GENESIS_DECLARATION.txt.sig"
fetch_pinned "vaidt/aura-specification" "091ab7a88ee626caa536c641fa3cee53a6e008df" "allowed_signers" "fa4fa29ed870f350f38157e9a1e15fe9654a6f86" "$WORK_DIR/allowed_signers"
genesis_sha256="$(sha256sum "$WORK_DIR/genesis/GENESIS_DECLARATION.txt" | awk '{print $1}')"
echo "Genesis exact-preimage SHA-256: $genesis_sha256"
if [[ "$genesis_sha256" != "6b5a4c4eaa258eef27452fe6a2f2d752484ae6c88968a039b0b40ca0ac8f2bb6" ]]; then
  echo "::error title=Genesis preimage digest mismatch::The exact Genesis bytes do not match the digest referenced by the M1 closure record and PR #32."
  exit 1
fi

# Current authority binding and P-008 records are pinned to the same inspected source HEAD.
fetch_pinned "vaidt/aura-specification" "991274eed57d5b3308b0607feeb4d01e6a485974" "AUTHORITY_BINDING_RECORD_v1.1.md" "f9dbbcc138a2e0d1bdb34aea2a238394a28ed2cd" "$WORK_DIR/binding/AUTHORITY_BINDING_RECORD_v1.1.md"
fetch_pinned "vaidt/aura-specification" "991274eed57d5b3308b0607feeb4d01e6a485974" "AUTHORITY_BINDING_RECORD_v1.1.md.sig" "eed7842fc54f5bfeaaafecca63f5dfbe24823b79" "$WORK_DIR/binding/AUTHORITY_BINDING_RECORD_v1.1.md.sig"
fetch_pinned "vaidt/aura-specification" "991274eed57d5b3308b0607feeb4d01e6a485974" "AURA_P008_RATIFICATION_RECORD_v1.0.md" "077a9b8a16dfdb7b700d7d1ec3e19f9c476c4f1e" "$WORK_DIR/p008/AURA_P008_RATIFICATION_RECORD_v1.0.md"
fetch_pinned "vaidt/aura-specification" "991274eed57d5b3308b0607feeb4d01e6a485974" "AURA_P008_RATIFICATION_RECORD_v1.0.md.sig" "54059184b417e13183da97ef8db05d9b506cf8e6" "$WORK_DIR/p008/AURA_P008_RATIFICATION_RECORD_v1.0.md.sig"

: > "$WORK_DIR/results.tsv"
verify_observation "GENESIS_DECLARATION" "kontakt.vaidt@gmail.com" "aura-genesis" "$WORK_DIR/allowed_signers" "$WORK_DIR/genesis/GENESIS_DECLARATION.txt.sig" "$WORK_DIR/genesis/GENESIS_DECLARATION.txt" "$WORK_DIR/genesis-verify.log"
verify_observation "AUTHORITY_BINDING_RECORD_v1.1" "kontakt.vaidt@gmail.com" "aura-governance" "$WORK_DIR/allowed_signers" "$WORK_DIR/binding/AUTHORITY_BINDING_RECORD_v1.1.md.sig" "$WORK_DIR/binding/AUTHORITY_BINDING_RECORD_v1.1.md" "$WORK_DIR/binding-verify.log"
verify_observation "AURA_P008_RATIFICATION_RECORD_v1.0" "kontakt.vaidt@gmail.com" "aura-governance" "$WORK_DIR/allowed_signers" "$WORK_DIR/p008/AURA_P008_RATIFICATION_RECORD_v1.0.md.sig" "$WORK_DIR/p008/AURA_P008_RATIFICATION_RECORD_v1.0.md" "$WORK_DIR/p008-verify.log"

export REPORT WORK_DIR genesis_sha256
export BETA_REVISION="$(git -C "$REPO_ROOT" rev-parse HEAD)"
export OPENSSH_VERSION="$(ssh -V 2>&1)"
export OBSERVED_AT="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
python3 - <<'PY'
import json, os
from pathlib import Path

rows=[]
for line in Path(os.environ["WORK_DIR"], "results.tsv").read_text(encoding="utf-8").splitlines():
    label, outcome, exit_code = line.split("\t")
    rows.append({"artifact": label, "verification_result": outcome, "exit_code": int(exit_code)})
doc={
    "record_id":"BETA-GOV-AUTH-SOURCE-OBS-0001",
    "classification":"NON_CONSTITUTIVE_TECHNICAL_OBSERVATION",
    "observed_at":os.environ["OBSERVED_AT"],
    "beta_revision":os.environ["BETA_REVISION"],
    "openssh_version":os.environ["OPENSSH_VERSION"],
    "genesis_preimage_sha256":os.environ["genesis_sha256"],
    "verification_inputs":{
        "genesis_source_commit":"89de18afc41e79afc0259116df861928dfae8cba",
        "authority_binding_and_p008_source_commit":"991274eed57d5b3308b0607feeb4d01e6a485974",
        "allowed_signers_source_commit":"091ab7a88ee626caa536c641fa3cee53a6e008df",
        "allowed_signers_blob_sha1":"fa4fa29ed870f350f38157e9a1e15fe9654a6f86"
    },
    "observations":rows,
    "interpretation_limit":"Each result reports exact-byte SSHSIG verification against the pinned repository-sourced allowed_signers input. Signature PASS does not independently establish natural-person identity, competent authority, canonical repository designation, effective date, ratification procedure, or normative effect."
}
Path=os.environ["REPORT"]
Path(Path).write_text(json.dumps(doc,indent=2)+"\n",encoding="utf-8")
PY

echo
echo "== Observation summary =="
printf '| Artifact | SSHSIG result | Exit code |\n|---|---:|---:|\n' >> "$SUMMARY"
while IFS=$'\t' read -r label outcome rc; do
  printf '| %s | %s | %s |\n' "$label" "$outcome" "$rc" >> "$SUMMARY"
done < "$WORK_DIR/results.tsv"
printf '\nInput integrity: PASS (all pinned Git blob SHA-1 values and Genesis SHA-256 matched).\n\nInterpretation limit: this workflow is observational, not a governance ratification. Its job success means the pinned inputs were retrieved and the outcomes recorded; it does not require every signature outcome to be PASS.\n' >> "$SUMMARY"
cat "$REPORT"
echo "Observation JSON: $REPORT"
