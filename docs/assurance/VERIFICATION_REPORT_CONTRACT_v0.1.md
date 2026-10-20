# AURA BETA — Verification Report Contract v0.1

**Status:** DRAFT · NON-NORMATIVE · NOT RATIFIED  
**Schema:** `schemas/verification-report.schema.json`  
**Scope:** AURA BETA local verification/reporting interface only

## 1. Purpose

Define a versioned machine-readable record for one verification attempt before implementing a CLI runner. The report separates technical execution, exact-byte provenance, the OpenSSH signature check, governance disposition, and the aggregate outcome.

## 2. Status dimensions are independent

- `technical_result.status`: did the declared verifier operation succeed, fail, or become blocked?
- `byte_evidence.status`: were captured artifacts and declared digest comparisons complete and consistent?
- `ssh_signature_gate.status`: what did OpenSSH report for the exact message/signature/allowed-signers inputs?
- `governance_gate.status`: does the declared, explicitly identified governance rule permit the governance claim within scope?
- `overall_result.status`: aggregate result under the named BETA policy, not a protocol decision.

A technical or SSH `PASS` does not imply governance `PASS`. The overall result may remain `BLOCKED` even when byte checks and the SSH check pass. Governance `PASS` requires explicit authority-continuity status, ratification status, a decision-authority reference, and evidence references; these structural requirements still do not establish that underlying claims are true.

## 3. Byte-level evidence

Every byte artifact has a stable ID, role, capture method, byte length, SHA-256 over exact captured bytes, optional Git blob SHA-1, optional expected SHA-256, comparison status, and source/artifact location where available.

- SHA-256 is the content-integrity digest over exact raw bytes.
- `git_blob_sha1` is a Git blob object identifier; it is not a substitute for SHA-256 or an independent trust root.
- `byte_length` is byte count, not character count.
- `MATCH`/`MISMATCH` compares `sha256` with `expected_sha256`; JSON Schema cannot compare the two values, so the companion invariant checker enforces this relation.
- Captured stdout/stderr are distinct byte artifacts, including empty output (zero bytes with SHA-256 of the empty byte sequence).
- Digests in synthetic fixtures are illustrative and must never be presented as real AURA evidence.

## 4. OpenSSH signature gate

The report records exact message, `.sig`, and `allowed_signers` artifacts by ID; OpenSSH tool/version; identity; namespace; key fingerprint when observable; stdout/stderr artifact IDs; and process exit code.

Status/exit-code constraints: `PASS` requires exit code 0 and cause `NONE`; `FAIL` requires a non-zero exit code and non-`NONE` cause; `BLOCKED`/`NOT_RUN` require null SSH exit code and an explicit cause.

OpenSSH `PASS` only proves signature validity for the exact tested bytes under the supplied key input, identity, and namespace. It does not by itself establish authority continuity, signer competence, normative effect, or ratification.

## 5. Governance and aggregate result

Governance uses explicit `PASS`, `FAIL`, or `BLOCKED` plus a reason code and rule ID. Authority continuity and ratification are separate fields. An aggregate `PASS` is structurally rejected unless the technical, byte, SSH and governance states all pass.

These are BETA workspace reporting semantics. They do not replace APS-300, define normative protocol serialization, or change G0/M1/P-008/WP-3.

## 6. APS-300 evidence binding

The verification report is a BETA assurance envelope; it is not itself an APS-300 Evidence Object or Evidence Pack. It must bind the corresponding protocol-level records (or explicitly state why they are absent) using `aps300_binding`.

The binding captures the exact source repository and commit, source-document blob SHA-1, BETA snapshot-manifest blob SHA-1, pinned Evidence Object and Evidence Pack schema blob SHAs, source schema maturity, and the known schema-ID namespace conflict. It also records each Evidence Object / Evidence Pack artifact ID, SHA-256, Git blob SHA-1, and independent schema-validation status.

A `PRESENT` binding requires both records to exist and pass structural validation against the pinned snapshots. A missing or blocked record has an explicit reason and cannot be presented as conformance. Current fixture state is deliberately `BLOCKED`: APS-300 is marked DRAFT in the pinned source, the schema IDs retain a conflicting namespace, and this change does not create a protocol Evidence Object or Pack. Passing draft-schema validation would still not establish protocol conformance or governance ratification.

## 7. Execution contract

The execution record stores `argv` as an array, not a shell command string. It records process state, exit code, environment, network policy/access observation, timestamps, and artifact IDs for stdin/stdout/stderr. Timestamps and runner environment are observational metadata; deterministic comparisons should operate on declared inputs and byte artifacts, not volatile report timestamps.

Runtime objective remains local-first and zero-cloud. CI may use Ajv to validate the draft schema, but the eventual verifier CLI should not require a database, web UI, or network service.

## 7. Limitations and decision boundary

- Schema validity is structural validity, not protocol conformance or governance adjudication.
- The schema does not determine canonical serialization or a protocol-level hash preimage.
- Cross-record relationships and digest comparisons require invariant checks beyond JSON Schema.
- APS-300 snapshots remain DRAFT; this is independent BETA metadata, not a reinterpretation of APS-300.
- No runner implementation is included in this change.

## 8. Acceptance criteria

1. Draft schema compiles under JSON Schema Draft 2020-12.
2. A synthetic byte PASS + SSH PASS + governance BLOCKED report is accepted.
3. A synthetic byte mismatch is represented as FAIL with SSH blocked from running on untrusted inputs.
4. A report missing a required reason code is rejected.
5. Governance PASS with continuity NOT_PROVEN and no ratification evidence is rejected.
6. The invariant checker rejects unresolved artifact references, duplicate artifact IDs, incorrect digest comparisons labelled MATCH, and impossible aggregate PASS combinations.
7. All artifacts remain explicitly non-normative.


An aggregate `PASS` also requires a `PRESENT` APS-300 binding with both protocol-level records structurally validated against the pinned schema snapshots. The report remains an envelope around those records rather than a substitute for them.
