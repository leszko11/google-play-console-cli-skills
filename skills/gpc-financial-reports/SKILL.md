---
name: gpc-financial-reports
description: Use when discovering or downloading Google Play financial reports from Cloud Storage with gpc, especially for normalized JSON, table, csv, or tsv outputs.
---

# gpc Financial Reports

## Overview

Use this skill when finance or operations workflows need Play earnings exports from Cloud Storage.

## Workflow

1. List available report objects first.
   Use `gpc reports financial list --bucket play_financial_reports --prefix earnings/`.
2. Download and normalize the desired object.
   Use `gpc reports financial get --gcs-uri gs://play_financial_reports/earnings/earnings_2026-03.csv --output json`.
3. Choose the output format for the downstream consumer:
   - `json` for automation
   - `table` for terminal review
   - `csv` or `tsv` for spreadsheet workflows

## Notes

- Keep the bucket and prefix explicit in automation.
- Treat Cloud Storage access failures separately from Play Console API issues.
