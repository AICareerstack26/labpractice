# Track 5 — Model Context Protocol
In a bank, MCP is an **authorisation** problem as much as an integration one.

## ▶️ Available now
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/05_mcp/lab07_mcp.ipynb)

**`lab07_mcp.ipynb`** — a **FastMCP** server of core-banking tools wrapped in **per-role scopes**
(teller / adviser / ops); a deliberate privilege-escalation attempt is blocked and audited.
*Simplified vs. the full track:* runs in-process (Colab can't easily host a stdio server + client),
and falls back to a pure-Python registry if the `mcp` SDK isn't present. Multi-client, contract
testing and full audit are ⏳ below. The scope logic — the actual lesson — is production-identical.

## Full track roadmap
*The complete track we're building toward. The lab above is the runnable, free-tier core; rows marked ⏳ are planned, not yet in the repo.*

| Lab | Studies | Free stack | Status |
|---|---|---|---|
| M-free | server + per-role scopes + audit | FastMCP (in-process) | ✅ built (`lab07`) |
| M1 | primitive design: resources vs tools | — | ⏳ planned |
| M3 | multi-client parity | two agents, one server | ⏳ planned |
| M4 | contract testing | schema contract tests | ⏳ planned |
| M5 | observability | trace identity, scope, payload | ⏳ planned |

**Expected discovery:** the hard part is not the protocol — a broad scope hands an unpredictable system broad power. Scope design *is* security design.
