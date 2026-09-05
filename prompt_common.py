
GLOBAL_COMPOSITION = {}
GLOBAL_COMPOSITION["tower"] = """
high-vantage point,
bird's eye view,
flat isometric ground projection,
average perspective distortion,
large readable silhouette,
visually balanced proportions.
clean white space background.
"""

GLOBAL_COMPOSITION["cloud"] = """
high-vantage point,
bird's eye view,
extreme elliptical compression matching a 60 degree camera looking down at a floor plane,
completely horizontal orientation,
no vertical rotation,
no z-axis rotation.
every component is separated by white space.
separated cleanly by white space.
"""

GLOBAL_COMPOSITION["unit"] = """
high-vantage point,
bird's eye view,
No parts overlap;
every component is separated by white space.
separated cleanly by white space.
"""


def compile_prompt(subject_description,
                   materials_description,
                   extra_style="",
                   composition_type="tower",
                   extra_compoistion=""):
    return f"""
A premium fantasy game asset,
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
rich warm materials,
soft bevels,
rounded edges,
visible brush-like texture variation,
appealing fantasy illustration,
polished professional artwork.
{extra_style}

The object should feel designed and painted by a fantasy game artist rather
than photographed or rendered as a realistic 3D model.

COMPOSITION:
{GLOBAL_COMPOSITION[composition_type]}
{extra_compoistion}

LIGHTING:
soft warm directional light from above and slightly from the front,
gentle painted-looking highlights,
soft ambient occlusion,
subtle contact shadow beneath the subject,
warm fantasy-game lighting,
no dramatic cinematic lighting.

MATERIALS:
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
