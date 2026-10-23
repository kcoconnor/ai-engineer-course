# Worked threat model (T4)

Scope: local synthetic support workflow. The trusted operator selects actors;
code, role map, database and host are trusted. Tickets, policy text and generator
output are untrusted. See the architecture diagram in the reference README.

| Entry point / threat | Impact | Implemented control | Verification |
|---|---|---|---|
| Query names private finance information | Cross-role disclosure | Filter document grants before ranking and generation | Spy-model ACL test, lab 7 |
| Model requests send, approval or a new recipient | Unauthorized action | Exact output schema; destination comes from immutable ticket; model has no tools | HostileModel tests, lab 12 |
| Model produces malicious text in a valid schema | Harmful customer reply | Mandatory human review of exact payload | Valid-shape malicious-text test |
| Requester approves own work | Approval bypass | Independent human allowlist enforced in code | Lab 3 and identity tests |
| Payload changes after review | Misleading approval | Digest checked at decision and effect | Tampering and stale-digest tests |
| Crash/retry after an effect | Duplicate reply | Atomic local transaction, unique outbox key | Lab 8, replay tests |
| Attacker chooses CLI actor | Identity spoofing | Not addressed by CLI; trusted operator boundary | Production authentication required |
| Tickets, payloads or traces expose personal data | Local disclosure | Synthetic data only in this demonstration | Production retention/redaction/access policy required |

Trifecta: the generator reads accessible data plus untrusted input. It has no
external communication tool. The only effect is a local outbox, guarded by a
separate human decision. This limits tool misuse; it does not make generated
text safe. A human can approve a bad draft. Citations establish membership, not
truth. Retrieved injection can still change wording with a real model.

Lab 12 assumes full generator compromise and probes structural rejection with
20 ticket/document payloads. It does not test real LLM attack success rates,
MCP poisoning, persistent memory or cross-agent attacks: those components are
absent. Adding any of them requires new trust boundaries and attack cases.

No Guardian model is used as a security boundary. Digest checks do not protect
against an attacker who controls both payload and digest in the database.
External delivery would need authenticated recipients, egress restrictions,
provider idempotency and reconciliation after ambiguous network failures.
