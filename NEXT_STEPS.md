# Next steps

Two of twelve engineering cores are complete: Linux operations toolkit and Linux
fleet automation, each with a verified v0.1.0 release. The supporting hub makes
three public repositories. Ten engineering projects remain. **The network/storage
lab is the only active engineering project**, with local implementation under
validation. Its overall state is implemented-unverified; its 120 fixture tests,
required lint and safe demo passed on uncommitted source. Projects 4–12 remain
roadmap entries.

## Current bounded task

1. Read the network/storage repository's `AGENTS.md` and `docs/validation.md`;
   inspect Git status and its owned provider state before any new VM operation.
   Continue the existing implementation rather than regenerating it. Network
   development validation is active and no current cleanup outcome is credited
   here; do not create a second VM or remove unrelated resources.
2. Resolve actual network-profile VM failures and rerun affected checks. Exercise
   all profiles against the revised 41-package snapshot lock after authenticated
   reboot into `6.8.0-146-generic`. An earlier development storage pass at a different
   fingerprint does not satisfy this required gate.
3. Review source, tests, documentation and outgoing secrets; create a meaningful
   source commit using the existing Git identity. From clean source, record the
   complete all-profile VM lifecycle, controller gates and standalone clean-clone
   quickstart. Preserve failed reports; require all core assertions and cleanup.
4. Review exact outgoing files/history, license, dependency records and claims.
   Run `make gate`, check the authorized target for collision, then use the
   credential-free publishing script to create the new public repository only
   after gates pass. Verify owner/visibility/branch/SHA and exact-target GitHub CI.
   Release only after the documented release gates pass.
5. Update every hub ledger with verified revision/evidence/publication state, then
   activate project 4. Create no empty future remote repositories.

No unresolved fleet core or publishing blocker remains. Preserve its completed
source and original evidence identities. No host configuration changes, cloud
resources, billable services or container publishing are authorized.

## Completed demonstrations

Run the toolkit's fixture and portable read-only demo:

```sh
cd /Users/hbsu/ops-linux-operations-toolkit
make validate
make demo
```

Its `make integration` requires Linux and reports unavailable on macOS. Run the
fleet controller policy demonstration without allocating a VM:

```sh
cd /Users/hbsu/ops-linux-fleet-automation
make doctor
make validate
make demo
```

The fleet demo executes real Ansible assertions with no guest provisioning or host
configuration changes. To repeat its real VM profiles, follow the
[released README](https://github.com/Yash-PK/ops-linux-fleet-automation/blob/v0.1.0/README.md):
review, scan and commit each generated evidence report between clean-source
integration runs. Development mode writes ignored diagnostics and does not satisfy
the release-evidence gate. The hub's `make demo` prints saved status and does not
execute sibling projects.

The active network/storage controller demo allocates no VM:

```sh
cd /Users/hbsu/ops-network-storage-services-lab
make doctor
make validate
make demo
```

Read its local README before a real integration run.
`make integration LAB=ops-network-storage-reference` requires clean committed source, creates one
owned VM and attempts scoped teardown. Do not run it while the active development
VM is registered. Development reports are ignored and cannot satisfy publication
or release gates. No network/storage GitHub URL has been verified.

Both recorded fleet guests were deleted and its provider registry is empty.
Approximately 1.05 GiB of image caches remains, alongside tools and ignored
metadata/credentials. Inspect owned state before any later teardown; do not remove private
ownership records or unrelated resources as a cleanup shortcut.

## Evidence and continuation

| Scope | Recorded revision |
| --- | --- |
| Toolkit original local/clean-clone source | `55f15eaacf3842fa15f44751d5f21a5094bd089c` |
| Toolkit released and CI-tested target | `0d164e9158eeb9540e895d5f48bcf4723f36667b` |
| Hub original local/clean-clone source | `850a33de075cd5f43c4a1a30f4efa3830fea944d` |
| Hub saved first-milestone publication/CI snapshot | `f1de5b4ee59176cb0eaf9e9a4e61af308ebf516e` |
| Hub latest verified publication/CI snapshot | `cd9a6741e3d6d54e3cd39fff18d1f40359bf5313` |
| Fleet controller/clean-clone/Ubuntu source | `c52155a5c15b04bdb2a85746b385da0243ecef93` |
| Fleet AlmaLinux source | `e333e1c8c37b107fb6e99924c869555acca0ad68` |
| Fleet released and CI-tested target | `1531b86b54eee87d01da83f7b55d7d405f43fadb` |

Both fleet VM reports share implementation fingerprint
`391a99a45747322a4358e199d1454d2b29f175e171592995cae890761137bb0d`.
The earlier failed `8db4d22e1c56` Ubuntu report remains archived. Later evidence,
documentation and release commits never replace original tested revisions.

Network/storage source is uncommitted in this snapshot. The earlier storage-only
development observation used implementation fingerprint
`cb7df988b7260c318f24f38db86a2e334f9b8f0ad773017abf977cb0a3a9b1a6`, with
438 commands, 63 assertions and VM cleanup passing. Current dependency/reboot
changes need fresh formal evidence; no completed project count is added for it.

Read AGENTS.md, PROJECT_STATUS.md, this file and the active project's instructions
on resumption. Reconcile actual files, Git status, remotes, evidence and owned
provider state before continuing the first incomplete task. Use the existing Git
identity. Nothing is scheduled to continue after the active session ends.
