# AURA Repository Consolidation Plan

**Record:** BETA-CONSOLIDATION-PLAN-0001  
**Status:** ACTIVE PLANNING · PARTIAL ARCHIVAL EXECUTED · REMAINDER BLOCKED  
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
| `kamilkrasinski4-sys/aura-specification` | Historical specification copy; baseline `528de0de6d34a4a7ff541db9cd93238587dac9ef` | ARCHIVED after notice; history preserved | Archive confirmed true |
| `vaidt/Aura-vNEXT` | New product implementation; README states an implementation role for its repository scope | RETAIN FOR NOW; inspect source/contract boundary before any archive | Admin / write |
| `vaidt/Aura-Guard` | Current Guard-named repository with CodeQL workflow, but README content is not a product description | REVIEW ROLE; do not archive based on name alone | Admin / write |
| `vaidt/aura-guard-v1.3` | Rust middleware, recent chain-integrity change and CI history | LEGACY CANDIDATE; preserve tests/evidence and migrate before archive | Admin / write |
| `vaidt/aura-poc-a-core-v3.3` | Historical Iron Core, referenced by current/legacy records | LEGACY CANDIDATE; preserve reproducible baselines before archive | Admin / write |
| `Aura-IDToken/aura-poc-a-core-v3.3` | Historical core source and execution history | MIGRATION CANDIDATE; notice/archive requires owner action | Read-only |
| `kamilkrasinski4-sys/aura-poc-a-core-v3.3` | Historical core copy; baseline `43f054f8deb7c9644c52148d6496b493512d32b0` | ARCHIVED after notice; history preserved | Archive confirmed true |
| `vaidt/Aura-Conformance-Kit` | Conformance kit with workflow evidence | RETAIN UNTIL TCK/fixture migration and independent reproduction | Admin / write |
| `kamilkrasinski4-sys/aura-guard-v1.3` | Historical middleware copy; baseline `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | ARCHIVED after notice; history preserved | Archive confirmed true |
| `kamilkrasinski4-sys/aura-p0-0-toolchain` | M0/P0 toolchain; last observed main commit 2026-10-15 | KEEP ACTIVE pending dependency review | Read-only; not archived |
| `Kamil1230xd/aura-sign-mvp` | Historical experimental signing/MVP repository | HISTORICAL CANDIDATE; preserve exact source and provenance | Read-only |

Repository inventory must be refreshed before operational changes. The table is not an instruction to archive every listed repository: explicit role and dependency checks are prerequisites.

### Completed archive actions — 2026-10-20

Three older copies in the `kamilkrasinski4-sys` namespace received a root `MIGRATION_NOTICE.md` on `main` **before** archival; GitHub subsequently reported `archived: true` for each. The archival action makes those repositories read-only and preserves the repository history; it did not delete code.

| Repository | Pre-notice baseline | Notice commit | Notice |
|---|---|---|---|
| [`kamilkrasinski4-sys/aura-specification`](https://github.com/kamilkrasinski4-sys/aura-specification) | `528de0de6d34a4a7ff541db9cd93238587dac9ef` | [`a39f58a603b6a682ae70be1f0141a7a7bf48415e`](https://github.com/kamilkrasinski4-sys/aura-specification/commit/a39f58a603b6a682ae70be1f0141a7a7bf48415e) | [MIGRATION_NOTICE.md](https://github.com/kamilkrasinski4-sys/aura-specification/blob/main/MIGRATION_NOTICE.md) |
| [`kamilkrasinski4-sys/aura-guard-v1.3`](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3) | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | [`27fcd82988a81e60e4f1866f394cb7ca371aa131`](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3/commit/27fcd82988a81e60e4f1866f394cb7ca371aa131) | [MIGRATION_NOTICE.md](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3/blob/main/MIGRATION_NOTICE.md) |
| [`kamilkrasinski4-sys/aura-poc-a-core-v3.3`](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3) | `43f054f8deb7c9644c52148d6496b493512d32b0` | [`96ad5e5f310f1c71a30d9ce7decc4f04bdfbafed`](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3/commit/96ad5e5f310f1c71a30d9ce7decc4f04bdfbafed) | [MIGRATION_NOTICE.md](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3/blob/main/MIGRATION_NOTICE.md) |

The archive flags were re-read after the changes and confirmed. These notices identify BETA as the operational coordination destination; they do not establish it as the ratified normative protocol source.

The `Aura-IDToken` repository set remains unarchived because the connected integration did not expose write permission for that owner. The `vaidt` repositories have not been bulk-archived: the current spec source, product implementation, conformance kit, and evidence-bearing repositories still need scoped migration and reproducibility review.

## 3. Rules for migration notices

A notice in a legacy repository must:
- state that the repository is read-only/historical or superseded, only when that status is authorized and factually correct;
- link to this BETA destination;
- preserve the old repo name, source HEAD SHA, relevant release/tag links, and date of migration;
- state where code, schemas, fixtures, workflows, reports and release artifacts moved;
- state what was not migrated or independently verified;
- avoid saying "official", "ratified", "canonical" or "superseded" without the appropriate basis.

Do not insert notices into repositories that the connected identity cannot mutate. Prepare a migration PR for owner review or provide a patch for the repository owner. This constraint currently applies to the inspected `Aura-IDToken` repositories; notices and archival were completed for the three selected Kamil-namespace copies listed above.

## 4. Archive gates

Repository archiving for remaining targets is deferred until all applicable checks pass. The three completed actions in §2 are an explicitly bounded first batch, not blanket authorization to archive other repositories:

- [x] Root migration notice committed to main before archival for the three repositories listed in §2.\n- [ ] Migration notices completed for remaining approved targets.
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

Issue [WP-1 — Verify AURA source authority, M1 signature binding, and current conformance baseline](https://github.com/vaidt/Projekt-Aura-BETA-/issues/2) remains the controlling evidence task. The completed three-repository archive batch is now recorded above. Next, obtain owner-authorized access for the Aura-IDToken namespace and complete role/dependency mapping before deciding whether additional repositories can be archived. Keep the active `kamilkrasinski4-sys/aura-p0-0-toolchain` available.
