# AURA Core — Source Provenance

## Source identity

- **Source repository:** [Aura-IDToken/aura-poc-a-core-v3.3](https://github.com/Aura-IDToken/aura-poc-a-core-v3.3)
- **Source commit:** `64bf959b1d23fbd5433723476c611ab66d423953`
- **Source Git tree:** `27192da6f11a54c6d043578de458a49c7b07fcfb`
- **Supplied source archive:** `aura-poc-a-core-v3.3-main (10).zip`
- **SHA-256 of the exact supplied ZIP bytes:** `8868c95f61b9dd3c88e8f8f535fcd835303a00e7921feb835a94064f46939e18`
- **Migration destination:** the archive root contents are placed beneath `core/` in this repository.

## Verification performed

The supplied archive was unpacked without editing source files. A temporary Git index was built from the extracted archive root and `git write-tree` returned `27192da6f11a54c6d043578de458a49c7b07fcfb`, exactly matching the tree SHA recorded for source commit `64bf959b1d23fbd5433723476c611ab66d423953`.

During transfer, every source file was fetched at that immutable commit and its Git blob SHA was compared with the source tree entry before it was added to the BETA migration tree. Original Git file modes were retained. The migration commit is accepted as a byte-/mode-preserving source import only if the resulting `core/` subtree SHA equals the source tree SHA above.

## Licence preservation

- **Licence file:** `core/LICENSE`
- **Licence:** Business Source License 1.1 (BSL 1.1)
- **SHA-256 of the source LICENSE bytes:** `d9a8061f66da072d6800d5770bd4358a3cc669ef2c22f4841c2366b5682afa26`
- **Git blob SHA-1:** `fe9de92496fe1b9475e52d4fe444cb9ea0b712bd`

The source licence is included unchanged. This provenance record does not provide legal advice or broaden the source licence.

## Delta and authority boundary

The source import itself does not modify or reinterpret source code, specifications, or licence text. Any subsequent compatibility fix or CI adaptation must be isolated in a separate, reviewable commit and must be visible as a delta from this baseline.

An exact source import, a successful test run, byte integrity, and cryptographic verification are distinct evidence classes. None of them alone establishes protocol conformance, constitutional authority, ratification, regulatory compliance, or production readiness. AURA BETA remains an operational engineering workspace; this file has no normative protocol effect.
