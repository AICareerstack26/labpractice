"""
Scorers (curriculum §2.2 `score` span).

Retrieval scorers are pure Python — deterministic and free.
Faithfulness uses an LLM judge; ALWAYS a different model from the generator.
"""
from .corpus import SUPERSEDED_IDS


# ---------- retrieval ----------
def hit_at_k(hits, gold) -> float:
    if gold["source"] is None: return 1.0            # refusal items
    return 1.0 if gold["source"] in [h["id"] for h in hits] else 0.0

def mrr(hits, gold) -> float:
    if gold["source"] is None: return 1.0
    ids = [h["id"] for h in hits]
    return 1.0 / (ids.index(gold["source"]) + 1) if gold["source"] in ids else 0.0

def version_correct(hits, gold) -> float:
    """0.0 if ANY superseded document was retrieved. The compliance metric."""
    return 0.0 if any(h["id"] in SUPERSEDED_IDS for h in hits) else 1.0


# ---------- generation ----------
def citation_accuracy(answer: str, hits) -> float:
    cited = {t.strip("[].,") for t in answer.split() if t.startswith("[")}
    cited = {c for c in cited if c}
    if not cited: return 0.0
    valid = {h["id"] for h in hits}
    return len(cited & valid) / len(cited)

def refusal_correct(answer: str, gold) -> float:
    refused = "INSUFFICIENT_CONTEXT" in answer.upper()
    should  = gold["source"] is None
    return 1.0 if refused == should else 0.0


def make_faithfulness_scorer(judge_llm):
    """judge_llm must expose .invoke(str) -> obj with .content"""
    def score(answer: str, hits) -> float:
        if "INSUFFICIENT_CONTEXT" in answer.upper(): return 1.0
        ctx = "\n".join(h["text"] for h in hits)
        p = (f"Context:\n{ctx}\n\nAnswer:\n{answer}\n\n"
             "Is EVERY factual claim in the answer supported by the context? "
             "Reply with only YES or NO.")
        try:
            return 1.0 if "YES" in judge_llm.invoke(p).content.upper() else 0.0
        except Exception:
            return float("nan")
    return score
