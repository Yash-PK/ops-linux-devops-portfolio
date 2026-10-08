# Next steps

Four of twelve engineering cores are complete: operations toolkit, fleet automation,
network/storage and the containerized service platform, each with a verified
v0.1.0 release. The hub makes five public repositories. Eight engineering projects
remain. **Cloud foundation IaC is the only active project**; its capability is
planned while dependency review and core definition begin. Projects 6–12 remain
roadmap entries.

## Current bounded task

1. Review official OpenTofu and AWS-provider support information, release notes,
   security advisories and testing documentation. Choose compatible maintained
   versions, verify downloads and record exact source references before adding
   dependencies. Use OpenTofu as the primary engine; do not claim Terraform
   compatibility without separate execution.
2. Define the project-5 acceptance checklist and create its standalone local
   repository without touching completed projects. Bound the AWS foundation to
   networking/subnets/routes, security groups, IAM, encryption, tags, state design
   and minimal compute configuration. Keep cost-bearing profiles disabled.
3. Implement real modules and negative policy/module fixtures. Run formatting,
   validation, applicable lint/policy checks and mock tests without credentials or
   authenticated AWS operations. Distinguish each check from a real plan/apply;
   exclude real state, saved plans and credentials from Git. Do not create cloud
   resources, expose services or enable billable services.
4. Document standalone bootstrap/quickstart, state/bootstrap/locking design and
   gated deployment prerequisites. Run a clean-clone static/mock profile and
   capture revision-linked evidence before publication. Project 5 currently has
   no verified repository URL, implementation proof or CI result.

No unresolved required core, publication or release blocker remains for projects
1–4. P4's [v0.1.0 release](https://github.com/Yash-PK/ops-containerized-service-platform/releases/tag/v0.1.0) and [exact-target CI](https://github.com/Yash-PK/ops-containerized-service-platform/actions/runs/37743579858)
are verified at `cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe`. Its formal runtime source
`3d58b9f7107f`, Linux artifact source `19ec88d5d4a6`, and earlier failed reports
remain immutable. All owned P4 instances are deleted; approximately 977 MiB of
ignored caches/tools remain. Do not restart the existing host Docker/Colima
context, install global packages, publish images or provision cloud resources.
Rootless Podman remains a planned extension.

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

The completed network/storage controller demo allocates no VM:

```sh
cd /Users/hbsu/ops-network-storage-services-lab
make doctor
make validate
make demo
```

Read its local README before a real integration run.
`make integration LAB=ops-network-storage-reference` requires clean committed source, creates one
owned VM and attempts scoped teardown. Check its registry before starting.
[Published v0.1.0](https://github.com/Yash-PK/ops-network-storage-services-lab/releases/tag/v0.1.0)
passed all profiles; development reports remain separate from release proof.

Run the completed container platform's safe controller demonstration:

```sh
cd /Users/hbsu/ops-containerized-service-platform
make doctor
make validate
make demo
```

Its real `make integration LAB=ops-container-platform-reference` requires the
supported macOS ARM64 VZ environment, clean committed source and a new evidence
path. It creates one owned 2-CPU/2-GiB VM with a 24-GiB sparse disk, runs the actual
Compose lifecycle inside it and attempts scoped teardown. Existing formal reports
cannot be overwritten. Read the released README before rerunning. The safe demo
above creates no VM or container.

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
| Hub latest verified publication/CI snapshot | `8b1154259f9a9f98ce8b725ca88a29d0da9be96c` |
| Fleet controller/clean-clone/Ubuntu source | `c52155a5c15b04bdb2a85746b385da0243ecef93` |
| Fleet AlmaLinux source | `e333e1c8c37b107fb6e99924c869555acca0ad68` |
| Fleet released and CI-tested target | `1531b86b54eee87d01da83f7b55d7d405f43fadb` |
| Container formal controller/clone/VM source | `3d58b9f7107fa1c7de3eec06b32c9b6f6ce644d6` |
| Container preserved Linux controller artifact | `19ec88d5d4a6aa7541e7722b994618c3a6929cc5` |
| Container released and CI-tested target | `cdea68d2a446d2c3e9c62f56631f4cc8a01ed3fe` |

Both fleet VM reports share implementation fingerprint
`391a99a45747322a4358e199d1454d2b29f175e171592995cae890761137bb0d`.
The earlier failed `8db4d22e1c56` Ubuntu report remains archived. Later evidence,
documentation and release commits never replace original tested revisions.

Network/storage controller source is `a9950a19f7fe578c9e27b4cf59e0a1ebafdbd8ac`;
formal VM/clone source is `e43bcdfdae1a604a095eea085e81eb8fbe2e6d00`, fingerprint
`0ddbae1dd5d52f9c6100f22910535571e189e49c29411f950731b4852bfea593`.
Release and exact-target CI passed at `53b78f81ed58602efd2c151d449338615ab61e9d`.
All 605 VM commands/110 assertions and cleanup passed; 122 controller tests passed.
The temporary clone and owned VM were removed. About 793 MiB of ignored project
caches/tools/private metadata remains. Earlier development failures stay documented.

Read AGENTS.md, PROJECT_STATUS.md, this file and the active project's instructions
on resumption. Reconcile actual files, Git status, remotes, evidence and owned
provider state before continuing the first incomplete task. Use the existing Git
identity. Nothing is scheduled to continue after the active session ends.
