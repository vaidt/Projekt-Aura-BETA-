# AURA Repository Consolidation Plan

**Record:** BETA-CONSOLIDATION-PLAN-0001  
**Status:** ACTIVE PLANNING · NO ARCHIVE ACTION CLAIMED  
**Date:** 2026-10-20T15:57:53.380Z

## 1. Target

Use `vaidt/Projekt-Aura-BETA-` as the single operational entry point for new cross-repository planning, audit, source inventory, and consolidation tracking.

Do not equate the project-workspace target with proven normative authority over the protocol. The latter remains blocked by source/authority conflicts.

## 2. Repository inventory and first disposition

The following set is a candidate inventory, not an exhaustive account inventory.

| Repository | Observed role / reason to retain | Initial disposition | Access observed by GitHub integration |
|---|---|---|---|
| `vaidt/Projekt-Aura-BETA-` | Consolidation, traceability, assurance workspace | TARGET | Admin / write |
| `vaidt/aura-specification` | Current spec/governance records; M1, DQ-006 and source conflicts remain active evidence | KEEP AVAILABLE; do not archive before controlled migration and governance review | Admin / write |
| `Aura-IDToken/aura-specification` | Competing canonical-source claim and historical spec history | MIGRATION CANDIDATE; notice/archive requires owner action | Read-only |
| `kamilkrasinski4-sys/aura-specification` | Additional specification copy / namespace source | MIGRATION CANDIDATE; compare before archive | Read-only |
| `vaidt/Aura-vNEXT` | New product implementation; README states an implementation role for its repository scope | RETAIN FOR NOW; inspect source/contract boundary before any archive | Admin / write |
| `vaidt/Aura-Guard` | Current Guard-named repository with CodeQL workflow, but README content is not a product description | REVIEW ROLE; do not archive based on name alone | Admin / write |
| `vaidt/aura-guard-v1.3` | Rust middleware, recent chain-integrity change and CI history | LEGACY CANDIDATE; preserve tests/evidence and migrate before archive | Admin / write |
| `vaidt/aura-poc-a-core-v3.3` | Historical Iron Core, referenced by current/legacy records | LEGACY CANDIDATE; preserve reproducible baselines before archive | Admin / write |
| `Aura-IDToken/aura-poc-a-core-v3.3` | Historical core source and execution history | MIGRATION CANDIDATE; notice/archive requires owner action | Read-only |
| `kamilkrasinski4-sys/aura-poc-a-core-v3.3` | Additional core copy | MIGRATION CANDIDATE; compare tree/history before archive | Read-only |
| `vaidt/Aura-Conformance-Kit` | Conformance kit with workflow evidence | RETAIN UNTIL TCK/fixture migration and independent reproduction | Admin / write |
| `kamilkrasinski4-sys/aura-guard-v1.3` | Additional middleware copy | MIGRATION CANDIDATE; compare tree/history before archive | Read-only |
| `kamilkrasinski4-sys/aura-p0-0-toolchain` | M0/P0 toolchain repository | ROLE REVIEW REQUIRED before archive | Read-only |
| `Kamil1230xd/aura-sign-mvp` | Historical experimental signing/MVP repository | HISTORICAL CANDIDATE; preserve exact source and provenance | Read-only |

Repository inventory must be refreshed before operational changes. The table is not an instruction to archive every listed repository: explicit role and dependency checks are prerequisites.

## 3. Rules for migration notices

A notice in a legacy repository must:
- state that the repository is read-only/historical or superseded, only when that status is authorized and factually correct;
- link to this BETA destination;
- preserve the old repo name, source HEAD SHA, relevant release/tag links, and date of migration;
- state where code, schemas, fixtures, workflows, reports and release artifacts moved;
- state what was not migrated or independently verified;
- avoid saying "official", "ratified", "canonical" or "superseded" without the appropriate basis.

Do not insert notices into repositories that the connected identity cannot mutate. Prepare a migration PR for owner review or provide a patch for the repository owner.

## 4. Archive gates

Repository archiving is deferred until all applicable checks pass:

- [ ] Migration notice merged into each target repo's default branch.
- [ ] Source snapshot and all signed artifacts are preserved and digest-checked.
- [ ] Material issues, PRs, branches, release tags and workflow artifacts have been inventoried.
- [ ] Consumers and CI dependencies have been identified.
- [ ] Required conformance runs can still be reproduced from BETA or a preserved immutable source snapshot.
- [ ] Repository owner/admin and permissions are verified.
- [ ] Archive operation is authorized and its exact target enumerated.
- [ ] Post-archive links and evidence resolution are checked.

## 5. Decision on "absolute SSoT"

**Adopted for workspace coordination:** BETA is the intended single operational entry point for new project-level consolidation work.

**Not established by this plan:** BETA as the sole absolute normative source of the AURA protocol. The source corpus currently includes duplicate canonical-source claims, a draft APS-300 model, unresolved governance dispositions and a signature-to-current-bytes mismatch. The operational workspace cannot resolve those by declaration alone.

## 6. Immediate follow-up

Issue [WP-1 — Verify AURA source authority, M1 signature binding, and current conformance baseline](https://github.com/vaidt/Projekt-Aura-BETA-/issues/2) remains the controlling evidence task. The first migration package should include a source/digest manifest, conflict register, and verified migration notices before any archive operation.
