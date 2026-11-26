# Installing KinoLab

## Claude Code
Clone this repository into your project, or add it as a trusted project repository. The skill is stored at the exact Claude Code discovery path:

`.claude/skills/kinolab-production/SKILL.md`

Claude Code discovers project skills from this directory. For personal installation, copy or symlink the `kinolab-production` folder into `~/.claude/skills/kinolab-production/`. Restart/reload the session if needed, then ask Claude to start a new commercial video production.

## claude.ai
Create a ZIP whose top-level folder is `kinolab-production/` and whose root inside that folder contains `SKILL.md`, `references/`, `templates/`, `scripts/`, and `evals/`. In other words, zip the contents of `.claude/skills/kinolab-production/` as a single enclosing `kinolab-production` folder, not the whole repository. Upload the ZIP through Claude's Skills settings if custom Skills are available on the account. GitHub repository hosting alone does not automatically install a custom Skill in claude.ai.

## Local utilities
- Python 3 standard library is enough for `scripts/validate_skill.py`.
- `scripts/media_probe.py` requires FFmpeg's `ffprobe`; optional scans also require `ffmpeg`.
- `scripts/contact_sheet.py` requires `ffmpeg`.
- Blender is optional and only needed for projects that genuinely use 3D. No Blender MCP is required.

## Verify
Run:

```bash
python3 .claude/skills/kinolab-production/scripts/validate_skill.py
```

Then run the evaluation cases in `evals/README.md` inside the actual Claude environment. Skill discovery and successful validation are not proof of production output quality.
