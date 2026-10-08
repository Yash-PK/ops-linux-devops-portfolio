# Portfolio plan

Configuration: owner `Yash-PK` (explicitly confirmed personal account), repository
prefix `ops-`, public visibility, separate sibling repositories, at most one active
engineering project. Primary future cloud: AWS. Original code license: MIT.
Cloud creation, billable services, host configuration changes, and container
package publication are disabled. No unstarted remote repositories are required.

The first milestone is the hub plus a usable `linux-operations-toolkit`. Complete
implementation, tests, documentation, a clean-clone validation, and a publishing
review for each bounded core before activating the next project. Progress is
evidence-driven; this plan is not evidence that the listed capabilities exist.

## Milestone 1: operations foundation

**Hub — `ops-linux-devops-portfolio` (active supporting index).** Acceptance:
maintain the plan, matrix, current status, next task, dependency map, evidence
index, scope boundaries, and continuation instructions; validate references and
repository hygiene; publish only as a clearly labeled work in progress. Local
and clean-clone gates passed at `850a33de075cd5f43c4a1a30f4efa3830fea944d`;
the public hub and exact-revision hosted CI are verified. See the
[local report](evidence/850a33de075c-local.json) and
[clean-clone report](evidence/850a33de075c-clean-clone.json).

**1. `ops-linux-operations-toolkit` (core complete; v0.1.0 released).** Implemented
Python standard-library collectors with Bash demonstration orchestration for CPU,
memory, load, disks/inodes, processes, services, sockets, local certificate expiry,
and explicit backup freshness. Include permissions/ownership/ACL and current
identity inspection, bounded journal/package/schedule/logrotate inspection, and
capability reporting for relevant troubleshooting tools. Completed core acceptance:

- Readable and versioned JSON output, validated thresholds/inputs, command
  timeouts, summary-only logging, and meaningful status/exit codes.
- Healthy, degraded, missing-tool, invalid-input, parser, and timeout fixtures.
- An unprivileged read-only live demo on the supported environment; Linux core
  integration evidence is required for Linux integration-tested claims.
- Required lint, tests, documentation/security gates, and a clean-clone run pass.
- Exact prerequisites, failure/recovery demo, runbooks, security model, decision
  record, and tested revision are documented; unavailable data remains unknown.

Local validation of `55f15eaacf3842fa15f44751d5f21a5094bd089c` passed 58 tests,
lint, demo, secret scans and a clean clone. Published revision
`0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` passed the
[Ubuntu Linux CI run](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607),
including seven live health sources, metadata/package/tool inspection, real
temporary-file backup freshness recovery, certificate expiry policies, an observed
systemd service, journald/schedules and ACL metadata. See the
[evidence index](docs/evidence-index.md) for exact scope. Privileged diagnostics,
full OS boot/reboot, cgroup policy and other distributions remain unverified.
[Release v0.1.0](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0)
is verified published at `0d164e9158eeb9540e895d5f48bcf4723f36667b`, with
[passing release-revision CI](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37573353795).
It is neither a draft nor a prerelease. The original local and Linux reports remain
tied to their earlier recorded source revisions.
No default toolkit command remediates or changes host configuration. The first
milestone is complete. Four engineering cores now have verified v0.1.0 releases.
Cloud foundation IaC is the only active project, beginning a static/mock core.

## Milestone 2: disposable operating-system labs

**2. `ops-linux-fleet-automation` (core complete; v0.1.0 released).** The bounded
core targets Ubuntu 24.04 ARM64 and AlmaLinux 9 ARM64 in explicitly owned
macOS ARM64 Lima VZ guests. Controller tools and official images are pinned;
controller dependencies are installed from hash-locked inputs. Source implements
one coherent Ansible baseline role for accounts, SSH/sudo, packages, chrony,
services, journald, native firewall policy and hardened nginx, with explicit
Ubuntu/AlmaLinux differences and AppArmor/SELinux checks. A separate maintenance
play gates package updates and guest reboot. The provider enforces private local
state, a fixed lab ID, strict SSH trust and one running guest at a time.

Recorded source `c52155a5c15b04bdb2a85746b385da0243ecef93` passed 74 controller
tests, required lint/doctor/demo/security gates and the clean-clone quickstart.
Its real Ubuntu run passed all nine workflow steps, including strict SSH changed-key
rejection, Molecule converge/idempotence/verify, invalid-input rejection with zero
changes, live service checks, reversible content change, patch/reboot verification
before repair, guest package metadata and owned teardown. The earlier failed
post-reboot firewall report remains archived; the corrected source passed a fresh
run. The safe controller input demo remains distinct from guest provisioning.

AlmaLinux 9.8 completed the same nine-step lifecycle at source
`e333e1c8c37b107fb6e99924c869555acca0ad68`, with the same implementation fingerprint
as the Ubuntu run, preserved SELinux/firewalld behavior and scoped teardown.
Outgoing checks, final clean-clone validation and publication passed.
[Release v0.1.0](https://github.com/Yash-PK/ops-linux-fleet-automation/releases/tag/v0.1.0)
is verified at `1531b86b54eee87d01da83f7b55d7d405f43fadb` with
[passing exact-target CI](https://github.com/Yash-PK/ops-linux-fleet-automation/actions/runs/37615270935).
The original reports retain their source identities. Debian, Rocky and other
providers remain separate unverified alternatives; no cloud deployment is claimed.

**3. `ops-network-storage-services-lab` (completed bounded core; integration-tested).**
The local sibling repository implements a real Ubuntu 24.04 ARM64 VM using the
released fleet provider, pinned at `1531b86b54eee87d01da83f7b55d7d405f43fadb` and
verified by source-file SHA256. Lima VZ is the supported macOS ARM64 provider. Private
Linux namespace clients inside the guest are not additional VMs. KVM/libvirt and
other providers remain unimplemented alternatives. No sibling checkout is required.

Six runnable network profiles implement DNS, isolated DHCP, NFS, Samba,
reverse-proxy/load-balancing/local TLS, and firewall/failure/capture checks over
guest-private bridges, VLANs and routed segments. Four storage profiles implement
GPT/ext4/XFS/fstab/quotas, LVM expansion, RAID1 degradation/rebuild, and LUKS
wrong-key rejection/reopen using inventoried guest-owned loop images. Explicit
lab identity, dry run and confirmation guard destructive operations and teardown.
The standalone bootstrap pins the provider, image and 41 packages from an Ubuntu
snapshot; preparation is followed by authenticated reboot and exact running-kernel
verification. Initial budget is one 2-CPU, 2-GiB VM with a 24-GiB sparse root disk.

The core passed 122 controller tests, required lint, the safe demo, full secret
scans, standalone clean-clone checks and formal all-profile VM integration (605
commands, 110 assertions and owned cleanup) at source `e43bcdfdae1a604a095eea085e81eb8fbe2e6d00`.
Its [v0.1.0 release](https://github.com/Yash-PK/ops-network-storage-services-lab/releases/tag/v0.1.0) is verified at
`53b78f81ed58602efd2c151d449338615ab61e9d`, with [passing exact-target CI](https://github.com/Yash-PK/ops-network-storage-services-lab/actions/runs/37735444827).
Earlier development failures remain documented; they were never relabeled as pass.

## Milestone 3: reference workload and delivery

**4. `ops-containerized-service-platform` (core complete; integration-tested, v0.1.0 released).**
The local common reference workload implements bounded asynchronous text analysis:
a Python API accepts an idempotent synthetic job, PostgreSQL commits durable
state, and a separate worker claims a leased row and fences completion. Valkey
caches terminal results only; nginx proxies HTTP. The acceptance checklist
preceded implementation. Source includes numbered checksum-verified migrations,
repeatable seeds, input/failure/safety tests, hash-locked Python dependencies,
digest-pinned multi-stage container images, Compose readiness and resource limits,
non-root application identities, generated ignored credentials and a data volume.

A guarded standalone runner pins the released fleet-provider component and
allocates a separate Ubuntu ARM64 VZ guest for Docker 29.8.2/Compose 5.6.0/Buildx
0.38.0. It uses 2 CPUs, 2 GiB RAM and a 24 GiB sparse disk, no host mounts and
no forwarded application ports; the client uses guest loopback. Formal source
`950e511f42173c00994496265bb48104623e1bea` passed 57 controller tests, required
lint/docs/config, doctor/demo, secret scans and standalone clean-clone checks.
Four development runs remain failed overall, although the fourth exercised
workload/recovery behavior and 21 real SQL assertions before process inspection
failed. The first formal VM attempt failed an oversized multiplexed SSH request
before guest phases; all those VMs were deleted. Current source
`3d58b9f7107fa1c7de3eec06b32c9b6f6ce644d6` adds bounded chunk transfer with 71
passing tests in its formal controller report. Its standalone clone and complete
formal VM run passed: 139 commands, 94 preparation/lifecycle assertions, 21 nested
SQL assertions and owned cleanup. This later report establishes asynchronous
completion, restart persistence, cache/database outage recovery, SQL semantics,
observed runtime settings and cleanup; earlier failed attempts stay failed.

The [public repository](https://github.com/Yash-PK/ops-containerized-service-platform) is verified at
`cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe`, matching the [v0.1.0 release](https://github.com/Yash-PK/ops-containerized-service-platform/releases/tag/v0.1.0),
with [passing exact-target CI](https://github.com/Yash-PK/ops-containerized-service-platform/actions/runs/37743579858). The preserved Linux controller
artifact retains source `19ec88d5d4a6` and the same implementation fingerprint.
P4 is complete and no longer active; no required core gate remains unresolved.
Rootless Podman is a separate planned extension. Publish no container packages
and provision no cloud resources under current flags.

**5. `ops-cloud-foundation-iac` (active; capability planned).** Begin official
support/release/advisory review for OpenTofu and the AWS provider before choosing
exact versions. OpenTofu is the primary engine; Terraform compatibility is not
claimed without separate tests. Define acceptance before implementation. Planned AWS core modules cover
VPC/subnets/routes, security groups, least-privilege IAM, encryption, tags,
state/bootstrap design, and minimal compute configuration. Core acceptance is
offline/static only: formatting, validation, lint, policy checks, and module mocks;
disabled cost-bearing profiles; ignored state/plans/credentials; explicit state
locking, drift, import, migration, and destroy procedures. Static, mock, authenticated
plan, and applied states are separate. Load balancers, managed databases,
Kubernetes, DNS, object storage, and audit logging are individually gated
extensions. No cloud resource creation is authorized.

**6. `ops-delivery-pipelines` (planned).** GitHub Actions is primary for the
reference workload. Separate untrusted PR checks from trusted release/promotion;
build once and promote the same digest where publishing is authorized. Implement
lint/test/build/security gates, artifacts, release preparation, rollback, and a
deliberately failing fixture. Core acceptance: exact-revision GitHub checks run,
the negative gate blocks, and local scripts reproduce the core steps. Jenkinsfile,
Configuration as Code, and isolated-agent operation form a distinct extension;
unexecuted Jenkins/GitLab pipelines remain unverified. Registry/cloud deployment
stays disabled under current authorization. Propose branch protections only after
check names exist; preserve a usable maintainer path.

## Milestone 4: local platform and operational signals

**7. `ops-kubernetes-gitops-platform` (planned).** Select kind or k3d, Helm,
Kustomize only where justified, Argo CD, a maintained Gateway API implementation,
a NetworkPolicy-enforcing CNI, and cert-manager where appropriate. Pin context and
namespace so scripts cannot target an existing cluster. Cover RBAC, service
accounts, Pod Security, configuration/secrets references, requests/limits,
health probes, storage, disruption budgets, metrics-backed autoscaling, rollouts,
image-pull/DNS/scheduling failure triage, and node maintenance. Core acceptance:
deploy workload; verify a denied network path; fail a bad release safely; restore
service by Git rollback; demonstrate drift reconciliation. Local storage and
control-plane limits remain explicit.

**8. `ops-observability-sre-lab` (planned).** Instrument the same workload with
OpenTelemetry. Resource-aware profiles use Prometheus, Grafana, Alertmanager,
Loki, Tempo, and one maintained collector. Provision dashboards and rules;
define an observable SLI/SLO, an error-budget policy, and runbook-linked alerts.
Core acceptance: locate one generated request in trace/log evidence; trigger and
resolve an alert using a controlled fault; run promtool rule tests and bounded k6
load tests. Record environment, timestamps, load parameters, and limits; short
measurements do not prove long-term availability. Explain sampling, cardinality,
retention, telemetry privacy, and latency/error/traffic/saturation indicators.

**9. `ops-devsecops-policy-lab` (planned).** Select a complementary minimal set for
secrets, vulnerability scanning, SBOMs, signatures, IaC policy, and Kubernetes
admission after maintenance/advisory review. Candidate tools are evaluated, not
preselected claims. Add SOPS with age for local secrets; keep keys out of Git and
logs. Core acceptance: safe valid/invalid fixtures exercise every enforced
control; signature verification checks intended identity and issuer; document
threat assumptions, findings, remediation, and narrow time-bound exceptions.
OpenBao/Vault or External Secrets is a separately justified integration.

## Milestone 5: recovery and service ownership

**10. `ops-backup-disaster-recovery` (planned).** Encrypted restic file backups and
PostgreSQL restore are the bounded core. Add WAL/PITR using a verified maintained
tool as a separately tested profile. Include scheduling, retention, integrity,
backup-failure alerts, and restore into a distinct clean destination. Core
acceptance: seed identifiable synthetic data; back it up; simulate loss only in
disposable lab resources; restore and verify records/checksums; measure observed
recovery time/data loss against lab RTO/RPO targets. A backup artifact alone is
not recovery evidence. Velero requires a backend/storage profile that can prove
the claimed recovery semantics.

**11. `ops-platform-engineering-golden-path` (planned).** Begin with a lightweight
template generator and input schema. Generate a tested service with CI, container
packaging, deployment configuration, telemetry hooks, ownership metadata, and
operational docs. Core acceptance: generate into an empty temporary directory;
reject invalid inputs; run generated tests; deploy to the local platform and
verify telemetry. Do not copy secrets, hardcode the original account, or silently
create repositories. Backstage is optional after resource/maintenance review.

**12. `ops-production-simulation-capstone` (planned).** Integrate pinned releases
without copying entire projects. Minimal and extended profiles demonstrate a
release, telemetry-driven fault detection, triage, rollback/restore, and recovery
verification. Core acceptance: repeatable bounded lifecycle script; failed
deployment, dependency outage, and data-recovery scenarios; reversible injection
with cleanup; actual timestamped results supporting a blameless *lab* postmortem
and actionable backlog. This is not a real production incident.

## Gates shared by all projects

Before dependencies are selected, record official version/support, release-note,
and advisory research. Pin reproducible versions and lockfiles, or state the exact
verification gap. Review source/configuration, tests, license/attribution, docs,
generated artifacts, staged files, and full outgoing history. Run required gates
from a clean checkout. Record commands, exit codes, environment, tool versions,
assertions, redacted output, and the tested source revision.

Only then check the exact authorized remote name for collisions and create a new
repository. Verify owner, public visibility, default branch, remote SHA, and the
Actions run for that SHA. Publication and CI are separate states; pending CI is
not release success. A versioned release requires its documented release gate.
