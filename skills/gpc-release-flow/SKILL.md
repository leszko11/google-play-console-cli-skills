---
name: gpc-release-flow
description: Use when shipping a Google Play release end to end with gpc, especially for staged rollouts, manifests, validation, waiting for generated APKs, and safe commit flows.
---

# gpc Release Flow

## Overview

Use this skill for the common release path: verify inputs, preview changes, deploy safely, and inspect the result.

## Workflow

1. Validate the release inputs first.
   Use `gpc release verify --package-name com.example.app --aab ./app.aab --notes-text "Bug fixes"`.
2. Prefer a manifest-driven release for repeatable CI.
   Use `gpc release full --package-name com.example.app --manifest ./release.yaml --dry-run` before any real commit.
3. Commit only with an explicit confirmation step.
   Use `gpc release full --package-name com.example.app --manifest ./release.yaml --confirm`.
4. If the artifact pipeline depends on bundle processing, wait for generated APK availability.
   Use `gpc bundles wait --package-name com.example.app --version-code 123456`.
5. Keep stdout machine-readable in automation.
   Prefer `--output json` or `GPC_DEFAULT_OUTPUT=json`.

## When To Use

- release trains
- staged rollout preparation
- CI/CD release jobs
- manifest review before shipping

## Notes

- Prefer `--dry-run` wherever available before `--confirm`.
- If rollout safety matters, pair this flow with `gpc-vitals-monitor`.
