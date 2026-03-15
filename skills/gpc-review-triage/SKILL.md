---
name: gpc-review-triage
description: Use when monitoring, grouping, and replying to Google Play user reviews with gpc, especially for support queues and release-quality feedback loops.
---

# gpc Review Triage

## Overview

Use this skill to convert incoming Play reviews into an actionable support or release feedback queue.

## Workflow

1. Pull the current review list.
   Use `gpc reviews list --package-name com.example.app --max-results 50`.
2. Group reviews into actionable buckets.
   Use `gpc reviews triage --package-name com.example.app`.
3. Inspect an individual review before replying.
   Use `gpc reviews get --package-name com.example.app --review-id <review-id>`.
4. Send a reply only after reading the original content and checking internal guidance.
   Use `gpc reviews reply --package-name com.example.app --review-id <review-id> --reply-text "Thanks for your feedback!"`.

## Best Practices

- Keep triage output in JSON if another tool will summarize or route it.
- Tie review spikes back to recent releases when investigating regressions.
