# Project 03: PCI DSS-Aligned Compliance Assessment

**Project type:** Simulated payment-card security compliance case study  
**Target roles:** GRC Analyst · IT Risk Analyst · Cybersecurity Compliance Specialist  
**Reference baseline:** PCI DSS v4.0.1  
**Core work:** Scope definition, control mapping, evidence requests, gap analysis, remediation tracking and executive reporting

> **Important disclosure:** This is a simulated portfolio exercise, not a Qualified Security Assessor (QSA) assessment, Report on Compliance (ROC), Self-Assessment Questionnaire (SAQ), Attestation of Compliance (AOC), or claim of PCI DSS compliance. No real cardholder data environment (CDE) was assessed. Requirement applicability and validation method depend on the actual environment, payment channels, scope and applicable PCI SSC guidance.

## 1. Business scenario

A fictional online retailer, **Northstar Retail**, accepts payment cards through an e-commerce checkout. Its payment flow may involve a hosted payment page or a payment service provider, but the exact integration and resulting scope must be confirmed before any real assessment. The retailer wants to organize its PCI DSS readiness work, identify evidence owners, record potential gaps, and prioritize remediation.

For this portfolio exercise, the organization and all observations are fictional. Gap statuses are **illustrative hypotheses**, not verified deficiencies.

## 2. Objectives

- Define the initial CDE and connected-system scoping questions.
- Map selected PCI DSS v4.0.1 requirement areas to control objectives and evidence.
- Build a structured evidence request list and gap register.
- Prioritize corrective actions using business impact and exposure.
- Define closure evidence and retesting criteria.
- Communicate assumptions, responsibilities and limitations to management.

## 3. Scope and scoping caveat

Potentially relevant assets include payment pages and integrations, systems that store/process/transmit account data, systems connected to or that can impact the security of the CDE, administrative identities, network security controls, endpoint/server configurations, logging, vulnerability management, change management, service providers and documented policies.

**Do not assume that using a third-party payment processor automatically removes the merchant from PCI DSS scope.** Scope depends on payment flow, integration, systems that can affect payment security, segmentation, service-provider responsibilities and the applicable validation path. Confirm scope with the acquirer/payment brands and a QSA where appropriate.

### Out of scope for this simulated exercise
- Processing or storing real Primary Account Numbers (PAN), sensitive authentication data, or any real cardholder data
- Penetration testing of real systems
- Formal compliance validation or legal advice
- Issuing a ROC, SAQ, AOC or compliance certification
- Declaring requirements not applicable without a documented, approved applicability rationale

## 4. Assessment workflow

1. Confirm payment channels, data flows, CDE boundaries and third-party responsibilities.
2. Identify in-scope systems, people, processes and network paths.
3. Select the appropriate PCI DSS validation path and applicable requirements.
4. Request evidence with owner, source, date, scope and period covered.
5. Evaluate control design, implementation and operating evidence.
6. Record each item as Pass, Fail, Partial, Not Tested or Not Applicable with rationale.
7. Record gaps and compensating-control considerations only where permitted and properly documented.
8. Assign risk-based remediation, due dates and accountable owners.
9. Retest fixes and obtain authorized approval for residual-risk or exception decisions.
10. Prepare a readiness summary that distinguishes evidence from assumptions.

## 5. Deliverables

- [Methodology and scoping guide](methodology.md)
- [Control mapping matrix](workpapers/pci-control-mapping.csv)
- [Evidence request list](workpapers/pci-evidence-request-list.csv)
- [Illustrative gap register](workpapers/pci-gap-register.csv)
- [Remediation tracker](workpapers/pci-remediation-tracker.csv)
- [Assessment test plan](workpapers/pci-assessment-test-plan.csv)
- [Executive summary](reports/executive-summary.md)

## 6. Coverage represented in this sample

The mapping covers selected requirement areas, including network security controls, secure configurations, protection of stored account data, encryption in transmission, malware protection, secure development, access control, authentication, physical security, logging and monitoring, security testing, policies, risk analysis and third-party service-provider management. It is a **selected readiness sample**, not an exhaustive mapping of every PCI DSS requirement and testing procedure.

## 7. Evidence quality rules

A policy alone does not prove that a control is implemented or operating. Each evidence item should identify its source, collection date, environment/scope, relevant review period, owner, completeness, reviewer, test performed and exceptions. Never upload real PAN, sensitive authentication data, passwords, API keys, private certificates, or unredacted production configuration to a public repository.

## 8. Status and limitations

This initial package provides the assessment structure and illustrative workpapers. **No organization has been assessed and no evidence has been collected or tested.** Gap entries are clearly marked as illustrative. Replace them with evidence-based results only after authorized review.

## 9. Success criteria

- Scope and payment flows are documented and approved.
- Each applicable requirement area has an owner and evidence plan.
- Gaps are traceable to requirements, evidence and business impact.
- Remediation actions have due dates and measurable closure criteria.
- Retesting is documented and residual risk is escalated appropriately.
- Reports avoid unsupported claims of compliance.
