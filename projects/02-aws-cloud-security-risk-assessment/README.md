# Project 02 — AWS Cloud Security Risk & Control Assessment

**Project type:** Simulated AWS GRC case study with a lab-validation plan  
**Target roles:** GRC Analyst · IT Risk Analyst · Cloud Security Compliance Specialist  
**Assessment domains:** IAM and least privilege, VPC segmentation, logging and monitoring, secure configuration and change control  
**References:** AWS Well-Architected Framework — Security Pillar; AWS shared responsibility model; NIST CSF 2.0 concepts; selected ISO/IEC 27001:2022 Annex A references

> **Disclosure:** This is a simulated portfolio assessment. No production AWS account was accessed, no real organization was assessed, and no control is claimed to be effective without evidence. The architecture and findings are illustrative. Lab evidence can be added later and must be labelled separately.

## 1. Business scenario

A fictional company, **Northstar Retail Cloud**, runs an e-commerce workload on AWS. The environment includes a public-facing application, private application services, a database tier, administrative access, centralized audit logging and infrastructure-as-code deployment.

Management wants to understand whether the design and operating procedures reduce risks relating to excessive permissions, unintended network exposure, insufficient audit visibility and insecure or drifting cloud configuration.

## 2. Objectives

1. Identify material cloud security risks and express them as business risk statements.
2. Define control objectives and map risks to relevant AWS capabilities and governance references.
3. Specify evidence required to assess control design and operating effectiveness.
4. Build a test plan with procedures, expected results and exception criteria.
5. Prioritize remediation and define closure evidence.
6. Communicate limitations and management decisions in an executive summary.

## 3. Scope

### In scope
- IAM users, roles, policies, privileged access and access review
- MFA for human privileged access and secure administrative access
- VPC trust zones, public/private subnet design, security groups and network ACLs where applicable
- CloudTrail management-event logging, log protection and retention
- CloudWatch monitoring and alerting for selected security events
- AWS Config configuration recording and compliance-rule evaluation, where enabled
- Secure baselines, change management, configuration drift and infrastructure-as-code review
- Evidence ownership, exceptions, remediation and risk acceptance

### Out of scope
- Penetration testing or exploitation
- Actual production account configuration changes
- Formal AWS certification or independent audit opinion
- Full PCI DSS assessment or legal interpretation
- Workload-specific application testing beyond the defined control scope

## 4. Reference architecture

See [architecture and trust zones](architecture.md). The intended pattern is a public entry layer, private application and data layers, restricted administration, and centralized security logging. This is a conceptual target architecture, not a diagram of a deployed account.

## 5. Project deliverables

| Deliverable | Purpose |
|---|---|
| [Assessment methodology](methodology.md) | Risk scoring, control assessment, evidence and limitations |
| [Architecture and trust zones](architecture.md) | Illustrative AWS design and security boundaries |
| [AWS risk register](workpapers/aws-risk-register.csv) | Risk statements, inherent ratings and treatment |
| [AWS control assessment matrix](workpapers/aws-control-assessment-matrix.csv) | Control objectives, evidence and test approach |
| [Evidence request list](workpapers/aws-evidence-request-list.csv) | Evidence owner, request and validation notes |
| [Control test plan](workpapers/aws-control-test-plan.csv) | Repeatable tests and expected results |
| [Remediation tracker](workpapers/aws-remediation-tracker.csv) | Owners, priorities, target timelines and closure criteria |
| [Executive summary](reports/executive-summary.md) | Management priorities and decisions |

## 6. Assessment workflow

1. Confirm account, region, workload, data classification and shared-responsibility boundaries.
2. Inventory identities, network paths, audit sources and configuration-management coverage.
3. Score inherent risk using the documented 5×5 model.
4. Map each risk to a control objective and applicable AWS service or process.
5. Request evidence with source, date, scope and owner.
6. Execute the test plan only against an authorized lab or approved environment.
7. Record results as Pass, Fail, Partial, or Not Tested; preserve evidence references and exceptions.
8. Assign remediation owners and target dates.
9. Validate fixes and reassess residual risk.
10. Report results, assumptions and open decisions to management.

## 7. Key GRC principle

An AWS service being available or enabled does not prove a control is effective. For example, enabling CloudTrail does not by itself prove that all relevant accounts and regions are covered, logs are protected, retention is appropriate, or alerts are reviewed. Likewise, a security group that looks restrictive in isolation may still allow a risky path through another network route or attached resource.

## 8. How to reproduce safely

Use a dedicated sandbox account, non-production data and least-privilege test credentials. Do not expose access keys, account identifiers, customer data, public IPs that create risk, or unredacted configuration in a public repository. Prefer read-only inventory and configuration checks. Obtain authorization before running any tests.

## 9. Current status and limitations

This initial repository version contains a simulated scenario, risk hypotheses, evidence requests and test procedures. **No AWS account has been inspected and no test has been executed.** All assessment results remain Not Tested until supported by real, appropriately redacted lab evidence.

## 10. Success criteria

- Every material risk has an owner, control objective and treatment.
- Every control test has a reproducible procedure and expected result.
- Evidence is traceable, dated, scoped and redacted.
- Exceptions have owners and due dates.
- Remediation closure requires validation evidence.
- The executive report distinguishes confirmed observations from assumptions and untested areas.
