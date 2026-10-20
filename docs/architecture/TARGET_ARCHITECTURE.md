# AURA BETA — Target Architecture

**Status:** Architecture proposal · review required · non-normative  
**Version:** 0.1.0-draft  
**Last updated:** 2026-10-20

## Architectural objective

Create a small, auditable path from protocol requirements to independent verification and operator-visible evidence. Keep protocol semantics, implementation behavior, evidence collection, verification, governance, and presentation separated.

## Logical layers

### L0 — Source and authority inventory
Inputs: specification repositories, governance records, implementation repositories, CI runs, signed release artifacts, and human decision records.

Each source entry binds repository identity, path, immutable revision/commit, content digest where available, retrieval time, access boundary, claimed role, and authority/currentness disposition.

### L1 — Contract and traceability registry
Maps requirement IDs to source clauses, invariants, vectors, implementations, test procedures, evidence artifacts, known conflicts, and decision dependencies.

It records references and statuses; it must not resolve semantic disagreements by silently selecting the most convenient source.

### L2 — Conformance Core
A deterministic evaluator that consumes explicitly versioned contracts, fixtures, implementation outputs, and verification rules.

Required properties:
- independent oracle and controlled vectors;
- explicit PASS / FAIL / INCONCLUSIVE / NOT_RUN outcomes;
- reproducible input/output binding;
- negative and adversarial cases;
- verifier version and environment identity;
- no use of a product's private tests as sole proof of conformance;
- no network dependency inside the deterministic evaluation core unless a later reviewed requirement expressly needs one.

### L3 — Evidence and provenance registry
Stores or references evidence metadata, immutable digests, verification reports, source revisions, collection methods, timestamps, coverage, reviewers, and supersession relations.

The initial design should be append-oriented. Corrections must create new records or explicit supersession links instead of silently rewriting historical outcomes.

### L4 — Governance gate
Tracks proposals, blocking prerequisites, decision authority evidence, ratification evidence, effective scope, and implementation authorization as separate transitions.

The gate may report that evidence is insufficient. It must not invent a competent issuer, infer continuity, or convert a proposed decision into a ratified one.

### L5 — Audit/control-plane interface
Presents the state derived from L0–L4, including:
- the exact scope last inspected;
- source freshness and failures;
- the evidence trail behind every important badge;
- unresolved gaps and conflicting records;
- drill-down from claim → requirement → evidence → verification run → source revision;
- exportable, reproducible audit snapshots.

The interface is a read model, not a normative authority and not the verification engine.

## Data path

```text
Sources
  → immutable source/revision inventory
  → requirement + invariant traceability
  → controlled fixtures + independent verifier
  → evidence/provenance records
  → governance gates
  → audit/control-plane read model
```

Collection, evaluation, and display must be separable. A collector may retrieve data without validating it; a verifier may validate evidence without ratifying a decision; a UI may display state without authoring it.

## Trust boundaries

1. **Source boundary:** retrieved source contents are untrusted until identity, revision, digest, and role are checked.
2. **Authority boundary:** account ownership and repository write access do not establish constitutional authority.
3. **Verifier boundary:** an implementation under test cannot be the only source of its expected result.
4. **Persistence boundary:** stored status must retain provenance and should be reconstructible from append-oriented records.
5. **Presentation boundary:** labels and colors cannot change the underlying result or upgrade evidence quality.
6. **Network boundary:** external collection is isolated from deterministic core evaluation.

## Initial design decisions still open

- canonical serialization and hash-domain semantics;
- authoritative status and conflict resolution for source repositories;
- schema/version policy for evidence records and conformance bundles;
- required signature/attestation model;
- supported implementation adapters and cross-language test contract;
- storage and UI technology;
- authentication, authorization, retention, and export policy.

These are not to be filled by implementation defaults. Each needs source evidence, an explicit decision owner, and a documented resolution path.

## Proposed quality attributes

- deterministic evaluation;
- reproducible verification;
- end-to-end provenance;
- least-privilege and read-only collection by default;
- no silent state transitions;
- explicit unknown/blocked states;
- testable interfaces between components;
- versioned schemas and backward-compatible migration policy.

## Scope of the first implementation

Do not start with a distributed platform. First establish the source inventory, data contracts, traceability, golden-vector governance, and a local deterministic conformance runner. Add connectors and UI only when their contracts can be tested against those foundations.
