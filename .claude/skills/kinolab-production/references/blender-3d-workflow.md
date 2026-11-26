# Blender 3D Production Workflow

Use genuine 3D only when it improves control, product fidelity, camera choreography, repeatability, simulation or the visual idea. Do not force 3D into every ad.

## Environment and version

Ask which Blender version is installed before writing version-sensitive code. The current official Blender API documentation is versioned; use the matching API and release notes rather than assuming an older recipe still works. Prefer local Blender Python execution. Blender MCP is optional, never a prerequisite.

## Workflow

1. Collect product references, dimensions and real-world scale.
2. Block out geometry and camera.
3. Lock composition and lens perspective.
4. Establish lighting and material response.
5. Refine geometry, bevels, normals, labels, decals and details.
6. Animate only the required action.
7. Render low-cost previews.
8. Inspect contact sheets and full-resolution critical frames.
9. Fix identified defects.
10. Render finals and verify outputs.
11. Archive .blend, linked assets, fonts, textures, scripts and render settings.

## Script quality

Every script should state version assumptions; use named objects, collections, materials, lights and cameras; set frame rate, frame range, resolution, color management and output explicitly; keep configurable values at the top; support preview mode; save before final render; log paths/errors; and avoid overwriting existing files without consent.

Use stable names and deterministic scene construction. Handle missing fonts/textures and unsupported API properties gracefully. Do not assume an object or context exists. Prefer data API over context-sensitive operators where practical.

## Render planning

Choose engine and settings based on the shot, hardware and time. Test one frame before long animation. Use denoising and samples appropriate to the scene. Consider render layers/passes and compositing only when they serve the finish. Do not invent render-time estimates.

## Validation

A generated script is not proof of a correct scene. Run it in the user's installed Blender, inspect actual preview output, and capture errors. Preserve the failing .blend and render before fixing. Never claim the code or image was tested if it was not executed and inspected.
