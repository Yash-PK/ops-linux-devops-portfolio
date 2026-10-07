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
No scanner finding is an absence-of-pattern finding, not a comprehensive audit.
No cloud, paid service, local VM/container or host configuration is created.
