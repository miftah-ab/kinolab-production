# Blender 3D Production Workflow

Use Blender when actual 3D adds measurable value: product hero shots, impossible camera moves, controlled simulations, repeatable geometry, precise lighting or scenes that generative video cannot reliably maintain. Do not force 3D into every commercial.

## Version and execution

- Ask which Blender version is installed before writing version-sensitive scripts.
- Prefer local Blender Python scripts executed by the user's Blender installation.
- Do not require Blender MCP, an add-on, cloud rendering or paid service.
- Use version-appropriate APIs and flag uncertain calls rather than pretending they are tested.
- Make scripts deterministic and rerunnable; avoid destructive scene edits unless explicitly requested.
- Save project files and renders to clearly named paths supplied or approved by the user.

## Staged scene workflow

1. Gather product/reference images and measurements where available.
2. Block out geometry and camera.
3. Lock composition and framing.
4. Establish lighting and material response.
5. Refine geometry, materials, labels and details.
6. Animate only what the shot needs.
7. Render low-cost previews.
8. Inspect preview and correct specific defects.
9. Render final quality.
10. Verify output and archive the .blend file and dependencies.

## Script requirements

A production script should:
- State the Blender version assumptions.
- Create or reuse a clearly named scene and collections.
- Set units, frame rate, frame range, resolution and output format explicitly.
- Use named objects/materials/lights/cameras.
- Avoid hidden external dependencies where possible.
- Include comments and configurable parameters near the top.
- Save the .blend file before final rendering.
- Support a preview mode with lower samples/resolution.
- Log output paths and failures clearly.
- Avoid silently overwriting user assets.

## Quality loop

When a render fails:
1. Preserve the failing render and scene.
2. Describe the exact defect.
3. Diagnose likely source: geometry, reference, material, lighting, camera, animation, render settings or compositing.
4. Change only the relevant cause.
5. Render a preview.
6. Compare against the approved reference and brief.
7. Record the fix.

Do not claim a script or render was tested unless it was actually executed in Blender. The user should share errors or preview frames for iteration.
