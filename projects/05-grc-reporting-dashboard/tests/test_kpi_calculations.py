from pathlib import Path
import sys
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kpi import load_data, calculate_overdue, control_distribution, remediation_sla, risk_trend, latest_risks

DATA = Path(__file__).resolve().parents[1] / "data"

def test_sample_data_validates_and_latest_snapshot_has_six_risks():
    risks, actions, controls = load_data(DATA)
    assert len(latest_risks(risks)) == 6
    assert len(actions) == 8
    assert len(controls) == 8

def test_overdue_excludes_closed_and_verified_actions():
    _, actions, _ = load_data(DATA)
    overdue = calculate_overdue(actions, "2026-10-23")
    assert set(overdue["action_id"]) == {"A-001", "A-002", "A-003", "A-004", "A-005"}

def test_control_distribution_preserves_not_tested():
    _, _, controls = load_data(DATA)
    dist = control_distribution(controls).set_index("status")
    assert dist.loc["Not Tested", "count"] == 2
    assert dist["count"].sum() == len(controls)

def test_sla_is_calculated_only_for_eligible_closed_actions():
    _, actions, _ = load_data(DATA)
    result = remediation_sla(actions)
    assert result["eligible"] == 3
    assert result["within_sla"] == 1
    assert round(result["rate"], 2) == 0.33

def test_risk_trend_uses_snapshot_dates_and_excludes_closed_risks():
    risks, _, _ = load_data(DATA)
    trend = risk_trend(risks)
    assert list(trend["high_critical_count"]) == [4, 4, 4]
