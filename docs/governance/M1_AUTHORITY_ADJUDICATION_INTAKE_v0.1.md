# AURA BETA — M1 Authority Adjudication Intake v0.1

**Record ID:** BETA-GOV-M1-AUTH-INTAKE-0001  
**Status:** INTAKE ONLY · NOT ADJUDICATED · NON-CONSTITUTIVE  
**Observed date:** 2026-10-20  
**Workspace:** `vaidt/Projekt-Aura-BETA-`, branch `alpha/bootstrap-architecture`  
**Related control:** WP-1 / G0 Authority Continuity / M1 status  
**Normative effect:** NONE

## 1. Purpose and decision boundary

This record prepares an evidence intake for a competent authority to decide the authority-continuity and M1-effectiveness questions. It does not appoint an office holder, ratify P-008, close M1, revoke a historical act, select a normative source, or authorize implementation.

The default disposition remains:

- Authority Continuity: **NOT PROVEN**
- M1 governance: **BLOCKED**
- P-008: **PROPOSED / RATIFICATION NOT ESTABLISHED**
- Implementation authorization: **NOT GRANTED**
- WP-3: **BLOCKED**
- BETA: operational coordination and engineering workspace only; normative effect **NONE**

This disposition is a conservative evidence status, not a finding that a particular person lacks authority. A status can change only on admissible evidence from a competent process.

## 2. Governing evidence discipline

The workspace rules require distinct treatment of artifact availability, verification result, audit coverage, and governance state. In particular:

- Presence of a document does not authenticate its author or establish authority.
- A repository account name, commit, workflow result, or assertion in a document does not by itself establish ratification.
- A cryptographic PASS establishes a result only for the specified bytes, key input, algorithm, and procedure. It does not itself establish the key holder's constitutional competence.
- `EXHAUSTED_WITHIN_SCOPE` is not equivalent to `RESOLVED`.
- No result from this intake can be used as a self-issued normative act by BETA.

No additional constitutional rule is assumed here. If the governing constitution, appointment procedure, or ratification procedure is unavailable, that missing primary source must be recorded rather than reconstructed by inference.

## 3. Intake items reviewed

### 3.1 Conversation-provided file: `Authority Kamil Krasiński Aura-IDToken.md`

The uploaded file asserts, among other things, that its issuer is the project creator/owner, that Kamil Krasiński is the current Chief Architect effective 2026-09-21, that the scope covers architecture and specification, and that ratification powers include P-001, P-002, P-003 and P-008. It also asserts that this instrument closes G0.

- SHA-256 of the received bytes: `4f1e9cc18c3a7cbdbbf5abcd2378d9159e2c4aec4837f029de049fb3cb0c1c03`
- Source URI / repository path / immutable source revision: **NOT PROVIDED**
- Cryptographic signature over these exact bytes: **NOT PROVIDED**
- Independent binding from the named issuer to a competent appointment power: **NOT ESTABLISHED**
- Independent identity/key binding and evidence of current validity: **NOT ESTABLISHED**

The digest identifies the exact attachment received for this intake. It does not authenticate authorship or make the file a constitutive instrument. The file's assertion that it closes G0 is a claim to be assessed, not a result accepted by this record.

### 3.2 Conversation-provided file: `AURA — WAVE 1 — Contract Closure Addendum v1.pdf`

- SHA-256 of the received bytes: `fb226496f441bb35e183ff132b7661412f09cde9dc3841f6ab13c38cb2109e1b`
- Document class: Engineering Contract / Closure Addendum
- Stated status: `PROPOSED / WORKING DRAFT`
- Stated normative effect: `NONE`
- Stated governance status: `BLOCKED / NOT ESTABLISHED`
- Stated constitutive authority: `NONE`

The addendum explicitly excludes P-008 ratification, DQ-006 governance closure, M1 closure, G0 authority continuity, protocol certification, and implementation authorization from its scope. It therefore cannot be used as proof that any of those governance gates is closed. Its boundary statements are consistent with maintaining separation between engineering closure and constitutive authority.

### 3.3 M1 exact-byte signature evidence

The OpenSSH verification is recorded in [workflow run #39456930057](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39456930057), with repeat checks in [#39468107358](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39468107358) and [#39468369882](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39468369882).

Observed result:

- Historical M1 Markdown at commit `6028ceda886db062488b29578d573f5826968d32`: **PASS**, exit code 0.
- Current amended Markdown at source commit `991274eed57d5b3308b0607feeb4d01e6a485974`: **FAIL**, exit code 255, `Signature verification failed: incorrect signature`.
- Historical and current signature files and `allowed_signers` fixtures are byte-identical in the pinned input set; the Markdown bytes differ.
- Most recent inspected CI run #39468369882: schema validation job **PASS**; strict M1 signature gate **FAIL**; aggregate workflow **FAIL**.

This proves a signature-to-bytes mismatch for the current Markdown under the tested public-key input. The `allowed_signers` source is repository history; it has not independently established the key holder's constitutional competence. A mismatch alone does not determine the legal or constitutional effect of the historical act.

## 4. Missing evidence required before adjudication

The following items are **not established by the intake reviewed here**. A competent reviewer should bind each item to an exact primary source and revision.

| Gate | Required evidence | Current status |
|---|---|---|
| Primary authority source | The applicable constitution, governance rule, appointment instrument, or delegation instrument, with exact source URI and immutable revision | NOT PROVIDED / NOT ESTABLISHED |
| Issuer competence | Evidence that the issuer had authority to appoint the named role or make the specified decision | NOT ESTABLISHED |
| Issuer identity | Independently verifiable binding between issuer, account/person or organization, and relevant credential | NOT ESTABLISHED |
| Current holder continuity | Evidence that the holder remained in office or retained the relevant delegation at the decision date | NOT ESTABLISHED |
| Scope | Explicit scope covering the exact question being decided: M1 status, ratification or deprecation, and—separately—P-008 if that decision is requested | NOT ESTABLISHED |
| Effective date and validity | Effective date, duration or continuing-effect rule, and evidence of no effective revocation/supersession within the inspected boundary | NOT ESTABLISHED |
| Signing-key authority | Exact signed payload, signature, algorithm, key fingerprint, and an authority-grounded binding of the key to a competent signer | NOT ESTABLISHED for the current M1 amendment |
| Decision procedure | The governing process, required participants/approvals, and evidence that the required process was followed | NOT PROVIDED / NOT ESTABLISHED |
| Constitutive outcome | A decision record identifying exact subject bytes/revisions, scope, disposition, effective date, issuer and verifiable authentication | NOT ISSUED / NOT ESTABLISHED |

The required chain is:

`Primary source → competent issuer → current holder → decision scope → effective date → current validity → authenticated outcome`

If the governing source does not define one of these requirements, that absence itself must be referred for competent interpretation; BETA must not invent a rule to fill it.

## 5. Adjudication procedure

### Gate A — Evidence admission

Register each candidate source with URI, immutable revision, Git blob or file digest, acquisition time, and custody/provenance notes. Preserve original bytes. A new digest identifies an input; it does not prove authority.

### Gate B — Competence and jurisdiction

A competent reviewer must identify the rule that gives the issuer authority to decide the question and verify the issuer-to-holder chain. Do not infer competence from authorship, ownership claims, repository administration, or a key merely appearing in the same repository.

### Gate C — Defined decision

The competent process must explicitly decide which question is in scope. M1 continuation, M1 re-ratification, M1 deprecation, appointment/authority continuity, and P-008 ratification are distinct decisions. Evidence for one must not silently close another.

### Gate D — Authenticated decision and independent verification

The decision record must bind its exact bytes to the authorized signature and include the decision's scope, effective date, primary authority basis, issuer/holder, and verification instructions. Verification must use a source-bound trust input whose authority basis is documented. Record tool versions, exact inputs, stdout/stderr and exit codes.

### Gate E — BETA status update

Only after the decision's competence, scope, authenticity and current effectiveness are independently established may BETA update its non-normative status mirror. BETA records the source decision; it does not create its effect.

## 6. Permitted dispositions for the competent process

This intake does not choose among these outcomes.

1. **Re-ratification / continuation.** Establish the competent issuer first, approve the exact intended M1 text and status, create an authenticated decision over those exact bytes, and independently verify it. A new signature by an unproven signer is not sufficient.
2. **Formal deprecation and successor record.** Establish the competent issuer and effective deprecation act; preserve the historical M1 bytes, detached signature, and failed current-byte relationship. A successor such as M1-R must have its own clear scope, source authority, effective date, and signature chain.
3. **Insufficient or conflicting evidence.** Retain `NOT PROVEN / BLOCKED`; identify the missing evidence precisely. This is the default until a competent process produces sufficient evidence.

No historical artifact may be overwritten to simulate a clean chain. No rebasing, force-push, silent signature replacement, or protocol implementation is authorized by this intake.

## 7. Stop conditions and acceptance criteria

Keep WP-3 and normative protocol migration blocked until the applicable constitutive decision is established and the separately required protocol contract, implementation authorization, fixtures, and conformance prerequisites are available.

This intake is complete only as an inventory of the items above. It is **not** an adjudication and does not satisfy G0, M1 closure, P-008 ratification, DQ-006 closure, implementation authorization, protocol conformance, or production readiness.

A future adjudication may be accepted only when the record supplies:
- exact primary source revisions and digests;
- evidence of issuer competence and current holder continuity;
- the specific decision scope and current effectiveness basis;
- verifiable authentication of the exact decision bytes;
- an independent review/reproduction record; and
- an explicit disposition, including its boundaries and unresolved questions.

## 8. Related records

- [Alpha Working Mandate](ALPHA_WORKING_MANDATE.md)
- [Status Semantics](STATUS_SEMANTICS.md)
- [Source Baseline & Integrity Findings](../assurance/SOURCE_BASELINE_2026-10-20.md)
- [WP-1 Issue #2](https://github.com/vaidt/Projekt-Aura-BETA-/issues/2)
- [Draft PR #1](https://github.com/vaidt/Projekt-Aura-BETA-/pull/1)

**Final intake state:** `NOT ADJUDICATED · AUTHORITY CONTINUITY NOT PROVEN · M1 BLOCKED`
