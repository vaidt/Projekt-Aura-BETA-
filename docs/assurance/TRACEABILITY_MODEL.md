# Requirement-to-Evidence Traceability Model

**Status:** Draft proposal · non-normative

## Traceability chain

```text
Requirement
  → authoritative source clause + exact revision
  → invariant / trust guarantee
  → approved conformance vector
  → implementation surface
  → execution procedure + verifier version
  → immutable result / artifact + digest
  → scoped finding and governance disposition
```

A missing link is an explicit gap. It must not be filled by a guessed mapping.

## Requirement record

Minimum fields proposed:

- stable `requirement_id`;
- source repository, path, ref/commit, and digest;
- source authority/currentness status and basis;
- exact clause/heading or line range;
- requirement text as retrieved, with a link to the immutable source;
- invariant/trust-guarantee references;
- executability: `EXECUTABLE`, `PARTIALLY_EXECUTABLE`, or `DOCUMENTARY`;
- one or more vector/fixture identifiers and expected outcomes, if authorized;
- implementation surface for each adapter;
- test procedure and verifier version;
- associated evidence records;
- known conflicts, assumptions, and excluded coverage;
- requirement state and transition rationale.

## Gap classifications

Use one primary classification and permit secondary tags:

- `SPECIFICATION_GAP` — meaning or contract is incomplete/ambiguous/conflicted.
- `GOVERNANCE_GAP` — authority, approval, scope, or effective status is not established.
- `TEST_GAP` — a requirement lacks a valid test/vector or negative case.
- `IMPLEMENTATION_GAP` — an implementation demonstrably violates a verified requirement.
- `EVIDENCE_GAP` — the required source or result is missing, stale, inaccessible, or unbound.
- `INTEGRATION_GAP` — components lack a tested contract/interface.
- `OPEN_QUESTION` — a decision is needed but there is not enough evidence to classify it more specifically.

Do not automatically classify every mismatch as an implementation bug. First validate the source contract, source revision, and expected result.

## Independence criteria

A conformance outcome is not independent if:
- expected output is copied from the implementation under test;
- the same implementation is the only oracle and the only verifier;
- fixtures are generated from the code being evaluated without an independently approved baseline;
- the verifier does not bind its result to inputs and version;
- the UI can manually override PASS/FAIL without an attributable, controlled decision record.

## Completion rule

Mark a requirement as verified only when the current authoritative contract is established, traceability is complete for the declared scope, applicable vectors and expected results are approved, the named check ran against identified inputs, and the result artifact is available. This BETA workflow rule does not itself establish protocol conformance or replace AURA's normative governance process.
