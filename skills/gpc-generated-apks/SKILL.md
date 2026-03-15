---
name: gpc-generated-apks
description: Use when inspecting or downloading generated APKs for a bundle upload with gpc, especially for post-processing checks and CI artifact validation.
---

# gpc Generated APKs

## Overview

Use this skill after bundle processing when you need to inspect generated APK artifacts or download them.

## Workflow

1. Wait for bundle processing if needed.
   Use `gpc bundles wait --package-name com.example.app --version-code 123456`.
2. Inspect generated APK metadata.
   Use `gpc generated-apks list --package-name com.example.app --version-code 123456`.
3. Download a specific generated APK when validation or distribution requires it.
   Use `gpc generated-apks download --package-name com.example.app --version-code 123456 --download-id <download-id> --output ./generated.apk`.

## Notes

- Generated APK downloads are bundle-version specific.
- Use JSON output when another pipeline step extracts `downloadId`.
