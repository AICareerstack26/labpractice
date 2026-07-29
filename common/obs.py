"""
Observability spine (curriculum §2).

Wraps Langfuse so every lab emits the same span tree:
    rag.request -> parse -> chunk -> embed -> retrieve -> rerank -> generate -> score
and tags every trace with a deterministic config hash, which is what turns
Langfuse into an experiment registry.
"""
import hashlib, json, functools
from .config import ROOT

try:
    from langfuse import Langfuse
    from langfuse.decorators import observe, langfuse_context
    _lf = Langfuse()
    ENABLED = True
except Exception as e:                                    # offline / no keys
    ENABLED = False
    _lf = None
    print(f"[obs] Langfuse disabled ({type(e).__name__}). Labs still run; traces are skipped.")

    def observe(*a, **kw):                                 # no-op decorator
        def deco(fn):
            @functools.wraps(fn)
            def inner(*args, **kwargs): return fn(*args, **kwargs)
            return inner
        return deco(a[0]) if a and callable(a[0]) else deco

    class _Ctx:
        def update_current_observation(self, **kw): pass
        def update_current_trace(self, **kw): pass
        def flush(self): pass
    langfuse_context = _Ctx()


def config_hash(cfg: dict) -> str:
    """Deterministic short hash of a run configuration."""
    clean = {k: v for k, v in cfg.items() if k != "hash"}
    return "cfg-" + hashlib.md5(json.dumps(clean, sort_keys=True, default=str).encode()).hexdigest()[:8]


def make_config(**kw) -> dict:
    cfg = dict(kw)
    cfg["hash"] = config_hash(cfg)
    return cfg


def span_meta(**kw):
    """Attach attributes to the current span (no-op when Langfuse is off)."""
    langfuse_context.update_current_observation(metadata=kw)


def trace_meta(tags=None, **kw):
    langfuse_context.update_current_trace(tags=tags or [], metadata=kw)


def flush():
    if ENABLED and _lf: _lf.flush()
