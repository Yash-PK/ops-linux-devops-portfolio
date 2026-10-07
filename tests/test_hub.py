"""Exercise ledger authorization, claim accounting and publication boundaries."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("hub", ROOT / "scripts/hub.py")
hub = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hub)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.ledger = json.loads((ROOT / "portfolio.json").read_text())

    def reject(self, text):
        errors = hub.validate_ledger(self.ledger)
        self.assertTrue(any(text in error for error in errors), errors)

    def test_repository_ledger_valid(self):
        self.assertEqual(hub.validate_ledger(self.ledger), [])

    def test_invalid_capability_status_rejected(self):
        self.ledger["projects"][0]["capability_status"] = "production-ready"
        self.reject("invalid capability status")

    def test_owner_change_rejected(self):
        self.ledger["owner"] = "different-account"
        self.reject("authorized personal account")

    def test_two_active_projects_rejected(self):
        self.ledger["projects"][0]["active"] = True
        self.ledger["projects"][1]["active"] = True
        self.reject("more than one")

    def test_cloud_authorization_cannot_be_enabled_by_ledger_edit(self):
        self.ledger["permissions"]["allow_cloud_resource_creation"] = True
        self.reject("allow_cloud_resource_creation must remain false")

    def test_unverified_remote_link_rejected(self):
        self.ledger["projects"][0]["publishing"] = {
            "state": "pending",
            "verified": False,
            "url": "https://github.com/Yash-PK/ops-linux-operations-toolkit",
        }
        self.reject("before remote verification")

    def test_remote_owner_mismatch_rejected_even_when_marked_verified(self):
        self.ledger["projects"][0]["publishing"] = {
            "state": "published",
            "verified": True,
            "url": "https://github.com/different-account/ops-linux-operations-toolkit",
            "verification": {
                "owner": "different-account",
                "visibility": "PUBLIC",
                "revision": "a" * 40,
                "default_branch": "main",
            },
        }
        self.reject("remote owner")

    def test_ci_pass_requires_exact_revision(self):
        self.ledger["projects"][0]["ci"] = {"state": "passed", "revision": None}
        self.reject("exact revision")

    def test_duplicate_or_missing_project_rejected(self):
        self.ledger["projects"][1] = copy.deepcopy(self.ledger["projects"][0])
        self.reject("twelve scoped projects once")

    def test_cloud_deployed_claim_rejected(self):
        self.ledger["projects"][4]["capability_status"] = "cloud-deployed"
        self.reject("disabled cloud authorization")

    def test_malformed_objects_fail_validation(self):
        self.ledger["projects"][0] = None
        self.reject("record must be an object")
        self.assertEqual(hub.validate_ledger([]), ["ledger must be an object"])


if __name__ == "__main__":
    unittest.main()
