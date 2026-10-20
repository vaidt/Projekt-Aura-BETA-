# AURA BETA — Engineering & Assurance Workspace

> **Repository bootstrap:** 2026-10-20  
> **Workspace:** `vaidt/Projekt-Aura-BETA-`  
> **Status:** BOOTSTRAP · NON-NORMATIVE · NO PRODUCT RELEASE CLAIM

## Purpose

AURA BETA is a controlled integration workspace for designing the AURA protocol engineering system: specification-to-implementation traceability, conformance verification, evidence provenance, and an audit/control-plane interface.

This repository is a **working engineering environment**, not a replacement for the existing AURA specification repositories and not, by itself, an authority to ratify protocol semantics.

## Initial operating principle

**Evidence before status; contract before implementation; independent verification before conformance claims.**

The repository follows these distinctions:

- EXISTS ≠ REACHABLE ≠ CURRENT ≠ AUTHORITATIVE ≠ NORMATIVE ≠ EFFECTIVE.
- EXHAUSTED ≠ RESOLVED.
- Implementation behavior does not define protocol semantics.
- A test suite does not become a conformance authority merely by passing.
- A dashboard label is not evidence unless it resolves to inspectable, revision-bound evidence.
- A design proposal has no normative effect unless the required authority and ratification path are independently established.

## Target architecture (proposed; not yet normative)

```text
Existing AURA specifications and governance records
                    │
                    ▼
     Contract & Requirement Inventory
                    │
                    ▼
       Protocol → Implementation Map
                    │
                    ▼
          Independent Conformance Core
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
   Vector / fixture set   Implementation adapters
          │                    │
          └─────────┬──────────┘
                    ▼
       Evidence + provenance registry
                    │
                    ▼
       Audit / control-plane interface
```

The audit interface is a presentation and operator-control layer. It must not become the normative source of truth or decide protocol compliance without a deterministic verification result and a traceable evidence chain.

## Delivery sequence

1. **M0 — Baseline control:** repository role, decision boundaries, evidence model, status vocabulary, change controls.
2. **M1 — Knowledge and governance lock:** source inventory, authority/precedence map, unresolved decision register; no inferred ratification.
3. **M2 — Golden-vector preparation:** identify contract decisions that block vector freeze; only freeze vectors after the required normative inputs are approved.
4. **M3 — Conformance closure:** independent runner, deterministic fixtures, traceability, negative cases.
5. **M4 — Protocol release preparation:** manifest, reproducible evidence, release gates.
6. **M5–M8 — Hardening and operational readiness:** security, failure/load behavior, release verification, operational controls.

This is a planning baseline. It does not assert that any milestone is complete.

## Repository layout

- `docs/governance/` — governance posture, authority boundary, decision log.
- `docs/architecture/` — target architecture and architecture decisions.
- `docs/assurance/` — evidence model, conformance and traceability.
- `docs/roadmap/` — milestone plan and exit criteria.
- `schemas/` — draft machine-readable schemas; non-normative until approved.
- `tests/` — tests for repository tooling and conformance harness as it is introduced.

## Current limits

At bootstrap, no product implementation, evidence collector, verifier, data store, UI, or CI result has been independently verified in this repository. No conformance, production readiness, or regulatory compliance claim is authorized by this README.

## Change discipline

- Make changes on a topic branch and submit a pull request.
- Every material decision must state its status, scope, rationale, evidence, and normative effect.
- Do not copy a document into this repository and silently promote it to canonical.
- Do not encode unresolved protocol decisions in implementation defaults.
- Do not merge or release solely because CI is green; review the contract and evidence scope.
- Preserve source revision, content digest, verification method, result, and coverage for any claim presented as verified.

## First review target

See [Bootstrap Plan](docs/roadmap/BOOTSTRAP_PLAN.md), [Governance Status](docs/governance/PROJECT_STATUS.md), and [Target Architecture](docs/architecture/TARGET_ARCHITECTURE.md). These are engineering proposals, not ratified protocol requirements.
