# Project 04 — Third-Party Risk Management (TPRM)

**Project type:** Simulated vendor due diligence and ongoing monitoring case study  
**Target roles:** GRC Analyst · IT Risk Analyst · Vendor Risk Analyst · Cybersecurity Compliance Specialist  
**Core deliverables:** Vendor inventory, due diligence questionnaire, inherent/residual risk scoring, evidence checklist, findings register, remediation tracker and monitoring plan

> **Portfolio disclosure:** This is a simulated case study using a fictional vendor and illustrative scores. No real vendor has been assessed. Scores and risk decisions are examples, not verified findings or legal/compliance determinations.

## 1. Business scenario

A fictional company, **Northstar Retail**, plans to use **CloudCart Services**, a fictional SaaS provider that supports e-commerce operations. The service may process business data and integrate with identity and payment-related workflows. Before onboarding, Northstar needs to understand the vendor's security posture, data access, resilience, subcontractors and contractual responsibilities.

The exact data types, integrations and PCI DSS responsibilities must be confirmed during real due diligence. Do not assume the vendor stores or processes payment-card data merely because the merchant operates an online store.

## 2. Objectives

- Classify vendors by criticality, data sensitivity, access and business dependency.
- Perform risk-based pre-contract due diligence.
- Request and evaluate evidence instead of relying only on questionnaire answers.
- Calculate transparent inherent and residual risk scores.
- Document findings, risk owners, treatment plans and approval gates.
- Establish ongoing monitoring, reassessment triggers and exit planning.

## 3. Lifecycle

1. Intake and business justification.
2. Vendor classification and service/data-flow scoping.
3. Inherent risk assessment before considering vendor controls.
4. Due diligence questionnaire and evidence collection.
5. Independent evidence validation and control-gap analysis.
6. Residual risk assessment after evaluating controls.
7. Risk treatment, contractual safeguards and authorized approval.
8. Onboarding decision and access provisioning.
9. Ongoing monitoring, periodic reassessment and issue escalation.
10. Renewal, termination, data return/deletion and access revocation.

## 4. Deliverables

- [Methodology and scoring model](methodology.md)
- [Vendor inventory](workpapers/vendor-inventory.csv)
- [Due diligence questionnaire](workpapers/vendor-due-diligence-questionnaire.csv)
- [Risk scoring worksheet](workpapers/vendor-risk-scoring.csv)
- [Evidence request checklist](workpapers/vendor-evidence-checklist.csv)
- [Findings register](workpapers/vendor-findings-register.csv)
- [Remediation tracker](workpapers/vendor-remediation-tracker.csv)
- [Ongoing monitoring plan](workpapers/vendor-monitoring-plan.csv)
- [Executive summary](reports/executive-summary.md)

## 5. Scoring model

Each inherent risk factor is rated from 1 (low) to 5 (very high). The illustrative model calculates the average across factors and maps the result to Low, Moderate, High or Critical. Control effectiveness is evaluated separately, and residual risk is then estimated with documented rationale. Do not subtract an arbitrary control score and treat the result as objective truth; risk decisions require evidence, context and accountable approval.

## 6. Decision outcomes

- **Approve:** due diligence is sufficient and residual risk is within delegated tolerance.
- **Approve with conditions:** specified actions, contract terms or compensating safeguards must be completed by an agreed date.
- **Defer:** material evidence or remediation is outstanding before onboarding.
- **Reject:** risk exceeds tolerance or mandatory requirements cannot be met.
- **Reassess:** a material service, data, ownership, incident or control change requires renewed review.

## 7. Professional safeguards

- Use evidence that is current, in scope and relevant to the service.
- Validate the scope and date of certifications and independent assurance reports; do not treat a certificate as proof that every control is effective.
- Review subcontractors, data locations, incident notification, audit rights, business continuity, recovery, deletion and exit assistance.
- Share only redacted evidence; never commit credentials, customer data, confidential contracts or proprietary assurance reports to a public repository.
- Align assessment depth and reassessment frequency to risk, contractual obligations and applicable regulation.
- Record exceptions with a named risk owner, rationale, expiry date and approval.

## 8. Status and limitations

This repository contains a reusable TPRM workflow and fictional sample data. The example vendor's answers, control conditions and scores are illustrative only. No due diligence has been performed on a real provider and no actual onboarding decision is implied.
