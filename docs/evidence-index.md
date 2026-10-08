# Evidence index

The toolkit, fleet, network/storage and container-platform cores completed their local/integration gates
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
| N-local: network/storage controller | `a9950a19f7fe578c9e27b4cf59e0a1ebafdbd8ac` | macOS ARM64, Python 3.14.7 | 122 tests, required lint, doctor/demo and full secret scans passed | [Controller report](https://github.com/Yash-PK/ops-network-storage-services-lab/blob/53b78f81ed58602efd2c151d449338615ab61e9d/evidence/a9950a19f7fe-controller.json) |
| N-storage-dev: earlier complete storage development profile | `uncommitted`; SHA-256 `cb7df988b7260c318f24f38db86a2e334f9b8f0ad773017abf977cb0a3a9b1a6` | Real Ubuntu ARM64 Lima VZ guest; 2026-10-08 05:10:20–05:11:45 UTC | 438 commands, 63 assertions, all storage profiles and cleanup passed; subsequent package/kernel changes required fresh integration | Local ignored `.runtime/reports/uncommitted-storage-vm-20261008T051145.json`; development-only, not public release evidence |
| N-VM: network/storage complete integration and standalone clone | `e43bcdfdae1a604a095eea085e81eb8fbe2e6d00` | macOS ARM64 VZ; Ubuntu 24.04 ARM64, kernel `6.8.0-146-generic`; Python 3.14.7 controller | 605 commands, 110 assertions and cleanup passed; fresh clone gates passed and scratch removed | [VM report](https://github.com/Yash-PK/ops-network-storage-services-lab/blob/53b78f81ed58602efd2c151d449338615ab61e9d/evidence/e43bcdfdae1a-all-vm.json), [clone report](https://github.com/Yash-PK/ops-network-storage-services-lab/blob/53b78f81ed58602efd2c151d449338615ab61e9d/evidence/e43bcdfdae1a-clean-clone.json) |
| N-CI and release v0.1.0 | CI artifact: `0f6f5faebc0c3d2e381a66fcaaa656e3e75ccaaa`; release: `53b78f81ed58602efd2c151d449338615ab61e9d` | Hosted Linux x86-64 controller; verified public main/tag | Original and release-target CI passed; release published 2026-10-08T06:03:14Z | [Preserved Linux report](https://github.com/Yash-PK/ops-network-storage-services-lab/blob/53b78f81ed58602efd2c151d449338615ab61e9d/evidence/0f6f5faebc0c-ci-linux.json), [release-target CI](https://github.com/Yash-PK/ops-network-storage-services-lab/actions/runs/37735444827), [release](https://github.com/Yash-PK/ops-network-storage-services-lab/releases/tag/v0.1.0) |
| Container platform earlier controller | `7766299b2d24ce26fe6e51edf8b6660d3eb3e60b` | macOS ARM64, Python 3.14.7; 2026-10-08 06:41:06–06:41:09 UTC | Doctor, lint/docs/config, 45 unit/controller/safety tests, safe demo and working/staged/full one-commit-history Gitleaks passed; source clean and unchanged | Local project `evidence/7766299b2d24-controller.json`; no remote yet |
| C-dev: first container-platform VM attempt | `uncommitted`; fingerprint `25aa04a2aa8bf80be1979195f9b7f3303d09683826edb2a07e47c2dfe24ddb64` | Real Ubuntu ARM64 VZ; 2026-10-08 06:36:13–06:40:00 UTC | Package preparation/cold boot passed; runtime-directory `0700` guard failed before credentials/containers; failure preserved; VM deletion passed | Ignored local `.runtime/evidence/20261008T063613637487-development.json`; not release proof |
| C-dev: development attempts two through four | Source/fingerprint recorded in each ignored report; fourth source `af50b84d648bc04cf63c6f103569bc2df033f4bc` | Real Ubuntu ARM64 VZ and, in runs three/four, Docker/Compose | All failed overall: engine startup; loopback HTTP refusal; process inspection. Fourth passed workload/recovery and 21 SQL assertions. All VM deletion passed | Local `.runtime/evidence/20261008T064105368194-development.json`, `20261008T064506703400-development.json`, `20261008T065059048620-development.json` |
| Container platform earlier controller and clean clone | `950e511f42173c00994496265bb48104623e1bea` | macOS ARM64 Python 3.14.7; 2026-10-08 07:04:57–07:05:13 UTC | 57 tests, lint/docs/config, doctor/demo and full secret scans passed; standalone clone bootstrap/checks passed and scratch removed | Local `evidence/950e511f4217-controller.json`, `evidence/950e511f4217-clean-clone.json` |
| C-formal-failed: first formal container VM attempt | `950e511f42173c00994496265bb48104623e1bea` | macOS ARM64 VZ; 2026-10-08 07:04:57–07:05:13 UTC | Failed at oversized multiplexed SSH request before guest phases, identified from retained private transport log; VM deletion passed | Local `evidence/950e511f4217-compose-vm.json`; preserved failure, not release proof |
| C-local: current formal controller and clone | `3d58b9f7107fa1c7de3eec06b32c9b6f6ce644d6` | macOS ARM64 Python 3.14.7; 2026-10-08 07:14:49–07:15:04 UTC | 71 tests and all controller/clone command groups passed; source clean/unchanged; scratch removed | [Controller report](https://github.com/Yash-PK/ops-containerized-service-platform/blob/cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe/evidence/3d58b9f7107f-controller.json), [clean-clone report](https://github.com/Yash-PK/ops-containerized-service-platform/blob/cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe/evidence/3d58b9f7107f-clean-clone.json) |
| C-VM: complete container platform lifecycle | `3d58b9f7107fa1c7de3eec06b32c9b6f6ce644d6` | Ubuntu ARM64 VZ, kernel `6.8.0-146-generic`; 2026-10-08 07:14:49–07:20:20 UTC | 22 preparation commands/assertions, 117 Compose commands, 72 Compose assertions and 21 nested SQL assertions passed; Compose resources and VM removed, inventory empty | [Formal VM report](https://github.com/Yash-PK/ops-containerized-service-platform/blob/cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe/evidence/3d58b9f7107f-compose-vm.json); retained at the released target |
| C-CI and initial publication | `19ec88d5d4a6aa7541e7722b994618c3a6929cc5` | Hosted CI; verified public `Yash-PK` repository, branch `main` | Exact-head `validate` passed in 18 seconds; Linux controller report preserved | [CI run](https://github.com/Yash-PK/ops-containerized-service-platform/actions/runs/37743386301); [Linux report](https://github.com/Yash-PK/ops-containerized-service-platform/blob/cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe/evidence/19ec88d5d4a6-ci-linux.json) |
| Container release v0.1.0 | `cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe` | Verified public `main` and tag; hosted CI | Exact-target CI passed; release verified | [CI run](https://github.com/Yash-PK/ops-containerized-service-platform/actions/runs/37743579858); [release](https://github.com/Yash-PK/ops-containerized-service-platform/releases/tag/v0.1.0) |
| Cloud foundation IaC | None | Active dependency review/static-core definition | planned; no executed implementation checks yet | None |
| Projects 6–12 | None | Roadmap | planned | None |

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
network/storage formal proof is independent of the fleet proof; neither extends
the other project's claimed platforms.

## Network/storage development boundary

The local repository is `ops-network-storage-services-lab`. It implements a
standalone controller using the hash-pinned released fleet provider, a real
Ubuntu ARM64 Lima VZ guest, private namespace clients and inventoried loop-backed
image files. The current released repository and formal evidence are linked above. The observations
below preserve the earlier development history; they do not substitute for that proof.

The earlier successful storage development run recorded fingerprint
`cb7df988b7260c318f24f38db86a2e334f9b8f0ad773017abf977cb0a3a9b1a6`,
`development=true`, `revision=uncommitted` and `selected_profile=storage`.
It ran from `2026-10-08T05:10:20.552148+00:00` to
`2026-10-08T05:11:45.176783+00:00`, with 438 commands and 63 assertions passing.
Observed behavior included GPT/ext4/XFS persistence, quota EDQUOT/recovery,
LVM/filesystem growth, RAID1 degradation/rebuild, LUKS wrong-key rejection and
reopen, profile cleanup and VM deletion. Earlier failed attempts were preserved.
The report remains ignored local development evidence; it is not an artifact from
a tested Git commit or a published release.

Subsequent review tightened library/kernel dependencies to 41 snapshot package
pins and separated preparation from authenticated reboot/profile execution.
Current code requires running kernel `6.8.0-146-generic`. A later formal all-profile
run at `e43bcdfdae1a604a095eea085e81eb8fbe2e6d00` passed this requirement and all
core assertions. Its fingerprint is
`0ddbae1dd5d52f9c6100f22910535571e189e49c29411f950731b4852bfea593`.

Development also found an oversized payload, partition-input error, Samba runtime
directory dependency and overly restrictive loopback firewall rule. Each failed
attempt remains described in the released validation report. The complete formal
run, not any earlier partial/development observation, qualifies the released core.
Its guest resources, VM and temporary clone were removed; local private caches and
diagnostics remain ignored. Cloud deployment and image publication remain disabled.

## Evidence handling

The previous container controller/clone reports retain source
`950e511f42173c00994496265bb48104623e1bea`. The controller report records fingerprint
`1058c9278fe1942b5becedbde4a5ffd312a846f18959af587ebe2e3615f3ad22`.
Controller checks and the standalone clone passed. The first formal VM attempt
failed during SSH payload delivery before guest phases; its successful VM cleanup
does not convert that result into a pass. Private diagnostics recorded
`mm_send_fd: sendmsg(2): Message too long` for a 54,532-byte encoded upload plus
installer. Source `3d58b9f7107f` now sends at most 8,000 bytes per checked chunk
and bounds the shell-quoted command to 16,000 bytes. It verifies guest staging
ownership, part sequence, and part/whole checksums. Current formal controller and
clone reports passed, with controller fingerprint
`2d02d563e250b498d07b3695894a21d825bc7310c6ed47bd2afc3ee55b1a2f2b`. Actual
chunked upload, the complete formal lifecycle and Compose/VM cleanup all passed.
The report records 139 commands, 94 preparation/lifecycle assertions and 21 nested
SQL assertions. Preserve each report's original revision.

The four development failures remain documented separately. Their fixes addressed
explicit private-parent creation, daemon startup/diagnostics, guest-loopback
publishing and an HTTP proxy readiness probe, then strict process UID/PID parsing.
The fourth run passed real job/recovery behavior and 21 SQL checks before process
inspection failed. Realized port mappings were added to the current assertions.
Those partial results stay failed overall; the later complete C-VM report is the
local acceptance proof. Publication, v0.1.0 and exact-target hosted CI are verified at
`cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe`. The copied Linux controller report
retains its `19ec88d5d4a6` source and records Python 3.14.7/Linux x86-64, 71 tests
and all doctor/validate/demo/security command groups passing. It explicitly does
not run the macOS VZ integration. All five
earlier owned VMs and the current formal VM were deleted; the provider inventory
is empty. The public report links preserve the tested `3d58b9f7107f` source identity.
The published evidence/docs commit is a separate revision.

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

A later hub-only snapshot was verified at
`cd9a6741e3d6d54e3cd39fff18d1f40359bf5313`, with
[passing exact-target CI](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37731050426).
It records index maintenance, not a replacement for original local/clone reports
or a replacement for the later formal network/storage integration proof.

Hub progress snapshot `e6bd08197a96f5f7ee4dc9b35b72ef1007792f0d` passed
[exact-target CI](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37734298497).
Its clean-clone source is `08a5cadecf05de18802e8c68643c4bdc78e8a6d2`, recorded in
[the preserved report](../evidence/08a5cadecf05-clean-clone.json).

The latest completed-core hub snapshot is
`8b1154259f9a9f98ce8b725ca88a29d0da9be96c`, with
[passing exact-target CI](https://github.com/Yash-PK/ops-linux-devops-portfolio/actions/runs/37736216993).
Its fresh clean-clone source is `f4e91897c4c18c0e9467f8c446012cf3bc18c21a`,
preserved in [the report](../evidence/f4e91897c4c1-clean-clone.json).
This validates the hub ledger, not the new container-platform implementation.
