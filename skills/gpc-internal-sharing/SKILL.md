---
name: gpc-internal-sharing
description: Use when uploading an app bundle or APK to Google Play internal app sharing with gpc for quick tester distribution and smoke validation.
---

# gpc Internal Sharing

## Overview

Use this skill for rapid tester distribution outside the full release-track flow.

## Workflow

1. Build the binary you want to share.
2. Upload it to internal sharing.
   Use `gpc internal-sharing upload --package-name com.example.app --file ./app.aab`.
3. Capture the returned sharing URL and pass it to testers or downstream automation.

## Notes

- Use this flow for quick validation, not as a replacement for staged rollout controls.
- Keep the returned URL in machine-readable output if another system consumes it.
