---
name: gpc-release-verify
description: Use when preflighting a Google Play release with gpc, especially for AAB readiness, notes validation, metadata checks, and non-mutating CI gates.
---

# gpc Release Verify

## Overview

Use this skill to block bad release inputs before any upload or commit path begins.

## Workflow

1. Verify the release artifact and notes before a real deploy.
   Use `gpc release verify --package-name com.example.app --aab ./app.aab --notes-text "Bug fixes"`.
2. Use this command as the CI safety gate before:
   - `gpc release alpha`
   - `gpc release full`
   - any workflow step that depends on a valid AAB and release metadata
3. Treat verification failures as input problems to fix locally, not retriable API incidents.

## Notes

- This is the non-mutating preflight layer for release automation.
- Pair it with `gpc-release-flow` in release pipelines.
