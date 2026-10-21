# ADR-001 — Evidence Boundaries and the Role of AURA BETA

- **Status:** ACCEPTED — BETA operational scope only
- **Decision date:** 2026-10-21
- **Decision class:** Local engineering / workspace architecture
- **Normative protocol effect:** NONE
- **Implementation authorization:** This ADR authorizes only the workspace and CI design described here; it does not authorize changes to frozen protocol semantics.

## Context

AURA work is spread across protocol specifications, reference implementations, middleware, and assurance artifacts. That structure has created ambiguity about where engineering integration is performed and what a passing check actually proves.

The repository's current README establishes AURA BETA as a working integration environment, not a replacement for existing specification repositories and not an authority to ratify protocol semantics. This ADR sharpens that boundary rather than overriding it.

## Decision

### 1. BETA is the operational source of truth for work performed in BETA

For engineering changes explicitly migrated into this repository, BETA is the authoritative workspace for:

- the reviewed change proposal and its Git revision;
- the CI workflow definition and its run records;
- source-migration manifests and provenance notes;
- conformance fixtures, test outputs, and engineering disposition;
- the current integration status of the migrated components.

Changes are made on topic branches and submitted as pull requests. No direct push to main, automatic merge, or implicit promotion of imported documents to canonical status is authorized by this ADR.

This operational ownership does **not** make BETA the sole constitutional or normative source of the AURA protocol.

### 2. Evidence classes remain separate

No evidence class implies another. In particular:

1. **Presence / reachability:** an artifact can be found at a path or through a Git reference.
2. **Byte integrity:** a digest matches the exact bytes examined.
3. **Cryptographic validity:** a signature verifies under a specified key and verification procedure.
4. **Semantic conformance:** a revision passes the applicable protocol contract and independent conformance vectors.
5. **Governance authority:** the relevant issuer, holder, scope, effective date, and current validity are established by competent constitutive evidence.
6. **Normative effect:** a decision has been ratified through the applicable authority and procedure.

A green CI job proves only the checks and inputs stated by that job. It does not, by itself, prove protocol conformance, signer competence, authority continuity, ratification, regulatory compliance, or production readiness.

### 3. The interface is a read model, not a verifier

Any dashboard or control-plane UI in BETA is a presentation layer. It must link status labels to inspectable, revision-bound evidence and must not independently infer compliance or governance state.

### 4. The first Python CI gate fails closed

The Full pytest suite workflow must install its declared test dependencies, verify the imports, install the migrated Core project, run its tests, and retain a test report. If core/pyproject.toml or actual test files are absent, the job must fail with an explicit migration error. A skipped or empty test suite must never be reported as a successful Core test run.

The workflow's dependency bootstrap currently installs pytest and rfc8785 as requested. The latter must remain only while the migrated code or test contract actually requires it; dependency minimization and the committed dependency declaration/lock strategy are follow-up acceptance items.

### 5. DQ-006 and protocol governance are not silently ratified here

This ADR resolves the **operational workspace boundary** for new BETA engineering changes: changes migrated into BETA are integrated and verified here rather than waiting for a code change to be accepted by an external implementation repository.

It does not close any DQ-006 finding that concerns the canonical normative source, authority continuity, issuer competence, or ratification of protocol semantics. Those questions remain governed by their existing decision and evidence records. They can change only when the required primary / constitutive evidence and competent decision are established. This ADR has no authority to manufacture that evidence.

## Consequences

- BETA can advance local CI, source inventory, conformance tooling, and engineering remediation without waiting for implementation changes in another repository.
- Each imported component must retain its license and record its source provenance, source revision where independently known, and any migration-only changes.
- A migration from an archive without a verified source commit must be labelled as an archive-derived snapshot; it must not be represented as a commit-pinned or reproducible Git migration.
- Protocol-contract changes remain blocked until the existing governance prerequisites are satisfied.
- Security checks such as cargo audit can become merge gates only after the Rust component and its lockfile are imported, the advisory database/input scope is recorded, and the check is configured as a required status check through repository rulesets.
- Branch protection / ruleset configuration and its effective behavior must be verified separately; the existence of this ADR or a workflow file does not prove that protection is active.

## Acceptance criteria

- [ ] The Core source and test suite are present in BETA with provenance and license retained.
- [ ] Full pytest suite executes real tests and records collection / pass / fail counts.
- [ ] CI does not pass when the Core source, test suite, or required dependencies are missing.
- [ ] Required status checks are bound to the intended workflow and verified in repository settings.
- [ ] No report describes a CI result as protocol ratification or conformance without independent, scope-matched evidence.

## Alternatives considered

- **Promote BETA to the sole normative protocol authority immediately:** rejected; an operational repository decision does not establish the required constitutional authority.
- **Wait for changes in another implementation repository before doing any engineering work:** rejected; it unnecessarily couples local CI and migration work to external implementation timing.
- **Use BETA as the operational integration workspace while preserving the normative authority boundary:** selected.

## Review note

The status ACCEPTED applies only to this local workspace architecture. It does not amend the protocol constitution, close M1, ratify P-008, grant implementation authorization for unresolved normative changes, or establish production readiness.
