# google-play-console-cli-skills

Agent skills for [`gpc`](https://github.com/leszko11/google-play-console-cli) workflows.

This repo packages reusable Codex skills around shipped Google Play Console CLI capabilities: release flows, vitals monitoring, rollout management, monetization setup, review triage, workspace bootstrap, and workflow authoring.

## Install

Copy the desired skill directories into `$CODEX_HOME/skills`, or clone this repo and symlink individual directories from `skills/`.

```bash
git clone https://github.com/leszko11/google-play-console-cli-skills.git
mkdir -p "$CODEX_HOME/skills"
ln -s "$PWD/google-play-console-cli-skills/skills/gpc-release-flow" "$CODEX_HOME/skills/gpc-release-flow"
```

## Included Skills

### Release And Rollout

- `gpc-release-flow`
- `gpc-vitals-monitor`
- `gpc-rollout-management`

### Setup And Bootstrap

- `gpc-bootstrap-workspace`
- `gpc-auth-setup`
- `gpc-workflow-authoring`

### Operational Workflows

- `gpc-review-triage`
- `gpc-monetization-setup`
- `gpc-changelog-sync`
- `gpc-listing-sync`
- `gpc-subscription-sync`
- `gpc-product-sync`
- `gpc-financial-reports`
- `gpc-generated-apks`
- `gpc-internal-sharing`
- `gpc-doctor-audit`
- `gpc-diff-review`
- `gpc-release-verify`

## Repository Layout

```text
skills/
  <skill-name>/
    SKILL.md
scripts/
  validate_skills.py
.github/workflows/
  ci.yml
```

## Validation

CI runs `scripts/validate_skills.py` to verify:

- every skill has a valid `SKILL.md`
- required frontmatter fields are present
- every skill references at least one `gpc` command
- referenced top-level `gpc` commands are known

## Scope

This repo only documents workflows for capabilities already shipped in `gpc`. Future skills for upcoming features should land only after the corresponding CLI support exists.
