# Contributing

This repository is the portfolio hub. Implementation changes belong to the
corresponding standalone project repository; keep project directories outside
the hub's Git working tree. Read [continuation guidance](AGENTS.md),
[project status](PROJECT_STATUS.md), and [next steps](NEXT_STEPS.md) first.

Use small meaningful commits for work actually completed. Preserve existing
authors and third-party attribution. Do not invent experience, benchmarks,
screenshots, test output, timestamps, or commit history.

Before submitting a hub change:

```sh
make doctor
make bootstrap
make validate
make security
```

Run the documented quickstart from a clean checkout when prerequisites or commands
change. Do not weaken checks to produce green output. Record unsupported checks
and blocked integrations visibly. An unavailable optional profile stays unverified;
a missing required gate blocks a tested/released designation.

Update the plan, skills matrix, status, next steps, and evidence index together
when capability claims change. Every new claim needs an implementation path,
executable check, and appropriately scoped evidence. Keep publication, CI, and
release state independent. Verify remote URLs before adding links.

For dependencies, record official support/release/advisory research, compatible
pins and lockfiles, and unresolved uncertainty. Explain tradeoffs before adding
competing tools. Future projects should be planned here, not created as empty
repositories. Review changes for secrets and private information before staging;
run staged/outgoing-history scans before publishing.

An issue or pull request should state the problem, final behavior or claim,
validation performed, limitations, and any remaining task. Use synthetic data.
Report sensitive findings according to [the security policy](SECURITY.md).
