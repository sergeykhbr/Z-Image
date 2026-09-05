import os
import torch
from diffusers import ZImagePipeline
from prompt_common import compile_prompt

pipe = ZImagePipeline.from_pretrained(
    "Tongyi-MAI/Z-Image-Turbo",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
)

# Important for 16 GB VRAM
pipe.enable_model_cpu_offload()

SEED = 544
REGEN_TOTAL = 10     # num of generation per one object
OBJ_TOTAL = 3       # first several object to generate

collection = {
    "Generate":[
        {
            "id":"goblin_basic_l1",
            "description":"""
The main subject is a modular character sheet of a wicked goblin archer unit.
The canvas is divided into a clear layout grid. 
On the left side of the canvas, there are four complete,
fully assembled goblin archers shown from four distinct,
separate rotation angles: 
- Upper-left quadrant: Front view.
- Lower-left quadrant: Back view.
- Middle-left upper row: Full profile view from the left side.
- Middle-left lower row: Full profile view from the right side.
All characters feature stylized game proportions with a massive
oversized head and short, stubby legs. 
On the right side of the canvas, it displays isolated spare parts:
separate unattached head,
separate torso,
separate left arm,
separate right arm holding a bow,
separate legs.
""",
            "material":"GoblinSkinToneBasic",
            "composition_type":"unit",
            "composition_extra":"""
massive oversized head that dominates its upper body profile,
a wide torso, and extremely short, stubby legs.
The head and shoulders appear significantly larger due to dramatic
downward perspective compression,
"""
        },
        {
            "id":"tower_black_l2",
            "description":"""
A pyramidal stone tower is the main subject.
The tower is a compact hexagonal stone building with assymetric form,
large irregular individual stone blocks,
a rounded metal doorway at the front,
two heraldic cloth banners hanging from the sides.
""",
            "material":"BlackStoneWithMetal",
            "composition_type":"tower",
            "composition_extra":""
        },
        {
            "id":"tower_classic_l1",
            "description":"""
A small medieval stone archer tower is the main subject.
The tower is a
compact cylindrical stone fortress with thick chunky masonry,
large irregular individual stone blocks,
a rounded wooden doorway at the front,
sturdy battlements and crenellations at the top,
and two blue heraldic cloth banners hanging from the sides.
""",
            "material":"GrayStoneBrickAndWood",
            "composition_type":"tower",
            "composition_extra":""
        },
        {
            "id":"tower_classic_l2",
            "description":"""
A small makeshift medieval defensive barricade is the main subject.
The structure is acrude semi-circular breastwork
built upon a low elevated dirt mound,
loosely stacked irregular fieldstones and thick rough-hewn wooden logs,
a simple gap-opening for access at the rear,
an elevated wooden platform on timber stilts rising behind the stone wall,
a single ragged blank cloth flag hanging from a wooden post.
""",
            "material":"GrayStoneBrickAndWood",
            "composition_type":"tower",
            "composition_extra":""
        },
        {
            "id":"toxic_cloud",
            "description":"""

The canvas is divided into a clear layout grid to generate several toxic gas clouds:
one toxic gas forms a tiny, compact, flat horizontal pool,
second toxic gas expands outward as a flat horizontal ring along the floor plane,
third toxic gas spreads wide as a sprawling,
forth toxic gas spreads thin as a massive, flat horizontal ring wave across the ground.
""",
            "material":"ToxicCloudBasic",
            "composition_type":"cloud",
            "composition_extra":"""
extreme elliptical compression matching a 60 degree camera looking down at a floor plane,
completely horizontal orientation,
no vertical rotation,
no z-axis rotation,
"""
        },

    ],
    "Materials":{
        "GrayStoneBrickAndWood":{
            "description":"""
warm beige and gray medieval stone,
slightly weathered masonry,
dark brown wood,
muted blue cloth,
dark steel details,
subtle moss and small patches of grass around the bottom,
painted material variation and edge highlights.
""",
            "style_extra":"""
carefully painted stone and wood surfaces,
"""
        },
        "BlackStoneWithMetal":{
            "description":"""
black moldy stone,
slightly weathered masonry,
dark red wood,
muted red cloth,
gold details,
subtle moss and small patches of grass around the bottom,
painted material variation and edge highlights.
""",
            "style_extra":"""
carefully painted stone and wood surfaces,
"""
        },
        "ToxicCloudBasic":{
            "description":"""
vibrant toxic lime-green and deep forest-green gas shades,
opaque and dense painterly smoke volumes,
painted material variation and glowing edge highlights,
no transparency against the background.
""",
            "style_extra":""
        },
        "GoblinSkinToneBasic":{
            "description":"""
Charming olive-green skin tones,
dark brown leather armor plates,
coarse burlap cloth rags,
a primitive wooden bow,
painted highlights on edges.
""",
            "style_extra":"""
The artwork must represent a game-ready character sheet
where a game artist can cleanly slice the arm,
leg, torso, head, and weapon assets for skeletal
and skeletal-mesh manual 2D animation.
"""
        }
    }
}

objcnt = 0
for obj in collection["Generate"]:
    if (objcnt >= OBJ_TOTAL):
        break
    objcnt = objcnt + 1

    material = collection["Materials"][obj["material"]]
    print("Generating: {0}".format(obj["id"]))

    prompt = compile_prompt(obj["description"],
                            material["description"],
                            material["style_extra"],
                            obj["composition_type"],
                            obj["composition_extra"])

    base_path = f"output/{obj['id']}/{obj['id']}"
    dir_name = os.path.dirname(base_path)
    os.makedirs(dir_name, exist_ok=True)
    with open(f"{base_path}.txt", "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"Saved {base_path}.txt")

    for i in range(REGEN_TOTAL):
        current_seed = SEED + i
        gen = torch.Generator("cuda").manual_seed(current_seed)
        image = pipe(
            prompt=prompt,
            height=1024,
            width=1024,
            num_inference_steps=9,
            guidance_scale=0.0,
            generator=gen,
        ).images[0]

        image.save(f"{base_path}_{current_seed}.png")
        print(f"Saved {base_path}_{current_seed}.png")

