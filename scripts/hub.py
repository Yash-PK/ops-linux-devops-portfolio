#!/usr/bin/env python3
"""Validate and summarize the saved portfolio ledger without running its projects."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = "Yash-PK"
PROJECT_IDS = (
    "linux-operations-toolkit",
    "linux-fleet-automation",
    "network-storage-services-lab",
    "containerized-service-platform",
    "cloud-foundation-iac",
    "delivery-pipelines",
    "kubernetes-gitops-platform",
    "observability-sre-lab",
    "devsecops-policy-lab",
    "backup-disaster-recovery",
    "platform-engineering-golden-path",
    "production-simulation-capstone",
)
CAPABILITY_STATES = {
    "planned",
    "implemented-unverified",
    "statically-validated",
    "integration-tested",
    "cloud-deployed",
}
PUBLISHING_STATES = {"not-created", "pending", "blocked", "published"}
CI_STATES = {"not-run", "pending", "blocked", "failed", "passed"}
DISABLED_PERMISSIONS = (
    "allow_cloud_resource_creation",
    "allow_billable_services",
    "allow_host_configuration_changes",
    "publish_container_packages",
)


def is_revision(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value) is not None


def validate_record(record, label, errors):
    if not isinstance(record, dict):
        errors.append(f"{label}: record must be an object")
        return
    status = record.get("capability_status")
    if not isinstance(status, str) or status not in CAPABILITY_STATES:
        errors.append(f"{label}: invalid capability status")
    if status == "cloud-deployed":
        errors.append(f"{label}: cloud-deployed conflicts with disabled cloud authorization")
    if type(record.get("active")) is not bool:
        errors.append(f"{label}: active must be a boolean")
    publishing = record.get("publishing")
    if not isinstance(publishing, dict):
        errors.append(f"{label}: publishing must be a separate object")
        publishing = {}
    state = publishing.get("state")
    if not isinstance(state, str) or state not in PUBLISHING_STATES:
        errors.append(f"{label}: invalid publication state")
    verified = publishing.get("verified")
    if type(verified) is not bool:
        errors.append(f"{label}: publication verified must be a boolean")
    url = publishing.get("url")
    if url is not None and verified is not True:
        errors.append(f"{label}: URL cannot be recorded before remote verification")
    if state == "published" or verified is True:
        expected = f"https://github.com/{OWNER}/{record.get('repository')}"
        if state != "published" or verified is not True or url != expected:
            errors.append(f"{label}: published remote owner/name/URL or verification mismatch")
        verification = publishing.get("verification")
        if not isinstance(verification, dict):
            errors.append(f"{label}: published remote verification metadata required")
        else:
            if verification.get("owner") != OWNER or verification.get("visibility") != "PUBLIC":
                errors.append(f"{label}: remote owner/visibility mismatch")
            if not is_revision(verification.get("revision")):
                errors.append(f"{label}: verified remote revision required")
            if not isinstance(verification.get("default_branch"), str) or not verification.get(
                "default_branch"
            ):
                errors.append(f"{label}: verified default branch required")
    elif publishing.get("verification") is not None:
        errors.append(f"{label}: verification metadata requires published state")
    ci = record.get("ci")
    if not isinstance(ci, dict):
        errors.append(f"{label}: CI must be a separate object")
        ci = {}
    ci_state = ci.get("state")
    if not isinstance(ci_state, str) or ci_state not in CI_STATES:
        errors.append(f"{label}: invalid CI state")
    revision = ci.get("revision")
    if ci_state in {"passed", "failed", "pending"} and not is_revision(revision):
        errors.append(f"{label}: executed/pending CI requires exact revision")
    elif revision is not None and not is_revision(revision):
        errors.append(f"{label}: invalid CI revision")
    if ci_state == "passed" and state != "published":
        errors.append(f"{label}: hosted CI pass requires a published repository")


def validate_ledger(data):
    errors = []
    if not isinstance(data, dict):
        return ["ledger must be an object"]
    if data.get("schema_version") != 1:
        errors.append("unsupported ledger schema version")
    if data.get("owner") != OWNER:
        errors.append("owner differs from explicitly authorized personal account")
    if data.get("repository_prefix") != "ops-" or data.get("visibility") != "public":
        errors.append("repository prefix/visibility differs from authorization")
    if type(data.get("max_active_projects")) is not int or data.get("max_active_projects") != 1:
        errors.append("max_active_projects must remain 1")
    permissions = data.get("permissions")
    if not isinstance(permissions, dict):
        errors.append("permissions must be an object")
        permissions = {}
    for permission in DISABLED_PERMISSIONS:
        if permissions.get(permission) is not False:
            errors.append(f"{permission} must remain false")
    if permissions.get("publish_to_github") is not True:
        errors.append("publish_to_github must reflect the existing authorization")
    hub = data.get("hub")
    validate_record(hub, "hub", errors)
    if isinstance(hub, dict) and hub.get("repository") != "ops-linux-devops-portfolio":
        errors.append("hub repository name mismatch")
    projects = data.get("projects")
    if not isinstance(projects, list):
        return [*errors, "projects must be an ordered array"]
    ids = [project.get("id") if isinstance(project, dict) else None for project in projects]
    if ids != list(PROJECT_IDS):
        errors.append("project IDs must contain the twelve scoped projects once, in planned order")
    active = 0
    for index, project in enumerate(projects):
        label = f"project[{index}]"
        validate_record(project, label, errors)
        if not isinstance(project, dict):
            continue
        if project.get("repository") != f"ops-{project.get('id')}":
            errors.append(f"{label}: repository name must match prefix and project ID")
        if project.get("active") is True:
            active += 1
    if active > 1:
        errors.append("more than one engineering project is active")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "demo"])
    parser.add_argument("--ledger", type=Path, default=ROOT / "portfolio.json")
    args = parser.parse_args()
    try:
        data = json.loads(args.ledger.read_text())
    except (OSError, ValueError) as error:
        raise SystemExit(f"Cannot read ledger: {error}") from error
    errors = validate_ledger(data)
    if errors:
        raise SystemExit("\n".join(errors))
    if args.command == "validate":
        print("Portfolio ledger structure and authorization constraints: PASS")
        return
    print("Saved portfolio ledger; this command does not execute engineering projects.")
    print(f"Owner: {data['owner']}; visibility: {data['visibility']}; active-project limit: 1")
    print("Cloud resources, billable services, host changes and container publishing: disabled")
    for record in [data["hub"], *data["projects"]]:
        print(
            f"{record['repository']}: {record['capability_status']}; "
            f"publishing={record['publishing']['state']}; CI={record['ci']['state']}"
            + ("; active" if record["active"] else "")
        )
    print("See PROJECT_STATUS.md and docs/evidence-index.md for actual revision-linked results.")


if __name__ == "__main__":
    main()
