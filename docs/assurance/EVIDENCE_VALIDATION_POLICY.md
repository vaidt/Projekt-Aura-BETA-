# Evidence Schema Validation Policy

**Status:** BETA engineering control · non-normative  
**Enforcement:** GitHub Actions workflow `Evidence Schema Validation`  
**Policy record:** BETA-ASSURANCE-SCHEMA-001

## 1. Gate

Before a live evidence collector is introduced, all JSON files in `evidence/` must be validated in CI. The workflow is fail-closed:

- every JSON file must live in one of the explicit contract directories;
- `evidence/registry/*.json` validates against the BETA evidence-metadata schema;
- `evidence/protocol/*.json` validates against the pinned APS-300 draft Evidence Object schema;
- `evidence/packs/*.json` validates against the pinned APS-300 draft Evidence Pack schema and its referenced schemas;
- unknown evidence locations, invalid JSON, missing required properties, additional properties where forbidden, invalid formats, invalid schema compilation, snapshot drift, or failing negative-control tests fail the job;
- a minimum non-empty registry evidence set is required so an empty directory cannot look like successful validation.

The script is `scripts/validate-evidence.sh`; the workflow is `.github/workflows/evidence-schema-validation.yml`.

## 2. Contract separation

The BETA `schemas/evidence-record.schema.json` defines the **audit registry metadata record** — provenance about a claim and a verification attempt. It is not the AURA protocol's Evidence Object.

The protocol Evidence Object and Evidence Pack use pinned schema snapshots from:

- source repository: `vaidt/aura-specification`;
- inspected source commit: `991274eed57d5b3308b0607feeb4d01e6a485974`;
- source document: `aps/APS-300_EVIDENCE_MODEL.md`, blob SHA `ad762de0fee86ece0c1fc75471a8fd510c6f91b5`;
- schemas: `schemas/aps300-draft/SNAPSHOT_MANIFEST.json`.

The source APS-300 currently labels itself `Version: 1.0-DRAFT` and `Status: DRAFT`. Its schemas also identify themselves as draft structural contracts. Therefore this CI enforces the current upstream draft shape reproducibly; it does **not** claim the model is ratified, universally authoritative, or semantically complete.

## 3. Provenance and update process

- Snapshot bytes must match the upstream Git blob SHAs recorded in the manifest. Editing a snapshot without updating the evidence-backed manifest fails CI.
- Updating a snapshot requires a source commit, source blob SHA, reviewed diff, and updated manifest in the same PR.
- Do not silently rewrite upstream `$id` values or normalize schema content. The current IDs retain the `AuraIDToken/aura-specification` namespace even when identical bytes were read from `vaidt/aura-specification`; that identity conflict is preserved and is itself auditable.
- Schema-valid data is not automatically cryptographically valid, authoritative, normative, effective, or conformant. Hash correctness, signatures, canonicalization, semantic contract, and governance remain separate checks.
- A `CLOSED` governance state must not be derived from schema validation. A cryptographic signature PASS establishes signature-to-exact-bytes verification under the specified key and namespace; it does not alone establish constitutional authority.

## 4. Test strategy

The CI compiles all required schemas using Ajv CLI with Draft 2020-12 support and format validation, tests one valid registry record, verifies rejection of a record missing `evidence_id`, verifies rejection of an unknown property, and validates all registry records.

Protocol evidence and pack directories may initially have no protocol fixtures; any JSON file added there is validated automatically under its respective schema. A future collector must write to these directories only and must treat a missing schema, unresolved reference, failed check, or missing source authority as BLOCKED/INCONCLUSIVE rather than PASS.

## 5. Dependency and maturity note

Ajv CLI and ajv-formats are pinned to explicit package versions in CI. This first gate uses exact top-level versions but does not yet commit a fully resolved npm dependency lockfile; full transitive dependency pinning should be added before using this as a production assurance control.

The workflow must pass on the BETA PR and receive review before any live collector can be enabled. No live collector is authorized by this document.
