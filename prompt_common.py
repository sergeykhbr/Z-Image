
GLOBAL_COMPOSITION_TYPED = {}
GLOBAL_COMPOSITION_TYPED['tower']=""
GLOBAL_COMPOSITION_TYPED['cloud']="""
extreme elliptical compression matching a 60 degree camera looking down at a floor plane,
completely horizontal orientation,
no vertical rotation,
no z-axis rotation,
"""


def compile_prompt(objtype, #'tower', 'cloud'
                   subject_description,
                   materials_description,
                   extra_style=""):
    return f"""
A premium fantasy tower-defense game asset,
inspired by classic hand-painted cartoon fantasy strategy games.

{subject_description}

VISUAL STYLE:
hand-painted fantasy game artwork,
charming cartoon aesthetic,
stylized three-dimensional construction,
2.5D game-art appearance,
exaggerated chunky forms,
simplified but highly expressive shapes,
painterly textures,
hand-painted highlights and shadows,
slightly exaggerated architectural and fluids details,
{extra_style}
rich warm materials,
soft bevels,
rounded edges,
visible brush-like texture variation,
appealing fantasy illustration,
polished professional tower-defense artwork.

The object should feel designed and painted by a fantasy game artist rather
than photographed or rendered as a realistic 3D model.

COMPOSITION:
single isolated asset,
centered in the image,
full object completely visible from bottom to top,
three-quarter front view,
high-vantage point,
bird's eye view,
consistent game asset viewing angle 60 degree,
flat isometric ground projection,
{GLOBAL_COMPOSITION_TYPED[objtype]}
average perspective distortion,
large readable silhouette,
visually balanced proportions.

LIGHTING:
soft warm directional light from above and slightly from the front,
gentle painted-looking highlights,
soft ambient occlusion,
subtle contact shadow beneath the tower,
controlled shadows between stone blocks,
warm fantasy-game lighting,
no dramatic cinematic lighting.

{materials_description}

PRESENTATION:
isolated game asset on a clean white background,
no environment,
no landscape,
no surrounding buildings,
no sky,
no scenery,
no battlefield,
no UI,
no text,
no logo,
no watermark.

The final image should look like a high-quality hand-painted fantasy tower
defense game asset with dimensional 3D forms, rather than a photorealistic
3D render or a generic modern 3D game asset.
"""
