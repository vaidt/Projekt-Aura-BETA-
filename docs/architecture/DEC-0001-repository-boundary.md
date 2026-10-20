# DEC-0001 — BETA Repository Boundary

**Status:** ADOPTED FOR WORKSPACE OPERATION ONLY  
**Normative effect on AURA protocol:** NONE  
**Decision date:** 2026-10-20  
**Scope:** Organization of this BETA repository and its engineering process

## Context

AURA work spans specifications, reference implementations, middleware, conformance tooling, historical evidence, and a proposed audit/control-plane interface. A new repository can make integration easier but also creates a risk of accidental duplicate canon or an implementation becoming the de facto source of protocol meaning.

## Decision

1. Treat `vaidt/Projekt-Aura-BETA-` as a **non-canonical integration and design workspace** until the owner establishes a separately evidenced governance decision changing that boundary.
2. Keep normative source documents in their identified source repositories. BETA may reference them using repository, path, revision, digest, and authority status; copied content must be labelled as a snapshot and must not silently become canonical.
3. Implement the conformance evaluator independently from product implementations. The oracle must come from an approved contract and controlled vectors, not from whichever implementation is under test.
4. Treat the audit UI as a read model over source-bound evidence. The UI may not create verification results or ratification status based on presentation logic.
5. Maintain separate evidence, verification, audit-coverage, and governance states as described in `docs/governance/STATUS_SEMANTICS.md`.
6. Do not choose a production database, web framework, or deployment topology until the evidence model, trust boundaries, data-flow requirements, and owner constraints have been reviewed.
7. Prefer small, reviewable PRs and explicit gates over direct changes to the default branch.

## Consequences

- The initial deliverable is a source inventory, architecture boundary, and evidence contract — not a broad code rewrite.
- Any live GitHub collector must be read-only by default and record the exact branch/commit queried.
- Every computed status must be reproducible from identified input records and a named verifier.
- Normative protocol changes remain outside the authority of this workspace until independently ratified through the proper AURA governance process.

## Rejected alternatives

- **Declare BETA the new source of truth at creation:** rejected; no authority or continuity evidence has been established by creating the repository.
- **Copy and edit the entire specification corpus immediately:** rejected; creates duplicate sources and risks status drift.
- **Build dashboard first and manually populate status badges:** rejected; UI state must be downstream of evidence, not a substitute for it.
- **Rewrite implementations before binding requirements to tests:** rejected; would conflate specification gaps with implementation defects.

## Review trigger

Revisit this decision only when a repository-level owner decision, supported by the required governance evidence, explicitly changes the BETA repository's role. A user request to begin engineering work authorizes this workspace to be developed; it does not itself ratify protocol semantics.
