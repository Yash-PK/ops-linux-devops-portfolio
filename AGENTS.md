# Portfolio continuation

This repository is the index and evidence ledger for original lab/reference
engineering work. It is not a record of employment or production experience.
Read `PROJECT_STATUS.md`, `NEXT_STEPS.md`, `PORTFOLIO_PLAN.md`, and the active
project's `AGENTS.md` before making changes. Reconcile those claims with actual
files, Git status, remotes, and recorded checks; do not regenerate completed work.

Architecture: the hub holds plans, capability accounting, and evidence pointers.
Each implementation lives in its own sibling Git repository, never inside this
working tree. At most one engineering project is active. The first completed core
is `ops-linux-operations-toolkit`; consult the ledger for current active work.
Toolkit, fleet automation and network/storage have completed bounded cores and
verified v0.1.0 releases. The containerized service platform is the only active
engineering project, beginning with acceptance/dependency review. Projects 5–12
remain roadmap entries. Read the active project's instructions and reconcile
owned runtime state before creating or cleaning resources.

Commands: use `make help` for the repository's supported task interface. Required
hub gates are documentation/reference checks, configuration checks, staged-file
and outgoing-history secret scanning, and a clean-clone validation. Unsupported
or unavailable checks must be recorded as such, not counted as passing.

Safety: target owner is the explicitly authorized personal account `Yash-PK`.
New `ops-` repositories may be public only after the local publishing gate passes.
Use the existing Git identity. Never overwrite an unrelated repository or force
push. Cloud resources, paid services, container package publication, global
package installation, and host configuration changes are disabled. No secrets,
private host inventory, raw sensitive logs, or credential directories belong here.

Accounting: capability status is one of `planned`, `implemented-unverified`,
`statically-validated`, `integration-tested`, or `cloud-deployed`. Track publication
and CI separately. A mocked or fixture test is not a real integration test. Link
only verified remote URLs. Keep tested source revisions distinct from later
evidence/documentation commits. A missing required gate blocks a release claim.

After each meaningful milestone update the plan, matrix, project status, evidence
index, and next steps. Save exact remaining work and blockers at session end.
