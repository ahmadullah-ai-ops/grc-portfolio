# AWS Cloud Security Assessment Methodology

## 1. Purpose and limitations

This method supports a simulated risk-based review of AWS IAM, VPC segmentation, logging and configuration controls. It is not an AWS security certification, penetration test, formal audit opinion or substitute for an organization's approved policies.

## 2. Assessment context

Before testing, record:
- AWS account/environment identifier in a private workpaper (redact from public output)
- In-scope regions and services
- Workload purpose and criticality
- Data classification and regulatory obligations
- Asset and identity owners
- Assessment period and evidence collection date
- Approved risk criteria and risk appetite
- Shared-responsibility boundaries
- Authorizations and exclusions

## 3. Risk statement structure

Use: **Because of [condition], [event] could occur, leading to [business impact].**

Example: If privileged IAM policies grant broader permissions than required, compromised credentials or operator error could enable unauthorized resource changes, data exposure or service disruption.

## 4. 5×5 scoring model

Score likelihood and impact from 1 to 5. Inherent risk = likelihood × impact.

| Score | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–15 | High |
| 16–25 | Critical |

Likelihood and impact definitions should be approved by the organization. The thresholds here are illustrative. A numeric score is a prioritization aid, not a precise prediction of loss.

## 5. Control assessment

Evaluate:
- **Design:** Would the control, if implemented as described, address the risk?
- **Implementation:** Is the control configured or adopted in the stated scope?
- **Operating effectiveness:** Does reliable evidence show that it operates consistently over the review period?

Use these test result values:
- **Pass:** test criteria met and evidence is sufficient.
- **Fail:** evidence demonstrates that criteria are not met.
- **Partial:** some criteria met but coverage or operation is incomplete.
- **Not Tested:** evidence, authorization or scope is insufficient.
- **Not Applicable:** applicability is documented and approved.

Never infer a Pass from service availability, a policy statement or an evidence request alone.

## 6. Evidence quality

For every evidence item, record source, collection date, scope, period covered, owner, completeness, integrity, test performed, result, exception and reviewer. Prefer read-only exports or configuration evidence from the relevant AWS service. Redact secrets, tokens, personal data and sensitive identifiers before publishing.

## 7. Control domains and evidence examples

### IAM and least privilege
Potential sources include IAM policy and role configuration, IAM Access Analyzer findings, credential/MFA configuration for human users, access review records, permission-boundary or organization guardrail documentation where used, and approved access requests. Interpret results in context; no single tool output proves least privilege across the environment.

### VPC segmentation
Potential sources include VPC/subnet/route tables, security-group rules, network ACLs, load balancer exposure, VPC endpoints and architecture/data-flow diagrams. Assess effective paths and intended trust boundaries, not just individual rule lists.

### Logging and monitoring
Potential sources include CloudTrail organization/account and region coverage, trail configuration, log validation and destination permissions, retention controls, CloudWatch alarms, log-source inventory, alert tests and incident/ticket records. Verify the actual scope and destinations.

### Configuration and drift
Potential sources include AWS Config recorder/status and resource coverage, configuration rules or conformance packs, Security Hub findings if enabled, approved baselines, infrastructure-as-code review, change tickets and exception approvals. A finding count alone does not establish risk or control effectiveness.

## 8. Risk treatment

- Mitigate: reduce likelihood and/or impact.
- Avoid: stop the activity creating the exposure.
- Transfer/share: allocate part of the financial exposure, without eliminating accountability.
- Accept: obtain documented approval from an authorized risk owner within risk appetite.

## 9. Residual risk and closure

Residual risk must be reassessed after remediation and control validation. Close a finding only when the fix is implemented, evidence is attached or referenced, a repeat test passes, exceptions are documented, residual risk is reviewed and the authorized owner approves closure.

## 10. Reference mapping

Use the AWS Well-Architected Framework Security Pillar and relevant NIST CSF 2.0 outcomes as organizing references. ISO/IEC 27001:2022 Annex A references are indicative and must be checked against the authoritative standard and organizational Statement of Applicability. Mapping is not proof of compliance.
