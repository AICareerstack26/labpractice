# Track 4 — Agentic AI
An agent is a control loop with a budget. Everything else is detail.

## ▶️ Available now
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AICareerstack26/labpractice/blob/main/04_agentic/lab06_agentic.ipynb)

**`lab06_agentic.ipynb`** — a hand-rolled **bounded agent loop**: tools (version-safe policy search,
rate lookup, escalate-to-human), a hard **step budget**, and a refuse/escalate path — scored on
outcome **and** trajectory. Compliant by construction: it cannot cite a superseded policy.
*Simplified vs. the full track:* memory, planning strategies, multi-agent and sandboxed HITL are ⏳ below.

## Full track roadmap
*The complete track we're building toward. The lab above is the runnable, free-tier core; rows marked ⏳ are planned, not yet in the repo.*

| Lab | Studies | Free stack | Status |
|---|---|---|---|
| A-free | bounded single agent + tools | LangGraph-style loop + Groq | ✅ built (`lab06`) |
| A2 | tool design + failure injection | JSON-schema tools | ⏳ planned |
| A3 | memory | Redis (short) + Qdrant (long) | ⏳ planned |
| A4 | planning: ReAct / Plan-Execute / Reflexion | — | ⏳ planned |
| A5 | multi-agent | orchestrator + subagents | ⏳ planned |
| A6 | guardrails / HITL / sandbox | NeMo Guardrails, `interrupt()` | ⏳ planned |

**Expected discovery:** one agent with four good tools usually beats an orchestrated fleet on success, cost *and* debuggability.
