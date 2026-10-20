# AURA BETA — Bootstrap and Delivery Plan

**Status:** Proposed plan · not a release commitment  
**Date:** 2026-10-20

## Guiding choice

Start with the smallest auditable system: source-bound records, traceability, and a deterministic conformance harness. A polished UI is useful only after the statuses it renders have stable meaning and provenance.

## Work packages

### WP-0 — Repository and decision control
**Goal:** establish boundaries and contribution discipline.

Deliverables:
- workspace role and non-normative status;
- status semantics;
- decision log and PR template;
- baseline source inventory;
- visible distinction between inherited and freshly verified facts.

Exit criteria:
- exact target repository identity is recorded;
- no unqualified "canonical", "ratified", "verified", or "production-ready" label exists;
- every open decision has an owner/path to resolution.

### WP-1 — AURA source and authority inventory
**Goal:** identify which current source controls which claim, without inferring authority from repository names.

Deliverables:
- repository/path/revision inventory;
- precedence and conflict register;
- authority and currentness evidence fields;
- source coverage declaration.

Exit criteria:
- every referenced source has an immutable revision or is explicitly marked unbound;
- conflicting canon claims remain visible;
- authority continuity is either supported by constitutive evidence or remains BLOCKED/NOT PROVEN.

### WP-2 — Contract-to-implementation binding matrix
**Goal:** connect requirements to invariants, vectors, code surfaces, and evidence.

Deliverables:
- machine-readable binding matrix;
- executable/partial/documentary classification;
- gap register using defined gap classes;
- testability and independence review.

Exit criteria:
- each in-scope requirement has a source binding;
- missing contract inputs are marked as specification/governance gaps, not patched by code assumptions.

### WP-3 — Minimal Conformance Core
**Goal:** deterministic test runner with independent expected results.

Deliverables:
- versioned input/result schema;
- approved positive and negative vectors;
- no-network evaluation core for deterministic comparisons;
- explicit exit codes and machine-readable report;
- unit and mutation-negative tests.

Exit criteria:
- results bind verifier version, fixture digest, source revision, and execution scope;
- an independent implementation can be evaluated without modifying the oracle;
- incomplete fixtures produce INCONCLUSIVE/BLOCKED, not false PASS.

### WP-4 — Evidence collector and provenance registry
**Goal:** safely obtain and bind external evidence.

Deliverables:
- read-only collectors;
- source revision and artifact-digest binding;
- retrieval failure records;
- append-oriented history and supersession;
- least-privilege permissions.

Exit criteria:
- collection is separate from verification;
- retries and partial coverage do not silently overwrite older observations;
- failures are visible and never converted into negative claims about the target.

### WP-5 — Audit/control-plane prototype
**Goal:** present verifiable state with drill-down rather than decorative badges.

Deliverables:
- overview and three-act narrative;
- evidence registry and gap register;
- requirement traceability;
- explicit coverage and freshness display;
- exportable audit snapshot.

Exit criteria:
- each status has a source trail;
- no manual status override is possible without an audited decision;
- demo/sample data are clearly separated from live evidence;
- empty/inaccessible states are rendered explicitly.

### WP-6 — Release and operational readiness
**Goal:** package and independently review the system.

Deliverables:
- threat model, data-flow map, security review;
- reproducibility and cross-implementation tests;
- artifact manifest/checksums and release report;
- operational and rollback procedure.

Exit criteria:
- all applicable critical invariants are bound to evidence;
- blocking gaps are either resolved with evidence or explicitly accepted by competent authority;
- release claims match observed test and scope results.

## Recommended execution order

```text
WP-0 → WP-1 → WP-2 → WP-3 → WP-4 → WP-5 → WP-6
```

Some UI wireframing may proceed in parallel, but it must use labelled sample state and cannot be represented as a live audit before collectors and verifiers exist.

## Immediate next actions

1. Obtain a current read-only snapshot of candidate AURA source repositories and workflows.
2. Confirm whether `vaidt/Projekt-Aura-BETA-` is the intended final name.
3. Create the initial source/authority inventory with evidence references and explicit unknowns.
4. Review the evidence schema and status vocabulary.
5. Only then choose the first executable conformance slice.
