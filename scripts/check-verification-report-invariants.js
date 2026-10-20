#!/usr/bin/env node
"use strict";
const fs = require("node:fs");
const paths = [
  "tests/fixtures/verification-report/valid-technical-pass-governance-blocked.json",
  "tests/fixtures/verification-report/valid-signature-fail.json",
  "tests/fixtures/verification-report/valid-input-digest-mismatch-ssh-blocked.json"
];
let failed = false;
function reject(file, message) { failed = true; console.error(`FAIL ${file}: ${message}`); }
for (const file of paths) {
  const report = JSON.parse(fs.readFileSync(file, "utf8"));
  const artifacts = report.byte_evidence.artifacts;
  const byId = new Map();
  for (const a of artifacts) {
    if (byId.has(a.artifact_id)) reject(file, `duplicate artifact_id ${a.artifact_id}`);
    byId.set(a.artifact_id, a);
    if (a.comparison_status === "MATCH" && a.sha256 !== a.expected_sha256) reject(file, `${a.artifact_id}: MATCH but digest differs from expected`);
    if (a.comparison_status === "MISMATCH" && a.sha256 === a.expected_sha256) reject(file, `${a.artifact_id}: MISMATCH but digests are equal`);
  }
  const refs = [
    [report.execution.stdin_artifact_id, ["VERIFIER_STDIN"]],
    [report.execution.stdout_artifact_id, ["VERIFIER_STDOUT"]],
    [report.execution.stderr_artifact_id, ["VERIFIER_STDERR"]],
    [report.ssh_signature_gate.message_artifact_id, ["SIGNED_MESSAGE"]],
    [report.ssh_signature_gate.signature_artifact_id, ["SSHSIG_FILE"]],
    [report.ssh_signature_gate.allowed_signers_artifact_id, ["ALLOWED_SIGNERS"]],
    [report.ssh_signature_gate.stdout_artifact_id, ["SSH_STDOUT"]],
    [report.ssh_signature_gate.stderr_artifact_id, ["SSH_STDERR"]]
  ];
  for (const [id, roles] of refs) {
    if (id === null) continue;
    const a = byId.get(id);
    if (!a) reject(file, `unresolved artifact reference ${id}`);
    else if (!roles.includes(a.role)) reject(file, `${id} has role ${a.role}; expected ${roles.join("/")}`);
  }
  if (report.byte_evidence.status === "PASS" && artifacts.some(a => a.comparison_status === "MISMATCH")) reject(file, "byte_evidence PASS includes a MISMATCH artifact");
  const ssh = report.ssh_signature_gate;
  if (ssh.status === "PASS" && (ssh.exit_code !== 0 || ssh.cause_code !== "NONE")) reject(file, "SSH PASS requires exit_code 0 and cause_code NONE");
  if (ssh.status === "FAIL" && (!Number.isInteger(ssh.exit_code) || ssh.exit_code === 0 || ssh.cause_code === "NONE")) reject(file, "SSH FAIL requires non-zero exit and explicit cause");
  if (["BLOCKED", "NOT_RUN"].includes(ssh.status) && (ssh.exit_code !== null || ssh.cause_code === "NONE")) reject(file, "SSH BLOCKED/NOT_RUN requires null exit and explicit cause");
  const gov = report.governance_gate;
  if (gov.status === "PASS" && (gov.authority_continuity !== "ESTABLISHED" || gov.ratification_status !== "RATIFIED" || !gov.decision_authority_ref || gov.evidence_refs.length === 0)) reject(file, "governance PASS lacks authority/ratification/reference evidence");
  if (report.overall_result.status === "PASS" && (report.technical_result.status !== "PASS" || report.byte_evidence.status !== "PASS" || ssh.status !== "PASS" || gov.status !== "PASS")) reject(file, "overall PASS conflicts with subordinate gate status");
  if (report.overall_result.status !== "PASS" && report.overall_result.reason_code === "NONE") reject(file, "non-PASS overall result requires explicit reason code");
  if (!failed) console.log(`PASS ${file}: artifact references and status invariants verified`);
}
if (failed) process.exit(1);
console.log("PASS: verification-report cross-reference and status invariants");

