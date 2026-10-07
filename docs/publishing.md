# Hub publication and recovery

The hub is a work-in-progress index. It may be published after its structural,
test, security and clean-clone gates; this does not release planned projects.
The authorized destination is a new public repository under `Yash-PK`.

```bash
make bootstrap
make validate
make demo
make security
make clean-clone
python3 scripts/publish.py --owner Yash-PK
```

The publishing script defaults to a dry run. After reviewing and committing the
exact files, use `.venv/bin/python scripts/publish.py --owner Yash-PK --execute`.
It reruns checks, verifies identity, refuses existing remotes/collisions, creates
the new repository and verifies owner/visibility/default branch/commit. The
underlying manual command, from this repository after the same gates, is:

```bash
gh repo create Yash-PK/ops-linux-devops-portfolio --public --source . --remote origin --push
```

If authentication is unavailable, use `gh auth login --hostname github.com`
locally. Never paste credentials into issues or chat. Network, policy or collision
errors block that publishing operation; do not change visibility, rename around a
collision, force-push or overwrite an existing repository.

After publication, inspect Actions for the exact pushed SHA. Record pending,
failed and passed independently from local results. Repository security features
may be enabled only when available without billing. Proposed future branch rules:
require `validate` on PRs, block force pushes/deletion, and document an owner
recovery path. Rules have not been applied automatically.

No hub versioned release is needed for this index. Toolkit releases have their
own acceptance and Linux execution evidence; future projects stay plain roadmap
entries until their implementation exists.
