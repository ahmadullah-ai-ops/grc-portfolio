# Methodology — GRC Reporting Dashboard

## Reporting date and data lineage

The sample reporting date is 2026-10-23. All rows are synthetic. Risk trend records are monthly snapshots of a fictional register; they are not claims about real performance. Production use should include source system, extraction timestamp, record owner, last-updated timestamp, and lineage for each dataset.

## KPI definitions

1. **Open risks by severity:** count distinct risk IDs in the latest snapshot where status is not Closed.
2. **High/critical risk trend:** count open High and Critical risks by snapshot month. A trend requires comparable scope and consistent rating criteria.
3. **Overdue remediation actions:** count actions not Closed/Verified whose due date is earlier than reporting date. Also report overdue days per action.
4. **Control effectiveness distribution:** counts and percentages for Effective, Partially Effective, Ineffective and Not Tested. Report Not Tested separately; never treat it as effective.
5. **Remediation SLA compliance:** closed actions closed within the configured target (30 calendar days in this sample) divided by all closed actions with valid opened/closed dates. Open actions are excluded from this historical closure-rate denominator and are separately reported as overdue.
6. **Risk closure rate:** risks marked Closed in the latest snapshot divided by all risks in that snapshot. In a production dataset, ensure one row per risk per snapshot and report scope.
7. **Evidence freshness:** controls with evidence review dates older than 365 days or no evidence review date should be flagged. The sample dashboard highlights evidence age/status but does not infer effectiveness from evidence freshness alone.

## Sample rating and status conventions

Risk ratings are Low, Moderate, High and Critical. Control statuses are Effective, Partially Effective, Ineffective and Not Tested. Remediation statuses are Open, In Progress, Blocked, Closed and Verified. Teams must formally define rating thresholds and status transitions before operational use.

## Governance and quality checks

- Validate unique identifiers and required fields.
- Reject invalid dates and unknown status labels rather than silently coercing them.
- Keep numerator and denominator visible for each percentage.
- Prevent double-counting when joining risk, action and control records.
- Preserve closed/verified actions for SLA calculation while excluding them from overdue counts.
- Reconcile dashboard totals to source exports and retain a dated snapshot.
- Restrict access to sensitive risk and vendor information; use aggregation for executive views.

## Limitations

This is a portfolio prototype, not a production GRC platform. It has no authentication, authorization, audit log, workflow approvals, database, or live integrations. Synthetic data and test results do not establish actual control effectiveness.
