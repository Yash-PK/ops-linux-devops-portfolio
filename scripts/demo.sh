#!/usr/bin/env bash
# Show validated saved state only; this does not run any sibling project.
set -euo pipefail
repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$repo_root"
if [[ -n "${PYTHON:-}" ]]; then
  interpreter="$PYTHON"
elif [[ -x "$repo_root/.venv/bin/python" ]]; then
  interpreter="$repo_root/.venv/bin/python"
else
  interpreter=python3
fi
exec "$interpreter" "$repo_root/scripts/hub.py" demo
