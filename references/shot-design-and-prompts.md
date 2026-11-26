# Shot Design and Image / Video Prompting

## Shot specification

Every shot receives a stable ID, for example `KL01_SC01_SH01`, and records:
- Duration and timeline position.
- Narrative/commercial purpose.
- Subject and visible action.
- Shot size, angle, composition and focus.
- Camera/lens perspective (describe the look; do not imply every generator obeys real lens metadata).
- Lighting and environment.
- Camera movement: normally one primary move at most.
- Continuity references and reference roles.
- Required product details and forbidden deviations.
- Image prompt, when a still/keyframe is needed.
- Video prompt, when motion generation is needed.
- Audio cues and edit transition.
- Aspect ratio and output requirements.

## Image prompt anatomy

Write a complete, concrete prompt describing:
1. Main subject and exact product identity.
2. Visible action / pose.
3. Composition, shot size, angle and subject placement.
4. Environment and relevant props.
5. Lighting direction, quality and contrast.
6. Palette, material and visual texture.
7. Cinematic treatment and depth of field.
8. Aspect ratio and framing.
9. Continuity locks and negative constraints.

Describe what must visibly appear. Avoid abstract adjectives without observable meaning. Keep text and logos out of generated imagery unless exact legibility is not important; add branding in post.

## Video prompt anatomy

For text-to-video, describe:
- Subject and environment.
- One simple, physically plausible action.
- Camera framing and one primary camera move.
- Lighting and atmosphere.
- Motion speed and start/end state.
- Continuity requirements.
- Duration and aspect ratio where supported.
- Artifacts or unwanted changes to avoid.

For image-to-video, the still already establishes appearance and composition. Focus the prompt mainly on the motion: what moves, how it moves, what remains fixed, and how the shot ends. Do not re-describe the entire image in ways that could alter it.

## Model-specific adaptation

Keep the master prompt provider-independent. Only adapt syntax, duration limits, reference features, negative-prompt fields, seed controls or parameter names after the user selects a specific generator and its current capabilities are verified. Never invent model features, prices or limits.

## Production discipline

- Approve stills/keyframes before expensive video generation.
- Pilot one representative shot before batch generation.
- Keep generated shots short enough to inspect and retake.
- Make one change per revision where possible.
- After two failed attempts at the same action, change the action, framing, edit solution or reference rather than endlessly regenerating.
- Never generate a full sequence before the visual bible and shot list are approved.
