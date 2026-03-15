---
name: gpc-changelog-sync
description: Use when syncing localized release notes from a directory into Google Play with gpc, especially for track-based changelog updates, fallback behavior, and dry-run review.
---

# gpc Changelog Sync

## Overview

Use this skill when release notes live in files and should be applied consistently across locales.

## Workflow

1. Keep release notes in a versioned directory structure.
2. Preview changelog changes before mutating Play.
   Use `gpc changelog sync --package-name com.example.app --track production --dir ./changelogs --dry-run`.
3. Apply the changelog only after reviewing the plan.
   Use `gpc changelog sync --package-name com.example.app --track production --dir ./changelogs --confirm`.
4. Use fallback behavior deliberately when some locales should inherit a shared default.
   Prefer the existing fallback patterns already supported by `gpc`.

## Notes

- Pair this flow with `gpc-release-flow` if changelog sync is part of a full release pipeline.
- Keep notes concise enough for Play Store limits before the sync step.
