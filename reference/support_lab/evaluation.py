"""Small transparent evals; fixture scores are not production evidence."""
from .core import OfflineModel, retrieve, scenario, validate_output


def evaluate(strategy="lexical", budget=100):
    rows = []
    for ticket in scenario()["tickets"]:
        context = retrieve(ticket["text"], "agent", strategy=strategy, budget=budget)
        output = validate_output(OfflineModel().generate(ticket, context), context)
        expected = ticket["expected_source"]
        rows.append({"ticket": ticket["id"], "retrieval_hit": expected in [d["id"] for d in context],
                     "quality_pass": expected in output["citations"],
                     "context_units": sum(len(d["body"].split()) for d in context)})
    return {"strategy": strategy, "budget": budget, "cases": rows,
            "recall_at_2": sum(r["retrieval_hit"] for r in rows) / len(rows),
            "quality_pass_rate": sum(r["quality_pass"] for r in rows) / len(rows),
            "context_units": sum(r["context_units"] for r in rows)}
