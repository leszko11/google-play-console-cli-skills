---
name: gpc-diff-review
description: Use when reviewing local-vs-live listing or track changes with gpc before mutating Google Play, especially for human review in PRs and dry-run workflows.
---

# gpc Diff Review

## Overview

Use this skill whenever local files or release parameters should be compared against live Play state first.

## Workflow

1. Review listing changes from a local directory.
   Use `gpc diff listing --package-name com.example.app --dir ./play/listing`.
2. Review a draft track release before promote or update steps.
   Use `gpc diff track --package-name com.example.app --track production --status inProgress --version-codes 123456`.
3. Use JSON output for automated review comments and table output for terminal review.

## Notes

- Treat diff output as a review artifact, not the mutation step.
- Pair this skill with `gpc-listing-sync` or `gpc-rollout-management` depending on the resource type.
