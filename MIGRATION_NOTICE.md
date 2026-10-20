# AURA Project Migration Notice

**Record:** AURA-BETA-MIGRATION-0001  
**Destination workspace:** [`vaidt/Projekt-Aura-BETA-`](https://github.com/vaidt/Projekt-Aura-BETA-)  
**Status:** MIGRATION TARGET · OPERATIONAL CONSOLIDATION PROPOSAL · NON-NORMATIVE  
**Recorded:** 2026-10-20T15:57:53.380Z

## Direction

New cross-repository AURA planning, engineering coordination, source inventories, assurance records, migration planning, and audit-control-plane development should be centralized in this BETA workspace.

The operational objective is to end fragmented day-to-day coordination across account namespaces and duplicate repository homes. BETA is the intended consolidation destination for the project workspace.

## Critical distinction

This notice does **not** establish BETA as the absolute normative source of the AURA protocol. The candidate specification repositories contain conflicting canonical-source claims and unresolved governance records. APS-300 currently declares `1.0-DRAFT`; a new repository notice cannot ratify those materials or independently confer constitutional authority.

Until the required migration and governance checks complete:

- BETA is the target home for new consolidation and assurance work;
- legacy repositories remain available as historical/source evidence;
- no source is silently promoted or discarded;
- protocol meaning and conformance claims must remain bound to identified source revisions and verified evidence.

## Archival gate

A repository is not ready to be archived solely because it is old or duplicated. Before each archive action:

1. identify its exact owner/repository and intended archival status;
2. add and review a `MIGRATION_NOTICE.md` in that repository's default branch, linking to this workspace and stating whether the repository is historical, superseded, or still needed for build/release;
3. preserve an immutable source reference (HEAD SHA, relevant tags/releases, signed artifacts and evidence);
4. map material content, open issues, PRs, workflows, release artifacts and external consumers;
5. verify permissions and obtain the repository owner's authorization where needed;
6. confirm that archiving will not break a required conformance, release, attestation or reproducibility path;
7. record the archive operation's result and timestamp in the consolidation register.

## Current execution status

This BETA notice is a destination notice only. It does not claim that legacy notices have been installed or that any repository has been archived. The connected GitHub integration currently reports read-only permissions for the inspected `Aura-IDToken` and `kamilkrasinski4-sys` repositories, and it does not expose a repository-archive action. Therefore those repositories cannot be safely migrated or archived by this change.

See [Repository Consolidation Plan](docs/governance/REPOSITORY_CONSOLIDATION_PLAN.md) for the current scope and blockers.

## Migration contact / route

Use this repository's issue tracker for consolidation tasks and source-bound migration records. Keep historical commit references and original signed content intact; a migration notice is not a substitute for forensic preservation.
