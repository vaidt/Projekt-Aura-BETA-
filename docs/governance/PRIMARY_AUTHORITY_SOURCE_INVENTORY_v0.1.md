# AURA BETA — Primary Authority Source Inventory & Delegation Chain v0.1

**Record ID:** BETA-GOV-AUTH-SOURCE-INVENTORY-0001  
**Status:** PARTIAL INVENTORY · SOURCE-BOUND · NON-CONSTITUTIVE  
**Observation date:** 2026-10-20  
**Workspace:** `vaidt/Projekt-Aura-BETA-`  
**Scope:** Candidate constitutional establishment source, Genesis declaration, identity/key binding, M1/P-008 linkage, and repository authority controls  
**Normative effect:** NONE

## 1. Executive disposition

A candidate primary instrument has been located: `GENESIS_DECLARATION.txt`, added to `vaidt/aura-specification` at commit `89de18afc41e79afc0259116df861928dfae8cba` on 2026-09-24, with a detached SSH signature in namespace `aura-genesis`. The declaration asserts Genesis Authority, appointment of Kamil Krasiński as initial Chief Architect, and powers over P-008 and implementation authorization.

This is a materially stronger source candidate than an unattached authority statement, but **it does not by itself complete the authority chain**. The declaration invokes Article XIII; Article XIII was added to a document still labelled Constitution v1.0 / FROZEN by commit `a53ef122f9cedbf110f30ed57ddd7ef1db6f1491` on 2026-09-21. The prior constitution blob lacks Article XIII, and the unchanged root-level `AURA Constitution_260723_190157.txt` also lacks Article XIII. Article XI of the same Constitution requires an RFC, Architecture Review, impact analysis, dependent-document updates, and Chief Architect approval for constitutional amendments. The examined source review (PR #32) records the procedural effect of the Article XIII insertion as not established from the reviewed sources. This is a source-bound procedural finding, not a final external-law judgment.

The Genesis declaration's detached signature, even if the exact-byte OpenSSH check passes, demonstrates a signature/key relationship under the tested `allowed_signers` input. That input is in the same repository history. It does not independently prove the signer's civil identity, prior constitutional competence, or that the repository named in the declaration was unambiguously the canonical repository. The current identity bridge draft itself says independent identity proof and an external signed trust anchor are pending.

**Current disposition:** candidate primary instrument **FOUND**; competence of issuer **NOT PROVEN**; holder identity/continuity **NOT PROVEN**; Article XIII procedure/effect **NOT ESTABLISHED FROM SOURCES REVIEWED**; M1 **BLOCKED**; P-008 ratification **CONFLICTED / NOT ESTABLISHED**; WP-3 **BLOCKED**.

## 2. Source inventory and immutable references

### 2.1 Constitution v1.0 and Article XIII insertion

| Item | Observed source fact | Evidence / limitation |
|---|---|---|
| Pre-Article-XIII constitution | `vaidt/aura-specification@865b0d68b2f566759f096e1b7a5c67b5ed4f858b`, blob `9be4bf9249d4156d7a0c00a83976a5233d2f0dd2`; label `Version: 1.0`, `Status: FROZEN`; no Article XIII | [Pre-amendment file](https://github.com/vaidt/aura-specification/blob/865b0d68b2f566759f096e1b7a5c67b5ed4f858b/constitution/AURA_CONSTITUTION.md) |
| Article XIII insertion | Commit `a53ef122f9cedbf110f30ed57ddd7ef1db6f1491`, authored 2026-09-21 19:32:53Z; adds four lines / the Article XIII section to the same path | [Exact commit diff](https://github.com/vaidt/aura-specification/commit/a53ef122f9cedbf110f30ed57ddd7ef1db6f1491) |
| Resulting constitution blob | `ae121ce247066fb2cc920fb7114e6547fd4f7398`; it still labels itself `Version: 1.0` and `Status: FROZEN`, while containing Article XIII | [Post-insertion file](https://github.com/vaidt/aura-specification/blob/a53ef122f9cedbf110f30ed57ddd7ef1db6f1491/constitution/AURA_CONSTITUTION.md) |
| Article XI procedure | RFC; Architecture Review; impact analysis; updates to dependent documents; approval by Chief Architect; FROZEN contents are immutable | Present in both the pre- and post-insertion Markdown |
| Original text copy | Root `AURA Constitution_260723_190157.txt`, blob `bf28a0b210f54835509665f3aacc42f69c433e23`, lacks Article XIII and preserves Article XI's amendment requirements | [Original text copy at source HEAD](https://github.com/vaidt/aura-specification/blob/991274eed57d5b3308b0607feeb4d01e6a485974/AURA%20Constitution_260723_190157.txt) |
| Procedural review | [PR #32](https://github.com/vaidt/aura-specification/pull/32), open and Draft at the observed state, carries a non-constitutive G1/Genesis evidence package and records Article XIII procedure as not established from sources reviewed | Draft status means the audit package is not itself a binding adjudication |

The textual facts above support a conflict between the document's frozen/versioned status and a later insertion without a version increment in the examined path. The current inventory has not established, from primary process records, that all Article XI steps were performed. It does not independently determine external legal validity.

### 2.2 Candidate Genesis establishment act

| Field | Observed value |
|---|---|
| Artifact | `GENESIS_DECLARATION.txt` |
| Source | `vaidt/aura-specification` at commit `89de18afc41e79afc0259116df861928dfae8cba` |
| Git blob SHA-1 | `9c19e97270a4539ea7788a0553db2a800a573c44` |
| Declared SHA-256 of exact preimage in M1 record / PR #32 | `6b5a4c4eaa258eef27452fe6a2f2d752484ae6c88968a039b0b40ca0ac8f2bb6` |
| Detached signature | `GENESIS_DECLARATION.txt.sig`, blob `82f114a695c5b30094500452c8770cb4d6d572f5`, added with the declaration at the same commit |
| Signature namespace | `aura-genesis` |
| Claimed signer identity | `kontakt.vaidt@gmail.com` |
| Verification key input | `allowed_signers` at commit `091ab7a88ee626caa536c641fa3cee53a6e008df`, blob `fa4fa29ed870f350f38157e9a1e15fe9654a6f86` |
| Public-key fingerprint in related authority record | `SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU` |

The declaration states that the signer converts technical ownership into constitutional Genesis Authority, enacts Article XIII, appoints the initial Chief Architect, and grants broad ratification / implementation powers. Those are **claims made by the instrument**. Signature verification is a separate technical question; competence, scope, and procedural effect must be independently established.

PR #32 reports that the Genesis preimage digest matches its M1 reference and that Python `cryptography`, OpenSSL CLI, and Node.js crypto verified the signature over the inspected preimage. That PR qualifies those results as different tool paths in one audit environment, not independent machines/backends. A separate source-pinned OpenSSH observation in [BETA workflow run #39472439876](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39472439876) verified the Genesis signature over the exact pinned preimage: **PASS / exit 0**. The same run verified the exact current bytes of `AUTHORITY_BINDING_RECORD_v1.1.md` and `AURA_P008_RATIFICATION_RECORD_v1.0.md` under the same repository-sourced allow-list: both **PASS / exit 0**. All source Git blob SHA-1 pins and the Genesis SHA-256 matched. These results establish the tested signature-to-bytes relationships under that key input; signing time, independent natural-person identity binding, prior issuer competence, canonical-repository designation, and constitutional procedure remain separate unresolved questions.

### 2.3 Authority/identity binding record

| Field | Observed value |
|---|---|
| Artifact | `AUTHORITY_BINDING_RECORD_v1.1.md` |
| Source revision | `vaidt/aura-specification@991274eed57d5b3308b0607feeb4d01e6a485974` |
| Git blob SHA-1 | `f9dbbcc138a2e0d1bdb34aea2a238394a28ed2cd` |
| Attached signature blob | `eed7842fc54f5bfeaaafecca63f5dfbe24823b79` |
| Declared status | `RATIFIED` |
| Claimed identity binding | Kamil Krasiński; email `kontakt.vaidt@gmail.com`; GitHub accounts `vaidt`, `Kamil1230xd`, `Aura-IDToken` |
| Declared key | Ed25519 fingerprint `SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU` |
| Declared authority | Key is stated to be under exclusive physical control; decrees in `aura-genesis` and `aura-governance` namespaces are claimed to carry constitutive authority |

The record's own assertions do not independently prove the identity claim, exclusive control, issuer competence, or the authority to declare this binding record ratified. The public-key/allow-list source is repository-bound. Even a successful exact-byte signature check cannot validate a self-asserted trust anchor without an independently established authority basis.

The current [Identity Bridge Draft v0.3](https://github.com/vaidt/aura-specification/blob/main/docs/governance/AURA-AUTHORITY-001-IDENTITY-BRIDGE-DRAFT-v0.3.md) explicitly states: competent issuer not established; independent identity proof not found/provided; external signed trust anchor URL and digest pending; signature artifact and effective date pending. This is not contradicted by the OpenSSH PASS results: those results validate exact bytes against a repository-sourced key, not the independent identity/competence chain. The draft says its purpose is to define a process, not to establish who currently has authority.

### 2.4 P-008 record and M1 status conflict

| Field | Observed value |
|---|---|
| Current P-008 record | [AURA_P008_RATIFICATION_RECORD_v1.0.md](https://github.com/vaidt/aura-specification/blob/991274eed57d5b3308b0607feeb4d01e6a485974/AURA_P008_RATIFICATION_RECORD_v1.0.md), blob `077a9b8a16dfdb7b700d7d1ec3e19f9c476c4f1e` |
| Attached signature blob | `54059184b417e13183da97ef8db05d9b506cf8e6` |
| Initial status fields | `Status: READY_FOR_EXECUTION`; `Ratification_Status: PENDING_EXECUTION` |
| Later content | A later section states `Normative_Effect: EFFECTIVE` for the stated P-008 scope |
| M1 closure claim | The current M1 closure record says P-008 was `EXECUTED` and asserts `M1_Governance_Gate: CLOSED`; current M1 bytes do not verify against its attached signature |

This is a material source-level status inconsistency. OpenSSH verified the current P-008 bytes against the attached signature (**PASS / exit 0**, run #39472439876), so the conflict is not a signature-to-bytes mismatch for this current record. It is a conflict in status assertions and authority/effectiveness. The signature does not choose which status is controlling. The current inventory therefore treats P-008 ratification as **CONFLICTED / NOT ESTABLISHED** until the competent issuer and authoritative status transition are established.

### 2.5 M1 closure record

The current M1 Markdown blob `1dde9631b646ef58bb6bdbe49cb5684c67aa4a43` still contains the asserted `RATIFIED / EXECUTED` and `CLOSED / PROVEN` fields, alongside the later warning that proposed deprecation is non-constitutive and not effective. OpenSSH checks in the BETA workflow have repeatedly returned historical exact-byte PASS (exit 0) and current amended-byte FAIL (exit 255). The mismatch is a byte/signature fact; it is not, by itself, a determination that the historic act was revoked, invalid, or superseded.

## 3. Repository-level canonical-source boundary

Observed main refs at the baseline:

- `vaidt/aura-specification`: `991274eed57d5b3308b0607feeb4d01e6a485974` (observed commit time 2026-10-19 18:17:37Z).
- `Aura-IDToken/aura-specification`: `82eba39008a627f1944a32be3ba2ff0c37a1a614` (observed commit time 2026-10-18 20:56:27Z).

The two repositories currently carry identical Git blobs for the Constitution Markdown with Article XIII (`ae121ce...`), Genesis declaration (`9c19e...`), Genesis signature (`82f114...`), and allowed-signers file (`fa4fa...`). Their main commits and histories differ, however, and both repositories make a canonical-source claim in repository material. Identical files across two repository copies do not independently prove which repository is canonical.

Article XIII's own precondition refers to control over “the canonical repository.” The inventory does not establish an uncontested constitutive designation of that repository independent of the Genesis claim being evaluated. This is a circularity risk to be referred to the competent authority process, not resolved by choosing a repository based on owner, recency, or CI status.

## 4. Authority chain assessment

| Link | Evidence observed | Current assessment |
|---|---|---|
| Primary authority source | Constitution v1.0 plus later Article XIII insertion; Genesis Declaration at immutable commit | **CANDIDATE FOUND; AMENDMENT PROCEDURE / PRIOR AUTHORITY NOT ESTABLISHED** |
| Competent issuer | Genesis declaration's self-description; commit metadata; repository allow-list | **NOT PROVEN** — these do not independently establish prior constitutional competence |
| Current holder / person-key binding | Authority Binding v1.1 assertions and shared key fingerprint; Identity Bridge Draft declares independent proof pending | **NOT PROVEN** |
| Decision scope | Article XIII speaks to appointment of initial Chief Architect; Genesis declaration additionally asserts broad P-008 and implementation powers | **SCOPE ALIGNMENT REQUIRES COMPETENT REVIEW** |
| Effective date | Text date 2026-09-24 and Git commit metadata | **DECLARED / OBSERVED; EFFECTIVENESS BASIS NOT INDEPENDENTLY ESTABLISHED** |
| Current validity / revocation | No independent external trust anchor or complete revocation/succession record established in this inventory; signature mismatch exists for amended M1 bytes | **NOT ESTABLISHED**; do not equate this with proof of revocation |
| Authenticated outcome | Genesis signature and other candidate signatures will be recorded by exact-byte OpenSSH observation; current M1 signature fails | **PARTIAL / CONFLICTED**; a cryptographic result does not itself prove authority |

Required chain:

`Primary source → competent issuer → current holder → authorized scope → effective date → continuing validity → authenticated outcome`

A missing or disputed link holds G0/M1 blocked. The absence of a proven link is not, by itself, proof that no authority exists.

## 5. Repository protection observation

A read of `/repos/vaidt/Projekt-Aura-BETA-/rulesets` returned an empty array at the observation point. The branch-protection endpoint `/branches/main/protection` returned HTTP 403, “Resource not accessible by integration.” Therefore the current integration did **not** permit independent verification of classic branch-protection settings or administrator enforcement. The empty rulesets response does not establish that classic branch protection is absent; do not claim protection was verified.

PR #1 is open, Draft, and unmerged. Its status is verified; the technical enforcement mechanism that prevents an authorized user from overriding checks has not been established here.

## 6. OpenSSH exact-byte observation

The source-pinned observation completed in [workflow run #39472439876](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39472439876). Environment: OpenSSH_9.6p1 Ubuntu-3ubuntu13.20 / OpenSSL 3.0.13. The PR branch head was `89fab12a9310dd72b243db2b3130d9d189d4b`; the workflow checked out merge ref `72883b1f607612be19fbcea4490f89125215c7e3`. All required Git blob SHA-1 pins and the declared Genesis SHA-256 matched.

| Artifact / namespace | Exact-byte result | Meaning |
|---|---|---|
| Genesis Declaration / `aura-genesis` | **PASS · exit 0** | Signature validates the pinned declaration bytes against the pinned repository-sourced `allowed_signers` entry. |
| Authority Binding v1.1 / `aura-governance` | **PASS · exit 0** | Signature validates the pinned current record bytes under the same tested key input. |
| Current P-008 record / `aura-governance` | **PASS · exit 0** | Signature validates the pinned current record bytes; internal status conflict remains unresolved. |
| M1 current amended record / `aura-governance` | **FAIL · exit 255** | Separate strict M1 workflow continues to reject current bytes against the attached signature. |

The Genesis SHA-256 was `6b5a4c4eaa258eef27452fe6a2f2d752484ae6c88968a039b0b40ca0ac8f2bb6`, matching the value referenced in M1 and PR #32. Planned durable registry records are `EVID-GOV-GENESIS-SIG-006`, `EVID-GOV-AUTHORITY-BINDING-SIG-007`, and `EVID-GOV-P008-SIG-008`. The run attached an observation JSON artifact.

The observation job is informational: its job PASS means pinned inputs were retrieved and results recorded, not that every relevant signature passed or that governance authority was established. The aggregate workflow remains FAIL because the strict M1 gate fails. A successful signature check proves neither issuer competence, independent natural-person identity, canonical-repository designation, effective date, ratification procedure, nor normative effect.

## 7. Required next actions

1. Inspect the OpenSSH observation report and record exact result/exit code for each candidate signature. If any source blob/digest pin differs, stop and refresh the source baseline before interpreting signature results.
2. Establish whether the Article XI amendment procedure was followed by retrieving the corresponding RFC, Architecture Review, impact analysis, dependent-document updates, and approval at immutable revisions. PR #32's draft finding is not itself a binding adjudication.
3. Resolve the “canonical repository” predicate with a competent primary source independent of the declaration being evaluated.
4. Obtain independent issuer-to-person/key binding and evidence of current holder continuity; a repository-sourced `allowed_signers` file is not an external trust anchor.
5. Reconcile Genesis scope against the exact appointment power in Article XIII and the broad powers asserted in the Genesis Declaration.
6. Reconcile the P-008 record's `PENDING_EXECUTION` and `EFFECTIVE` declarations against the signed exact content and any competent execution/ratification event.
7. Keep M1, P-008, implementation authorization, and WP-3 blocked pending the competent procedure. Preserve all historic and current bytes, signatures, commits, and failed verification outputs.

## 8. Limits and disposition

This inventory is read-only with respect to the candidate `Aura-IDToken` and `vaidt` source repositories. It does not ratify, revoke, supersede, or amend any source act. It does not establish civil identity or external-law validity, and it does not close G0, M1, P-008, DQ-006, or any implementation authorization.

**Disposition:** `CANDIDATE GENESIS ACT FOUND · ISSUER COMPETENCE NOT PROVEN · IDENTITY CONTINUITY NOT PROVEN · ARTICLE XIII PROCEDURAL EFFECT NOT ESTABLISHED FROM SOURCES REVIEWED · M1 BLOCKED · WP-3 BLOCKED`.

## Related records

- [M1 Authority Adjudication Intake v0.1](M1_AUTHORITY_ADJUDICATION_INTAKE_v0.1.md)
- [AURA-AUTHORITY-001 Identity Bridge Draft v0.3](https://github.com/vaidt/aura-specification/blob/main/docs/governance/AURA-AUTHORITY-001-IDENTITY-BRIDGE-DRAFT-v0.3.md)
- [AURA-ACT-001 Crisis Resolution Draft](https://github.com/vaidt/aura-specification/blob/main/docs/governance/AURA-ACT-001-CRISIS-RESOLUTION.md)
- [PR #32 — Audit G1: Genesis SSHSIG verification and Article XIII source review](https://github.com/vaidt/aura-specification/pull/32)
- [WP-1 Issue #2](https://github.com/vaidt/Projekt-Aura-BETA-/issues/2)
- [Draft PR #1](https://github.com/vaidt/Projekt-Aura-BETA-/pull/1)
