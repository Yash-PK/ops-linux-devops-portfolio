# Skills and evidence matrix

This is capability accounting, not a list of claimed professional experience.
Paths for planned rows are design targets, not assertions that files exist.
The project name identifies the independent repository; a sibling checkout is
never an implicit runtime dependency. No future project is credited because this
document mentions a tool.

Status vocabulary:

| Status | Meaning |
| --- | --- |
| `planned` | No implementation/evidence has been credited. |
| `implemented-unverified` | Relevant source/configuration exists, but required checks have not been recorded. |
| `statically-validated` | Recorded static/fixture checks pass; runtime integration is not established. |
| `integration-tested` | The claimed behavior ran in the stated real local integration environment. |
| `cloud-deployed` | An actual authorized cloud deployment was exercised and evidenced. |

Evidence keys below resolve through the [evidence index](docs/evidence-index.md):
**T-local** is macOS ARM64 validation and a clean clone of
`55f15eaacf3842fa15f44751d5f21a5094bd089c`; **T-Linux** is the passing Ubuntu
x86-64 [CI run](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607)
for `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4`. Toolkit paths refer to the
[verified standalone repository](https://github.com/Yash-PK/ops-linux-operations-toolkit).

A capability can have different statuses for fixture and live profiles. Missing
tools, skipped integrations, and mocks never become live passes. Publication and
CI are tracked in [project status](PROJECT_STATUS.md), independently of this table.

| Skill / bounded capability | Project | Implementation path / target | Executable check / target | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| Portfolio architecture, sequencing, acceptance | Hub | `PORTFOLIO_PLAN.md`, `docs/architecture.md`, `scripts/hub.py` | `make validate` | Hub local and clean-clone reports at `850a33de075c`; see evidence index | statically-validated |
| Evidence accounting and continuation | Hub | `portfolio.json`, `scripts/hub.py`, `tests/test_hub.py` | `make test`; `make demo` | Hub local and clean-clone reports at `850a33de075c`; 11 tests and demo passed | statically-validated |
| CPU utilization, memory, normalized load | Toolkit | `src/ops_toolkit/collectors.py`: `cpu`, `memory`, `load` | `make test`; `make integration` metric invariants | T-local; T-Linux | integration-tested |
| Disk capacity and inode pressure | Toolkit | `src/ops_toolkit/collectors.py`: `filesystem` | Fixture policy tests; portable demo; live Linux check | T-local; T-Linux | integration-tested |
| Process counts/state and systemd service state | Toolkit | `src/ops_toolkit/collectors.py`: `processes`, `service` | Count/state invariants; observed `dbus.service` | T-Linux; no boot/reboot exercise | integration-tested |
| Listening sockets via `ss` | Toolkit | `src/ops_toolkit/collectors.py`: `sockets` | Parser/privacy fixtures; live TCP/UDP count assertions | T-local; T-Linux | integration-tested |
| Local certificate expiry and backup freshness | Toolkit | `src/ops_toolkit/collectors.py`: `certificate`, `backup`; `scripts/integration.py` | Temporary marker fresh/stale/recovered; generated certificate with two policies | T-Linux; no actual backup restore or TLS trust test | integration-tested |
| Mode/ownership/ACL metadata and numeric identity/users/groups inventory | Toolkit | `src/ops_toolkit/collectors.py`: `path_metadata`, `acl`; `backend.py`: identity | Explicit README path, UID invariant and `getfacl`; fixture metadata tests | T-local; T-Linux; no user/group administration | integration-tested |
| journald priorities, cron/logrotate entry counts, systemd timer inventory | Toolkit | `src/ops_toolkit/collectors.py`: `journal`, `file_schedules`, `timers` | `make integration` journal/schedules inspection | T-Linux; schedule execution/log rotation not tested | integration-tested |
| Debian package count and diagnostic tool availability | Toolkit | `src/ops_toolkit/collectors.py`: `packages`, `inspect` | Positive package-count invariant; live capability discovery | T-Linux; no package mutation/advisory audit | integration-tested |
| RPM package-count parser | Toolkit | `src/ops_toolkit/collectors.py`: `packages`; `tests/test_toolkit.py`: `test_rpm_inventory` | Synthetic RPM fixture | T-local; no RPM-family live integration | statically-validated |
| `lsof`, `vmstat`, `iostat`, `sar`, `strace`, `tcpdump` availability only | Toolkit | `src/ops_toolkit/collectors.py`: tool discovery | Present/missing tool fixtures and live inventory | T-local; T-Linux; diagnostics were not executed | integration-tested |
| Bash orchestration; structured Python CLI | Toolkit | `bin/ops-toolkit`, `scripts/demo.sh`, `src/ops_toolkit/cli.py` | ShellCheck/shfmt/Ruff, CLI tests, portable demo and Linux integration | T-local; T-Linux | integration-tested |
| JSON contract, thresholds, validation, exits and timeouts | Toolkit | `src/ops_toolkit/model.py`, `cli.py`, `backend.py`; `tests/` | Healthy/degraded/unavailable/invalid/parser/timeout assertions within 58 tests | T-local; T-Linux unit gates; timeout failure simulation | statically-validated |
| Troubleshooting and read-only operational runbooks | Toolkit | `docs/demo.md`, `docs/runbooks/triage.md`, `scripts/demo.sh` | `make demo`; temporary-file freshness recovery in integration | T-local; T-Linux; bounded lab workflow | integration-tested |
| Users, SSH/sudo policy, packages, chrony | Fleet automation | Planned Ansible roles/cloud-init | ansible-lint, Molecule, per-distro converge | None | planned |
| Services, firewall, logging, rolling patch orchestration | Fleet automation | Planned roles/playbooks | VM reachability, reversible change, second converge | None | planned |
| apt/dnf differences, SELinux/AppArmor handling | Fleet automation | Planned explicit distro branches | Per-distro config rejection and security assertions | None | planned |
| Virtualization, cloud-init, systemd/reboots | Fleet automation; network/storage lab | Planned disposable VM inventory/provider | VM boot/reboot and inventory-scoped teardown | None | planned |
| DNS, isolated DHCP, routing, subnets, bridges/VLANs | Network/storage lab | Planned network profiles | Client/server queries, bounded fault, scoped capture | None | planned |
| NFS, Samba, reverse proxy/load balancing, local TLS | Network/storage lab | Planned service profiles | Client read/write, proxy routing, TLS validation | None | planned |
| nftables/firewalld and network failure diagnosis | Network/storage lab | Planned firewall/fault profiles | Allowed/denied connectivity assertions | None | planned |
| Partitions, ext4/XFS, LVM, RAID, mounts, quotas, LUKS | Network/storage lab | Planned lab-owned disk profiles | Ownership preflight; expansion/degradation/restore assertions | None | planned |
| API, async worker, PostgreSQL, queue/cache, migrations | Container platform | Planned reference application | Submit/complete job; deterministic seeds; API tests | None | planned |
| Docker/Compose, image builds, readiness, persistence | Container platform | Planned Dockerfiles/Compose | Clean setup; restart persistence; outage handling | None | planned |
| Namespaces/cgroups, signals, networking, image layers | Container platform | Planned bounded demonstrations | Graceful stop and resource/network observations | None | planned |
| Rootless Podman | Container platform extension | Planned separate profile | Rootless clean setup and workflow assertions | None | planned |
| IaC modules, AWS networking/IAM/encryption/state | Cloud foundation | Planned primary engine/modules | fmt, validate, lint, policy, module mocks | None | planned |
| Authenticated AWS plan / cloud deployment | Cloud foundation gated profile | Planned gated configuration | Real plan/apply only after new authorization | None; disabled | planned |
| GitHub Actions lint/test/build/artifacts/promotion | Delivery pipelines | Planned workflows/local scripts | Exact-SHA Actions run and local reproduction | None | planned |
| Blocking quality gate and release rollback | Delivery pipelines | Planned negative fixture/promotion scripts | Intentional failure; restore prior artifact | None | planned |
| Jenkins, JCasC, isolated agents | Delivery pipelines extension | Planned Jenkins profile | Executed isolated pipeline | None | planned |
| Kubernetes, Helm, Gateway API, CNI/NetworkPolicy | Kubernetes/GitOps | Planned cluster/charts/policies | Deployment plus verified denied network path | None | planned |
| RBAC, Pod Security, probes, resources, storage, scaling | Kubernetes/GitOps | Planned manifests/profiles | Health/RBAC/metrics-backed scaling assertions | None | planned |
| Argo CD reconciliation, Git rollback, safe rollout | Kubernetes/GitOps | Planned GitOps layout | Bad release, Git rollback, drift reconciliation | None | planned |
| OpenTelemetry, metrics/logs/traces and correlation | Observability/SRE | Planned instrumentation/collector | Locate one request's trace and log | None | planned |
| Prometheus, Grafana, Alertmanager, Loki, Tempo | Observability/SRE | Planned provisioned profiles | Controlled fault, alert firing and resolution | None | planned |
| SLI/SLO/error budgets, performance and load | Observability/SRE | Planned rules/runbooks/load tests | promtool plus bounded k6 measurements | None | planned |
| Secrets/vulnerability scanning, SBOM, signatures | DevSecOps policy | Planned complementary toolchain | Safe accept/reject fixtures; intended signer/issuer | None | planned |
| IaC policy, Kubernetes admission | DevSecOps policy | Planned policy packs | Allowed/denied fixtures and admission exercise | None | planned |
| SOPS/age local secrets workflow | DevSecOps policy | Planned ignored runtime keys and encrypted fixtures | Encrypt/decrypt/rotation exercise without key disclosure | None | planned |
| Encrypted file backups and PostgreSQL restore | Backup/recovery | Planned restic/DB profiles | Identifiable seed, loss, isolated restore, checksum/record check | None | planned |
| WAL/PITR and optional Kubernetes recovery | Backup/recovery extensions | Planned distinct profiles | Point-in-time record assertions; accurate backend restore | None | planned |
| Scheduling, retention, integrity, RTO/RPO observation | Backup/recovery | Planned runbooks/measurement scripts | Failure alert and measured recovery | None | planned |
| Developer self-service template, schema, catalog | Golden path | Planned generator/schema/catalog | Generate clean service; reject inputs; tests/deploy/telemetry | None | planned |
| Incident triage, bounded failure injection, postmortem | Capstone | Planned pinned-release scenario | Failed deployment, dependency outage, data restore lifecycle | None | planned |

Enterprise tools and additional clouds are scoped in the
[extension backlog](docs/extension-backlog.md). Their status is planned until a
meaningful implementation and appropriately scoped evidence exist. In particular,
tool availability reporting is not expertise or exercised troubleshooting with
that tool; a local IaC mock is not AWS deployment; an SBOM is not a vulnerability
remediation; and a backup file is not a successful recovery.
