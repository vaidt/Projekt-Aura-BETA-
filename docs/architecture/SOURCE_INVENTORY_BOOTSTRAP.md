# AURA BETA — Initial Source Inventory

**Status:** Initial discovery plan · not a verified source-of-truth register  
**Recorded:** 2026-10-20  
**Rule:** Every entry below is a candidate source until its current branch, commit, contents, authority role, and accessibility have been independently re-checked.

| Candidate source | Intended inspection purpose | Initial classification | Verification still required |
|---|---|---|---|
| https://github.com/vaidt/aura-specification | Current specification and governance artifacts | Candidate specification source | Default branch, HEAD, canonicality claim, key document statuses, conflicts |
| https://github.com/Aura-IDToken/aura-specification | Parallel specification history and possible competing source claim | Candidate / conflict-sensitive | Default branch, HEAD, overlap and conflicts with the `vaidt` repository |
| https://github.com/vaidt/Aura-vNEXT | Product/core implementation referenced in supplied system-state report | Candidate implementation | Current existence and role, HEAD, CI, tests, implementation/contract bindings |
| https://github.com/vaidt/Aura-Guard | Guard/middleware implementation | Candidate implementation | Current existence and role, HEAD, test/CI status, relation to previous repo names |
| https://github.com/vaidt/aura-guard-v1.3 | Historical Rust middleware and chain-integrity work | Historical/reference candidate | Current HEAD, preserved defects/findings, relation to successor implementations |
| https://github.com/vaidt/Aura-Conformance-Kit | Conformance tooling and fixtures | Candidate verifier/test source | Current HEAD, fixture provenance, verifier independence, actual recent execution results |
| https://github.com/Kamil1230xd/aura-sign-mvp | Historical signing/MVP implementation | Historical/reference candidate | Historical scope, relevant commits, supersession and provenance |
| https://github.com/Aura-IDToken/aura-poc-a-core | Historical PoCA/core implementation | Historical/reference candidate | Historical scope, relevant commits, relation to the current specification and code |

## Evidence required for each source

For every entry, the inventory pass must record:

- repository URL and GitHub-reported full name;
- default branch and exact HEAD commit SHA at retrieval time;
- timestamp of retrieval;
- selected file paths and immutable commit URLs;
- file digest when bytes can be retrieved;
- access/retrieval limitations;
- source role as claimed by that repository;
- independent basis for currentness, authority, normative status, and effective status;
- overlapping or conflicting claims from other repositories;
- reviewer and verification procedure.

## Important limit

A README declaring a repository canonical is evidence that the README makes that declaration. It is not, by itself, proof that the declaration is authoritative or current. The same rule applies to branch names, merged PRs, signatures without trust-root verification, and workflow badges.

This document intentionally does not assign a canonical winner. The initial task is to establish source facts and expose conflicts, not resolve authority by convenience or recency.


## Current operational disposition update — 2026-10-20

The following changes occurred after the original candidate inventory was drafted. The table above is retained as the initial discovery record; these rows supersede its initial disposition for the listed repositories only.

| Repository | Exact pre-notice baseline | Current disposition | Evidence |
|---|---|---|---|
| `kamilkrasinski4-sys/aura-specification` | `528de0de6d34a4a7ff541db9cd93238587dac9ef` | ARCHIVED after root migration notice | [Notice commit](https://github.com/kamilkrasinski4-sys/aura-specification/commit/a39f58a603b6a682ae70be1f0141a7a7bf48415e); [notice](https://github.com/kamilkrasinski4-sys/aura-specification/blob/main/MIGRATION_NOTICE.md); machine record `EVID-MIG-ARCHIVE-AURA-SPECIFICATION` |
| `kamilkrasinski4-sys/aura-guard-v1.3` | `35082d7b4880dad780fb55a1a5f3ac0ef4322674` | ARCHIVED after root migration notice | [Notice commit](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3/commit/27fcd82988a81e60e4f1866f394cb7ca371aa131); [notice](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3/blob/main/MIGRATION_NOTICE.md); machine record `EVID-MIG-ARCHIVE-AURA-GUARD-V1-3` |
| `kamilkrasinski4-sys/aura-poc-a-core-v3.3` | `43f054f8deb7c9644c52148d6496b493512d32b0` | ARCHIVED after root migration notice | [Notice commit](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3/commit/96ad5e5f310f1c71a30d9ce7decc4f04bdfbafed); [notice](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3/blob/main/MIGRATION_NOTICE.md); machine record `EVID-MIG-ARCHIVE-AURA-POC-A-CORE-V3-3` |
| `kamilkrasinski4-sys/aura-p0-0-toolchain` | `main@76a9519137eb87d16aeefb33e9af0757845f7db5` | ACTIVE / not archived | Its most recent observed commit was 2026-10-15; map role and consumers before any archival decision. |
| `Aura-IDToken/aura-specification` | `main@82eba39008a627f1944a32be3ba2ff0c37a1a614` | ACCESS BLOCKED for mutation; not archived | The connected integration is read-only. The repository also retains a canonical-source claim and a different current HEAD from `vaidt/aura-specification`. |
| `Aura-IDToken/aura-poc-a-core-v3.3` | `main@43f054f8deb7c9644c52148d6496b493512d32b0` | ACCESS BLOCKED for mutation; not archived | Owner-authorized write/admin access required before adding a notice or archiving. |

Three archive actions were verified by re-reading GitHub repository metadata after the operation (`archived=true`). The action preserved the repositories and their history; no source code was deleted.

The `vaidt` repositories have not been bulk-archived. Roles, migration completeness, CI dependencies, signed/release artifacts, and reproducibility requirements must be assessed per repository.

## Schema-validation gate — current CI evidence

The GitHub Actions workflow [Evidence Schema Validation, PR run #39454759685](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39454759685) passed on commit `160ae35a0b87e040d94a185ea3fd55d20a8b813a`. It compiled the BETA evidence-registry schema and pinned APS-300 DRAFT schemas, accepted the valid fixture, rejected the two invalid fixtures, verified the schema snapshot Git blob SHAs, and validated all five JSON evidence registry records.

This proves structural validation for that workflow execution and input revision only. The pinned APS-300 material remains DRAFT; CI PASS does not prove protocol conformance or ratification.
