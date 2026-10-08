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

Fleet paths refer to the [verified released repository](https://github.com/Yash-PK/ops-linux-fleet-automation).
**F-local** and **F-Ubuntu** identify controller/clean-clone and Ubuntu VM reports at
`c52155a5c15b04bdb2a85746b385da0243ecef93`; **F-Alma** identifies the complete
AlmaLinux VM report at `e333e1c8c37b107fb6e99924c869555acca0ad68`.
Both VM profiles passed with the same implementation fingerprint. The released
fleet core is integration-tested; other distributions/providers remain unverified.
Network/storage paths identify the local `ops-network-storage-services-lab`
repository; no remote is published. **N-local** records 120 fixture tests and
required lint/demo passing on uncommitted source, with formal revision-linked
evidence still pending. **N-storage-dev** records an earlier actual storage VM
development run, before current kernel/dependency changes. It cannot qualify the
current implementation for release; overall project state is implemented-unverified.

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
| Locked fleet controller/bootstrap | Fleet automation | `requirements-dev.lock`, `collections.lock.json`, `provider.lock.json`, `scripts/bootstrap_fleet.py` | `make bootstrap`; `make doctor`; clean-clone gate | F-local: locked installation/doctor/validation/demo/security passed in clean clone; scratch removed | statically-validated |
| Provider ownership, strict SSH and scoped Ubuntu lifecycle | Fleet automation | `scripts/lab.py`, `tests/test_lab.py`, `tests/test_paths.py`, `scripts/integration.py` | Provider safety tests; actual Ubuntu boot, changed-key rejection and teardown | F-local; F-Ubuntu: expected SSH exit 255 and owned teardown passed | integration-tested |
| Typed role input rejection and safe controller demo | Fleet automation | `roles/ops_baseline/tasks/validate_inputs.yml`, `playbooks/check-input.yml`, `tests/test_role_inputs.py` | `make test`; `make demo` | F-local: actual Ansible assertions within 74 tests; valid input accepted and invalid input rejected | statically-validated |
| Ubuntu users, SSH/sudo policy, apt packages and chrony | Fleet automation | `roles/ops_baseline/tasks/accounts.yml`, `roles/ops_baseline/tasks/packages.yml`, `roles/ops_baseline/tasks/services.yml`; `roles/ops_baseline/templates/` | `make integration LAB=ubuntu` | F-Ubuntu: real converge/verification, zero-change second converge and guest package-version capture | integration-tested |
| Ubuntu nftables, journald, nginx and AppArmor preservation | Fleet automation | `roles/ops_baseline/tasks/firewall.yml`, `roles/ops_baseline/tasks/services.yml`, `roles/ops_baseline/tasks/web.yml`, `roles/ops_baseline/vars/Ubuntu.yml`; `playbooks/tasks/verify-state.yml` | Live service/policy/response assertions and post-reboot state checks | F-Ubuntu: all workflow steps passed; AppArmor retained; earlier firewall reboot failure archived | integration-tested |
| AlmaLinux dnf, service differences, SELinux and firewalld | Fleet automation | `roles/ops_baseline/vars/AlmaLinux.yml`, `roles/ops_baseline/tasks/preflight.yml`, `roles/ops_baseline/tasks/firewall.yml`; shared baseline tasks | `make integration LAB=alma` | F-Alma: complete real-VM configuration and post-reboot checks passed; SELinux enforcing and firewalld retained | integration-tested |
| Ubuntu rolling converge, idempotence and content change/rollback | Fleet automation | `playbooks/site.yml`, `molecule/default/molecule.yml`, `scripts/integration.py` | Real Molecule converge/idempotence/verify; live changed/restored responses | F-Ubuntu: second converge changed=0; invalid input exit 2 with zero changes; change and restoration verified | integration-tested |
| Ubuntu cloud-init, systemd and explicit patch/reboot | Fleet automation | `scripts/lab.py`, `playbooks/patch.yml`, `playbooks/tasks/verify-state.yml` | `make integration LAB=ubuntu` with explicit lab identity | F-Ubuntu: real boot, patch/reboot and state checks before repair passed; teardown passed | integration-tested |
| AlmaLinux lifecycle, idempotence and change/reboot acceptance | Fleet automation | Same guarded playbooks/provider; AlmaLinux variables and native service policy | `make integration LAB=alma` | F-Alma: all nine steps, zero-change second converge, rejection/change/restore/reboot and scoped teardown passed | integration-tested |
| Standalone pinned VM provider, snapshot packages, guarded controller and evidence gate | Network/storage lab | `scripts/bootstrap_provider.py`, `scripts/lab.py`, `scripts/evidence.py`, `component.lock.json`, `packages.lock.json`, `tests/` | `make validate`; `make demo`; malformed/unsafe/stale-proof rejection fixtures | N-local: 120 tests, required lint and safe demo passed; uncommitted source; formal clone/revision evidence pending | statically-validated |
| macOS ARM64 Lima VZ lifecycle with authenticated reboot | Network/storage lab | `scripts/lab.py`, `guest/prepare.py`, `guest/main.py`; pinned released fleet component | `make integration LAB=ops-network-storage-reference`; exact kernel/AppArmor and owned cleanup assertions | N-storage-dev proves an earlier VM/storage lifecycle only; revised reboot/all-profile proof pending | implemented-unverified |
| DNS, isolated DHCP, routing, subnets, bridges/VLANs | Network/storage lab | `guest/network.py`: `Session.topology`, `dns` with optional DHCP; `tests/test_network.py` | Guest client queries/leases and routed reachability; fixture boundaries | N-local fixtures; live network development validation active, no passing integration credited | implemented-unverified |
| NFS, Samba, reverse proxy/load balancing, local TLS | Network/storage lab | `guest/network.py`: `nfs`, `samba`, `proxy` | Client read/write; authenticated SMB with anonymous rejection; two backends and TLS trust/hostname rejection | N-local fixtures; real service assertions awaiting passing VM evidence | implemented-unverified |
| nftables, network failure/recovery and bounded private tcpdump capture | Network/storage lab | `guest/network.py`: `firewall` and `Session.cleanup` | Actual denied/recovered path and private capture; owned inventory cleanup | N-local fixtures; current live assertions not yet passed; no firewalld implementation in this project | implemented-unverified |
| GPT, ext4/XFS, fstab and actual quota limits | Network/storage lab | `guest/storage.py`: `filesystems`, `quota`; `tests/test_storage.py` | Persisted checksums, non-root EDQUOT/recovery and scoped unmount/cleanup | N-storage-dev passed on earlier uncommitted fingerprint; current all-profile gate pending | implemented-unverified |
| LVM/filesystem expansion, RAID1 degradation/rebuild, LUKS | Network/storage lab | `guest/storage.py`: `lvm`, `raid`, `luks` | Growth/data invariants; degraded/rebuilt array checksums; wrong-key rejection and reopen | N-storage-dev: 438 total storage commands/63 assertions passed with VM deletion; current dependency revision unverified | implemented-unverified |
| KVM/libvirt, other hypervisors and multiple-VM private switching | Network/storage extensions | No implementation | Separate supported provider and real lifecycle required | None; namespace clients are not additional VMs | planned |
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
