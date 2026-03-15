---
name: gpc-product-sync
description: Use when managing one-time products in Google Play with gpc, especially for dry-run planning, JSON inputs, and repeatable sync operations.
---

# gpc Product Sync

## Overview

Use this skill for one-time product catalogs that should be updated from files instead of manual console changes.

## Workflow

1. Prepare the product input file in version control.
2. Preview the sync without mutation.
   Use `gpc products sync --package-name com.example.app --input ./products.json --dry-run`.
3. Apply the sync after review.
   Use `gpc products sync --package-name com.example.app --input ./products.json --confirm`.
4. If individual product inspection is needed, use the `gpc products` subcommands before or after sync.

## Notes

- Prefer JSON output when another tool needs to summarize product changes.
- Use this alongside `gpc-monetization-setup` when both subscriptions and one-time products ship together.
