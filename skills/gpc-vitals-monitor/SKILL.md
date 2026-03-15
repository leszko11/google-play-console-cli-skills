---
name: gpc-vitals-monitor
description: Use when monitoring Play Developer Reporting vitals after a release, especially for crash and ANR thresholds, freshness checks, and release gating decisions with gpc.
---

# gpc Vitals Monitor

## Overview

Use this skill to inspect vitals readiness before rollout, then monitor regressions after shipping.

## Workflow

1. Check freshness for the metric set you care about.
   Use `gpc reports vitals get --package-name com.example.app --metric-set crash-rate`.
2. Query rows when you need actual values over a time window.
   Use `gpc reports vitals query --package-name com.example.app --metric-set crash-rate --input ./crash-rate-query.json`.
3. Gate a release directly when the rollout should halt on bad metrics.
   Use `gpc release full --package-name com.example.app --manifest ./release.yaml --confirm --vitals-gate 'crashRate<2.0,anrRate<0.5' --vitals-wait 24h --auto-halt-on-regression`.
4. Summarize health alongside other reporting signals when needed.
   Use `gpc reports summary --package-name com.example.app`.

## Best Practices

- Treat freshness metadata and threshold values separately.
- Keep threshold expressions explicit in CI logs and workflow files.
- Use JSON output for downstream alerting or dashboards.
