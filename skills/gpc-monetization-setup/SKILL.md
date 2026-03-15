---
name: gpc-monetization-setup
description: Use when creating or syncing subscriptions and one-time products in Google Play with gpc, especially for manifest-driven monetization rollout and dry-run review.
---

# gpc Monetization Setup

## Overview

Use this skill to create or update monetization resources from manifests instead of manual console edits.

## Workflow

1. Preview monetization changes first.
   Use `gpc monetization setup --package-name com.example.app --manifest ./subscription.yaml --dry-run`.
2. Sync an existing subscription definition with activation when ready.
   Use `gpc monetization sync --package-name com.example.app --manifest ./subscription.yaml --dry-run --activate`.
3. For one-time products, keep the same dry-run-first pattern.
   Use `gpc products sync --package-name com.example.app --input ./products.json --dry-run`.
4. For subscription-focused repos, use the dedicated command family when it fits better.
   Use `gpc subscriptions sync --package-name com.example.app --manifest ./subscription.yaml --dry-run`.

## Notes

- Keep manifests in version control.
- Use dry-run output as the review artifact in PRs and CI.
