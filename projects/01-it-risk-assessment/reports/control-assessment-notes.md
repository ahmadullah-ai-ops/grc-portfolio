# Control Assessment Notes

## Assessment status

This workpaper is a planning-level demonstration. No actual system evidence has been collected or tested. Therefore, the controls below should be treated as **not yet validated**; illustrative status labels must not be represented as audit conclusions.

## Illustrative assessment questions

### Access control and MFA
- Is access provisioned from an approved request?
- Are privileged roles limited to business need?
- Are emergency accounts controlled and reviewed?
- Does technical configuration enforce MFA for all in-scope privileged accounts?
- Are exceptions approved, time-bound and monitored?

### Network segmentation
- Are trust zones and data flows documented?
- Are security-group/firewall rules limited to required paths?
- Are administrative interfaces restricted?
- Are network-rule changes approved and periodically reviewed?

### Vulnerability management
- Are assets and scan coverage complete?
- Are findings prioritized using severity and business context?
- Are remediation SLAs approved and tracked?
- Are overdue findings escalated or formally accepted?

### Logging and monitoring
- Are critical systems sending relevant logs to a central location?
- Are retention and access restrictions defined?
- Are alerts tested and reviewed?
- Are logging failures detected?

### Backup and recovery
- Are backup jobs monitored?
- Are restoration tests performed?
- Do observed recovery times meet approved RTO/RPO?
- Are failures tracked to closure?

### Third-party risk
- Are vendors tiered by business criticality and data access?
- Is due diligence proportionate to risk?
- Are contractual security obligations defined?
- Are material changes and reassessments tracked?

### Secure development and secrets
- Are code review and security checks integrated into the delivery process?
- Are exceptions approved?
- Are secrets scanned, stored securely and rotated?
- Are production credentials excluded from public repositories and portfolio artifacts?

## Evidence evaluation checklist

For every evidence item, record the source, owner, date, scope, period covered, completeness, integrity, test performed, result, exceptions and reviewer. Redact personal data and never publish credentials, tokens, private IP details that create exposure, or confidential configuration.

## Conclusion discipline

Use “not assessed” where evidence is unavailable. Distinguish between a missing control, missing evidence and an ineffective control. These are different findings and require different remediation.
