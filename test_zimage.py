import torch
from diffusers import ZImagePipeline

pipe = ZImagePipeline.from_pretrained(
    "Tongyi-MAI/Z-Image-Turbo",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
)

# Important for 16 GB VRAM
pipe.enable_model_cpu_offload()

SEED = 101
OUT_PNG = "output01"

OBJECT = [
"""
A small medieval stone archer tower is the main subject.
The tower is a
compact cylindrical stone fortress with thick chunky masonry,
large irregular individual stone blocks,
a rounded wooden doorway at the front,
sturdy battlements and crenellations at the top,
and two blue heraldic cloth banners hanging from the sides.
""",
"""
A small makeshift medieval defensive barricade is the main subject.
The structure is acrude semi-circular breastwork
built upon a low elevated dirt mound,
loosely stacked irregular fieldstones and thick rough-hewn wooden logs,
a simple gap-opening for access at the rear,
an elevated wooden platform on timber stilts rising behind the stone wall,
a single ragged blank cloth flag hanging from a wooden post.
"""
]

prompt = f"""
A premium fantasy tower-defense game asset, inspired by classic hand-painted
cartoon fantasy strategy games.

{OBJECT[1]}

VISUAL STYLE:
hand-painted fantasy game artwork,
charming cartoon aesthetic,
stylized three-dimensional construction,
2.5D game-art appearance,
exaggerated chunky forms,
simplified but highly expressive shapes,
painterly textures,
hand-painted highlights and shadows,
rich warm materials,
carefully painted stone and wood surfaces,
visible brush-like texture variation,
soft bevels,
rounded edges,
slightly exaggerated architectural details,
appealing fantasy illustration,
polished professional tower-defense artwork.

The object should feel designed and painted by a fantasy game artist rather
than photographed or rendered as a realistic architectural model.

COMPOSITION:
single isolated tower asset,
centered in the image,
full tower completely visible from the bottom of the base to the top,
three-quarter front view,
high-vantage point,
bird's eye view,
consistent game asset viewing angle 60 degree,
orthographic-like perspective,
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

MATERIALS:
warm beige and gray medieval stone,
slightly weathered masonry,
dark brown wood,
muted blue cloth,
dark steel details,
subtle moss and small patches of grass around the bottom,
painted material variation and edge highlights.

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

image = pipe(
    prompt=prompt,
    height=1024,
    width=1024,
    num_inference_steps=9,
    guidance_scale=0.0,
    generator=torch.Generator("cuda").manual_seed(SEED),
).images[0]

image.save(f"output/{OUT_PNG}.png")

print(f"Saved output/{OUT_PNG}.png")

