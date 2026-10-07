# Hub validation

Hub code validates the machine-readable portfolio ledger's status vocabulary,
repository identity, explicit publication verification, exact CI revision, active
project limit and disabled cloud/cost flags. Eleven tests include invalid-state,
multiple-active-project and falsely verified remote rejection. These are ledger
checks; they do not execute future engineering projects.

Required gates are `make doctor`, `make validate`, `make demo`, `make security`
and `make clean-clone`. The clean-clone gate creates only its inventoried temporary
directory, independently downloads locked developer tools, runs documented gates,
records failures and timeouts, and verifies cleanup. No sibling checkout is used.

The evidence recorder requires committed clean source and preserves its exact
SHA. Reports are committed afterward; that later commit is not relabelled as the
original test revision. See the evidence index for recorded results as they become
available. CI validates the index on standard hosted Ubuntu with read-only
permissions, pinned actions and no secrets or publishing job.

Security scans cover working files, staged blobs and full outgoing Git history.
A scan with no findings means configured patterns did not match; it is not a comprehensive audit.
No cloud, paid service, local VM/container or host configuration is created.

## Recorded local gates

Tested clean source: `850a33de075cd5f43c4a1a30f4efa3830fea944d` on macOS ARM64,
Python 3.14.7. [Local report](../evidence/850a33de075c-local.json) records doctor,
validate (11 tests plus lint/repository/ledger checks), demo and security, all
exit 0. [Independent clone report](../evidence/850a33de075c-clean-clone.json)
records a fresh locked bootstrap and every documented gate, all exit 0; the clone
remained clean and the scratch directory was removed. Network bootstrap took
305.267 seconds in that observed run; this is one recorded duration, not a benchmark.

These reports are committed after the tested source. Later ledger and documentation
updates keep that provenance intact. Publication/CI state is maintained separately
in PROJECT_STATUS.md and the machine-readable ledger.
