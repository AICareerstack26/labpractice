# Capstone — The Meridian Assistant

> **There is no notebook to open here — this is the capstone *you* build.** Assemble the eight
> labs into one Meridian Bank assistant, then defend every choice with a number from your own harness.

## What you assemble
Compose the pieces you built in Labs 0–7 into a single system:

- **Retrieval** — the winning stack from Lab 3 (hybrid + rerank + version filter), so it never cites a superseded policy.
- **Serving** — the caching/routing from Lab 4, costed on p95 and $/query.
- **Agentic layer** — the bounded loop from Lab 6, with a refuse/escalate path.
- **Access** — tools exposed with per-role scopes from Lab 7.
- **Observability & eval** — everything traced and scored on the Lab 0 harness.

## Deliverables
| Deliverable | Standard |
|---|---|
| Evaluation report | Every architectural choice justified with a number from your own harness |
| SLO & cost model | p95 latency and $/query at projected volume, with the degradation path |
| Risk register | Failure modes, guardrails, and what remains unmitigated |
| Incident replay | A deliberately broken run, traced and diagnosed end to end |

## The exam
Answer *"why did you choose that?"* six times in a row — each time with a number from an
experiment you ran, and at least once with *"we tried the more sophisticated option and it did
not earn its keep."*

---
*Status: this is an open-ended brief, not a fill-in notebook. Start from the 8 built labs
([repo README](../README.md)); a guided capstone notebook is on the roadmap.*
