# Next steps

The Linux operations toolkit core is complete and published; local source
`55f15eaacf3842fa15f44751d5f21a5094bd089c` passed the required local and clean-clone
gates, and published source `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` passed
[Linux CI](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607).
There are zero active engineering projects. The hub remains the active supporting
index while first-milestone publication work finishes.

## Finish the first milestone

1. Retain the actual Linux CI evidence in the toolkit and finalize its validation,
   scope and release documentation. Preserve the tested source revisions in later
   evidence/documentation commits. Create a release only after its documented
   gates pass; none has been created at the time of this status update.
2. Run the hub's updated required checks, commit reviewed source, and run its
   clean-clone validation and revision-linked recorder. Its existing 11 tests,
   lint and ledger demo passed, but this does not replace those remaining gates.
3. Review exact outgoing hub files, license/claims, staged contents and all outgoing
   history. Publish the new authorized public hub only after its gates pass;
   verify owner, visibility, branch, remote SHA and Actions for that exact SHA.
4. Update `portfolio.json`, `PROJECT_STATUS.md`, the evidence index and this file
   with actual final hub publication/CI state and toolkit release state. Keep
   pending or blocked operations explicit and retain a credential-free recovery
   command if publication fails. Do not start another project during this session.

## Demo commands

From the toolkit checkout:

```sh
make bootstrap
make validate
make demo
```

`make integration` requires the documented Linux environment and tools. It is not
a passing Linux test on macOS. The demo intentionally asserts degraded/unavailable
fixture outcomes while returning success when those expected outcomes are met.
From this hub checkout, `make demo` prints the validated saved portfolio ledger.

## Next bounded task after this milestone

Review fleet-automation VM prerequisites: permitted CPU, RAM, disk, architecture
and virtualization/provider support, then maintained distro/Ansible/Molecule
versions from official documentation, release notes and advisories. Define its
bounded core acceptance and disposable VM boundary before creating roles or a new
repository. Real systemd/reboot/distro claims will need appropriate VM evidence;
container-only tests do not substitute for it. Do not alter the host or provision
cloud resources to satisfy prerequisites. See [dependencies](docs/dependency-map.md).

## Resume protocol

Read `AGENTS.md`, `PROJECT_STATUS.md`, this file, and the toolkit's `AGENTS.md` and
validation report. Inspect working-tree status, evidence and actual remotes before
editing. Reconcile saved claims with current files and CI. Complete the first
unfinished gate without regenerating completed source or fabricating activity.
This document does not schedule work after the active session ends.
