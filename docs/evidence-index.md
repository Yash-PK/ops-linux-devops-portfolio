# Evidence index

The toolkit has completed local and Linux integration evidence. The hub's local
structural checks passed, but its clean-clone run, initial tested commit and hosted
CI remain pending. No hub SHA or remote link is asserted here.

| Scope | Tested source revision | Environment | Check/result | Record |
| --- | --- | --- | --- | --- |
| Hub ledger and structure | Not yet committed | macOS ARM64 | 11 tests, lint and ledger demo passed; final gate pending | Revision-linked hub evidence pending |
| T-local: toolkit fixtures/static checks and portable demo | `55f15eaacf3842fa15f44751d5f21a5094bd089c` | macOS 26.6.2 ARM64, Python 3.14.7, Bash 3.2 | 58 tests, lint, repository checks, fixture/portable demo and required secret scans passed | Toolkit `evidence/55f15eaacf38-local.json` |
| T-local: toolkit clean clone | `55f15eaacf3842fa15f44751d5f21a5094bd089c` | Temporary clone on macOS ARM64 | Locked bootstrap, doctor, validation, demo and security passed; scratch clone removed | Toolkit `evidence/55f15eaacf38-clean-clone.json` |
| T-Linux: toolkit core and observed systemd/ACL inspection | `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` | Hosted Ubuntu x86-64, kernel `6.17.0-1022-azure`, Python 3.14.7 | Linux integration assertions passed, including live optional systemd/journal/schedules and ACL checks | [Passing CI run and artifact](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607); report `evidence/0b0f077933bb-linux.json` |
| Toolkit full OS boot/reboot and privileged diagnostics | None | Appropriate disposable VM exercise required | Unverified; not established by the read-only CI integration | None |
| Other eleven engineering projects | None | Not started | planned | None |

The actual Linux report was produced by the CI run linked above. Its artifact is
the source of the local evidence copy; a subsequent evidence/documentation commit
must preserve its recorded `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` tested revision.
The verified toolkit remote is
[ops-linux-operations-toolkit](https://github.com/Yash-PK/ops-linux-operations-toolkit),
owner `Yash-PK`, visibility `PUBLIC`, branch `main`, verified remote SHA
`0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` at this update. A later commit is not
silently substituted for either tested source revision.

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

## Evidence handling

Committed records identify source revision, timestamps, environment, tool
versions, commands, exit codes, assertions and reviewed/redacted output. Synthetic
fixture input remains explicitly separate from live observations. Gitleaks found
no findings in the required working/staged/history scans; this is not a guarantee
that every kind of secret can be detected. Temporary integration data and clone
storage were cleaned; local ignored developer caches remain.

Use [project status](../PROJECT_STATUS.md) for publication/CI/release state and
[the matrix](../SKILLS_MATRIX.md) for capability status. Failed, skipped, pending,
unavailable and passed are distinct outcomes. A passing local check does not
establish hosted CI, and a passing toolkit CI run does not establish a hub run.
