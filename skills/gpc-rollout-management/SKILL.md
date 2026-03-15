---
name: gpc-rollout-management
description: Use when promoting, halting, rolling back, or diffing track releases in Google Play with gpc, especially around staged rollouts and production safety.
---

# gpc Rollout Management

## Overview

Use this skill when rollout state needs to change after the initial upload.

## Workflow

1. Inspect current live track state first.
   Use `gpc tracks get --package-name com.example.app --track production`.
2. Preview desired release differences before mutating the track.
   Use `gpc diff track --package-name com.example.app --track production --status inProgress --version-codes 123456`.
3. Promote between tracks safely with a dry run first.
   Use `gpc release promote --package-name com.example.app --from-track internal --to-track production --dry-run`.
4. Halt or roll back only with explicit confirmation.
   Use `gpc rollback --package-name com.example.app --track production --confirm`.

## Use Cases

- staged rollout progression
- emergency rollout halt
- promotion review between testing and production tracks
- live state inspection during incidents
