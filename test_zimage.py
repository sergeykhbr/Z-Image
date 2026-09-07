import os
import torch
from diffusers import ZImagePipeline
from game_assets import ArcherTower, HandTower, RoundIcon

pipe = ZImagePipeline.from_pretrained(
    "Tongyi-MAI/Z-Image-Turbo",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
)

# Important for 16 GB VRAM
pipe.enable_model_cpu_offload()

SEED = 580

def generate_asset(objlist, N=1):
    for obj in objlist:
        prompt = obj.prompt()

        base_path = f"output/{obj.name}/{obj.namelvl}"
        dir_name = os.path.dirname(base_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(f"{base_path}.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"Saved {base_path}.txt")

        for i in range(N):
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



objlist = [
    #ArcherTower(level=1),
    #ArcherTower(level=2),
    #ArcherTower(level=3),
    #ArcherTower(level=4),
    #ArcherTower(level=5),
    #ArcherTower(level='5-fire'),
    #ArcherTower(level='5-poison'),
    #HandTower(level=1),
    #HandTower(level=2),
    #RoundIcon(type='lightning'),
    RoundIcon(type='poison'),
]
generate_asset(objlist, N=10)