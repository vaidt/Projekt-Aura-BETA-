# AURA BETA — Primary Authority Inventory Addendum v0.2

**Record ID:** BETA-GOV-AUTH-SOURCE-ADDENDUM-0002  
**Status:** SOURCE-BOUNDED · NON-CONSTITUTIVE  
**Observation date:** 2026-10-20  
**Normative effect:** NONE  
**Relationship:** Supplements `PRIMARY_AUTHORITY_SOURCE_INVENTORY_v0.1.md`; supersedes no source record.

## 1. Executive finding

The current OpenSSH observation verifies three separate artifacts against the same Ed25519 public-key fingerprint, `SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU`, using the same `allowed_signers` entry from the examined `vaidt/aura-specification` history. These are three verified signature artifacts, **not three independent key roots, signers, or trust anchors**.

A chronology check found the `allowed_signers` path was first added in the inspected repository history by commit `091ab7a88ee626caa536c641fa3cee53a6e008df` at 2026-09-24 20:34:41 UTC. Genesis Declaration was added at 20:08:08 UTC and P-008 at 20:18:45 UTC. The parent tree of the Genesis commit, `3b807a527789d3341b13b71bf9579f0c8c68bd15`, has no `allowed_signers` path. The list used for current verification is therefore a later repository registration, not an independently demonstrated prior root of trust for those earlier acts. This does **not** invalidate mathematical signature verification; it limits the trust/authority inference.

The current source tree has one indexed RFC: RFC-001, a DRAFT about APS-001 M1 execution, unrelated to a constitutional amendment. No Article XIII-specific RFC, ARR, impact-analysis package, or amendment approval was identified in the inspected reachable source tree. This is a bounded search, **not proof that no such record exists elsewhere**.

**Disposition:** Genesis candidate PRESENT; exact-byte signatures PASS; prior independent trust anchor and issuer competence NOT PROVEN from reviewed sources; Article XIII procedure NOT ESTABLISHED FROM SOURCES REVIEWED; M1 BLOCKED; P-008 CONFLICTED / NOT ESTABLISHED; WP-3 BLOCKED.

## 2. Source chronology

| UTC | Source event | Observation |
|---|---|---|
| 2026-09-21 19:32:53 | [Article XIII commit a53ef122](https://github.com/vaidt/aura-specification/commit/a53ef122f9cedbf110f30ed57ddd7ef1db6f1491) | Adds four lines to `constitution/AURA_CONSTITUTION.md`; leaves Version 1.0 / FROZEN label and does not include Article XI procedure artifacts. GitHub reports the commit signature as verified; this does not prove amendment compliance. |
| 2026-09-24 20:08:08 | [Genesis Declaration commit 89de18a](https://github.com/vaidt/aura-specification/commit/89de18afc41e79afc0259116df861928dfae8cba) | Adds declaration and detached SSHSIG. |
| 2026-09-24 20:18:45 | [P-008 record commit bf835561](https://github.com/vaidt/aura-specification/commit/bf83556139422f341d6b75f48b6b9a2412ef941a) | Adds signed P-008 artifact before the inspected allow-list path exists in this repository history. |
| 2026-09-24 20:34:41 | [First `allowed_signers` commit 091ab7a](https://github.com/vaidt/aura-specification/commit/091ab7a88ee626caa536c641fa3cee53a6e008df) | Introduces the key-to-identity mapping used by later SSHSIG checks. |

The allow-list chronology establishes when the file enters the examined Git history, not the exact wall-clock time a private key created a signature. A prior trust anchor may exist outside the reviewed corpus; none was located or verified here.

## 3. Article XI procedure inventory

The non-truncated reachable tree at `vaidt/aura-specification@991274eed57d5b3308b0607feeb4d01e6a485974` has 332 entries. Governance-path inspection found:

- `rfcs/README.md` indexes one RFC: `RFC-001_APS001_MILESTONE1_EXECUTION_SCOPE.md`;
- RFC-001 is `DRAFT`, targets APS-001 M1 execution, and says Architecture Review and Chief Architect approval remain pending for its own scope; it is not an Article XIII amendment RFC;
- `adrs/ADR-001_DOCUMENT_MODEL.md`, `adrs/ADR-001_REPOSITORY_STRUCTURE.md`, and two CK003-specific ADR files were present, but no Article XIII-specific ARR was identified;
- `governance/evidence/AURA_ARTICLE_XIII_AUTHORSHIP_AND_INTENT_RECORD_v0.1.md` is DRAFT / NON-CONSTITUTIVE / NOT RATIFIED and expressly states that the insertion commit does not itself include the RFC, Architecture Review, impact analysis, or dependent-document updates required by Article XI.

No Article XIII-specific RFC, ARR, impact-analysis package, or amendment approval was identified in the tree and associated records inspected. The only pull request surfaced by GitHub for the copied Article XIII commit is [Aura-IDToken/aura-specification PR #47](https://github.com/Aura-IDToken/aura-specification/pull/47), merged 2026-10-18 with 133 files changed; it is a large synchronization from `vaidt/aura-specification`, not an Article XIII-specific amendment PR. Its review and issue-comment collections were empty.

**Disposition:** repository insertion of Article XIII ESTABLISHED; procedural and normative effect NOT ESTABLISHED FROM SOURCES REVIEWED. Do not convert this source-bounded search finding into a claim that a record cannot exist outside the reviewed corpus.

## 4. OpenSSH results and independence boundary

[BETA workflow #39472439876](https://github.com/vaidt/Projekt-Aura-BETA-/actions/runs/39472439876), using OpenSSH_9.6p1 / OpenSSL 3.0.13, reported:

| Artifact | Namespace | Exact-byte result |
|---|---|---|
| Genesis Declaration | `aura-genesis` | PASS / exit 0 |
| Authority Binding v1.1 | `aura-governance` | PASS / exit 0 |
| Current P-008 record | `aura-governance` | PASS / exit 0 |
| Current amended M1 closure record | `aura-governance` | FAIL / exit 255 in the strict M1 gate |

All first three success lines reported the same public-key fingerprint. The phrase “three independent signatures” is therefore imprecise: there are three separately verified artifacts, but one shared key fingerprint, one repository-sourced allow-list, and a single observed CI environment.

The older `AURA_ARTICLE_XIII_AUTHORSHIP_AND_INTENT_RECORD_v0.1.md` says standards-compliant SSHSIG envelope validation was not established because of an alleged anomalous algorithm identifier. The later source-pinned OpenSSH run successfully verifies the pinned Genesis bytes with `ssh-keygen -Y verify` in the declared namespace. For the exact-byte SSHSIG question, that later result is stronger than the older bounded assessment; the older record remains preserved and should be cross-referenced in any future reconciliation, not silently rewritten by BETA.

The PASS results still do not establish independent natural-person identity, prior issuer competence, authority to bootstrap Genesis, a prior external trust anchor, an uncontested canonical-repository designation, Article XI compliance, effective date, revocation/succession state, M1 closure, or P-008 ratification.

## 5. Updated authority chain

| Required link | Current posture |
|---|---|
| Primary authority source | Genesis Declaration found as candidate; prior rule empowering its issuer not established |
| Competent issuer | NOT PROVEN from reviewed evidence |
| Current holder / identity binding | Signed self-assertions and repository metadata present; independent identity/person-key chain NOT PROVEN |
| Key registration / trust root | Exact-byte signature PASS; allow-list in this repository appears after Genesis and P-008 |
| Scope | Genesis asserts broad powers; independent authority for that scope NOT PROVEN |
| Article XIII amendment procedure | NOT ESTABLISHED FROM SOURCES REVIEWED |
| Effective date / continuing validity | Git timestamps and status labels observed; effective authority, revocation and succession independently established? NO |
| Authenticated technical outcome | Genesis / binding / P-008 PASS under same key; current M1 exact-byte gate FAIL |
| Governance outcome | G0 continuity NOT PROVEN; M1 BLOCKED; P-008 CONFLICTED / NOT ESTABLISHED; WP-3 BLOCKED |

## 6. Required evidence to advance

1. Locate a primary instrument that grants Genesis establishment authority to the issuer, and show its effective date and competent issuer.
2. Bind the person, historical accounts and key through an independent channel. The later repository `allowed_signers` entry cannot act as its own antecedent authority basis.
3. Locate and bind the RFC, Architecture Review, impact analysis, dependent-document updates and approval required by Article XI, or preserve a bounded record of items unavailable in the reviewed corpus.
4. Resolve the Constitution version/status discrepancy and P-008's contradictory status assertions through an independently competent process.
5. Preserve all historical blobs, signatures, commits and failed verification outputs. Keep the strict M1 gate, WP-3 hold and PR Draft/unmerged state until competent authority and procedure are demonstrated.

This addendum is a non-constitutive engineering evidence report. It does not create, revoke, ratify, amend or supersede an AURA normative act.
