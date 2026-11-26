# Shot Design and Image / Video Prompting

## Required shot card

Each shot receives a stable ID (for example `KL01_SC01_SH01`) and:
- Timeline start and duration.
- Commercial/story purpose.
- Subject and one clear visible action.
- Shot size, camera angle, composition and focus.
- Perspective/lens look.
- Lighting and environment.
- One primary camera move (or locked camera).
- Start/end state and motion speed.
- Reference files and each reference's role.
- Product/character/scene continuity locks.
- Image prompt, if a keyframe is required.
- Video prompt, if motion generation is required.
- Audio cues, edit transition and output ratio.

## Image prompt

Specify subject/product truth, pose/action, composition, environment, props, lighting, materials, palette, visual treatment, focus/depth, aspect ratio and constraints. Use concrete observable language. Avoid metaphor-only prompts.

## Text-to-video prompt

Specify subject, environment, one simple action, framing, one primary camera move, lighting, motion pace, start/end state, duration/aspect ratio if supported, continuity references and failure modes to inspect.

## Image-to-video prompt

The still establishes appearance and composition. Focus on motion: what moves, direction, speed, start/end state, what stays fixed, and camera behavior. Avoid rewriting the entire image description in a way that may mutate the established frame.

## Model adaptation

Keep a provider-independent master prompt. After a specific generator is selected, check its current official documentation for supported input references, clip length, aspect ratios, negative prompting, camera controls, audio generation, resolution, watermark and commercial terms. Adapt only the syntax and controls that model actually supports. Never assume one model's prompting rules apply to another.

## Generation economics

- Approve storyboard and stills before paid video generation.
- Pilot one representative shot.
- Track model, settings, prompt version, reference files, output filename, credits/cost and review status.
- Keep shots simple and short enough to inspect.
- After two failures, change the visual plan rather than blindly retry.
- Do not batch-generate unapproved shots.
