# Project status

Capability, publication, CI and release state are independent. This portfolio is
lab/reference engineering work. The [evidence index](docs/evidence-index.md)
identifies the exact source revisions and execution environments. Three of twelve
engineering cores are complete; the hub makes four verified public repositories.
Nine engineering projects remain. The containerized service platform is the only
active engineering project, beginning with acceptance and dependency review.

| Project | Work state | Capability state | Publication | CI | Release |
| --- | --- | --- | --- | --- | --- |
| Portfolio hub | First milestone complete; supporting index | statically-validated; original local/clone source `850a33de075c` | [Public hub](https://github.com/Yash-PK/ops-linux-devops-portfolio) verified at `cd9a6741e3d6` | [Passed for `cd9a6741e3d6`](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37731050426) | Work-in-progress index; no release intended |
| Linux operations toolkit | Bounded core complete; no longer active | integration-tested on Ubuntu x86-64 CI | Public repository; release target `0d164e9158ee` | Passed for `0d164e9158ee` | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0) |
| Linux fleet automation | Bounded core complete; no longer active | integration-tested on Ubuntu and AlmaLinux ARM64 VMs | [Public repository](https://github.com/Yash-PK/ops-linux-fleet-automation); target `1531b86b54ee` | [Passed for `1531b86b54ee`](https://github.com/Yash-PK/ops-linux-fleet-automation/actions/runs/37615270935) | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-fleet-automation/releases/tag/v0.1.0) |
| Network/storage services lab | Bounded core complete | integration-tested on Ubuntu ARM64 VZ | [Public repository](https://github.com/Yash-PK/ops-network-storage-services-lab); target `53b78f81ed58` | [Passed](https://github.com/Yash-PK/ops-network-storage-services-lab/actions/runs/37735444827) | [v0.1.0](https://github.com/Yash-PK/ops-network-storage-services-lab/releases/tag/v0.1.0) |
| Containerized service platform | Only active project; acceptance and dependency review | planned | Not created | Not run | None |
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
all four public repositories without adding a paid service. No account-wide settings were changed.

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
trees on resumption. [NEXT_STEPS.md](NEXT_STEPS.md) records the active container platform
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

## Completed network/storage core

The [public repository](https://github.com/Yash-PK/ops-network-storage-services-lab) and [v0.1.0 release](https://github.com/Yash-PK/ops-network-storage-services-lab/releases/tag/v0.1.0)
are verified at `53b78f81ed58602efd2c151d449338615ab61e9d`, with [passing exact-target CI](https://github.com/Yash-PK/ops-network-storage-services-lab/actions/runs/37735444827).
Controller source `a9950a19f7fe578c9e27b4cf59e0a1ebafdbd8ac` passed 122 tests,
required lint, safe demo and working/staged/full-history secret scans. Clean-clone
and real VM evidence belong to `e43bcdfdae1a604a095eea085e81eb8fbe2e6d00` and fingerprint
`0ddbae1dd5d52f9c6100f22910535571e189e49c29411f950731b4852bfea593`; later documentation/evidence commits do not replace them.

The Ubuntu 24.04 ARM64 VZ run passed 605 commands and 110 assertions: private
VLANs/routing, DNS/DHCP, NFS, encrypted SMB3 with anonymous rejection, two TLS proxy
backends with trust/hostname rejection, firewall denial/recovery and bounded
capture; GPT/ext4/XFS/fstab/quotas, LVM expansion, RAID degradation/rebuild and
LUKS rejection/reopen. It verified 41 selected snapshot package pins, authenticated
cold boot into `6.8.0-146-generic`, retained AppArmor, guest cleanup and VM deletion.
Namespaces are clients within one VM; loop images are not physical-disk evidence.

The temporary clone and VM were removed; the owned registry is empty. About
793 MiB of local tools, caches and ignored private metadata remains. Earlier
uncommitted failures and development passes remain documented as development only.
Secret scans found no matches; selected dependency review is not a full image or
transitive vulnerability audit. No cloud resources or container packages were published.

## Active continuation — containerized service platform

Project 4 is selected next. Define its bounded API/worker/PostgreSQL/cache/proxy
acceptance before coding; verify dependencies, resource limits and the available
container execution environment. Capabilities remain planned until implementation
and appropriate evidence exist. Projects 5–12 remain roadmap entries; no remote
repositories have been created for them. See [next steps](NEXT_STEPS.md).

The latest verified hub snapshot before this update is
`e6bd08197a96f5f7ee4dc9b35b72ef1007792f0d`, with
[passing CI](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37734298497).
Historical hub source and publication identities remain in the evidence index.
