# PCI DSS Readiness Assessment Methodology

## 1. Purpose

This methodology organizes a simulated readiness review using PCI DSS v4.0.1 as the reference baseline. It does not replace the PCI DSS standard, its testing procedures, PCI SSC guidance, acquirer instructions or advice from a QSA.

## 2. Start with scope

Before control testing, document:
- Payment channels and transaction flows
- Whether account data is stored, processed or transmitted by the organization
- CDE system components and connected systems
- Systems that can impact CDE security
- Segmentation boundaries and evidence that segmentation is effective
- Third-party payment, hosting, security and service-provider responsibilities
- Locations, people, processes, cloud accounts and network connections
- Applicable validation route (for example, SAQ or ROC) as confirmed with the acquirer and relevant parties

Scope is not determined only by whether a system stores PAN. Connected systems and systems that can impact the security of the CDE may also be relevant. Segmentation reduces scope only when it is properly designed and validated.

## 3. Control mapping fields

For each requirement area, record: requirement reference; applicability; control objective; system/process owner; evidence requested; evidence period; test procedure; result; gap reference; remediation; retest result; reviewer and approval. The CSV matrix uses selected requirement references and does not reproduce the full standard.

## 4. Assessment results

- **Pass:** documented criteria were met by sufficient, relevant evidence.
- **Fail:** evidence demonstrates that the criteria were not met.
- **Partial:** some criteria were met but coverage or operation was incomplete.
- **Not Tested:** evidence or authorization is insufficient.
- **Not Applicable:** a documented applicability rationale is reviewed and approved; use only where allowed under PCI DSS rules.

A missing evidence item should normally remain Not Tested or be recorded as an evidence gap until the assessment can determine the actual control condition. Do not automatically convert absence of evidence into a confirmed technical failure.

## 5. Gap severity

Use the illustrative prioritization categories in the gap register:
- **Critical:** plausible direct exposure of account data or a major failure in a foundational control; urgent management escalation.
- **High:** significant control weakness with material potential to affect CDE security.
- **Medium:** meaningful weakness with limited scope or mitigating controls requiring validation.
- **Low:** documentation, consistency or lower-impact issue that still requires accountable treatment.

These labels are portfolio prioritization aids, not official PCI DSS severity ratings. Real severity should be aligned to the organization's risk method, actual evidence and applicable obligations.

## 6. Evidence handling

For every item, record source, timestamp/date, system scope, period covered, custodian, collection method, integrity, completeness, reviewer and finding reference. Use redacted configuration exports, approved screenshots, change tickets, access review records, scan reports and test records as appropriate. Do not include real cardholder data or sensitive authentication data in the portfolio.

## 7. Remediation and retesting

Each action must have an accountable owner, priority, target date, dependencies and closure criteria. A remediation is not closed merely because a ticket is marked complete. Retest the control, preserve safe evidence, confirm scope and exceptions, reassess risk, and obtain authorized approval.

## 8. Third-party responsibilities

Document which PCI DSS responsibilities are performed by the merchant and which by service providers. Obtain relevant service-provider compliance evidence and confirm its scope, services, dates and responsibility allocation. A provider's AOC does not automatically demonstrate that the merchant's own controls or integration are compliant.

## 9. Compensating controls and customized approach

Do not label a workaround a compensating control without following the PCI DSS requirements and documentation process. Where a customized approach is considered, follow the current PCI DSS guidance and appropriate assessor/acquirer process. This portfolio does not make applicability decisions or validate compensating controls.

## 10. Reporting caveat

The project is a simulated readiness exercise. It cannot support an assertion of PCI DSS compliance, an AOC, ROC, SAQ completion or formal assessment conclusion.
