# Project Organization, Naming and Version Control

## Folder structure
Use a predictable project root and never mix unrelated client projects:

```text
PROJECT_NAME/
  00_admin/
    brief.md
    approvals.md
    change-log.md
  01_references/
    client-assets/
    visual-references/
  02_preproduction/
    concept.md
    script.md
    visual-bible.md
    storyboard/
    shot-list.csv
  03_generation/
    prompts/
    generated-stills/
    generated-video/
    generation-log.csv
  04_production/
    blender/
    live-action/
    stock/
  05_audio/
    voice/
    music/
    ambience/
    foley/
    sfx/
    cue-sheet.md
  06_edit/
    project-files/
    proxies/
    previews/
  07_exports/
    review/
    masters/
    platform-versions/
    captions/
  08_delivery/
    qa-report.md
    asset-manifest.csv
```

## Naming
- Project slug: short, stable, readable, no client secrets in public filenames.
- Shot IDs: `KL01_SC01_SH01` (project/scene/shot) and never recycle an ID.
- Version files explicitly: `projectname_9x16_v003_review.mp4`, `projectname_16x9_master_v001.mp4`.
- Keep generated outputs linked to prompt version, model, settings and reference assets.
- Do not overwrite approved masters or source files. Save a new version.

## Asset manifest
Track every external or generated asset: filename, creator/source, role, date, licence/permission, attribution, commercial usage limits, reference role, version and approval state.

## Backups and archive
Keep source assets, project files, linked fonts/textures, prompts, generation log, approvals, final exports and QA report together. Confirm the project can reopen before archiving. Do not claim a backup exists unless it was actually made and checked.

## Privacy
Do not put private client data, customer contact details, credentials or unreleased campaign information in public repo paths, filenames or example fixtures.
