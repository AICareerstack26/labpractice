"""
Golden evaluation set (curriculum §2.4 step 4).

Each item carries the ground-truth source id AND the version that must be cited,
so we can score `version_correct` separately from ordinary retrieval accuracy.
Expand toward ~100 items for the full track; keep the version traps.
"""
GOLDEN = [
    dict(qid="q1", q="How many years of certified accounts does a self-employed BTL applicant need?",
         answer="Two years, supported by an accountant reference.",
         source="pol-v3", version="v3", difficulty="easy", trap="version"),

    dict(qid="q2", q="What is the minimum interest cover ratio for BTL lending?",
         answer="145%.", source="pol-v3", version="v3", difficulty="easy", trap="version"),

    dict(qid="q3", q="What is the BTL 2-year fixed rate at 75% LTV?",
         answer="4.84%.", source="rate-1", version="v3", difficulty="medium", trap="table"),

    dict(qid="q4", q="Is 80% LTV offered on buy-to-let?",
         answer="No, 80% LTV is not offered.", source="rate-1", version="v3",
         difficulty="medium", trap="table"),

    dict(qid="q5", q="When is enhanced due diligence required for cash deposits in the UK?",
         answer="Deposits over GBP 10,000 in a rolling 30-day period.",
         source="aml-1", version="v1", difficulty="easy", trap="jurisdiction"),

    dict(qid="q6", q="Can a BTL applicant with one late payment 18 months ago be considered?",
         answer="Yes, with underwriter sign-off, since it is older than 12 months.",
         source="pol-v3", version="v3", difficulty="hard", trap="version"),

    dict(qid="q7", q="How old can a disputed card transaction be and still be raised?",
         answer="Under 120 days.", source="ops-1", version="v4", difficulty="easy", trap=None),

    dict(qid="q8", q="What is Meridian's policy on cryptocurrency lending?",
         answer="INSUFFICIENT_CONTEXT", source=None, version=None,
         difficulty="hard", trap="refusal"),   # must refuse, not invent
]
