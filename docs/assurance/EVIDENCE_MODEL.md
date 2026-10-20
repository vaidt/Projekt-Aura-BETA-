# Evidence and Provenance Model

**Status:** Draft proposal · non-normative  
**Scope:** BETA workspace evidence records, not the AURA protocol's normative evidence format

## Purpose

A finding must be inspectable and reproducible. A status badge must lead to the evidence and procedure that produced it. This model prevents a filename, screenshot, workflow existence, or prose assertion from being mistaken for verified proof.

## Minimum record

The initial JSON Schema is in `schemas/evidence-record.schema.json`. Each record should capture:

| Field | Purpose |
|---|---|
| `evidence_id` | Stable record identifier |
| `claim_id` | Claim or requirement the record is intended to support |
| `source_uri` | Source location or immutable artifact URL |
| `source_revision` | Branch/commit/version or immutable object identity |
| `content_digest` | Cryptographic digest over the exact bytes, with algorithm identified |
| `evidence_availability` | PRESENT / MISSING / INACCESSIBLE / STALE / CONFLICTED |
| `verification_method` | Named check and version, including command/procedure where applicable |
| `verification_result` | PASS / FAIL / INCONCLUSIVE / NOT_RUN |
| `scope_coverage` | What was included and excluded |
| `observed_at` | When the source/result was collected |
| `reviewer` | Actor or automation identity responsible for disposition |
| `limitations` | Known gaps, assumptions, environment constraints, and interpretation boundary |
| `supersedes` | Explicit relation to older records, if applicable |

## Rules

1. Do not store a bare PASS without a check identity, scope, inputs, and result artifact.
2. A digest proves byte identity relative to the computed digest; it does not prove author identity, authority, correctness, or normative status.
3. A signature must be verified against an identified trust root and scope; presence of a signature file is not successful signature verification.
4. A Git commit proves repository history facts within that repository, not the constitutional authority of the committer.
5. Evidence from an inaccessible source must be labelled inaccessible, not inferred from snippets or search excerpts.
6. Conflicts remain visible until a competent process resolves them. Do not select a source merely because it is newer, larger, merged, or easier to access.
7. The registry should be append-oriented. Corrections add a replacement/supersession record and retain the old result for audit.
8. Every reported aggregate must expose its denominator and covered scope. No unexplained percentages or invented totals.
9. Store collection failures as evidence about the audit attempt, not as proof that the target claim is false.
10. Mark all imported historical assertions with their original date and the date on which they were independently re-verified.

## Evidence lifecycle

```text
EXPECTED → COLLECTED → IDENTITY/REVISION CHECKED → VERIFIED / FAILED / INCONCLUSIVE
                                             ↘ BLOCKED (access or prerequisite gap)
```

This lifecycle describes workflow stages, not a single linear status enum. A record may be present while verification is NOT_RUN, or verification may fail because the source is stale.

## Out of scope for draft v0.1

No choice has been ratified here for AURA protocol hash domains, canonical JSON, signature envelope, key management, retention period, or normative Evidence Pack serialization. Those must be resolved in their proper authoritative specification.
