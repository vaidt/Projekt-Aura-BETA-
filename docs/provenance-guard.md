# Aura-Guard v1.3 — Source Provenance

## Selected source

- **Repository:** [vaidt/aura-guard-v1.3](https://github.com/vaidt/aura-guard-v1.3)
- **Immutable source commit:** `e0ed7a8b381b725fe65bd86716894bfdf17d3a94`
- **Source Git tree SHA:** `67e2fc417cf6e2ecf0110e8684db2522d8149071`
- **Source tree entries:** 162 total (136 file blobs plus directory entries)
- **Migration target:** `guard/` in `vaidt/Projekt-Aura-BETA-`
- **Source Cargo.lock blob SHA:** `20e1751ac062c84732e82885ce97fdcca5b5bd70`
- **Source Cargo.toml blob SHA:** `2d4eab5a6006af42431fb2cb5b1cf8bbb092209e`

## Exact tree verification

At import time, every source file was fetched from the immutable source commit and its Git blob SHA was checked against the source tree. Text files were transferred without changing their bytes; non-UTF-8 RFC 3161 timestamp-response fixtures were transferred through the base64 Git blob interface and their destination blob SHAs were verified. The original Git file modes were retained.

The resulting target `guard/` tree SHA was read back from the BETA repository and is exactly:

`67e2fc417cf6e2ecf0110e8684db2522d8149071`

This is byte-/mode-preserving evidence that the imported subtree matches the selected source tree before the security patch.

## Licence preservation

- **Path:** `guard/LICENSE`
- **Licence:** MIT
- **Original Git blob SHA:** `e1d0d46ec668bd38d94cb5c85f12cdc9a7cf1f57`
- **Original file size:** 1,084 bytes

The target `guard/LICENSE` retains the same blob SHA. Its content was not edited.

## Supplied archive reconciliation

The supplied `aura-guard-v1.3-main (7).zip` has SHA-256:

`b78fd1fee42b953f41a61960994efb1da21b7f4decbc715677af9a6bbef52416`

Its unpacked Git tree is `dfcf69fd2aaa6dee870085c71fab1ab786204c6a`, corresponding to source commit `35082d7b4880dad780fb55a1a5f3ac0ef4322674` in `Aura-IDToken/aura-guard-v1.3` (2026-08-20). That older archive does not include `tests/guard_rs_001_concurrency_stress.rs` or `docs/GATE4_EXTERNAL_E2E.md`. Because these are explicit acceptance targets for this migration, the archived snapshot was not silently treated as the current source; the newer, commit-pinned `vaidt/aura-guard-v1.3` tree above was selected instead.

## Security baseline recorded before the patch

The selected source lockfile resolved:
- `rustls-webpki 0.103.15`
- `webpki-roots 1.0.7`
- compatibility package `webpki-roots 0.26.11`, which depends on `webpki-roots 1.0.7`

RustSec advisories issued 2026-10-20 identify the two older resolutions as affected:
- [RUSTSEC-2026-0381 — webpki-roots](https://rustsec.org/advisories/RUSTSEC-2026-0381.html), fixed in `1.0.10+`
- [RUSTSEC-2026-0382 — rustls-webpki](https://rustsec.org/advisories/RUSTSEC-2026-0382.html), fixed in `0.103.16+`

The issue involves certificate-path acceptance involving distrusted emSign intermediates and the bundled emSign ECC Root CA G3. The dependency patch and resulting test evidence are recorded separately from this source-import baseline.

## Evidence limits

Exact source provenance does not itself establish that the imported code passes BETA CI, that the patched dependency graph is free of every advisory, or that Gates 3 and 4 have passed in BETA. Those are separate claims requiring the corresponding workflow results. This document has no normative protocol effect.
