# Quality Control, Media Inspection and Delivery

## Three distinct review layers

1. **Automated technical inspection:** metadata, duration, streams, black/frozen frames, silence/clipping indicators where tools support them.
2. **Human visual inspection:** product truth, artifacts, continuity, framing, text, grade and commercial clarity.
3. **Human audio inspection:** voice, music, ambience, Foley, SFX, clipping, gaps, balance and ending.

Passing one layer does not imply passing the others.

## Visual review checklist

Inspect every shot for product/brand fidelity, identity and location continuity, anatomy and object interaction, physical plausibility, warping, flicker, morphing, texture crawl, unstable labels, focus, exposure, camera motion, color, composition, safe areas, CTA accuracy and story clarity.

Review the complete sequence at normal speed and selected frames at full resolution. A contact sheet helps locate problems but does not replace playback.

## Audio review checklist

Listen to the complete export on headphones and a phone speaker. Check intelligibility, pronunciation, music balance, sync, ambience, Foley, SFX, clipping, distortion, clicks, gaps, abrupt cuts and clean ending. Measure loudness and true peak with an appropriate meter when available; report actual measurements, not guesses.

## Automated checks

If FFmpeg/ffprobe are installed, use `scripts/media_probe.py` and `scripts/contact_sheet.py`. Run the skill validator with `scripts/validate_skill.py`. These scripts report technical signals only; they do not judge whether the ad is persuasive or beautiful.

## Technical delivery

Verify that the exported file plays from beginning to end, has correct ratio/dimensions/frame rate/duration/codec/audio, contains no unintended black/frozen sections, has no missing expected audio, has correct filename and is compatible with destination. Use the actual export file, not editor settings alone.

## Final handoff

Deliver only agreed formats. Include final exports, source/project files if agreed, caption files, asset manifest/attributions, brief version, known limitations and QA status. Never call a file "final" before human review and required client approval.
