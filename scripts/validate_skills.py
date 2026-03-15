#!/usr/bin/env python3
"""Validate skill structure and minimal command references."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
COMMAND_RE = re.compile(r"`(gpc [^`]+)`")
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)
KNOWN_TOP_LEVEL = {
    "auth",
    "bootstrap",
    "appinit",
    "apps",
    "app-recoveries",
    "changelog",
    "edits",
    "tracks",
    "apks",
    "bundles",
    "deobfuscation",
    "deploy",
    "diff",
    "doctor",
    "e2e",
    "release",
    "rollback",
    "setup",
    "status",
    "reviews",
    "reports",
    "orders",
    "external-transactions",
    "device-tier-configs",
    "system-apks",
    "generated-apks",
    "subscriptions",
    "monetization",
    "notify",
    "products",
    "iap",
    "listing",
    "purchases",
    "users",
    "grants",
    "internal-sharing",
    "completion",
    "workflow",
}


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def frontmatter_body(text: str, path: pathlib.Path) -> tuple[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        fail(f"{path}: malformed YAML frontmatter")
    return parts[0][4:], parts[1]


def main() -> None:
    if not SKILLS_DIR.is_dir():
        fail("skills/ directory is missing")

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if len(skill_dirs) < 8:
        fail("expected at least 8 skills")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"{skill_dir}: missing SKILL.md")

        text = skill_file.read_text(encoding="utf-8")
        frontmatter, body = frontmatter_body(text, skill_file)

        name_match = NAME_RE.search(frontmatter)
        desc_match = DESC_RE.search(frontmatter)
        if not name_match:
            fail(f"{skill_file}: missing frontmatter name")
        if not desc_match:
            fail(f"{skill_file}: missing frontmatter description")

        name = name_match.group(1).strip().strip('"')
        if name != skill_dir.name:
            fail(f"{skill_file}: frontmatter name {name!r} must match directory {skill_dir.name!r}")

        commands = COMMAND_RE.findall(body)
        if not commands:
            fail(f"{skill_file}: must reference at least one gpc command")

        for command in commands:
            parts = command.split()
            if len(parts) < 2:
                fail(f"{skill_file}: invalid command reference {command!r}")
            top_level = parts[1]
            if top_level not in KNOWN_TOP_LEVEL:
                fail(f"{skill_file}: unknown top-level gpc command {top_level!r}")

    print(f"validated {len(skill_dirs)} skills")


if __name__ == "__main__":
    main()
