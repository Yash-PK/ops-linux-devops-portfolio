# Next steps

The Linux operations toolkit core is complete and published; local source
`55f15eaacf3842fa15f44751d5f21a5094bd089c` passed the required local and clean-clone
gates, and published source `0b0f077933bb06e2b9016f50ff5d8b1fbcebddf4` passed
[Linux CI](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37459272607).
[Release v0.1.0](https://github.com/Yash-PK/ops-linux-operations-toolkit/releases/tag/v0.1.0)
is now published as a non-draft, non-prerelease at
`0d164e9158eeb9540e895d5f48bcf4723f36667b`, with
[passing exact-revision CI](https://github.com/Yash-PK/ops-linux-operations-toolkit/actions/runs/37573353795).
The earlier local and Linux evidence revisions remain unchanged.
There are zero active engineering projects. The hub remains the active supporting
index while first-milestone publication work finishes.

## Finish the first milestone

1. Preserve the completed hub local and clean-clone evidence for source
   `850a33de075cd5f43c4a1a30f4efa3830fea944d`. Both reports record passing gates,
   and clean-clone scratch removal is confirmed. Later documentation/ledger
   updates are separate commits and need their applicable checks; do not relabel
   them as the original tested source.
2. Review exact outgoing hub files, license/claims, staged contents and all outgoing
   history. Publish the new authorized public hub only after its gates pass;
   verify owner, visibility, branch, remote SHA and Actions for that exact SHA.
3. Update `portfolio.json`, `PROJECT_STATUS.md`, the evidence index and this file
   with actual final hub publication/CI state. Keep pending or blocked operations
   explicit and retain a credential-free recovery command if publication fails.
   Toolkit release v0.1.0 is already verified published; do not recreate it.

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
