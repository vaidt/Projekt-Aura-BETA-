#!/usr/bin/env bash
set -euo pipefail

MANIFEST="tests/fixtures/m1/SSHSIG_INPUT_MANIFEST.json"
if [[ ! -f "$MANIFEST" ]]; then
  echo "::error::Missing M1 SSHSIG input manifest: $MANIFEST"
  exit 1
fi

echo "== AURA governance signature gate: M1 =="
echo "OpenSSH: $(ssh -V 2>&1)"
echo "BETA revision: $(git rev-parse HEAD)"

EXPECTED_SOURCE_HEAD="$(jq -er '.source_current_commit' "$MANIFEST")"
CURRENT_SOURCE_HEAD="$(curl --fail --silent --show-error --location \
  -H 'Accept: application/vnd.github+json' \
  -H 'X-GitHub-Api-Version: 2022-11-28' \
  'https://api.github.com/repos/vaidt/aura-specification/branches/main' | jq -er '.commit.sha')"

echo "Pinned AURA specification main: $EXPECTED_SOURCE_HEAD"
echo "Observed AURA specification main: $CURRENT_SOURCE_HEAD"
if [[ "$CURRENT_SOURCE_HEAD" != "$EXPECTED_SOURCE_HEAD" ]]; then
  echo "::error::The upstream specification main HEAD changed. Refresh and review the M1 source-bound fixtures and manifest before treating this gate as current."
  exit 1
fi

check_blob() {
  local path="$1"
  local expected="$2"
  local actual
  actual="$(git hash-object --no-filters "$path")"
  if [[ "$actual" != "$expected" ]]; then
    echo "::error file=$path::Input bytes do not match the source Git blob. Expected $expected; got $actual."
    exit 1
  fi
  printf 'PINNED %s %s\n' "$path" "$actual"
}

HIST_MSG="$(jq -er '.historical.message_path' "$MANIFEST")"
HIST_MSG_SHA="$(jq -er '.historical.message_blob_sha' "$MANIFEST")"
HIST_SIG="$(jq -er '.historical.signature_path' "$MANIFEST")"
HIST_SIG_SHA="$(jq -er '.historical.signature_blob_sha' "$MANIFEST")"
HIST_SIGNERS="$(jq -er '.historical.allowed_signers_path' "$MANIFEST")"
HIST_SIGNERS_SHA="$(jq -er '.historical.allowed_signers_blob_sha' "$MANIFEST")"
CURRENT_MSG="$(jq -er '.current.message_path' "$MANIFEST")"
CURRENT_MSG_SHA="$(jq -er '.current.message_blob_sha' "$MANIFEST")"
CURRENT_SIG="$(jq -er '.current.signature_path' "$MANIFEST")"
CURRENT_SIG_SHA="$(jq -er '.current.signature_blob_sha' "$MANIFEST")"
CURRENT_SIGNERS="$(jq -er '.current.allowed_signers_path' "$MANIFEST")"
CURRENT_SIGNERS_SHA="$(jq -er '.current.allowed_signers_blob_sha' "$MANIFEST")"
IDENTITY="$(jq -er '.identity' "$MANIFEST")"
NAMESPACE="$(jq -er '.namespace' "$MANIFEST")"

echo
echo "== 1. Verify all M1 input snapshot blob SHAs =="
check_blob "$HIST_MSG" "$HIST_MSG_SHA"
check_blob "$HIST_SIG" "$HIST_SIG_SHA"
check_blob "$HIST_SIGNERS" "$HIST_SIGNERS_SHA"
check_blob "$CURRENT_MSG" "$CURRENT_MSG_SHA"
check_blob "$CURRENT_SIG" "$CURRENT_SIG_SHA"
check_blob "$CURRENT_SIGNERS" "$CURRENT_SIGNERS_SHA"

echo
echo "== 2. Prove the control inputs are identical where expected =="
if ! cmp -s "$HIST_SIG" "$CURRENT_SIG"; then
  echo "::error::Historical and current M1 signature files differ; review manifest and source revision."
  exit 1
fi
if ! cmp -s "$HIST_SIGNERS" "$CURRENT_SIGNERS"; then
  echo "::error::Historical and current allowed_signers files differ; review manifest and source revision."
  exit 1
fi
if cmp -s "$HIST_MSG" "$CURRENT_MSG"; then
  echo "::error::Historical and current M1 content unexpectedly match; expected an explicit source revision difference."
  exit 1
fi
echo "CONFIRMED: signature and allow-list bytes are identical; M1 message bytes differ."

verify_signature() {
  local label="$1"
  local message="$2"
  local signature="$3"
  local signers="$4"
  local output_file="$5"
  local rc=0

  set +e
  ssh-keygen -Y verify -f "$signers" -I "$IDENTITY" -n "$NAMESPACE" -s "$signature" \
    < "$message" > "$output_file" 2>&1
  rc=$?
  set -e

  echo "--- $label (exit=$rc) ---"
  cat "$output_file"
  return "$rc"
}

echo
echo "== 3. Historical exact bytes must verify =="
if verify_signature "Historical M1 exact bytes" "$HIST_MSG" "$HIST_SIG" "$HIST_SIGNERS" "$RUNNER_TEMP/m1-historical-verify.log"; then
  echo "PASS: historical M1 signature validates against the exact historical message bytes."
else
  echo "::error::Historical signed baseline failed verification. This invalidates the test control; investigate before interpreting the current mismatch."
  exit 1
fi

echo
echo "== 4. Current amended M1 bytes must verify before M1 can be considered cryptographically bound =="
if verify_signature "Current M1 exact bytes" "$CURRENT_MSG" "$CURRENT_SIG" "$CURRENT_SIGNERS" "$RUNNER_TEMP/m1-current-verify.log"; then
  echo "::error::The current M1 message now verifies. This is a baseline change and requires review of the new source revision before any gate can be closed."
  exit 1
else
  rc=$?
  echo "::error::CRITICAL ERROR: M1 CONTENT / SIGNATURE MISMATCH (FAIL). The attached signature does not validate the current exact Markdown bytes."
  echo "M1 remains BLOCKED. A successful CI run is intentionally impossible while this current-byte verification fails."
  exit "$rc"
fi
