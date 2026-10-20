# AURA BETA — Target Architecture v0.1 (Proposal)

**Status:** DRAFT · NON-NORMATIVE · NOT RATIFIED  
**Scope:** Engineering workspace architecture only  
**Protocol authority:** None conferred by this document  
**Change control:** Topic branch + pull request + review

## 1. Decision

AURA BETA will be designed as an evidence-oriented integration and assurance workspace around existing AURA specifications and implementations. It will not become a replacement specification, protocol authority, or source of protocol semantics.

The system should make claims inspectable and revision-bound. It must never infer normative authority from repository location, recency, successful tests, UI status, or implementation behavior.

## 2. Architectural boundaries

1. **Source intake:** discover and record candidate specifications, governance records, implementation revisions, fixtures, and test outputs.
2. **Contract inventory:** extract requirements and references while preserving source location, revision, and authority status. Extraction is not ratification.
3. **Traceability graph:** link each requirement to implementations, tests, vectors, evidence, and unresolved decisions. Missing links remain explicit.
4. **Conformance runner:** execute deterministic, versioned checks against approved inputs. The runner reports observations; it does not authorize protocol semantics.
5. **Evidence registry:** preserve source revision, content digest, method/tool version, execution context, result, coverage, and provenance.
6. **Assurance evaluation:** apply only explicitly approved acceptance rules; represent unresolved or inapplicable cases without silently converting them to pass.
7. **Control-plane UI/API:** present evidence and permit bounded operator actions. Presentation state is not authoritative evidence.
8. **Release gate:** assemble a revision-bound package and report whether each declared release criterion has supporting evidence.

## 3. Trust boundaries

- Source repositories are inputs, not automatically authoritative merely because they are connected.
- Imported documents retain their original provenance and status.
- The conformance runner is separate from the implementation under test.
- Evidence records are immutable once finalized; corrections create a new revision or superseding record.
- UI/API services cannot edit finalized evidence or manufacture verification results.
- Credentials and signing keys must not be stored in repository content or logs.
- Any external/network access must be explicit, logged, and separable from offline deterministic verification.

## 4. Canonical evidence envelope (proposal)

Each evidence record should carry at least:

- evidence_id
- subject and claim_scope
- source_uri or repository/path
- source_revision (commit, tag, or immutable identifier)
- content_digest and digest algorithm
- method_id, method_version, and toolchain identity
- execution_context (including platform where relevant)
- observed_result and result vocabulary version
- coverage and omitted/unexecuted cases
- created_at (metadata only; never used to determine authority)
- supersedes or correction linkage, when applicable

This envelope is a design proposal. It does not define protocol-level serialization, hashing, signatures, or normative result semantics.

## 5. Non-goals

- Ratifying unresolved protocol decisions, including P-008.
- Establishing authority continuity or appointing a Protocol Custodian.
- Replacing the canonical specification repository.
- Claiming certification, regulatory compliance, or production readiness.
- Treating green CI, passing tests, or dashboard badges as sufficient proof of conformance.
- Implementing protocol behavior before its governing contract is established.

## 6. Initial implementation order

1. Inventory repository contents and establish a revision-bound baseline.
2. Define the source/authority/status inventory schema as a non-normative workspace model.
3. Build traceability and gap reporting before a conformance verdict engine.
4. Define the evidence envelope and validation tests.
5. Add a minimal independent runner with explicit input manifests.
6. Add adapters only after input/output contracts are documented.
7. Add a UI after the evidence model and state transitions are testable.

## 7. Acceptance criteria for this architecture proposal

- Every displayed claim resolves to a specific source revision and evidence record, or is explicitly marked unverified.
- Unresolved authority and contract decisions remain visible blockers.
- The runner cannot silently translate unknown/unresolved states into PASS.
- Results can be reproduced from a declared manifest and toolchain.
- The UI cannot create or modify evidence as a side effect of presentation.
- Changes to this proposal are reviewed through a pull request and do not imply protocol ratification.

## 8. Open questions

- Which source repositories and refs are currently authorized as inputs, and who can attest to that scope?
- Which result vocabulary is already approved versus merely proposed?
- What is the minimum offline execution environment?
- Which evidence artifacts require cryptographic signatures, and under what authority?
- What retention and correction policy applies to evidence records?
- What are the exact release-gate criteria and their approving authority?

Until these questions are resolved by suitable evidence and authorized decisions, this document remains a design proposal only.