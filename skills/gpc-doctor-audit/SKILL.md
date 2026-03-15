---
name: gpc-doctor-audit
description: Use when diagnosing gpc environment readiness, package access, fixture availability, and project defaults before deeper Play Console operations.
---

# gpc Doctor Audit

## Overview

Use this skill before blaming a downstream command when the real issue might be auth, package access, or local configuration.

## Workflow

1. Run the doctor check with the target package.
   Use `gpc doctor --package-name com.example.app`.
2. Read the output as a preflight report for:
   - auth state
   - package visibility
   - project defaults
   - fixture or environment readiness
3. If the issue is identity-related, switch to `gpc-auth-setup`.

## Notes

- Use this skill early in triage, not after several failing release attempts.
- Prefer JSON output in CI so the failure can be attached to logs or notifications.
