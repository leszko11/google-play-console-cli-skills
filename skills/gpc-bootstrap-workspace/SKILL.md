---
name: gpc-bootstrap-workspace
description: Use when creating or refreshing a local Google Play workspace from live state with gpc, including app details, listings, changelogs, and project-local config defaults.
---

# gpc Bootstrap Workspace

## Overview

Use this skill to build a local working tree from live Play Console state before making changes.

## Workflow

1. Start with the top-level bootstrap flow.
   Use `gpc bootstrap --package-name com.example.app --dir ./play --write-project-config`.
2. Use `appinit export` when you need more control or a GPP-style layout.
   Use `gpc appinit export --package-name com.example.app --dir ./store --layout gpp`.
3. Preview local-vs-live changes before syncing back.
   Use `gpc diff listing --package-name com.example.app --dir ./play/listing`.
4. Keep `.gpc.yaml` as the project-local default source for package, profile, output, track, and locale.

## Notes

- Prefer the `gpc` layout for round-trip work inside this ecosystem.
- Use the exported workspace as the input for listing sync, changelog sync, and workflow manifests.
