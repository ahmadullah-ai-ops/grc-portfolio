# Illustrative AWS Architecture and Trust Zones

## Status

This is a conceptual target architecture for the simulated Northstar Retail Cloud case study. It is not evidence of a deployed AWS environment.

## Logical flow

```text
Internet users
     |
     v
Public entry layer (e.g., CDN/WAF/load balancer as appropriate)
     |
     v
Public subnets: only explicitly required ingress components
     |
     v
Private application subnets
     |
     v
Private data subnets (database access restricted to approved app tier)

Administrators --> approved identity federation / MFA --> controlled admin role
AWS account services --> audit logging --> protected central log destination
Configuration inventory --> AWS Config / security findings --> triage and remediation
Infrastructure-as-code --> review / approval --> controlled deployment pipeline
```

## Trust zones and design intent

| Zone | Intended assets | Primary control intent |
|---|---|---|
| Public entry | Publicly reachable entry components only | Limit exposure; allow only required inbound paths |
| Application | Application services in private subnets where practical | Permit only approved ingress from the entry tier and required egress |
| Data | Databases and sensitive data services | No direct internet exposure; restrict access to approved application identities and paths |
| Administration | Human and automation administrative identities | Strong authentication, least privilege, short-lived access where feasible, monitored actions |
| Audit/logging | CloudTrail and other security logs, protected destination | Centralized collection, restricted modification/deletion, defined retention and monitoring |
| Deployment | Source control, CI/CD and infrastructure-as-code | Peer review, protected secrets, controlled roles and traceable changes |

## Key design questions

1. Which components must be publicly reachable, and why?
2. Can the database tier be reached only from approved application resources?
3. Are administrative paths separate from normal application traffic?
4. Are security groups based on required source identities or security groups rather than broad ranges where feasible?
5. Are management events collected across the intended accounts and regions?
6. Can workload operators modify or delete the logs they are expected to be monitored by?
7. Is configuration drift detected and assigned to an accountable owner?
8. Are exceptions documented with business justification, approver and expiry?

## Evidence needed to validate the design

- Current architecture and data-flow diagram
- VPC, subnet, route-table and security-group exports
- Load balancer and public endpoint configuration
- IAM role trust policies and permission policies
- CloudTrail coverage and destination configuration
- AWS Config recording status, resource coverage and rules
- Change-management records and infrastructure-as-code review evidence

## Security note

Do not publish live account IDs, access keys, session tokens, private customer information, or sensitive network details. If lab screenshots or exports are added, redact identifiers and label the evidence as generated in a personal lab.
