from pathlib import Path
import pandas as pd

RISK_SEVERITIES = {"Low", "Moderate", "High", "Critical"}
CONTROL_STATUSES = {"Effective", "Partially Effective", "Ineffective", "Not Tested"}
ACTION_STATUSES = {"Open", "In Progress", "Blocked", "Closed", "Verified"}

def load_data(data_dir: str | Path):
    data_dir = Path(data_dir)
    risks = pd.read_csv(data_dir / "risk-register.csv", parse_dates=["snapshot_date"])
    actions = pd.read_csv(data_dir / "remediation-actions.csv")
    controls = pd.read_csv(data_dir / "control-status.csv")
    for col in ("opened_date", "due_date", "closed_date"):
        actions[col] = pd.to_datetime(actions[col], errors="coerce")
    if not set(risks["severity"]).issubset(RISK_SEVERITIES):
        raise ValueError("Unknown risk severity")
    if not set(controls["status"]).issubset(CONTROL_STATUSES):
        raise ValueError("Unknown control status")
    if not set(actions["status"]).issubset(ACTION_STATUSES):
        raise ValueError("Unknown remediation status")
    if risks.duplicated(["snapshot_date", "risk_id"]).any():
        raise ValueError("Duplicate risk_id within snapshot")
    if actions["action_id"].duplicated().any():
        raise ValueError("Duplicate action_id")
    if controls["control_id"].duplicated().any():
        raise ValueError("Duplicate control_id")
    return risks, actions, controls

def latest_risks(risks: pd.DataFrame) -> pd.DataFrame:
    latest_date = risks["snapshot_date"].max()
    return risks[risks["snapshot_date"] == latest_date].copy()

def calculate_overdue(actions: pd.DataFrame, reporting_date) -> pd.DataFrame:
    reporting_date = pd.Timestamp(reporting_date)
    open_mask = ~actions["status"].str.lower().isin(["closed", "verified"])
    mask = open_mask & actions["due_date"].notna() & (actions["due_date"] < reporting_date)
    result = actions.loc[mask].copy()
    result["days_overdue"] = (reporting_date - result["due_date"]).dt.days
    return result

def control_distribution(controls: pd.DataFrame) -> pd.DataFrame:
    counts = controls["status"].value_counts()
    total = len(controls)
    return pd.DataFrame([
        {"status": status, "count": int(counts.get(status, 0)),
         "percentage": (int(counts.get(status, 0)) / total if total else 0.0)}
        for status in ["Effective", "Partially Effective", "Ineffective", "Not Tested"]
    ])

def remediation_sla(actions: pd.DataFrame) -> dict:
    closed = actions[actions["status"].str.lower().isin(["closed", "verified"])].copy()
    closed = closed[closed["opened_date"].notna() & closed["closed_date"].notna()]
    closed["duration_days"] = (closed["closed_date"] - closed["opened_date"]).dt.days
    closed = closed[closed["duration_days"] >= 0]
    if closed.empty:
        return {"eligible": 0, "within_sla": 0, "rate": None}
    within = int((closed["duration_days"] <= closed["sla_days"]).sum())
    return {"eligible": len(closed), "within_sla": within, "rate": within / len(closed)}

def risk_trend(risks: pd.DataFrame) -> pd.DataFrame:
    work = risks.copy()
    work["is_open_high_critical"] = (
        work["severity"].isin(["High", "Critical"]) &
        work["status"].str.lower().ne("closed")
    )
    return (work.groupby("snapshot_date", as_index=False)["is_open_high_critical"]
            .sum().rename(columns={"is_open_high_critical": "high_critical_count"}))
