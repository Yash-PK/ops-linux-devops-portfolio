PYTHON ?= $(if $(wildcard .venv/bin/python),$(CURDIR)/.venv/bin/python,python3)
SHELL := /bin/bash
.PHONY: help doctor bootstrap lint test validate demo integration security clean gate publish clean-clone
help:
	@printf '%s\n' 'bootstrap  Install locked developer tools locally (network required)' 'doctor     Inspect required tool versions' 'lint       Ruff, ShellCheck, shfmt, actionlint and repository checks' 'test       Deterministic standard-library tests' 'validate   Required lint and test gates' 'demo       Print the validated portfolio ledger; no project execution' 'integration Not applicable to this index (exits 3)' 'security   Gitleaks working files, staged blobs and all history' 'gate       Required local publishing gates' 'publish    Print credential-free publishing instructions (no writes)' 'clean-clone Validate an isolated checkout (network required)' 'clean      Remove only repository-owned .runtime data'
bootstrap:
	$(PYTHON) scripts/bootstrap.py
doctor:
	$(PYTHON) scripts/doctor.py
lint:
	.venv/bin/ruff check .
	.venv/bin/ruff format --check .
	.tools/bin/shellcheck scripts/demo.sh
	.tools/bin/shfmt -d -i 2 scripts/demo.sh
	PATH="$(CURDIR)/.tools/bin:$$PATH" .tools/bin/actionlint
	$(PYTHON) scripts/quality.py
	$(PYTHON) scripts/hub.py validate
test:
	$(PYTHON) -m unittest discover -s tests -v
validate: lint test
demo:
	bash scripts/demo.sh
integration:
	@printf '%s\n' 'Not applicable: hub is a documentation/ledger repository; Linux integrations belong to the toolkit.'
	@exit 3
security:
	$(PYTHON) scripts/security.py
clean-clone:
	$(PYTHON) scripts/clean_clone.py
gate: doctor validate demo security clean-clone
publish:
	$(PYTHON) scripts/publish.py --owner Yash-PK
clean:
	$(PYTHON) scripts/clean.py
