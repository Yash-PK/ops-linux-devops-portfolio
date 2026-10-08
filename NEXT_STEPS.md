# Next steps

Two of twelve engineering cores are complete: Linux operations toolkit and Linux
fleet automation, each with a verified v0.1.0 release. The supporting hub makes
three public repositories. Ten engineering projects remain. **The network/storage
lab is the only active engineering project**, at prerequisite/acceptance review;
its capability state remains planned. Projects 4–12 remain roadmap entries.

## Current bounded task

1. Reconcile the workspace and active-project instructions before creating files.
   Review the existing fleet provider's tested constraints and the host's current
   resources. Do not assume a completed fleet VM proves isolated DHCP, private
   multi-guest networking or safe attachable storage.
2. Select and verify one supported local provider/profile for project 3 using
   official documentation, supported versions and security advisories. Keep
   host networking/configuration unchanged. Any KVM/libvirt or alternative
   provider claim needs its own available environment and evidence.
3. Define bounded core acceptance before implementation: inventoried guests,
   isolated private network, lab-owned virtual disks, explicit teardown, an
   executable client/server service check, one network fault and one storage
   recovery. Document CPU, memory, disk, architecture and privilege requirements.
4. Implement and test one usable profile at a time. Require explicit lab identity,
   dry run and confirmation for destructive exercises; never discover or format
   arbitrary host devices. Keep future profiles planned until executable evidence
   exists. Create no empty remote repository.

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
| Fleet controller/clean-clone/Ubuntu source | `c52155a5c15b04bdb2a85746b385da0243ecef93` |
| Fleet AlmaLinux source | `e333e1c8c37b107fb6e99924c869555acca0ad68` |
| Fleet released and CI-tested target | `1531b86b54eee87d01da83f7b55d7d405f43fadb` |

Both fleet VM reports share implementation fingerprint
`391a99a45747322a4358e199d1454d2b29f175e171592995cae890761137bb0d`.
The earlier failed `8db4d22e1c56` Ubuntu report remains archived. Later evidence,
documentation and release commits never replace original tested revisions.

Read AGENTS.md, PROJECT_STATUS.md, this file and the active project's instructions
on resumption. Reconcile actual files, Git status, remotes, evidence and owned
provider state before continuing the first incomplete task. Use the existing Git
identity. Nothing is scheduled to continue after the active session ends.
