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
