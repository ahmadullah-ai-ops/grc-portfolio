# Third-Party Risk Management Methodology

## 1. Purpose

This methodology provides a risk-based workflow for assessing vendors before onboarding and throughout the relationship. Adapt it to the organization's risk appetite, procurement process, contractual commitments and applicable laws/regulations.

## 2. Intake and classification

Collect vendor legal identity, service owner, business purpose, service description, business criticality, data categories, data subjects, hosting/data locations, integrations, privileged access, subcontractors, recovery dependencies, contract term and planned go-live date.

Classify the vendor using at least:
- Data sensitivity and volume
- System access and privilege
- Business criticality and substitutability
- Internet exposure and integration complexity
- Regulatory/contractual impact
- Concentration and fourth-party dependencies
- Availability and recovery requirements

Do not use spend alone as a proxy for cyber or operational risk.

## 3. Inherent risk scoring

Rate each factor from 1 to 5:
1 = Low, 2 = Limited, 3 = Moderate, 4 = High, 5 = Very High.

Illustrative factors: data sensitivity, access/privilege, business criticality, integration/exposure, regulatory impact, resilience dependency and fourth-party concentration. Calculate the arithmetic mean. Example bands:
- 1.00-1.79: Low
- 1.80-2.59: Moderate
- 2.60-3.39: High
- 3.40-5.00: Critical

These thresholds are a sample policy, not a universal standard. An organization may instead use weighted scoring or mandatory criticality overrides. Document the method and use it consistently.

## 4. Due diligence and evidence validation

Questionnaire responses are assertions until supported. Request relevant evidence, confirm its date and scope, identify exceptions and determine whether it covers the actual service. Evidence may include a suitably scoped independent assurance report, security certification, penetration-test executive summary, vulnerability management process, incident response plan, recovery test summary, access-control standards, privacy/data processing terms, subcontractor list and secure deletion process.

A SOC 2 report and ISO certificate have different scopes and purposes. Review period, exceptions, complementary user-entity controls, subservice organizations, qualified opinions and remediation plans where applicable. Do not upload restricted reports to a public repository.

## 5. Control effectiveness

For each control, record:
- Design: would the control address the identified risk if implemented?
- Implementation: is it in place for this service and scope?
- Operating evidence: is there sufficient evidence it operated during the relevant period?
- Exceptions: what gaps, carve-outs or limitations apply?
- Confidence: how reliable and current is the evidence?

Use labels such as Effective, Partially Effective, Ineffective, Not Evidenced or Not Applicable with a rationale. Missing evidence should not automatically be described as a confirmed control failure; record it as an evidence limitation or unresolved risk.

## 6. Residual risk

Residual risk is the remaining risk after considering validated controls and planned/implemented treatments. For this sample, assign a residual rating from 1 to 5 with a written rationale. Do not mechanically subtract control scores unless the organization has a formally approved calibrated model. Risk acceptance belongs to an authorized business risk owner, not solely to the assessor.

## 7. Findings and remediation

Each finding should include ID, risk statement, evidence reference, affected service, likelihood/impact rationale, severity, accountable owner, due date, treatment, dependencies, status and closure evidence. Define measurable closure criteria and independently retest material remediation.

## 8. Monitoring and reassessment

Use risk-based cadence, for example:
- Critical: continuous alerting where feasible; formal review at least quarterly or more often if policy requires.
- High: quarterly monitoring and at least annual formal reassessment.
- Moderate: semiannual monitoring and annual or risk-based reassessment.
- Low: annual or event-driven review.

These are illustrative starting points, not mandatory universal intervals. Contract terms, regulation, incidents or organizational policy may require different timing. Trigger reassessment after a major incident, ownership change, new data category, material service change, new subcontractor, assurance lapse, significant vulnerability, contract renewal or material performance deterioration.

## 9. Contractual and exit controls

Before approval, assess security obligations, permitted data use, encryption, access restrictions, incident notification timelines, cooperation, audit/assurance rights, subcontractor approval/notice, data location, continuity/recovery, vulnerability remediation, records retention, deletion/return, transition assistance and termination rights.

At exit, disable accounts and tokens, revoke connections, retrieve business records, verify data return/deletion where contractually appropriate, resolve retained copies/backups, transfer service ownership and document residual dependencies.

## 10. Decision governance

Set explicit decision gates: no production access before required approvals and critical conditions are met; conditional approvals must have an owner, due date and expiry; exceptions require documented rationale and authorized acceptance; overdue critical findings are escalated. Procurement, legal, privacy, information security, business ownership and continuity teams should participate according to service risk.
