---
name: gpc-listing-sync
description: Use when syncing store listing metadata and images from a local directory with gpc, including dry-run review, delete-missing behavior, and diffing live state first.
---

# gpc Listing Sync

## Overview

Use this skill for round-trip local listing management.

## Workflow

1. Export or bootstrap a local listing workspace first.
   Use `gpc bootstrap --package-name com.example.app --dir ./play --write-project-config`.
2. Compare local content against live state before writing.
   Use `gpc diff listing --package-name com.example.app --dir ./play/listing`.
3. Run a dry-run listing sync.
   Use `gpc listing sync --package-name com.example.app --dir ./play/listing --dry-run`.
4. Apply only after reviewing the change plan.
   Use `gpc listing sync --package-name com.example.app --dir ./play/listing --confirm`.

## Notes

- Be explicit about `--delete-missing` because it changes destructive behavior.
- Keep image validation local before attempting API writes.
