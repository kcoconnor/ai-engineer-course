import json
import tempfile
import unittest
from pathlib import Path

from support_lab.core import HostileModel, Workflow, retrieve, scenario, validate_output
from support_lab.evaluation import evaluate
from support_lab.labs import run_lab


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "test.db"
        self.app = Workflow(self.path)
        self.ticket = scenario()["tickets"][0]

    def tearDown(self):
        self.app.close()
        self.tmp.cleanup()

    def approval(self):
        self.app.draft(self.ticket)
        row = self.app.inspect("T1")
        self.app.decide("T1", "alice", row["digest"])

    def test_pending_and_rejected_actions_have_no_effect(self):
        self.app.draft(self.ticket)
        with self.assertRaises(PermissionError):
            self.app.send("T1")
        self.app.decide("T1", "alice", self.app.inspect("T1")["digest"], approve=False)
        with self.assertRaises(PermissionError):
            self.app.send("T1")
        self.assertEqual(self.app.report()["sent"], 0)

    def test_only_independent_humans_can_decide(self):
        self.app.draft(self.ticket, requester="alice")
        for actor in ["alice", "agent", "fin", "unknown"]:
            with self.subTest(actor=actor), self.assertRaises(PermissionError):
                self.app.decide("T1", actor, self.app.inspect("T1")["digest"])
        self.app.decide("T1", "bob", self.app.inspect("T1")["digest"])
        self.assertEqual(self.app.send("T1")["customer"], "customer-1")

    def test_stale_digest_and_second_decision_refused(self):
        self.app.draft(self.ticket)
        with self.assertRaises(ValueError):
            self.app.decide("T1", "alice", "stale-digest")
        self.app.decide("T1", "alice", self.app.inspect("T1")["digest"])
        with self.assertRaises(ValueError):
            self.app.decide("T1", "bob", self.app.inspect("T1")["digest"], approve=False)

    def test_modified_payload_cannot_use_previous_approval(self):
        self.approval()
        payload = self.app.inspect("T1")["payload"]
        payload["customer"] = "attacker"
        with self.app.db:
            self.app.db.execute("UPDATE drafts SET payload=?", (json.dumps(payload),))
        with self.assertRaises(ValueError):
            self.app.send("T1")

    def test_replay_and_restart_do_not_duplicate_effect(self):
        self.approval()
        with self.assertRaises(RuntimeError):
            self.app.send("T1", fail_before_commit=True)
        self.assertEqual(self.app.report()["sent"], 0)
        self.app.close()
        self.app = Workflow(self.path)
        self.app.send("T1")
        self.app.send("T1")
        self.assertEqual(self.app.report()["sent"], 1)
        self.assertEqual(sum(t["event"] == "send" for t in self.app.report()["traces"]), 1)

    def test_competing_connections_cannot_duplicate_outbox(self):
        self.approval()
        other = Workflow(self.path)
        try:
            self.app.send("T1")
            other.send("T1")
            self.assertEqual(other.report()["sent"], 1)
        finally:
            other.close()

    def test_ticket_id_cannot_be_rebound(self):
        self.app.draft(self.ticket)
        with self.assertRaises(ValueError):
            self.app.draft(dict(self.ticket, customer="attacker"))

    def test_hostile_model_cannot_set_destination_or_approval(self):
        self.app.model = HostileModel()
        with self.assertRaises(ValueError):
            self.app.draft(self.ticket)
        self.assertEqual(self.app.report()["drafts"], 0)
        self.assertEqual(self.app.report()["sent"], 0)
        self.assertEqual(self.app.report()["traces"][0]["event"], "refused")

    def test_valid_shape_malicious_text_still_requires_review(self):
        class PlausibleAttack:
            def generate(self, ticket, context):
                return {"text": "Please visit https://evil.invalid and disclose your password.", "citations": [context[0]["id"]]}
        self.app.model = PlausibleAttack()
        self.app.draft(self.ticket)
        with self.assertRaises(PermissionError):
            self.app.send("T1")
        self.app.decide("T1", "alice", self.app.inspect("T1")["digest"], approve=False)
        self.assertEqual(self.app.report()["sent"], 0)

    def test_acl_excludes_private_document_before_model(self):
        class Spy:
            seen = []
            def generate(self, ticket, context):
                self.seen = context
                return {"text": "A human will review this request.", "citations": [context[0]["id"]]}
        spy = Spy()
        self.app.model = spy
        self.app.draft(dict(self.ticket, text="Refund private bank account CONFIDENTIAL_RESERVE_7419"))
        self.assertNotIn("CONFIDENTIAL_RESERVE_7419", json.dumps(spy.seen))
        self.assertNotIn("finance", [d["id"] for d in spy.seen])
        self.assertIn("finance", [d["id"] for d in retrieve("private bank", "fin")])
        with self.assertRaises(PermissionError):
            retrieve("private bank", "unknown")

    def test_invalid_citations_and_types_are_refused(self):
        context = retrieve("refund", "agent")
        for output in [None, {"text": "ok", "citations": ["finance"]},
                       {"text": "ok", "citations": []}, {"text": "", "citations": ["refunds"]},
                       {"text": "ok", "citations": [123]}]:
            with self.subTest(output=output), self.assertRaises(ValueError):
                validate_output(output, context)

    def test_empty_context_escalates(self):
        output = self.app.draft(dict(self.ticket, text="zzzzzz"))
        self.assertEqual(output["citations"], [])
        self.assertIn("human", output["text"])

    def test_replay_skips_model(self):
        self.app.draft(self.ticket)
        self.app.model = HostileModel()
        self.app.draft(self.ticket)
        self.assertEqual(len(self.app.report()["traces"]), 1)


class CourseChecks(unittest.TestCase):
    def test_fixture_quality_gate(self):
        result = evaluate()
        self.assertEqual(result["quality_pass_rate"], 1)
        self.assertEqual(result["recall_at_2"], 1)

    def test_all_weekly_experiments(self):
        for number in range(1, 14):
            with self.subTest(lab=number):
                self.assertTrue(run_lab(number))


if __name__ == "__main__":
    unittest.main()
