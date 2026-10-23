# Project 05 — GRC Reporting Dashboard

**Purpose:** Turn risk, remediation and control-status records into decision-useful management reporting.  
**Stack:** Python, Streamlit, Plotly, pandas, pytest.  
**Scenario:** Fictional Northstar Retail; all records are synthetic and intended for portfolio demonstration only.

## Business questions answered

- What is the current distribution of open risks by severity?
- Are critical/high risks increasing or decreasing across monthly snapshots?
- Which remediation actions are overdue, and by how many days?
- What proportion of assessed controls are effective, partially effective or ineffective?
- Are remediation SLAs being met, and what requires management escalation?

## Run locally

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

Run KPI tests with `pytest -q`.

## Data and calculation integrity

The dashboard reads the CSV files in `data/` and calculates KPIs at runtime. KPI definitions and denominators are documented in [methodology.md](methodology.md). Dates are ISO-formatted. The sample includes monthly snapshots to illustrate trends; snapshots are illustrative and are not historical operational records.

- [Risk register](data/risk-register.csv)
- [Remediation actions](data/remediation-actions.csv)
- [Control status](data/control-status.csv)
- [Methodology and KPI definitions](methodology.md)
- [Management report](reports/management-report.md)
- [KPI calculation tests](tests/test_kpi_calculations.py)

## Interpretation safeguards

- The dataset is fictional and must not be represented as an actual organization assessment.
- Risk trends are based on sample monthly snapshots, not measured organizational history.
- "Effective" is only a sample status; a real dashboard must link status to dated, scoped test evidence and approval.
- Overdue means an action is open and its due date is earlier than the dashboard's reporting date.
- SLA compliance is calculated only for closed actions with both opened and closed dates.
- KPI denominators are shown in the dashboard to prevent misleading percentages.
