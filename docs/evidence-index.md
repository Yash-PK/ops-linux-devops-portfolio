# Evidence index

The toolkit and fleet cores have completed their required local/integration gates
and published v0.1.0 releases. Hub local gates are recorded against its first tested source
revision, and its clean-clone gate passed with scratch cleanup confirmed. Hub
publication and hosted CI are now verified at the recorded snapshot below.

| Scope | Tested source revision | Environment | Check/result | Record |
| --- | --- | --- | --- | --- |
| Hub local gates | `850a33de075cd5f43c4a1a30f4efa3830fea944d` | macOS ARM64, Python 3.14.7 | Doctor, validation including 11 tests, demo and security all exit 0 | [Actual local report](../evidence/850a33de075c-local.json) |
| Hub clean clone | `850a33de075cd5f43c4a1a30f4efa3830fea944d` | Temporary clone on macOS ARM64 | Locked bootstrap, doctor, validation, demo and security passed; scratch removed | [Actual clean-clone report](../evidence/850a33de075c-clean-clone.json) |
| Hub fleet-index update clean clone | `9c5aeb69bce0db5660fe62391049ffd5c1f8af0a` | Temporary macOS ARM64 clone | Locked bootstrap, doctor, validation, demo and security passed; scratch removed | [Actual report](../evidence/9c5aeb69bce0-clean-clone.json) |
| Hub initial restricted-network attempt | `9c5aeb69bce0db5660fe62391049ffd5c1f8af0a` | Command sandbox without package-network access | Bootstrap failed on PyPI DNS; subsequent targets not run; scratch removed; the separate permitted-network retry above passed | [Preserved failed attempt](../evidence/9c5aeb69bce0-clean-clone-network-blocked.json) |
| Hub hosted validation | `f1de5b4ee59176cb0eaf9e9a4e61af308ebf516e` | Ubuntu x86-64, Python 3.14.7 | 11 tests plus lint, ledger demo and complete history scanning; all command groups exit 0 | [CI run](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37573748935); [preserved report](../evidence/f1de5b4ee591-local.json) |
| T-local: toolkit fixtures/static checks and portable demo | `55f15eaacf3842fa15f44751d5f21a5094bd089c` | macOS 26.6.2 ARM64, Python 3.14.7, Bash 3.2 | 58 tests, lint, repository checks, fixture/portable demo and required secret scans passed | Toolkit `evidence/55f15eaacf38-local.json` |
| T-local: toolkit clean clone | `55f15eaacf3842fa15f44751d5f21a5094bd089c` | Temporary clone on macOS ARM64 | Locked bootstrap, doctor, validation, demo and security passed; scratch clone removed | Toolkit `evidence/55f15eaacf38-clean-clone.json` |
| T-Linux: toolkit core and observed systemd/ACL inspection | `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` | Hosted Ubuntu x86-64, kernel `6.17.0-1022-azure`, Python 3.14.7 | Linux integration assertions passed, including live optional systemd/journal/schedules and ACL checks | [Passing CI run and artifact](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607); report `evidence/0b0f077933bb-linux.json` |
| Toolkit release v0.1.0 | `0d164e9158eeb9540e895d5f48bcf4723f36667b` | Hosted CI | Exact-target CI passed; release verified non-draft and non-prerelease | [CI run](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37573353795); [published release](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0) |
| Toolkit full OS boot/reboot and privileged diagnostics | None | Appropriate disposable VM exercise required | Unverified; not established by the read-only CI integration | None |
| F-local: fleet controller | `c52155a5c15b04bdb2a85746b385da0243ecef93` | macOS ARM64; Python 3.14.7 | 74 tests, doctor, production-profile Ansible lint, other required lint, input demo and Gitleaks passed | [Controller report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/c52155a5c15b-local.json) |
| F-local: fleet clean clone | `c52155a5c15b04bdb2a85746b385da0243ecef93` | Temporary macOS ARM64 clone | Locked bootstrap, doctor, validation, demo and security passed; scratch removed | [Clean-clone report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/c52155a5c15b-clean-clone.json) |
| F-Ubuntu: complete fleet Ubuntu profile | `c52155a5c15b04bdb2a85746b385da0243ecef93` | macOS ARM64 Lima VZ; Ubuntu 24.04 ARM64, kernel `6.8.0-146-generic`, guest Python 3.12.3 | Nine workflow steps, strict SSH rejection, Molecule/idempotence, rejection/change/restore and patch/reboot passed; package versions captured; scoped teardown passed | [Ubuntu report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/c52155a5c15b-ubuntu-vm.json) |
| Fleet earlier Ubuntu failure retained | `8db4d22e1c567943ed80e2e8fe6ceebdc56d0fb7` | Real Ubuntu ARM64 VM | Post-reboot firewall unit enabled but inactive; acceptance failed; cleanup passed; corrected boot ordering was retested at `c52155a5c15b` | [Archived failed report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/8db4d22e1c56-ubuntu-vm.json) |
| F-Alma: complete fleet AlmaLinux profile | `e333e1c8c37b107fb6e99924c869555acca0ad68` | macOS ARM64 Lima VZ; AlmaLinux 9.8 ARM64, kernel `5.14.0-687.54.1.el9_8.aarch64`, guest Python 3.9.25 | All nine workflow steps passed, including SELinux/firewalld checks, patch/reboot and scoped teardown | [Actual AlmaLinux report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/e333e1c8c37b-alma-vm.json) |
| Fleet publishing clean clone and hosted controller CI | `627e25c38de2ef44f43416e171102eaae3bc20ca` | Temporary macOS clone / hosted Ubuntu controller | Required checks passed; scratch removed; preserved Linux artifact | [Clean-clone report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/627e25c38de2-clean-clone.json); [Linux CI report](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/1531b86b54eee87d01da83f7b55d7d405f43fadb/evidence/627e25c38de2-ci-linux.json) |
| Fleet release v0.1.0 | `1531b86b54eee87d01da83f7b55d7d405f43fadb` | Verified public main and exact-target hosted CI | Non-draft, non-prerelease release published `2026-10-07T11:38:28Z`; CI passed | [CI run](https://github.com/Yash-PK/ops-linux-fleet-automation/actions/runs/37615270935); [release](https://github.com/Yash-PK/ops-linux-fleet-automation/releases/tag/v0.1.0) |
| Network/storage lab | None credited | Active prerequisite/acceptance review | Capabilities planned; no integration or publication credited | None |
| Projects 4–12 | None | Roadmap | planned | None |

The actual Linux report was produced by the CI run linked above. Its artifact is
the source of the local evidence copy; a subsequent evidence/documentation commit
must preserve its recorded `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` tested revision.
The verified toolkit remote is
[ops-linux-operations-toolkit](https://github.com/Yash-PK/ops-linux-operations-toolkit),
owner `Yash-PK`, visibility `PUBLIC`, branch `main`. Release v0.1.0 targets
`0d164e9158eeb9540e895d5f48bcf4723f36667b` and has its own passing CI run. It does
not replace the `55f15eaacf3842fa15f44751d5f21a5094bd089c` local or
`0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` original Linux evidence revisions.
Similarly, later hub documentation/ledger commits do not replace the hub source
`850a33de075cd5f43c4a1a30f4efa3830fea944d` recorded in its actual local report.

## What the Linux run established

- Seven live health sources were available: CPU, load, memory, filesystem capacity,
  inodes, processes and `ss` socket counts. Assertions checked bounded CPU/memory
  metrics, positive CPU/process counts and consistent process state totals.
- Live explicit-path metadata, numeric identity, installed package count and
  diagnostic availability were collected. Path and identity UID assertions and a
  positive package-count assertion passed.
- A real temporary backup marker passed freshness, became degraded after its mtime
  was moved back 48 hours, and recovered after refreshing mtime. The integration
  asserted expected health exit codes; it did not back up or restore application data.
- An actual temporary self-signed certificate exercised two expiry thresholds.
  Its ephemeral private key was never logged and was removed with the temporary
  directory. Trust chains and hostname validation were outside this check.
- Read-only observation of a loaded `dbus.service`, journald priority metadata,
  cron/logrotate directory entry counts, systemd timers and ACL metadata succeeded.
  No service mutation, scheduler execution, log rotation, boot/reboot, privileged
  diagnostics or security-policy validation was performed.

Tool discovery does not establish executed `tcpdump`, `strace`, `sar`, `iostat`,
`vmstat` or `lsof` troubleshooting. Linux execution on one hosted Ubuntu environment
does not prove other distributions, architecture variants, VM lifecycle behavior,
container isolation, cgroup-aware capacity policy or a cloud deployment.

## Fleet evidence boundary

The [fleet repository](https://github.com/Yash-PK/ops-linux-fleet-automation) is
verified public under `Yash-PK`, default branch `main`, at released revision
`1531b86b54eee87d01da83f7b55d7d405f43fadb`. Its v0.1.0 release and exact-target
hosted CI passed. Published source/report links above pin that release revision.
Original controller/clean-clone/Ubuntu execution source remains
`c52155a5c15b04bdb2a85746b385da0243ecef93`; AlmaLinux execution source is
`e333e1c8c37b107fb6e99924c869555acca0ad68`. That intervening commit preserved
observed evidence without changing implementation. Both VM reports record SHA-256
`391a99a45747322a4358e199d1454d2b29f175e171592995cae890761137bb0d`.
Later evidence, documentation and release commits do not replace these identities.

Both VM reports record strict SSH changed-key rejection (expected exit 255),
Molecule converge/zero-change idempotence/verify, invalid configuration rejection
with zero changes (expected exit 2), unchanged-service verification, content
change/verification/restoration/verification, and explicit patch/reboot. Shared
guest-state assertions ran immediately after reboot, before repair. Guest OS,
architecture, kernel, Python and relevant package versions were recorded.
All nine steps passed for each profile, and both owned guests were removed.
Ubuntu retained AppArmor; AlmaLinux retained enforcing SELinux and firewalld.

The earlier `8db4d22e1c56` report remains failed because its post-reboot firewall
unit was enabled but inactive. Corrected boot ordering passed a fresh Ubuntu run;
the original failure was not overwritten. Its precise earlier ordering conflict
was inferred rather than captured as a complete boot transaction trace.

The final fleet working tree was clean and its provider registry empty at release
verification. Approximately 1.05 GiB of image caches, local tools and ignored
private metadata/credentials were retained. Hosted Linux controller validation
is distinct from macOS VZ integration. Neither proves additional distros/providers,
external network denial, multi-host availability or cloud deployment. The active
network/storage prerequisite review has no implementation evidence credited yet.

## Evidence handling

Committed records identify source revision, timestamps, environment, tool
versions, commands, exit codes, assertions and reviewed/redacted output. Synthetic
fixture input remains explicitly separate from live observations. Gitleaks found
no findings in the required working/staged/history scans; this is not a guarantee
that every kind of secret can be detected. Toolkit temporary integration data and
clone storage were cleaned; local ignored developer caches remain. The hub
clean-clone scratch checkout was also removed after its successful gate.

Use [project status](../PROJECT_STATUS.md) for publication/CI/release state and
[the matrix](../SKILLS_MATRIX.md) for capability status. Failed, skipped, pending,
unavailable and passed are distinct outcomes. A passing local check does not
establish hosted CI, and a passing toolkit CI run does not establish a hub run.

The [public hub](https://github.com/Yash-PK/ops-linux-devops-portfolio) was verified
as PUBLIC under Yash-PK with default branch main at
`f1de5b4ee59176cb0eaf9e9a4e61af308ebf516e`. Its copied artifact retains the recorder's
`local` profile name (hub validation), while its environment correctly identifies
Linux. It is not Linux toolkit integration evidence. The separate
[publication receipt](../evidence/publication-2026-10-07.json) records the verified
remote/security/release snapshot. Later index-only commits do not change these
original evidence identities.
