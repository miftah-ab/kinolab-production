# KinoLab Production Skill

A Claude skill for planning and supervising cinematic commercial video production for real businesses.

## What it does

- Guides a user through a simple, one-question-at-a-time production intake.
- Turns a business objective into an ad concept, script, visual bible and shot plan.
- Writes detailed, generator-independent image and video prompts.
- Plans genuine Blender 3D shots with local Python automation where appropriate.
- Produces editing, motion graphics, color and full sound-design instructions.
- Applies cost, licensing, technical and human quality gates.

## Install

Use the root `SKILL.md` as the skill entry point in a Claude-compatible skills workflow. Keep the `references/`, `templates/`, and `evals/` folders alongside it; the skill references them by relative path.

For Claude Code, place the repository folder in the project's `.claude/skills/kinolab-production/` directory (or your user-level skills directory) with this same structure.

## Operating model

Claude is the creative director and production supervisor. The user runs prompts in their chosen image/video generator, runs Blender scripts in Blender, and edits in their chosen editor (currently CapCut Desktop). This skill does not require paid APIs, provider accounts, or Blender MCP.

## Quality and limitations

The skill provides a disciplined workflow, not a guarantee that any generative model or render will be flawless. Every important visual must be inspected; every final export must pass technical checks and human review. Do not claim media was inspected if it was not actually provided or accessible.
