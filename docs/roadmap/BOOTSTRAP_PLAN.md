# AURA BETA — Bootstrap Plan

**Status:** DRAFT · NON-NORMATIVE · Working plan only  
**Baseline date:** 2026-10-20  
**Branch:** beta/architecture-baseline-001

## Purpose

Establish a controlled, inspectable engineering workspace before adding protocol-facing implementation. This plan does not assert that any milestone is complete and does not authorize normative protocol changes.

## Work packages

### B0 — Repository baseline and hygiene
- Inventory the default branch, files, workflows, branch protections where accessible, and current commit.
- Resolve README links to documents that exist at the referenced paths.
- Record baseline revision and a tree/file inventory.
- Acceptance: findings are revision-bound; missing files and inaccessible controls are explicitly reported.

### B1 — Governance and source inventory
- Catalogue candidate specification, governance, implementation, fixture, and evidence sources.
- Record source revision, status, provenance, and known authority limitations.
- Preserve unresolved authority and decision gaps; do not infer ratification.
- Acceptance: every source entry distinguishes existence, reachability, currency, authority, normative status, and effect where known.

### B2 — Evidence and traceability model
- Propose a workspace-level evidence envelope and traceability relationships.
- Define schema validation and negative tests for missing provenance, unknown status, and incomplete coverage.
- Acceptance: malformed or incomplete evidence cannot be silently represented as verified.

### B3 — Minimal independent verification runner
- Define an explicit input manifest and deterministic runner interface.
- Keep the verifier separate from implementation-under-test adapters.
- Preserve stdout/stderr, toolchain identity, exit status, inputs, and output digests as evidence.
- Acceptance: reproducible local run and negative tests; no normative claim implied.

### B4 — Implementation adapters and conformance matrix
- Add adapters only after contract inputs and result semantics are established by authoritative sources.
- Map each check to a source requirement, test/vector, implementation, and evidence record.
- Acceptance: all gaps remain visible; unresolved protocol decisions block affected conformance claims.

### B5 — Operator interface and release evidence
- Build a UI only after the evidence and state model is testable.
- Ensure every badge/status links to revision-bound evidence and method.
- Assemble release manifests only after explicit gate criteria and approver roles are established.

## Governance stop conditions

- No implementation of unresolved protocol semantics.
- No P-008 ratification or authority-continuity inference.
- No claim of conformance, certification, production readiness, or regulatory compliance without a scoped evidence package and authorized decision.
- No direct changes to canonical specification repositories from this workspace plan.
- No merge to main or release solely because CI is green.

## Immediate sequence

1. Review this plan and TARGET_ARCHITECTURE_v0.1.md.
2. Complete baseline/tree inventory and reconcile referenced-but-missing documentation.
3. Create a source and authority inventory with evidence links.
4. Propose and test the evidence envelope.
5. Only then select the smallest executable vertical slice.

## Reporting format

Each work package report must state: status; repository and revision; scope; actions performed; evidence links/digests; findings; limitations; risks; decision needed; and whether any normative effect exists.