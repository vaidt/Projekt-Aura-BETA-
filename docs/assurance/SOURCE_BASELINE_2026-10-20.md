# AURA BETA — Source Baseline & Integrity Findings

**Record ID:** BETA-ASSURANCE-2026-10-20-001  
**Observed at:** 2026-10-20 (UTC, GitHub API retrieval)  
**Status:** PARTIAL INVENTORY · SOURCE-BOUND · NON-NORMATIVE  
**Purpose:** Record a bounded current-state inspection of candidate repositories, workflows, and one detached-signature/source-revision relationship.

## 1. Executive finding

The candidate repository set is not a single interchangeable codebase. It includes competing canonical-source declarations, different branches/commit histories, distinct product and conformance roles, and CI results with different scopes. The inspected evidence is sufficient to require a source/authority conflict register; it is not sufficient to choose a normative winner or make a protocol-conformance claim.

A cryptographic check also found that the detached SSH signature attached to the current M1 closure Markdown verifies the historical content, but does **not** verify the current amended content. This establishes a signature-to-bytes mismatch for the current file; it does not by itself revoke the historical act, decide legal/constitutional validity, or establish which authority may resolve the issue.

## 2. Repository heads observed

These are immutable commit observations from GitHub API responses. A branch name is a mutable ref; the SHA is the identity of the inspected commit. Timestamps are UTC.

| Candidate source | Inspected branch | HEAD SHA | Commit time | Notes |
|---|---|---|---|---|
| [vaidt/aura-specification](https://github.com/vaidt/aura-specification) | `main` | `991274eed57d5b3308b0607feeb4d01e6a485974` | 2026-10-19 18:17:37 | README says it is the single canonical source; core APS status table still lists APS-001 as draft / architecture review required. |
| [Aura-IDToken/aura-specification](https://github.com/Aura-IDToken/aura-specification) | `main` | `82eba39008a627f1944a32be3ba2ff0c37a1a614` | 2026-10-18 20:56:27 | README has the same Git blob SHA as the `vaidt` README and also declares a single canonical source. Different HEAD does not by itself prove content conflict, but the duplicate canonical claim requires explicit resolution. |
| [vaidt/Aura-vNEXT](https://github.com/vaidt/Aura-vNEXT) | `claude/aura-vnext-genesis-xerti8` | `bdec831c165b3a5465bc25f325ed801558cbf81a` | 2026-09-10 22:14:21 | Default branch is this named branch, not `main`; README claims a new canonical implementation for that repository's product scope. |
| [vaidt/Aura-Guard](https://github.com/vaidt/Aura-Guard) | `main` | `7d2f5746ae61a66edcd11d75bff0787bed854363` | 2026-09-13 09:44:08 | README is only 29 characters (`# Here are your Instructions`). Latest inspected CodeQL run passed on this SHA; that is not full build/conformance evidence. |
| [vaidt/aura-guard-v1.3](https://github.com/vaidt/aura-guard-v1.3) | `main` | `e0ed7a8b381b725fe65bd86716894bfdf17d3a94` | 2026-10-17 12:16:42 | Latest inspected merge is PR #11 for chain-integrity fixes. |
| [vaidt/Aura-Conformance-Kit](https://github.com/vaidt/Aura-Conformance-Kit) | `main` | `2982c5c0060cfba2b7229c23acb5530014d02125` | 2026-09-20 18:45:41 | Candidate conformance tooling; current content and execution coverage need deeper review. |
| [Kamil1230xd/aura-sign-mvp](https://github.com/Kamil1230xd/aura-sign-mvp) | `main` | `47178695d88d865e872db07a3bc02b6325f5eb7a` | 2026-07-28 18:43:26 | README labels this an experimental, time-boxed research repository, not production-ready. |
| [Aura-IDToken/aura-poc-a-core-v3.3](https://github.com/Aura-IDToken/aura-poc-a-core-v3.3) | `main` | `43f054f8deb7c9644c52148d6496b493512d32b0` | 2026-08-23 21:32:22 | Historical/legacy core candidate; inspected Execution Checks run on this SHA failed. |

## 3. Selected workflow observations

Only the named workflow run and its configured scope are established by a passing or failing conclusion. A green workflow does not automatically establish conformance, governance validity, or production readiness.

| Repository | Workflow/run | Observed result | Scope limit |
|---|---|---|---|
| `vaidt/aura-specification` | [Draft Conformance #39301296818](https://github.com/vaidt/aura-specification/actions/runs/39301296818) | SUCCESS, 2026-10-19 | This workflow only; does not close DQ-006 or establish all APS contracts. |
| `Aura-IDToken/aura-specification` | [Draft Conformance #39165592778](https://github.com/Aura-IDToken/aura-specification/actions/runs/39165592778) | FAILURE, 2026-10-18 | The failure requires its own log review; it does not alone invalidate the other repository. |
| `vaidt/Aura-vNEXT` | [baseline #34536425369](https://github.com/vaidt/Aura-vNEXT/actions/runs/34536425369) | SUCCESS, 2026-09-10 | Older run on repository-specific default branch; current re-execution was not observed. |
| `vaidt/Aura-Guard` | [CodeQL Advanced #39072105218](https://github.com/vaidt/Aura-Guard/actions/runs/39072105218) | SUCCESS, 2026-10-17 | Scheduled CodeQL analysis only, on an unchanged older commit; not a general test-suite result. |
| `vaidt/aura-guard-v1.3` | [Rust #39031893550](https://github.com/vaidt/aura-guard-v1.3/actions/runs/39031893550), [CI #39031893546](https://github.com/vaidt/aura-guard-v1.3/actions/runs/39031893546), [coverage #39031893517](https://github.com/vaidt/aura-guard-v1.3/actions/runs/39031893517), [semgrep #39031893538](https://github.com/vaidt/aura-guard-v1.3/actions/runs/39031893538), [Docker #39031893532](https://github.com/vaidt/aura-guard-v1.3/actions/runs/39031893532) | All five SUCCESS, 2026-10-17 | Evidence of these workflow runs only; independent protocol-level conformance remains a separate question. |
| `vaidt/Aura-Conformance-Kit` | [Aura TCK CI #35530103237](https://github.com/vaidt/Aura-Conformance-Kit/actions/runs/35530103237) | SUCCESS, 2026-09-20 | Older run; current rerun on 2026-10-20 not observed. CodeQL run on Oct 16 is not a TCK rerun. |
| `Aura-IDToken/aura-poc-a-core-v3.3` | [Execution Checks #32667830035](https://github.com/Aura-IDToken/aura-poc-a-core-v3.3/actions/runs/32667830035) | FAILURE, 2026-08-23 | Historical run on current observed HEAD; detailed job logs still need review. |

The BETA workflow run [#39456930057](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39456930057) ran against PR merge commit `4f98747b9e4bc7097e5fd8249f15a351edd06ac9`: schema-validation job PASS; strict M1 exact-byte signature gate FAIL as designed; overall workflow FAIL. This is not a green CI baseline.

## 4. Detached SSH signature check — M1 closure record

### Inputs and source binding

- Current repository: `vaidt/aura-specification`, `main` at `991274eed57d5b3308b0607feeb4d01e6a485974`.
- Current Markdown file: [`AURA_M1_CLOSURE_RECORD_v1.0.md`](https://github.com/vaidt/aura-specification/blob/main/AURA_M1_CLOSURE_RECORD_v1.0.md), Git blob SHA `1dde9631b646ef58bb6bdbe49cb5684c67aa4a43`.
- Detached signature file: [`AURA_M1_CLOSURE_RECORD_v1.0.md.sig`](https://github.com/vaidt/aura-specification/blob/main/AURA_M1_CLOSURE_RECORD_v1.0.md.sig), Git blob SHA `e36a2ff03e39e3614c298dfb42c90964f058d65e`.
- Historical pre-warning Markdown at commit `6028ceda886db062488b29578d573f5826968d32`, Git blob SHA `2a729379f8d306a1f371db26d0ec4577cf8701b6`.
- Commit that amended the current Markdown: [`2780a4e34be07e21ad04a27f24195805451826fa`](https://github.com/vaidt/aura-specification/commit/2780a4e34be07e21ad04a27f24195805451826fa), 2026-10-17. It adds a warning identifying proposed deprecation as non-constitutive and not effective, and proposes `NOT PROVEN / BLOCKED` pending competent ratification, registration, and independent verification.
- History of the detached signature file shows its last/only observed change at commit `6028ceda886db062488b29578d573f5826968d32` on 2026-09-24; no later signature update was observed.

### Verification procedure and results

A local verifier parsed the OpenSSH SSHSIG envelope (version 1, namespace `aura-governance`, hash algorithm `sha512`, Ed25519 key/signature), bound its public key to the public key entry in the repository's `allowed_signers`, and verified the OpenSSH-defined signed message over SHA-512 of the exact file bytes.

| Target bytes | Result | Meaning |
|---|---|---|
| Historical M1 Markdown at the signed revision | **PASS** | The detached signature validates the exact historical bytes against the public key in the repository's `allowed_signers`. |
| Current M1 Markdown including the Oct 17 warning | **FAIL** | The same detached signature does not validate the current amended bytes. |

### Interpretation boundary

The cryptographic result establishes a mismatch between current Markdown bytes and the attached detached signature. It does **not** by itself revoke the historically signed record, prove the identity or constitutional competence of the key holder, or determine which governance act may supersede the record. The public key and allow-list are repository-bound inputs; their existence is not independent proof of constitutional authority.

Operational treatment in BETA: show the current file as `PRESENT + SIGNATURE_MISMATCH`; do not show the current file as cryptographically signed/verified. Preserve both historical and current revisions, plus the supersession/ratification question, in the audit trail.

## 5. Governance contradictions retained

- `GOVERNANCE_STATUS_INDEX.md` routes readers to M1 closure and authority-binding records as records of reference.
- Current M1 closure Markdown declares itself `RATIFIED / EXECUTED / CLOSED`, while a later attached warning says proposed deprecation is non-constitutive and not effective and requests a `NOT PROVEN / BLOCKED` disposition pending further acts.
- `AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.3.md` describes itself as a proposed, non-effective register and records authority continuity, holder verification, M1 closure, P-008 competence, and TCK authorization as not proven from the assessed evidence.
- `closures/DQ-006_CLOSURE_PACKAGE.md` declares DQ-006 `OPEN`, with specification closed but conformance evidence partial.

These are conflicting claims with different asserted status and legal/constitutional effect. BETA records the conflict; it does not resolve the conflict by choosing the most convenient or latest-looking sentence.

## 6. Current disposition

| Question | Disposition |
|---|---|
| Was the candidate repository HEAD observed? | YES for rows in §2 at the stated retrieval snapshot. |
| Were all files and branches of those repositories exhaustively reviewed? | NO. This is a bounded baseline, not exhaustive source forensics. |
| Is `vaidt/aura-specification` the uncontested normative authority? | NOT ESTABLISHED by this record. Duplicate canonical claims and governance contradictions remain. |
| Does the current M1 Markdown validate against its attached signature? | NO — verification against current exact bytes returned FAIL. |
| Does the historical M1 Markdown validate against that signature? | YES — historical exact bytes returned PASS. |
| Is M1 legally/constitutionally revoked or closed by this technical check? | NOT DETERMINED. A signature mismatch alone does not decide that question. |
| Is DQ-006 closed? | Current closure package says OPEN. |
| Is the BETA PR CI green? | No checks observed; do not infer PASS. |
| Can BETA make protocol decisions effective? | NO. It is a non-canonical design/integration workspace. |

## 7. Recommended next actions

1. Preserve the current M1 Markdown, historical signed bytes, signature, and signature-validation output as distinct revision-bound records.
2. Review the exact signed payload and signature verification report independently; record tool/version and reviewer.
3. Reconcile the authority-binding/identity chain and M1 status only through the required competent governance procedure; do not use this engineering repository to ratify itself.
4. Inspect the full current DQ-006 package, P-008 record, constitution procedure, and relevant signed decrees as a separately scoped forensic review.
5. Re-run current CI and independent conformance only after source revisions, fixtures, and expected-result authority are bound.

This document records a bounded technical observation and proposed work. It has no normative effect on AURA.


## 8. Independent reproduction with OpenSSH

The verification above used a local SSHSIG-envelope parser and Ed25519 verification implementation following the OpenSSH SSHSIG signed-message format. A second review can reproduce the result from a clean clone using the standard OpenSSH verifier.

```bash
git clone https://github.com/vaidt/aura-specification.git /tmp/aura-specification
cd /tmp/aura-specification

git show 6028ceda886db062488b29578d573f5826968d32:AURA_M1_CLOSURE_RECORD_v1.0.md > /tmp/m1-historical.md
git show 991274eed57d5b3308b0607feeb4d01e6a485974:AURA_M1_CLOSURE_RECORD_v1.0.md > /tmp/m1-current.md
git show 991274eed57d5b3308b0607feeb4d01e6a485974:AURA_M1_CLOSURE_RECORD_v1.0.md.sig > /tmp/m1-current.sig
git show 091ab7a88ee626caa536c641fa3cee53a6e008df:allowed_signers > /tmp/aura-allowed-signers

# Expected exit code 0: the historical bytes are signed.
ssh-keygen -Y verify -f /tmp/aura-allowed-signers \
  -I kontakt.vaidt@gmail.com -n aura-governance \
  -s /tmp/m1-current.sig < /tmp/m1-historical.md

# Expected non-zero exit code: the warning amendment is not covered by that signature.
ssh-keygen -Y verify -f /tmp/aura-allowed-signers \
  -I kontakt.vaidt@gmail.com -n aura-governance \
  -s /tmp/m1-current.sig < /tmp/m1-current.md
```

Recorded independent run: OpenSSH_9.6p1 Ubuntu-3ubuntu13.19 / OpenSSL 3.0.13; historical verification exit code 0; current verification exit code 255; BETA checked-out merge commit `4f98747b9e4bc7097e5fd8249f15a351edd06ac9`; source main pinned at `991274eed57d5b3308b0607feeb4d01e6a485974`. The expected outcomes were reproduced. If future outcomes differ, mark the finding `INCONCLUSIVE` and investigate; do not suppress or reinterpret the discrepancy. The signer allow-list comes from the same repository history and therefore provides a cryptographic verification key input, not an external trust anchor for constitutional authority.
