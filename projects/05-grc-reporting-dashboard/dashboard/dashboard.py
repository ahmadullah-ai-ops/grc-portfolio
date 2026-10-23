from pathlib import Path
from datetime import date
import sys

import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from kpi import (load_data, calculate_overdue, control_distribution,
                 remediation_sla, risk_trend, latest_risks)

st.set_page_config(page_title="GRC Reporting Dashboard", layout="wide")
st.title("GRC Reporting Dashboard")
st.caption("Fictional Northstar Retail dataset • Portfolio demonstration • Reporting date: 2026-10-23")

risks, actions, controls = load_data(ROOT / "data")
reporting_date = st.date_input("Reporting date", value=date(2026, 10, 23))
overdue = calculate_overdue(actions, reporting_date)
latest = latest_risks(risks)
distribution = control_distribution(controls)
sla = remediation_sla(actions)
trend = risk_trend(risks)

open_risks = latest[latest["status"].str.lower() != "closed"]
high_critical = open_risks[open_risks["severity"].isin(["High", "Critical"])]
sla_text = f"{sla['rate']:.0%}" if sla["rate"] is not None else "N/A"
cols = st.columns(4)
cols[0].metric("Open risks", len(open_risks))
cols[1].metric("Open High/Critical risks", len(high_critical))
cols[2].metric("Overdue actions", len(overdue))
cols[3].metric("Remediation SLA compliance", sla_text,
               help=f"{sla['within_sla']} / {sla['eligible']} eligible closed actions")

st.subheader("Risk trends")
st.plotly_chart(px.line(trend, x="snapshot_date", y="high_critical_count",
                        markers=True, title="Open High/Critical risks by snapshot"),
                use_container_width=True)
st.caption("Trend values are counts from synthetic monthly snapshots, not real organizational history.")

left, right = st.columns(2)
with left:
    st.subheader("Latest risk register by severity")
    severity_counts = open_risks.groupby("severity").size().reindex(
        ["Critical", "High", "Moderate", "Low"], fill_value=0
    ).rename("count").reset_index(names="severity")
    st.plotly_chart(px.bar(severity_counts, x="severity", y="count"),
                    use_container_width=True)
with right:
    st.subheader("Control status")
    st.plotly_chart(px.bar(distribution, x="status", y="count", title="Control count by status"),
                    use_container_width=True)
    st.dataframe(distribution, hide_index=True, use_container_width=True)

st.subheader("Overdue remediation actions")
if overdue.empty:
    st.success("No actions are overdue as of the selected reporting date.")
else:
    st.dataframe(overdue[["action_id", "risk_id", "title", "priority", "owner",
                          "due_date", "days_overdue", "status"]].sort_values(
                              ["days_overdue", "priority"], ascending=[False, True]),
                 hide_index=True, use_container_width=True)

st.subheader("Remediation SLA denominator")
st.write(f"{sla['within_sla']} of {sla['eligible']} eligible closed actions were closed within their SLA.")
st.caption("Open actions are excluded from historical closure SLA compliance and tracked separately through overdue metrics.")

st.subheader("Control evidence freshness")
fresh = controls.copy()
fresh["evidence_review_date"] = pd.to_datetime(fresh["evidence_review_date"], errors="coerce")
fresh["evidence_age_days"] = (pd.Timestamp(reporting_date) - fresh["evidence_review_date"]).dt.days
fresh["evidence_flag"] = fresh["evidence_review_date"].apply(
    lambda d: "Missing" if pd.isna(d) else ("Stale >365 days" if (pd.Timestamp(reporting_date) - d).days > 365 else "Present; validate scope")
)
st.dataframe(fresh[["control_id", "control_name", "status", "evidence_review_date",
                    "evidence_age_days", "evidence_flag", "evidence_reference"]],
             hide_index=True, use_container_width=True)

st.warning("Synthetic data only. Dashboard status does not independently prove control effectiveness. Validate source data, evidence scope, and approval before operational use.")
