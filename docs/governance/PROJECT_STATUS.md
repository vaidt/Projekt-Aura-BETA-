# AURA BETA — Project Status Register

**Record ID:** BETA-STATUS-0001  
**Recorded:** 2026-10-20  
**Status:** WORKING BASELINE · NON-NORMATIVE  
**Repository:** `vaidt/Projekt-Aura-BETA-`  
**Branch for this proposal:** `alpha/bootstrap-architecture`

## 1. Workspace state verified during bootstrap

| Item | Observation | Interpretation |
|---|---|---|
| Repository | Public repository found as `vaidt/Projekt-Aura-BETA-` | The actual GitHub name includes a trailing hyphen |
| Initial state | Empty repository before bootstrap | No previous code or Git history was available to preserve |
| Default branch | `main` | One minimal bootstrap README was created on `main` to initialize the empty repository |
| Work branch | `alpha/bootstrap-architecture` | Additional architecture and governance proposal belongs in a PR |
| Product/runtime | Not present at bootstrap | No implementation or operational behavior is claimed |
| CI/conformance at bootstrap | Not verified and not yet established | This records the initial empty-repository state; subsequent schema CI is documented in §7 |

The URL supplied in the request omitted the trailing hyphen. This record uses the repository name returned by GitHub. Renaming the repository is outside this change.

## 2. Inherited AURA baseline — requires fresh source verification

The following positions are inherited from supplied project records and prior analysis. They are **not a claim that all source repositories were re-checked on 2026-10-20**.

| Topic | Inherited position | Required treatment in BETA |
|---|---|---|
| M1 reconstruction | EXHAUSTED | Treat as completion of reconstruction only, not closure |
| Evidence disposition | COMPLETE in the prior record | Re-check source coverage, revisions, and disposition before relying on it |
| Authority continuity | NOT PROVEN in the prior record | Keep governance closure blocked until constitutive authority evidence is verified |
| Governance closure | BLOCKED in the prior record | Do not infer closure from a document title, account name, commit, or unsigned declaration |
| P-008 | PROPOSED / BLOCKED in the prior record | No normative effect and no implementation authorization unless later ratification evidence is established |
| Conformance | Historical records report unresolved specification/fixture/independent-verification gaps | Inventory and verify current source state before calculating live status |

Historical material can inform work planning; it cannot, by itself, establish currentness, authority, or normative effect.

## 3. Operating state

The workspace starts in **DESIGN / INVENTORY**, not implementation delivery.

Permitted now:
- repository structure, source inventory, architecture proposals, evidence/status schemas, traceability design, and test strategy;
- read-only examination of existing AURA sources;
- explicit marking of unknowns, conflicts, inaccessible material, and stale evidence.

Not permitted by this baseline:
- silently promoting this repository or its documents to canonical protocol status;
- declaring unresolved P-008 or another decision ratified;
- treating the dashboard, its counts, or the implementation as the authority for conformance;
- broad rewrites of existing reference implementations before contract-to-implementation gaps are established.

## 4. Exit criteria for the bootstrap stage

- [ ] Owner confirms the intended repository name, including whether the trailing hyphen is intentional.
- [ ] Source repositories are inventoried with branch, commit SHA, and authority/currentness status.
- [ ] Governance and normative source precedence is mapped without assuming contested links.
- [ ] The evidence record and status vocabulary receive review.
- [ ] Architecture and implementation boundaries are approved for the next stage.
- [ ] First conformance work package is tied to verified requirements and independently checkable vectors.

## 5. Decision discipline

Status changes require new, source-bound evidence. A report's existence does not make its claims current. An exhaustive search does not resolve an authority gap. Each future status update must identify the previous status, new evidence, verification method, reviewer, effective scope, and reason for the transition.


## 6. Fresh partial source review — 2026-10-20

A bounded source review was performed after the initial baseline was drafted. It covered current HEADs and selected workflow runs for candidate specification, implementation, and conformance repositories, plus a detached-signature-to-exact-bytes check for the M1 closure record.

The results are recorded separately in [SOURCE_BASELINE_2026-10-20.md](../assurance/SOURCE_BASELINE_2026-10-20.md). Material findings:

- two specification repositories retain the same canonical-source claim in their README while pointing to different `main` commits;
- the inspected `Draft Conformance` runs differ (success on the `vaidt` source HEAD; failure on the `Aura-IDToken` source HEAD);
- the attached M1 SSH signature verifies the historical exact Markdown bytes but fails against the current amended bytes;
- the current DQ-006 closure package states `OPEN`; the broader governance conflict is not resolved by the signature check.

This was a bounded inspection, not exhaustive Git history reconstruction and not a final authority adjudication. Current status disposition remains **CONFLICTED / NOT PROVEN pending independent review and the competent governance process**.


## 7. Current operational consolidation and validation status — 2026-10-20

### Repository consolidation

BETA is the operational coordination and assurance target for new AURA project work. Three older `kamilkrasinski4-sys` repositories received root `MIGRATION_NOTICE.md` files on `main` and were then archived. GitHub archive metadata was re-read and confirmed `archived=true` for each:

- [`kamilkrasinski4-sys/aura-specification`](https://github.com/kamilkrasinski4-sys/aura-specification) — baseline `528de0de6d34a4a7ff541db9cd93238587dac9ef`; notice commit [`a39f58a`](https://github.com/kamilkrasinski4-sys/aura-specification/commit/a39f58a603b6a682ae70be1f0141a7a7bf48415e).
- [`kamilkrasinski4-sys/aura-guard-v1.3`](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3) — baseline `35082d7b4880dad780fb55a1a5f3ac0ef4322674`; notice commit [`27fcd82`](https://github.com/kamilkrasinski4-sys/aura-guard-v1.3/commit/27fcd82988a81e60e4f1866f394cb7ca371aa131).
- [`kamilkrasinski4-sys/aura-poc-a-core-v3.3`](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3) — baseline `43f054f8deb7c9644c52148d6496b493512d32b0`; notice commit [`96ad5e5`](https://github.com/kamilkrasinski4-sys/aura-poc-a-core-v3.3/commit/96ad5e5f310f1c71a30d9ce7decc4f04bdfbafed).

Machine-readable archive evidence records are under `evidence/registry/EVID-MIG-ARCHIVE-*.json`. No archived repository content was deleted.

The `kamilkrasinski4-sys/aura-p0-0-toolchain` remains active pending role/dependency review. The inspected `Aura-IDToken` repositories remain unarchived because the active connection is read-only; owner-authorized mutation access is required. Current `vaidt` source/product/conformance repositories were not bulk-archived.

### Evidence schema gate

[Evidence Schema Validation, PR run #39454759685](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39454759685) returned **SUCCESS** on commit `160ae35a0b87e040d94a185ea3fd55d20a8b813a`. The job verified pinned schema blob SHAs, compiled the registry schema and pinned APS-300 Evidence Object / Evidence Pack draft schemas, accepted the valid fixture, rejected missing-field and extra-property fixtures, and validated all five JSON files under `evidence/registry/`.

This is a schema-structure PASS for a specific workflow run, not a conformance or governance PASS. The upstream APS-300 text and schema snapshots identify themselves as DRAFT. No live collector is connected or authorized by this status record.

### Current gate disposition

- Operational project coordination target: BETA.
- Absolute normative protocol SSoT: NOT ESTABLISHED.
- M1 closure / authority continuity: CONFLICTED / NOT PROVEN pending independent reproduction and competent governance disposition.
- Schema-validation CI: PASS at the specific run and source revision cited above.
- Live collection: NOT STARTED / BLOCKED until source inventory, authority scope, and contracts are reviewable.
