# ADR 0001: independent local-first labs with explicit evidence levels

Status: accepted for the first milestone.

## Context

The portfolio needs broad Linux/DevOps coverage supported by executable work.
The development host is macOS ARM64; Linux VMs, a running container runtime, cloud
credentials, and privileged execution cannot be assumed. The user authorizes new
public GitHub repositories after local gates, while disabling cloud resource
creation, paid services, host configuration changes, and container publishing.

## Decision

Keep a small portfolio hub and one standalone sibling repository for each completed
engineering core. Activate only one engineering project at a time. Start with an
unprivileged read-only operations toolkit using Bash for orchestration and Python
for structured logic. Build tests around synthetic input and label those results
separately from live execution. Require an appropriate Linux environment before
claiming Linux integration; require actual VMs for systemd/reboot assertions.

Use a single asynchronous jobs application for later platform projects and consume
pinned releases instead of copying codebases. Select one primary tool per
capability after official dependency/support/advisory review. Add alternative
tools only as independently testable extensions.

Maintain capability status, publication state, CI state, and release state
independently. Keep revision-linked records of environment, commands, exit codes,
assertions, and redacted outputs. A documentation mention is not implementation;
a passing mock is not integration; a CI configuration is not a CI run.

## Consequences

The first milestone can produce useful code with low local resource needs and no
privileged remediation. Independent repositories make each demo reviewable and
reproducible, but require explicit dependency versioning and coordinated releases
when integration begins. Evidence accounting adds maintenance work and may leave
profiles visibly unverified until a suitable execution environment is available.
That limitation is intentional and preferable to unsupported claims.

The hub is publishable as a work-in-progress index once its own gates pass. A
project release requires the project's full documented release gate, including
exact-revision CI where required. Future infrastructure remains planned until it
has an implementation and appropriate evidence.

## Alternatives considered

A single repository would simplify cross-project checkout but blur standalone
dependency boundaries and complicate release scope. Creating all repositories
up front would increase apparent breadth without executable value. Running
privileged host setup would improve some integration access but violate the
explicit authorization boundary. Those options are not selected.
