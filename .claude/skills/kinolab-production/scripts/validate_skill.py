#!/usr/bin/env python3
"""Validate KinoLab skill frontmatter and local Markdown links (stdlib only)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors, warnings = [], []
skill = ROOT / "SKILL.md"
if not skill.is_file():
    errors.append("Missing SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter")
    else:
        end = text.find("\n---\n", 4)
        if end < 0:
            errors.append("Missing closing frontmatter delimiter")
        else:
            front = text[4:end]
            name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front, re.M)
            desc = re.search(r"^description:\s*(.+)$", front, re.M)
            if not name or len(name.group(1)) > 64:
                errors.append("Invalid or missing skill name")
            if not desc or not desc.group(1).strip() or len(desc.group(1)) > 1024:
                errors.append("Invalid or missing skill description")
    if len(text.splitlines()) >= 500:
        warnings.append("SKILL.md is 500 lines or more; consider splitting it")
for md in ROOT.rglob("*.md"):
    content = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]*)?\)", content):
        if "://" not in target and not (md.parent / target).resolve().is_file():
            errors.append(f"{md.relative_to(ROOT)} links to missing file: {target}")
if errors:
    print("FAIL")
    for e in errors: print("ERROR:", e)
    sys.exit(1)
print("PASS: frontmatter and local Markdown links")
for w in warnings: print("WARNING:", w)
