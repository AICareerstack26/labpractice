"""
The harness every lab calls (curriculum §2.4 step 6).

    from common.harness import evaluate
    row = evaluate(cfg, pipeline_fn)

`pipeline_fn(query, cfg) -> {"answer": str, "hits": [ {id,text,...} ]}`
Returns a one-row summary and writes the full per-question detail to results/.
"""
import time, json
import pandas as pd
from .golden import GOLDEN
from .config import RESULTS
from .obs import flush
from . import scorers as S


def evaluate(cfg, pipeline_fn, golden=None, judge=None, verbose=False, save=True):
    golden = golden or GOLDEN
    faith = S.make_faithfulness_scorer(judge) if judge else None
    rows = []

    for g in golden:
        t0 = time.time()
        try:
            out = pipeline_fn(g["q"], cfg)
        except Exception as e:
            print(f"  !! {g['qid']} failed: {type(e).__name__}: {e}")
            continue
        dt = time.time() - t0
        hits, ans = out["hits"], out["answer"]

        r = dict(
            qid=g["qid"], difficulty=g["difficulty"], trap=g.get("trap"),
            hit_at_k=S.hit_at_k(hits, g),
            mrr=S.mrr(hits, g),
            version_correct=S.version_correct(hits, g),
            citation=S.citation_accuracy(ans, hits),
            refusal_correct=S.refusal_correct(ans, g),
            latency_s=round(dt, 3),
        )
        if faith: r["faithfulness"] = faith(ans, hits)
        rows.append(r)
        if verbose:
            print(f"  {g['qid']}: {ans[:80]}")

    detail = pd.DataFrame(rows)
    summary = detail.mean(numeric_only=True).round(3).to_dict()
    summary["config"] = cfg["hash"]
    for k in ("embed_model", "chunk_strategy", "retriever", "k", "version_filter", "reranker"):
        if k in cfg: summary[k] = cfg[k]

    if save:
        detail.to_csv(RESULTS / f"detail_{cfg['hash']}.csv", index=False)
        with open(RESULTS / f"summary_{cfg['hash']}.json", "w") as f:
            json.dump(summary, f, indent=2, default=str)
    flush()
    return summary


def leaderboard(summaries, sort_by="version_correct"):
    df = pd.DataFrame(summaries)
    front = [c for c in ["config","embed_model","chunk_strategy","retriever","k","version_filter"] if c in df]
    rest  = [c for c in df.columns if c not in front]
    return df[front + rest].sort_values(sort_by, ascending=False).reset_index(drop=True)
