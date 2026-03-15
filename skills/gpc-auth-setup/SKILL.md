---
name: gpc-auth-setup
description: Use when provisioning or verifying gpc authentication, including service-account setup, profile switching, doctor checks, and package-access verification.
---

# gpc Auth Setup

## Overview

Use this skill for initial machine setup or when an environment loses Play Console access.

## Workflow

1. For one-shot environment setup, use the top-level setup flow.
   Use `gpc setup --auto --project-id play-prod --package-name com.example.app --dir ./play`.
2. For direct profile initialization, use auth init.
   Use `gpc auth init --service-account /path/to/service-account.json --profile default`.
3. Inspect the current active profile.
   Use `gpc auth status`.
4. List or switch profiles when debugging identity mismatches.
   Use `gpc auth profiles list --output table`.
5. Run a local diagnostic when the issue might be credentials, package access, or environment state.
   Use `gpc doctor --package-name com.example.app`.

## Notes

- Prefer service accounts for CI.
- Keep `GPC_DEFAULT_OUTPUT=json` in automation for stable parsing.
