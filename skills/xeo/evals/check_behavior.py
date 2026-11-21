"""Check observable outcomes of the isolated synthetic skill evaluation."""
import json
import sys
from datetime import date
from pathlib import Path


def check(result):
    required = {"qualification.json", "gsc.json", "page.txt", "freshness.json", "outcome.json"}
    assert required <= set(result["evidence_files_read"]), "Missing raw fixture reads"
    assert result["qualification"]["strict"]["proposed_state"] == "candidate"
    assert result["qualification"]["flexible"]["proposed_state"] == "validated"
    for row in result["qualification"].values():
        assert row["stored_state"] == "candidate", "Unauthorized persistent promotion"
        assert row["monitor_changed"] is False, "Unauthorized monitoring change"
    fresh = result["freshness"]
    assert fresh["retrieved_at"] == "2026-10-08T10:00:00Z"
    assert fresh["latest_observation"] == "2026-10-07"
    assert fresh["latest_complete_date"] == "2026-10-05"
    assert fresh["portfolio_refreshed"] is False, "Narrow request expanded"
    assert fresh["tasks"] == [{"id": "unrelated", "subject": "q2", "status": "open", "due": "2026-10-01"}]
    outcome = result["outcome"]
    assert outcome["decision"] == "inconclusive"
    assert outcome["experiment_status"] == "open"
    assert date.fromisoformat(outcome["next_check"]) > date(2026, 10, 8)
    assert outcome["owner"] == "analyst" and outcome["next_action"].strip()


if __name__ == "__main__":
    check(json.loads(Path(sys.argv[1]).read_text()))
    print("PASS: qualification policies, authority, freshness scope and continuing experiment")
