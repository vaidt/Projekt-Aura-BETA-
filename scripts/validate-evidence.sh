#!/usr/bin/env bash
set -euo pipefail

AJV_BIN="${AJV_BIN:-ajv}"
SCHEMA_ROOT="schemas"
EVIDENCE_ROOT="evidence"

run_ajv() {
  "$AJV_BIN" "$@"
}

echo "== AURA BETA evidence validation =="
echo "Validator: $(command -v "$AJV_BIN")"
echo "Validator package versions are pinned in .github/workflows/evidence-schema-validation.yml (ajv-cli@5.0.0, ajv-formats@3.0.1)."

echo
echo "== 1. Verify pinned upstream schema snapshots =="
node <<'NODE'
const fs = require("node:fs");
const { execFileSync } = require("node:child_process");
const manifestPath = "schemas/aps300-draft/SNAPSHOT_MANIFEST.json";
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
if (manifest.status !== "NON_NORMATIVE_SNAPSHOT") {
  throw new Error("APS-300 schema snapshot manifest must remain explicitly non-normative");
}
const schemaEntries = manifest.copied_schemas;
if (!Array.isArray(schemaEntries) || schemaEntries.length < 5) {
  throw new Error("Expected the pinned APS-300 evidence schemas to be listed in the snapshot manifest");
}
for (const entry of schemaEntries) {
  const actual = execFileSync("git", ["hash-object", "--no-filters", entry.destination_path], {encoding:"utf8"}).trim();
  if (actual !== entry.source_blob_sha) {
    throw new Error(`Schema snapshot drift for ${entry.destination_path}: expected source blob ${entry.source_blob_sha}, got ${actual}`);
  }
  console.log(`PINNED ${entry.destination_path} ${actual}`);
}
NODE

echo
echo "== 2. Compile the BETA evidence registry schema =="
run_ajv compile --spec=draft2020 --strict=false -c ajv-formats -s "$SCHEMA_ROOT/evidence-record.schema.json"

echo
echo "== 2b. Compile the BETA verification report schema =="
run_ajv compile --spec=draft2020 --strict=false --validate-formats=true -c ajv-formats \
  -s "$SCHEMA_ROOT/verification-report.schema.json"

echo
echo "== 3. Compile the pinned APS-300 draft evidence object and pack schemas =="
run_ajv compile --spec=draft2020 --strict=false --validate-formats=true -c ajv-formats \
  -s "$SCHEMA_ROOT/aps300-draft/evidence-object.schema.json"
run_ajv compile --spec=draft2020 --strict=false --validate-formats=true -c ajv-formats \
  -s "$SCHEMA_ROOT/aps300-draft/evidence-pack.schema.json" \
  -r "$SCHEMA_ROOT/aps300-draft/evidence-object.schema.json" \
  -r "$SCHEMA_ROOT/aps300-draft/attestation.schema.json" \
  -r "$SCHEMA_ROOT/aps300-draft/evaluation-result.schema.json" \
  -r "$SCHEMA_ROOT/aps300-draft/policy-reference.schema.json"

echo
echo "== 4. Positive and negative schema regression tests =="
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$SCHEMA_ROOT/evidence-record.schema.json" \
  -d tests/fixtures/valid/evidence-record.json --valid
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$SCHEMA_ROOT/evidence-record.schema.json" \
  -d tests/fixtures/invalid/evidence-record-missing-id.json --invalid
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$SCHEMA_ROOT/evidence-record.schema.json" \
  -d tests/fixtures/invalid/evidence-record-extra-field.json --invalid

echo
echo "== 4b. Verification report contract regression tests =="
REPORT_SCHEMA="$SCHEMA_ROOT/verification-report.schema.json"
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$REPORT_SCHEMA" \
  -d tests/fixtures/verification-report/valid-technical-pass-governance-blocked.json --valid
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$REPORT_SCHEMA" \
  -d tests/fixtures/verification-report/valid-signature-fail.json --valid
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$REPORT_SCHEMA" \
  -d tests/fixtures/verification-report/invalid/missing-overall-reason-code.json --invalid
run_ajv test --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
  -s "$REPORT_SCHEMA" \
  -d tests/fixtures/verification-report/invalid/governance-pass-unproven-authority.json --invalid
node scripts/check-verification-report-invariants.js

echo
echo "== 5. Validate every JSON file under evidence/ =="
mapfile -d '' evidence_files < <(find "$EVIDENCE_ROOT" -type f -name '*.json' -print0 | sort -z)
if [ "${#evidence_files[@]}" -eq 0 ]; then
  echo "::error::No evidence JSON files found. Empty evidence inventory is not an acceptable validation baseline."
  exit 1
fi

for file in "${evidence_files[@]}"; do
  case "$file" in
    evidence/registry/*)
      schema="$SCHEMA_ROOT/evidence-record.schema.json"
      ;;
    evidence/protocol/*)
      schema="$SCHEMA_ROOT/aps300-draft/evidence-object.schema.json"
      ;;
    evidence/packs/*)
      schema="$SCHEMA_ROOT/aps300-draft/evidence-pack.schema.json"
      ;;
    *)
      echo "::error file=$file::Evidence JSON is outside a validated contract directory. Move it to evidence/registry, evidence/protocol, or evidence/packs."
      exit 1
      ;;
  esac
  echo "VALIDATING $file against $schema"
  if [ "$schema" = "$SCHEMA_ROOT/aps300-draft/evidence-pack.schema.json" ]; then
    run_ajv validate --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats \
      -s "$schema" \
      -r "$SCHEMA_ROOT/aps300-draft/evidence-object.schema.json" \
      -r "$SCHEMA_ROOT/aps300-draft/attestation.schema.json" \
      -r "$SCHEMA_ROOT/aps300-draft/evaluation-result.schema.json" \
      -r "$SCHEMA_ROOT/aps300-draft/policy-reference.schema.json" \
      -d "$file"
  else
    run_ajv validate --spec=draft2020 --strict=false --validate-formats=true --all-errors -c ajv-formats -s "$schema" -d "$file"
  fi
done

echo
echo "PASS: every JSON file under evidence/ matched its assigned schema; schema snapshots and negative controls were checked."
echo "LIMIT: APS-300 schemas are upstream DRAFT contracts. Passing structural validation is not protocol conformance or governance ratification."
