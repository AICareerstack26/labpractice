# Track 5 — Model Context Protocol  (Curriculum §5)
In a bank, MCP is an **authorisation** problem as much as an integration one.

| Lab | Studies | Free stack | Key metric |
|---|---|---|---|
| M0 | Build a server | **FastMCP** | mock core-banking: accounts, transactions, cards, limits |
| M1 | Primitive design | resources vs tools vs prompts | agent success rate per modelling choice |
| M2 | Auth & least privilege | per-role scopes (teller/adviser/ops) | **deliberate escalation attempts** |
| M3 | Multi-client | two agent clients, one server | behavioural parity |
| M4 | Contract testing | schema contract tests | breaking-change detected before the agent |
| M5 | Observability | trace identity, scope, payload | regulator-grade audit trail |

**Expected discovery:** the hard part is not the protocol — a broad scope hands an
unpredictable system broad power. Scope design *is* security design.
