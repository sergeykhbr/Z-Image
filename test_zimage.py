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
A premium fantasy tower-defense game asset,
inspired by classic hand-painted cartoon fantasy strategy games.

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

CLOUD_STAGES = [
    "The toxic gas forms a tiny, compact, flat horizontal pool exactly in the center of the floor plane, covering a 10 percent footprint radius.",
    "The toxic gas expands outward as a flat horizontal ring along the floor plane, covering a 20 percent footprint radius.",
    "The toxic gas stretches further along the ground as a perfectly flat 2D horizontal ring, covering a 30 percent footprint radius.",
    "The toxic gas forms a wider horizontal ring wave flat against the floor plane, covering a 40 percent footprint radius.",
    "The toxic gas pushes out into a broad, horizontal circular ring expansion on the floor plane, covering a 50 percent footprint radius.",
    "The toxic gas spreads wide as a sprawling, flat horizontal ring along the floor plane, covering a 60 percent footprint radius.",
    "The toxic gas spreads thin as a massive, flat horizontal ring wave across the ground, covering a 70 percent footprint radius.",
    "The toxic gas reaches its maximum boundary as a giant, faint horizontal ring flat on the floor plane, covering an 80 percent footprint radius."
]

prompts = []
for i in range(8):
    frame_prompt = f"""
A premium fantasy tower-defense game asset, inspired by classic hand-painted
cartoon fantasy strategy games.

The main subject is a single isolated toxic gas ring wave expanding outward along a flat floor plane.
{CLOUD_STAGES[i]}
The toxic gas is completely flat, sprawling entirely on the horizontal ground plane without vertical height or depth, behaving as an elliptical floor decal.

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
carefully painted toxic smoke and vapor surfaces,
visible brush-like texture variation,
soft bevels,
rounded edges,
slightly exaggerated fluid details,
appealing fantasy illustration,
polished professional tower-defense artwork.

The object should feel designed and painted by a fantasy game artist rather
than photographed or rendered as a realistic fluid simulation model.

COMPOSITION:
single isolated gas ring asset,
centered in the image,
full ring completely visible from its inner empty space to its outer edge boundaries,
three-quarter front view,
high-vantage point,
bird's eye view,
consistent game asset viewing angle 60 degree,
flat isometric ground projection,
extreme elliptical compression matching a 60 degree camera looking down at a floor plane,
completely horizontal orientation,
no vertical rotation,
no z-axis rotation,
large readable silhouette,
visually balanced proportions.

LIGHTING:
soft warm directional light from above and slightly from the front,
gentle painted-looking highlights on the edges of the smoke puffs,
soft ambient occlusion between gas layers,
subtle contact shadow beneath the cloud ring,
controlled shadows within the billowing smoke folds,
warm fantasy-game lighting,
no dramatic cinematic lighting.

MATERIALS:
vibrant toxic lime-green and deep forest-green gas shades,
opaque and dense painterly smoke volumes,
painted material variation and glowing edge highlights,
no transparency against the background.

PRESENTATION:
isolated game asset on a clean white background,
no tower,
no building,
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
    prompts.append(frame_prompt)

for i in range(8):
    current_seed=SEED + i
    image = pipe(
        prompt=prompts[i],
        height=1024,
        width=1024,
        num_inference_steps=9,
        guidance_scale=0.0,
        generator=torch.Generator("cuda").manual_seed(current_seed),
    ).images[0]

    image.save(f"output/fog{current_seed}_{i}.png")
    print(f"Saved output/fog{current_seed}_{i}.png")

