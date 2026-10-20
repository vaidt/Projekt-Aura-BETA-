# AURA BETA — PR #5 Merge and CLI Readiness Checklist v0.1

**Status:** DRAFT · NON-NORMATIVE · Review gate only  
**Assessment date:** 2026-10-20  
**Repository:** `vaidt/Projekt-Aura-BETA-`  
**Scope:** PR #1 baseline, PR #5 Evidence Contract, PR #4 disposition, and entry criteria for a local CLI verifier

> This checklist is not an authorization to merge, a governance adjudication, or an implementation authorization. A checked item records an observed fact or a satisfied review criterion only within its stated scope.

## 1. Current evidence snapshot

| Control | Observed state | Disposition |
|---|---|---|
| `main` | `88ba12c44afe692f85ec5acc0ee41892897d5138`; README-only tree | Baseline not yet consolidated |
| PR #1 | Open, Draft, unmerged; `alpha/bootstrap-architecture`; 63 changed files | Primary candidate baseline; full review required |
| PR #4 | Open, Draft, unmerged; overlaps target architecture, bootstrap plan, and status documents already present in PR #1 | Hold; do not merge independently |
| PR #5 | Open, Draft, unmerged; based on `alpha/bootstrap-architecture`; latest head `a5225a08c4d0b5badc7e84ad7e8f5eb9fc7effc1` at assessment time | Contract review required; not merge-ready |
| Latest PR #5 CI | [Run #39490004260](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39490004260): report/schema validation PASS; source-signature observation PASS; strict M1 exact-byte gate FAIL; aggregate workflow FAIL | Structural contract checks pass on this revision; overall gate remains red |
| `main` protection | GitHub reports `protected=false`; required status checks disabled; rulesets list empty | Administrative hard-gate gap confirmed |

## 2. Gate A — PR #1 baseline review

PR #1 is the proposed baseline, not an automatic merge candidate. Review every changed file and the full commit range.

- [ ] Review all 63 changed files, including workflows, scripts, schemas, fixture content, evidence records, and the static UI prototype.
- [ ] Confirm the README's three links resolve to `docs/roadmap/BOOTSTRAP_PLAN.md`, `docs/governance/PROJECT_STATUS.md`, and `docs/architecture/TARGET_ARCHITECTURE.md` on the PR tree.
- [ ] Confirm imported APS-300 schemas are pinned to the recorded source commit and Git blob SHAs and remain explicitly DRAFT/non-normative.
- [ ] Confirm candidate authority-source records preserve source conflicts and do not infer issuer competence from a valid SSH signature, repository access, commit authorship, or matching key fingerprints.
- [ ] Review the `Evidence and Governance Verification` workflow and its permissions, dependency lockfile, exact-byte inputs, and failure behavior.
- [ ] Resolve the strict M1 gate disposition through the competent project process. The current exact-byte mismatch is an actual FAIL for the current Markdown bytes; it must not be bypassed or relabelled PASS simply because fail-closed behavior is intended.
- [ ] Do not merge while the aggregate workflow is red unless a separately authorized, explicit control change defines how this governance gate is handled. No such exception is established by this checklist.
- [ ] Before any merge to `main`, have a repository administrator enable branch protection/rulesets and configure appropriate required status checks, including the intended fail-closed gate policy. Verify the effective settings after they are changed.
- [ ] Obtain the required human review and record the disposition of every blocking issue.

**Gate A decision at assessment time: BLOCKED.** PR #1 is still Draft/unmerged, the aggregate CI workflow fails at M1, and `main` has no enforced protection. The PR should not be merged by bypassing the failed gate.

## 3. Gate B — PR #5 Evidence Contract review

PR #5 is a stacked change. It must be reviewed as an extension of the approved baseline, not as an independent replacement for PR #1.

- [x] The schema is versioned as `0.1.0-draft` and declares `normative_effect: NONE`.
- [x] The report separates technical execution, exact-byte evidence, SSH signature verification, governance disposition, and aggregate result.
- [x] Exact-byte artifacts include SHA-256, byte length, optional Git blob SHA-1, expected digest and comparison status.
- [x] OpenSSH fields include tool/version, identity, namespace, key fingerprint when available, message/signature/allowed-signers artifact references, process output references, and exit code.
- [x] The report explicitly binds APS-300 source revision and schema snapshots, and separately records Evidence Object / Evidence Pack availability and schema-validation status.
- [x] The latest inspected schema-validation job accepted the three valid report fixtures and rejected the invalid fixtures for missing reason code, unsupported governance PASS, aggregate PASS without APS-300 records, and APS-300 marked PRESENT against a DRAFT/conflicted source.
- [x] A separate fixture distinguishes byte-integrity mismatch with SSH BLOCKED from byte integrity PASS with SSH signature FAIL.
- [ ] Review the complete schema diff and approve the status vocabulary, reason codes, artifact roles, and source-binding fields.
- [ ] Confirm `aps300_binding.status` can be PRESENT only when the source schema is RATIFIED, schema identifiers are CONSISTENT, and both protocol-level records exist and validate against pinned schemas.
- [ ] Confirm the aggregate PASS constraints cannot be satisfied by a report with any non-PASS subordinate gate, missing required artifact reference, absent APS-300 binding, DRAFT source, or schema-ID conflict.
- [ ] Review the invariant checker for duplicate IDs, unresolved references, digest comparison consistency, and any cross-field constraints that JSON Schema cannot express.
- [ ] Confirm synthetic fixture digests are visibly illustrative and cannot be mistaken for real AURA evidence.
- [ ] Confirm the report contract remains a BETA evidence envelope, not an APS-300 Evidence Object/Evidence Pack and not a protocol-level hash-preimage definition.
- [ ] Require CI on the exact final head. The schema-validation job must pass; the aggregate workflow state must be explicitly accounted for and must not be called green while the M1 gate fails.
- [ ] Complete human review and leave Draft status only after review criteria are met.

**Gate B decision at assessment time: REVIEW REQUIRED / MERGE BLOCKED.** Schema validation passed at the observed revision, but the overall workflow remains red due to the strict M1 gate, and PR #1 has not yet been accepted as the baseline.

## 4. Merge sequence and PR disposition

1. [ ] Resolve Gate A, including the M1 failure through the competent process and enforced `main` protection.
2. [ ] Review and merge PR #1 only when its actual merge criteria are satisfied; preserve its scope as the BETA operational workspace, not protocol authority.
3. [ ] After PR #1 is merged, retarget PR #5 to `main`, refresh its diff against the merged baseline, inspect the exact new head SHA, and rerun CI.
4. [ ] Merge PR #5 only after its review is approved, its report-schema checks pass on the exact merge candidate, the aggregate CI policy is satisfied, and `main` protection enforces the required checks.
5. [ ] Keep PR #4 unmerged. After the baseline review, either close it as superseded or extract a genuinely unique change into a focused follow-up PR after comparing the exact diffs. Do not merge the overlapping documents independently.

## 5. Gate C — Entry criteria for the local CLI runner

Do not begin executable runner implementation until PR #5's contract has been reviewed and accepted through the agreed PR sequence.

- [ ] Freeze the reviewed schema version and record its exact Git commit/blob SHA in the CLI design note.
- [ ] Define a deterministic CLI interface: input manifest, explicit argv, exit codes, stdout JSON report, stderr diagnostics, and behavior for missing or malformed inputs.
- [ ] Declare the supported runtime and OpenSSH dependency/version strategy. “Zero-DB / Zero-Cloud” does not by itself mean zero system binaries; any dependency must be explicit, versioned, and observable.
- [ ] Implement byte acquisition and hashing over raw bytes without text normalization or newline conversion; record byte length, SHA-256, and Git blob SHA-1 where applicable.
- [ ] Verify all manifest pins before invoking the verifier. A pin mismatch or missing artifact must stop the dependent check and result in FAIL/BLOCKED with a reason code.
- [ ] Execute OpenSSH with an argument array/process API where possible, record exact input bytes and stdout/stderr, and preserve the exact exit status. Never convert a failed signature result into PASS.
- [ ] Implement APS-300 binding from a revision-pinned local manifest. Do not depend on runtime network fetches to determine the deterministic report result.
- [ ] Enforce fail-closed APS-300 behavior: DRAFT source or conflicted schema IDs force `aps300_binding=BLOCKED`; missing Evidence Object/Pack records cannot be fabricated; no overall PASS while the binding is not PRESENT and valid.
- [ ] Keep cryptographic validity and governance authority separate. A valid signature cannot itself upgrade authority continuity, ratification, or normative effect.
- [ ] Add positive, negative, mutation, malformed-input, missing-file, stale-pin, and wrong-signature cases.
- [ ] Demonstrate repeatability from the same input manifest and declared toolchain; identify which report metadata is volatile and keep it out of deterministic byte comparisons.
- [ ] Produce a run report bound to the exact source revision and fixture manifest, then obtain independent review before describing the CLI as a verifier.

## 6. Governance stop conditions

The following state is preserved and must not be changed by this checklist or CLI engineering:

- G0 — Authority Continuity: `NOT PROVEN`.
- M1 — Governance Closure: `BLOCKED`.
- P-008 — Protocol Change: `CONFLICTED / NOT ESTABLISHED`.
- WP-3 — Conformance Execution: `BLOCKED`.

Schema-valid JSON, a green schema job, valid SSH signature bytes, a merged BETA PR, or a working CLI do not independently resolve those governance states.

## 7. Current decision

**Do not merge PR #5 yet and do not start the CLI implementation yet.** First close the PR #1 baseline review and hard-gate decisions. The observed schema-validation component is passing, but the aggregate CI workflow is still failing on M1 and the default branch remains unprotected. After PR #1 is properly resolved and merged, retarget/review PR #5 against `main`, require fresh evidence on the exact candidate commit, and only then authorize the runner work package.

### Evidence links

- [PR #1 — Bootstrap baseline](https://github.com/vaidt/Projekt-Aura-BETA-/pull/1)
- [PR #5 — Verification Report Contract](https://github.com/vaidt/Projekt-Aura-BETA-/pull/5)
- [PR #4 — Overlapping architecture notes](https://github.com/vaidt/Projekt-Aura-BETA-/pull/4)
- [CI run #39490004260](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39490004260)
- [Repository branch protection metadata](https://api.github.com/repos/vaidt/Projekt-Aura-BETA-/branches/main)
- [Repository rulesets](https://api.github.com/repos/vaidt/Projekt-Aura-BETA-/rulesets)
