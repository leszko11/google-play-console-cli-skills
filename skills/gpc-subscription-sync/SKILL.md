---
name: gpc-subscription-sync
description: Use when creating or updating Play subscriptions from manifests with gpc, especially for base plans, offers, activation, and dry-run review.
---

# gpc Subscription Sync

## Overview

Use this skill when subscription resources should be managed declaratively.

## Workflow

1. Preview the subscription plan first.
   Use `gpc subscriptions sync --package-name com.example.app --manifest ./subscription.yaml --dry-run`.
2. Review whether base plans, listings, and offers match expectations.
3. Apply the sync after review.
   Use `gpc subscriptions sync --package-name com.example.app --manifest ./subscription.yaml --confirm`.
4. If the workflow includes activation, make that explicit in the command and in PR review notes.

## Notes

- Keep subscription manifests in source control.
- Use this skill instead of ad hoc console changes for repeatable billing configuration.
