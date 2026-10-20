# Status Semantics

**Status:** Draft proposal · non-normative · BETA workspace only  
**Purpose:** Prevent unlike kinds of state from being compressed into a single badge.

## Required separation

Every dashboard row, report, and machine-readable export must keep these axes independent.

### A. Evidence availability

| Value | Meaning |
|---|---|
| `PRESENT` | The referenced artifact was retrieved |
| `MISSING` | The expected artifact was not found within the stated search boundary |
| `INACCESSIBLE` | An access or retrieval boundary prevented inspection |
| `STALE` | The artifact is available but does not match the required current revision/window |
| `CONFLICTED` | Sources make incompatible claims or bind to different revisions |

`PRESENT` does not mean valid, authoritative, normative, or effective.

### B. Verification result

| Value | Meaning |
|---|---|
| `PASS` | The named check completed and passed for the stated scope |
| `FAIL` | The named check completed and failed |
| `INCONCLUSIVE` | The check ran but the evidence does not support a verdict |
| `NOT_RUN` | No check execution is evidenced |

Every result must identify its method, scope, verifier version, input revision/digest, and output artifact when applicable.

### C. Audit coverage

| Value | Meaning |
|---|---|
| `NOT_ASSESSED` | Coverage has not been measured |
| `PARTIAL` | Only a documented subset was inspected |
| `EXHAUSTED_WITHIN_SCOPE` | The declared search/inspection plan was completed for a bounded scope |
| `COMPLETE_FOR_REQUIREMENT` | All declared evidence obligations for one requirement were covered and independently checked |

`EXHAUSTED_WITHIN_SCOPE` must never be displayed as `RESOLVED` by implication.

### D. Governance state

| Value | Meaning |
|---|---|
| `PROPOSED` | A change or decision is being proposed |
| `BLOCKED` | A named prerequisite is absent or unsatisfied |
| `RATIFIED` | A competent authority's ratification evidence was verified for the stated scope |
| `SUPERSEDED` | A later identified decision explicitly supersedes this item |
| `NOT_APPLICABLE` | The control is shown to be outside the declared scope |

A governance state requires an authority/effectiveness basis. A Git commit, passing workflow, maintainer role, account name, or assertion in a document is not sufficient by itself to infer ratification.

## UI rule

Do not derive one axis from another. In particular:

- `PRESENT + PASS` does not imply `RATIFIED`.
- `EXHAUSTED_WITHIN_SCOPE` does not imply `COMPLETE_FOR_REQUIREMENT`.
- `RATIFIED` does not prove implementation conformance.
- `PASS` applies only to the check, verifier version, source revision, and coverage explicitly named.
- Missing evidence is not evidence that a claim is false; it means that the claim has not been established within the stated scope.

These semantics are a design proposal for the BETA workspace. They do not amend the AURA protocol.
