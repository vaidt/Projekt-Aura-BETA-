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
| CI/conformance | Not verified and not yet established | No passing CI or conformance claim is made |

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
