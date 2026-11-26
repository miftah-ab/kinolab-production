# KinoLab Production

KinoLab is a Claude skill for directing commercial video production from the first client question to final delivery.

## Canonical skill

The installable skill lives at:

`.claude/skills/kinolab-production/SKILL.md`

It includes a one-question-at-a-time production intake, commercial strategy, scripts/storyboards, cinematography, image/video prompts, optional Blender 3D, editing, sound design, platform exports, rights/compliance, media QC, templates and utility scripts.

## Install in Claude Code

Claude Code discovers project skills at `.claude/skills/<skill-name>/SKILL.md`. This repository uses that exact structure. Clone/open this repository as the project and use Claude Code in the repository. For personal scope, copy or symlink the `kinolab-production` folder into `~/.claude/skills/kinolab-production/`.

## Install in claude.ai

Zip the contents of `.claude/skills/kinolab-production/` as a single top-level `kinolab-production/` folder and upload it through Claude's custom Skills settings, if available on your plan/account. Do not upload the entire repository as the skill bundle. GitHub hosting does not automatically install a custom Skill in claude.ai.

See [INSTALL.md](.claude/skills/kinolab-production/INSTALL.md) for exact instructions.

## Validate

From the repository root:

```bash
python3 .claude/skills/kinolab-production/scripts/validate_skill.py
```

For media inspection, the optional scripts require FFmpeg/ffprobe. Blender and Blender MCP are not mandatory.

## Research

See [.claude/skills/kinolab-production/REFERENCES.md](.claude/skills/kinolab-production/REFERENCES.md) for the researched source repositories, official technical documentation and selection notes.

## Important

This is a production workflow and skill package, not a guarantee of perfect generated media. The evaluations must be run in the actual Claude environment, and every finished video still needs human visual/audio review and client approval.
