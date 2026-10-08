# Project status

Capability, publication, CI and release state are independent. This portfolio is
lab/reference engineering work. The [evidence index](docs/evidence-index.md)
identifies the exact source revisions and execution environments. Two of twelve
engineering cores are complete; the hub makes three verified public repositories.
Ten engineering projects remain incomplete, with network/storage implementation
under active validation.

| Project | Work state | Capability state | Publication | CI | Release |
| --- | --- | --- | --- | --- | --- |
| Portfolio hub | First milestone complete; supporting index | statically-validated; original local/clone source `850a33de075c` | [Public hub](https://github.com/Yash-PK/ops-linux-devops-portfolio) verified at `cd9a6741e3d6` | [Passed for `cd9a6741e3d6`](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37731050426) | Work-in-progress index; no release intended |
| Linux operations toolkit | Bounded core complete; no longer active | integration-tested on Ubuntu x86-64 CI | Public repository; release target `0d164e9158ee` | Passed for `0d164e9158ee` | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0) |
| Linux fleet automation | Bounded core complete; no longer active | integration-tested on Ubuntu and AlmaLinux ARM64 VMs | [Public repository](https://github.com/Yash-PK/ops-linux-fleet-automation); target `1531b86b54ee` | [Passed for `1531b86b54ee`](https://github.com/Yash-PK/ops-linux-fleet-automation/actions/runs/37615270935) | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-fleet-automation/releases/tag/v0.1.0) |
| Network/storage services lab | Only active engineering project; local source and fixtures implemented | implemented-unverified overall; controller statically validated | Not created | Not run | None |
| Containerized service platform | Not started | planned | Not created | Not run | None |
| Cloud foundation IaC | Not started | planned | Not created | Not run | None |
| Delivery pipelines | Not started | planned | Not created | Not run | None |
| Kubernetes/GitOps platform | Not started | planned | Not created | Not run | None |
| Observability/SRE lab | Not started | planned | Not created | Not run | None |
| DevSecOps policy lab | Not started | planned | Not created | Not run | None |
| Backup/disaster recovery | Not started | planned | Not created | Not run | None |
| Platform engineering golden path | Not started | planned | Not created | Not run | None |
| Production simulation capstone | Not started | planned | Not created | Not run | None |

## Completed toolkit core

The verified public repository is
[ops-linux-operations-toolkit](https://github.com/Yash-PK/ops-linux-operations-toolkit),
owned by the confirmed personal account `Yash-PK`, visibility `PUBLIC`, default
branch `main`. The verified non-draft, non-prerelease
[release v0.1.0](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0)
targets `0d164e9158eeb9540e895d5f48bcf4723f36667b`. Its
[exact-revision CI run](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37573353795)
passed. The earlier remote/evidence revision `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4`
remains the tested source for the original Linux report.

Local source revision `55f15eaacf3842fa15f44751d5f21a5094bd089c` passed 58 tests,
Ruff, ShellCheck, shfmt, actionlint, repository checks, the fixture/portable live
demo, Gitleaks scans and clean-clone validation. Local checks ran on macOS ARM64.
The [Linux Actions run](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607)
passed for the exact published `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` revision.
Its Ubuntu x86-64 environment used kernel `6.17.0-1022-azure` and Python 3.14.7.

The Linux run exercised seven health sources (CPU, load, memory, disks, inodes,
processes and listening sockets) with metric invariants; live path, numeric
identity, package and tool inspection; temporary backup freshness transitioning
fresh → stale → recovered; actual locally generated certificate expiry under two
policies; `dbus.service`, journald and schedule metadata; and `getfacl` ACL metadata.
All integration assertions completed with exit 0. A degraded fixture or stale
backup intentionally returned its expected nonzero health status inside the
successful validation workflow.

Tool availability is the implemented scope for `lsof`, `vmstat`, `iostat`, `sar`,
`strace` and `tcpdump`; these diagnostics were not executed. No full OS boot/reboot,
privileged administration, cgroup policy, SELinux/AppArmor behavior, other-distro
integration or cloud deployment is claimed. A freshness marker is not proof of
backup recovery, and certificate expiry does not validate trust or hostname.

## Environment, security and cleanup

The local development host is macOS 26.6.2 ARM64 with 14 logical CPUs,
Python 3.14.7 and Bash 3.2. Fleet prerequisite inspection verified 24 GiB RAM,
hardware virtualization and about 1.6 TiB free disk at assessment time. Docker
tooling is installed and existing Colima was stopped at the original assessment.
The first milestone's toolkit Linux evidence comes from hosted CI. Fleet work has
completed Ansible and real OS-lifecycle acceptance in isolated Ubuntu 24.04 and
AlmaLinux 9.8 ARM64 Lima VZ guests locally. Neither guest is represented as a
container or cloud deployment.

Gitleaks found no findings in the required outgoing working/staged/history scans.
Pattern scanning does not guarantee absence of every secret. Secret scanning,
push protection and private vulnerability reporting were verified enabled for
all three public repositories without adding a paid service. No account-wide settings were changed.

Toolkit temporary clones and integration files, including the ephemeral certificate
key, were cleaned. The hub clean-clone gate passed and removed its scratch checkout. Ignored local developer caches (`.venv`, `.tools`) remain for repeat
runs. Both recorded fleet guests were deleted, its owned registry is empty and
its working tree was clean at release verification. Approximately 1.05 GiB of
image caches, local tools and ignored private metadata/credentials remain.
Inspect provider state before any resumed cleanup. Cloud creation, paid services,
host configuration changes and container package publication remain **disabled**.
Existing Git identity was used.

## Completed first-milestone snapshot

The first milestone is complete: toolkit v0.1.0 and this public hub are published.
The hub's recorded publication/CI snapshot is
`f1de5b4ee59176cb0eaf9e9a4e61af308ebf516e`, owner `Yash-PK`, visibility `PUBLIC`,
default branch `main`. Its hosted workflow passed all four required command groups;
[the preserved CI report](evidence/f1de5b4ee591-local.json) records actual results.
Secret scanning, push protection and private vulnerability reporting were enabled
and verified on both repositories. Branch rules are proposed, not imposed.

Hub local/clone source remains `850a33de075cd5f43c4a1a30f4efa3830fea944d`; reports
are committed later. Subsequent index/evidence commits are identified in Git and
receive their own CI runs; do not reinterpret them as the original tested source.
The final handoff checks the latest remote HEAD separately from this saved snapshot.

No unresolved required check or publication blocker remains for the first
milestone. Its optional full OS lifecycle, privileged diagnostics, non-Ubuntu Linux
and cgroup policy remain unverified. No cloud deployment was performed. Its
temporary resources were cleaned; fleet resource cleanup is recorded separately
below.

Changed artifacts in this milestone include the toolkit source/tests/CI/runbooks,
the hub's plan, ledger, matrix, dependency/evidence indexes, and revision-linked
reports. Commits describe those actual implementation and verification steps;
no author identity, activity or results were fabricated. Inspect completed working
trees on resumption. [NEXT_STEPS.md](NEXT_STEPS.md) records the active network/storage
validation work.

## Completed fleet core

The verified public [fleet repository](https://github.com/Yash-PK/ops-linux-fleet-automation)
is owned by `Yash-PK`, visibility `PUBLIC`, default branch `main`.
[Release v0.1.0](https://github.com/Yash-PK/ops-linux-fleet-automation/releases/tag/v0.1.0)
is non-draft and non-prerelease, published `2026-10-07T11:38:28Z` at
`1531b86b54eee87d01da83f7b55d7d405f43fadb`. The remote/tag SHA and
[passing CI for that exact target](https://github.com/Yash-PK/ops-linux-fleet-automation/actions/runs/37615270935)
were verified. No required core gate or publication blocker remains.

Controller/clean-clone/Ubuntu source remains
`c52155a5c15b04bdb2a85746b385da0243ecef93`; AlmaLinux source is
`e333e1c8c37b107fb6e99924c869555acca0ad68`. The implementation fingerprint is
`391a99a45747322a4358e199d1454d2b29f175e171592995cae890761137bb0d` in both VM
reports. Controller validation passed 74 tests plus doctor, required lint, input
demo and Gitleaks. The later `627e25c38de2` publishing clean clone and hosted Linux
controller artifact passed separately; they do not replace original VM evidence.

Both real VMs passed all nine workflow steps: strict SSH changed-key rejection
(expected exit 255), Molecule converge/zero-change idempotence/verify, invalid
input rejection with zero changes (expected exit 2), unchanged-service checks,
content change/verification/restoration/verification, and patch/reboot with state
checks before repair. Guest package versions and scoped teardown were recorded.
Ubuntu retained AppArmor; AlmaLinux retained enforcing SELinux and firewalld policy.
Each used macOS ARM64 Lima VZ, 2 CPUs, 2 GiB RAM and a 24 GiB sparse disk, one at
a time, with no host mounts. Full results are in the [evidence index](docs/evidence-index.md).

The earlier `8db4d22e1c56` post-reboot firewall failure remains archived. The
corrected unit boot ordering passed a fresh Ubuntu run; no failed result was
converted into a pass. Other distros/providers, external network-denial tests,
multi-host availability and cloud deployment are outside the demonstrated core.

## Active continuation — network/storage services lab

Project 3 is the only active engineering project. Source exists locally at
`/Users/hbsu/ops-network-storage-services-lab`; overall status is
**implemented-unverified**. No remote, GitHub CI run or release exists. Its bounded
acceptance was defined before implementation. Projects 4–12 remain roadmap entries.

The implementation uses a hash-pinned released fleet provider and local Lima VZ
to provision one Ubuntu ARM64 VM, with guest-private namespace clients and owned
loop-backed image files. It implements six network profiles (DNS, DHCP, NFS,
Samba, TLS reverse proxy/load balancing, firewall/failure/capture) and four storage
profiles (filesystems/fstab/quotas, LVM expansion, RAID recovery and LUKS).
Its standalone bootstrap pins 41 Ubuntu snapshot packages; the controller separates
preparation, authenticated reboot and profile execution, requiring the exact locked
running kernel and retained AppArmor. No host mounts or host configuration changes
are part of this design.

The uncommitted implementation passed 120 fixture tests, Ruff, ShellCheck, shfmt,
actionlint, documentation checks and the safe dry-run/invalid-input demo. These
establish controller/static behavior only. No formal tested Git revision exists.
An earlier real storage development run passed 438 commands and 63 assertions,
including GPT/ext4/XFS persistence, quota EDQUOT/recovery, LVM growth, RAID1
degradation/rebuild, LUKS rejection/reopen and scoped cleanup. Its source was
uncommitted and subsequent kernel/library pinning requires a fresh run; this is
not current-code release proof. The [evidence index](docs/evidence-index.md)
retains its exact fingerprint and development boundary.

Network development validation is active; no successful network or all-profile
integration is credited in this snapshot. The earlier storage VM was deleted.
The completed `053143` development run passed package/kernel, VLAN/routing, DNS,
DHCP and NFS checks, then failed Samba startup. Its VM deletion passed. A fresh
diagnostic run is in progress; inspect owned provider state before allocation
or cleanup. Its ignored tools,
image caches, runtime credentials and private diagnostics must remain unpublished.

Next: resolve actual network VM failures, run fresh development profiles after any
fixes, review/commit source, collect formal all-profile VM and controller/clean-clone
evidence, then complete outgoing security/publishing gates and exact-head CI before
release. No cloud deployment or container-package publication has occurred.

The latest separately verified hub publication/CI snapshot is
`cd9a6741e3d6d54e3cd39fff18d1f40359bf5313`, with
[passing exact-target CI](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37731050426).
It does not replace the original `850a33de075c` local/clone source or the archived
`f1de5b4ee591` first-milestone hosted evidence.
