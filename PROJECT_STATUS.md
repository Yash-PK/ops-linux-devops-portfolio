# Project status

Capability, publication, CI and release state are independent. This portfolio is
lab/reference engineering work. The [evidence index](docs/evidence-index.md)
identifies the exact source revisions and execution environments.

| Project | Work state | Capability state | Publication | CI | Release |
| --- | --- | --- | --- | --- | --- |
| Portfolio hub | Active supporting index; first milestone gates in progress | statically-validated; local and clean-clone gates passed at `850a33de075c` | Pending final review and remote verification | Not run | Work in progress; no release |
| Linux operations toolkit | Bounded core complete; no longer active | integration-tested on Ubuntu x86-64 CI | Public repository; release target `0d164e9158ee` | Passed for `0d164e9158ee` | [v0.1.0 published](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0) |
| Linux fleet automation | Not started | planned | Not created | Not run | None |
| Network/storage services lab | Not started | planned | Not created | Not run | None |
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
Python 3.14.7 and Bash 3.2. RAM/disk and virtualization prerequisites still need a
permitted resource assessment before selecting a heavy VM profile. Docker tooling
is installed; Colima was stopped at assessment and no local runtime was created.
The Linux evidence comes from the hosted CI runner, not this macOS host.

Gitleaks found no findings in the required outgoing working/staged/history scans.
Pattern scanning does not guarantee absence of every secret. Toolkit repository
secret scanning, push protection and private vulnerability reporting were verified
enabled without adding a paid service. No account-wide settings were changed.

Toolkit temporary clones and integration files, including the ephemeral certificate
key, were cleaned. The hub clean-clone gate passed and removed its scratch checkout. Ignored local developer caches (`.venv`, `.tools`) remain for repeat
runs. No local containers/VMs, host configuration, services or cloud resources were
created. Cloud creation, paid services and container package publication remain
**disabled**. Existing Git identity was used.

## Remaining first-milestone work

Toolkit release v0.1.0 is published. Complete the hub's final outgoing review/scans,
new-repository publication and exact-SHA CI verification.
Hub source `850a33de075cd5f43c4a1a30f4efa3830fea944d` passed `make doctor`,
`make validate` (including 11 tests), `make demo` and `make security`; the actual
[local report](evidence/850a33de075c-local.json) records all four exit codes as 0.
The [clean-clone report](evidence/850a33de075c-clean-clone.json) for the same source
records successful locked bootstrap, doctor, validation, demo and security, with
scratch cleanup confirmed. Later documentation/ledger commits are not that
original tested revision. Hub publication remains pending, with no hub remote URL
or hosted CI result asserted yet. The other eleven projects have no implementation
directories or remote repositories. No engineering project is active.

See [next steps](NEXT_STEPS.md) for the exact continuation boundary.
