"""
Meridian Bank corpus (curriculum §3.3).

Deliberately awkward on purpose:
  * the SAME lending policy exists as v2 and v3  -> version trap
  * a rate card is tabular                        -> punishes naive parsing/chunking
  * AML text is jurisdiction-specific             -> forces metadata filtering
A correct system as of AS_OF must never cite pol-v2.
"""
from .config import AS_OF

DOCS = [
    dict(id="pol-v2", doc="Lending Policy", version="v2", effective="2024-01-01",
         jurisdiction="UK", doctype="policy",
         text=("BTL lending. Maximum LTV is 75%. Self-employed applicants must provide "
               "3 years of certified accounts. Minimum interest cover ratio is 125%. "
               "Applicants with any late payment in the last 24 months are declined.")),

    dict(id="pol-v3", doc="Lending Policy", version="v3", effective="2026-04-01",
         jurisdiction="UK", doctype="policy",
         text=("BTL lending. Maximum LTV is 75%. Self-employed applicants must provide "
               "2 years of certified accounts where supported by an accountant reference. "
               "Minimum interest cover ratio is 145%. A single late payment older than "
               "12 months may be accepted with underwriter sign-off.")),

    dict(id="rate-1", doc="Rate Card", version="v3", effective="2026-04-01",
         jurisdiction="UK", doctype="table",
         text=("BTL 2-year fixed rates. 60% LTV: 4.29%. 70% LTV: 4.55%. "
               "75% LTV: 4.84%. 80% LTV: not offered. Product fee GBP 1,495.")),

    dict(id="aml-1", doc="AML Procedure", version="v1", effective="2023-06-01",
         jurisdiction="UK", doctype="procedure",
         text=("Enhanced due diligence is required for politically exposed persons and for "
               "any cash deposit exceeding GBP 10,000 within a rolling 30-day period. "
               "Source of funds evidence must be retained for 5 years.")),

    dict(id="aml-2", doc="AML Procedure", version="v1", effective="2023-06-01",
         jurisdiction="IE", doctype="procedure",
         text=("Enhanced due diligence applies to cash deposits exceeding EUR 10,000 "
               "within a rolling 30-day period. Reporting is to the FIU within 5 days.")),

    dict(id="ops-1", doc="Branch Runbook", version="v4", effective="2025-11-01",
         jurisdiction="UK", doctype="runbook",
         text=("Card dispute intake. Step 1: verify identity. Step 2: confirm the disputed "
               "transaction is under 120 days old. Step 3: raise a chargeback case. "
               "Step 4: provisional credit within 2 business days if value is under GBP 500.")),
]

def current_docs(as_of: str = AS_OF, jurisdiction: str | None = "UK"):
    """Only documents in force at `as_of`, newest version per document name."""
    pool = [d for d in DOCS if d["effective"] <= as_of]
    if jurisdiction:
        pool = [d for d in pool if d["jurisdiction"] == jurisdiction]
    newest = {}
    for d in pool:
        if d["doc"] not in newest or d["effective"] > newest[d["doc"]]["effective"]:
            newest[d["doc"]] = d
    return list(newest.values())

SUPERSEDED_IDS = {"pol-v2"}   # citing any of these is a compliance failure
