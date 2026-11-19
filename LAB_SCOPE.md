# AURA M1 GitHub-hosted isolation lab — non-constitutive

- LAB-only, source parent: main@88ba12c44afe692f85ec5acc0ee41892897d5138.
- Tests a candidate SSHSIG verifier, not M1 governance ratification or current M1 signature validity.
- Historical M1 exact-byte signature expected PASS; current M1 exact-byte signature expected FAIL.
- The current M1/P-008/RELEASE states remain BLOCKED / NOT RATIFIED / NO-GO.
- GitHub-hosted workflow has token contents:read, one push trigger for isolated branch, 8-minute timeout.
- Tests generate ephemeral private keys ONLY in temporary runner directories; never included in Git.
- Embedded digest pins are bounded LAB integrity controls, not an independent governance trust anchor.
- No merge into main, no ruleset change, no deployment or workflow_dispatch authorized by evidence alone.
- Verify exact GitHub App 15368 check-run source, run/job SHA, and trust-boundary limitations before any promotion.
