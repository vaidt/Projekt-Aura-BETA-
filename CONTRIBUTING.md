# Contributing to AURA BETA

This repository is an engineering/design workspace. Until separately established by evidence and the applicable governance process, it is not a normative source for the AURA protocol.

## Change flow

1. Create a topic branch from the current reviewed base.
2. State the problem, scope, expected outcome, risks, and affected requirements.
3. For status or evidence changes, link the source revision and verification method.
4. Keep each PR narrow and inspectable.
5. Run available checks and report exactly what ran and what did not.
6. Request human review before merging.
7. Preserve unresolved conflicts and blocked prerequisites in the record.

## Decision labels

Every material decision must state:
- identifier and status;
- decision scope;
- evidence considered;
- known counter-evidence or alternative;
- rationale and consequences;
- authority/effectiveness basis when a governance claim is involved;
- whether it changes protocol semantics (the default is **no**).

## Hard prohibitions

- Do not call a decision ratified without verified authority and ratification evidence.
- Do not promote copied or generated content into canonical status by implication.
- Do not treat CI success as proof that an untested requirement is satisfied.
- Do not overwrite historical audit evidence without an explicit supersession record.
- Do not introduce network access or nondeterministic behavior into the deterministic evaluation core without a separately reviewed design.
- Do not put secrets, credentials, private evidence, or personal data in commits or test fixtures.

## Review standard

Reviewers should examine correctness, source binding, change scope, failure behavior, negative cases, data exposure, and whether the stated conclusion is supported by the presented evidence. "Tests pass" is not a substitute for reviewing what those tests prove.
