# Track 4 — Agentic AI  (Curriculum §5)
An agent is a control loop with a budget. Everything else is detail.

| Lab | Studies | Free stack | Key metric |
|---|---|---|---|
| A0 | Trajectory harness | LangGraph + Langfuse | outcome **and** trajectory (steps, tools, $) |
| A1 | Bounded single agent | LangGraph | completion rate vs budget; KYC triage |
| A2 | Tool design + failure injection | JSON-schema tools | recovery rate, **silent-failure rate** |
| A3 | Memory | Redis (short) + Qdrant (long) | none / buffer / summary / vector recall |
| A4 | Planning strategies | ReAct vs Plan-Execute vs Reflexion | success, steps, cost |
| A5 | Multi-agent | orchestrator + subagents | **the threshold where it starts to pay** |
| A6 | Guardrails / HITL / sandbox | NeMo Guardrails, `interrupt()`, Docker | blocked-action rate, bypass attempts |
| A7 | Observability + replay | Langfuse traces, checkpointer | mean time to diagnose |

**Expected discovery (A5):** one agent with four good tools usually beats an orchestrated
fleet on success, cost *and* debuggability.
