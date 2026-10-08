# Project status

Capability, publication, CI and release state are independent. This portfolio is
lab/reference engineering work. The [evidence index](docs/evidence-index.md)
identifies the exact source revisions and execution environments. Four of twelve
engineering cores have completed releases; the hub makes five verified public repositories.
Eight engineering projects remain. Cloud foundation IaC is the only active
engineering project, beginning dependency review and a static/mock OpenTofu/AWS
core. Its capability remains planned. Cloud execution is disabled.

| Project | Work state | Capability state | Publication | CI | Release |
| --- | --- | --- | --- | --- | --- |
| Portfolio hub | First milestone complete; supporting index | statically-validated; original local/clone source `850a33de075c` | [Public hub](https://github.com/Yash-PK/ops-linux-devops-portfolio) verified at `8b1154259f9a` | [Passed for `8b1154259f9a`](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37736216993) | Work-in-progress index; no release intended |
| Linux operations toolkit | Bounded core complete; no longer active | integration-tested on Ubuntu x86-64 CI | Public repository; release target `0d164e9158ee` | Passed for `0d164e9158ee` | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0) |
| Linux fleet automation | Bounded core complete; no longer active | integration-tested on Ubuntu and AlmaLinux ARM64 VMs | [Public repository](https://github.com/Yash-PK/ops-linux-fleet-automation); target `1531b86b54ee` | [Passed for `1531b86b54ee`](https://github.com/Yash-PK/ops-linux-fleet-automation/actions/runs/37615270935) | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-fleet-automation/releases/tag/v0.1.0) |
| Network/storage services lab | Bounded core complete | integration-tested on Ubuntu ARM64 VZ | [Public repository](https://github.com/Yash-PK/ops-network-storage-services-lab); target `53b78f81ed58` | [Passed](https://github.com/Yash-PK/ops-network-storage-services-lab/actions/runs/37735444827) | [v0.1.0](https://github.com/Yash-PK/ops-network-storage-services-lab/releases/tag/v0.1.0) |
| Containerized service platform | Bounded core complete; no longer active | integration-tested on Ubuntu ARM64 VZ/Compose | [Public repository](https://github.com/Yash-PK/ops-containerized-service-platform); target `cdea68d2a446` | [Passed for `cdea68d2a446`](https://github.com/Yash-PK/ops-containerized-service-platform/actions/runs/37743579858) | [v0.1.0](https://github.com/Yash-PK/ops-containerized-service-platform/releases/tag/v0.1.0) |
| Cloud foundation IaC | Only active project; dependency review and core definition starting | planned | Not created | Not run | None |
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
all five public repositories without adding a paid service. No account-wide settings were changed.

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

## Completed containerized service platform core

Project 4 exists locally at `/Users/hbsu/ops-containerized-service-platform`.
Its bounded acceptance was recorded before implementation. Source implements a
Python HTTP API and separate worker, PostgreSQL durable job state/lease fencing,
idempotent requests, checksum-verified migrations and repeatable synthetic seeds.
Valkey caches successful results only; nginx exposes the API. Digest-pinned
multi-stage containers, Compose readiness/resource settings, fresh local
credentials, a guarded VM runner, negative/safety tests and operational docs are
present. Capability state is **integration-tested** for the recorded local ARM64
VM/Compose environment. The [public repository](https://github.com/Yash-PK/ops-containerized-service-platform) is verified under
`Yash-PK`, visibility `PUBLIC`, default branch `main`, at
`cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe`, matching the verified
[v0.1.0 tag and release](https://github.com/Yash-PK/ops-containerized-service-platform/releases/tag/v0.1.0). [Exact-target hosted CI](https://github.com/Yash-PK/ops-containerized-service-platform/actions/runs/37743579858)
passed. The preserved [Linux controller artifact](https://github.com/Yash-PK/ops-containerized-service-platform/blob/cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe/evidence/19ec88d5d4a6-ci-linux.json)
records `19ec88d5d4a6aa7541e7722b994618c3a6929cc5`: all 71 tests and the
doctor/validate/demo/security groups passed on Linux x86-64 with Python 3.14.7.
These evidence/docs commits do not replace the formal runtime source.

Formal source `950e511f42173c00994496265bb48104623e1bea`, fingerprint
`1058c9278fe1942b5becedbde4a5ffd312a846f18959af587ebe2e3615f3ad22`, passed
doctor, lint/docs/configuration checks, all 57 unit/controller/safety tests,
the safe demo and working/staged/full outgoing history secret scans. Its
controller report confirms clean source at start and unchanged source at finish.
The standalone clean clone also passed bootstrap, doctor, validation, demo and
security; its temporary checkout was removed. Earlier controller evidence at
`7766299b2d24` remains valid only for its original 45-test source revision.

The first formal VM report for `950e511f4217` failed during SSH payload upload
with exit 255 before guest phases; VM deletion passed. Its private transport log
reported `mm_send_fd: sendmsg(2): Message too long` and file-descriptor handoff
failure. The 54,532-byte encoded payload plus installer exceeded the multiplexed
transport request's capacity despite fitting the application's former bound.
This remains a failed formal attempt, not a container acceptance pass.

Current source `3d58b9f7107fa1c7de3eec06b32c9b6f6ce644d6` implements validated
chunks of at most 8,000 encoded bytes, a 16,000-byte shell-quoted command cap,
staging ownership/sequence checks, part/whole checksums and interrupted-transfer
cleanup. The formal controller report passed all 71 tests and required command groups,
with clean/unchanged source and fingerprint
`2d02d563e250b498d07b3695894a21d825bc7310c6ed47bd2afc3ee55b1a2f2b`. The fresh
standalone clone passed all gates and was removed. The complete formal VM run
passed from 07:14:49 to 07:20:20 UTC on 2026-10-08: 22 preparation commands and
assertions, 117 Compose commands, 72 Compose assertions and 21 nested SQL
assertions. Compose resources and the VM were removed; inventory is empty.
Observed Python/Psycopg/libpq/valkey-py versions are 3.14.7/3.3.6/18.6/6.1.1.
Preserve earlier evidence identities.

All four earlier development runs remain failed overall with successful VM
cleanup: private runtime-parent mode, engine startup, guest-loopback connection,
and process inspection respectively. The fourth passed asynchronous jobs,
restart persistence, cache/database outage recovery, API shutdown, repeatable
migrations/seeds and all 21 real SQL assertions, then failed because `docker top`
was invoked without the PID column it needs. Strict UID/PID parsing and realized
port checks were implemented in `950e511f4217` and subsequently passed the
complete `3d58b9f7107f` formal lifecycle. The original partial failures remain
failed and are not substituted for that later complete evidence.

The runner uses an owned Ubuntu ARM64 VZ VM with Docker 29.8.2, Compose 5.6.0 and
Buildx 0.38.0. Only nginx joins the normal edge bridge for guest-loopback publishing;
frontend/backend remain internal. No host Colima context is adopted. Local publishing
gates, hosted CI and release verification passed, and the working tree was clean.
Configured-only hardening fields and worker graceful-exit verification remain
explicitly outside the observed acceptance scope. A completed lab core does not
claim those optional extensions or production readiness.

Private vulnerability reporting, dependency alerts, secret scanning and push
protection were verified enabled for P4; no ruleset was changed. Owned instances
are zero. Approximately 977 MiB remains ignored: 755 MiB in `.runtime`, 166 MiB
in `.tools` and 56 MiB in `.venv`. These retained caches are not a cleanup blocker.

Rootless Podman, other runtime providers and cloud execution remain unverified
extensions. Preserve P4 source and immutable evidence while building the next core.

## Active continuation — cloud foundation IaC

Project 5 is the only active engineering project. Its next bounded task is official
support/release/advisory review for OpenTofu and the AWS provider, then acceptance
definition and a local static/mock AWS foundation. Capability is still **planned**;
no implementation result, repository URL, hosted CI or deployment is claimed.
Use OpenTofu as the primary engine and claim compatibility only with engines
actually tested. Keep real state, plans and credentials out of Git, disable
cost-bearing profiles, and provide no cloud apply or authenticated cloud operation
under current authorization. Projects 6–12 remain roadmap entries.
See [next steps](NEXT_STEPS.md) for the exact task.

The latest verified hub snapshot before this update is
`8b1154259f9a9f98ce8b725ca88a29d0da9be96c`, with
[passing CI](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37736216993).
Historical hub source and publication identities remain in the evidence index.
