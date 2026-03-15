---
name: gpc-workflow-authoring
description: Use when authoring or reviewing .gpc/workflow.yml pipelines for gpc, including variable interpolation, dependency ordering, dry-run planning, and captured step output.
---

# gpc Workflow Authoring

## Overview

Use this skill for repeatable `gpc` automation expressed as `.gpc/workflow.yml`.

## Workflow

1. Keep workflows limited to real shipped `gpc` commands.
2. Start with a dry-run plan.
   Use `gpc workflow run --file .gpc/workflow.yml --dry-run`.
3. Prefer `${var}` placeholders and override them from CI only when needed.
   Use `gpc workflow run --file .gpc/workflow.yml --dry-run --var packageName=com.example.app`.
4. Execute only after the plan output matches expectations.
   Use `gpc workflow run --file .gpc/workflow.yml --confirm`.

## Authoring Rules

- Give each step a stable `id`.
- Use `needs` for deterministic ordering.
- Keep each step command focused on one observable action.
- Favor JSON-producing commands for machine-consumable pipelines.
