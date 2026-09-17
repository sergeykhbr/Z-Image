import os
import csv
import torch
from torch.profiler import profile, ProfilerActivity
from diffusers import ZImagePipeline
from game_assets import ArcherTower, HandTower, RoundIcon, UnitOrc

pipe = ZImagePipeline.from_pretrained(
    "Tongyi-MAI/Z-Image-Turbo",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
)

# Important for 16 GB VRAM
pipe.enable_model_cpu_offload()

SEED = 700
PROFILER = True

def profile_generation(pipe, prompt, gen, trace_path, csv_path):
    with profile(
        activities=[
            ProfilerActivity.CPU,
            ProfilerActivity.CUDA,
        ],
        record_shapes=True,
    ) as prof:
        image = pipe(
            prompt=prompt,
            height=1024,
            width=1024,
            num_inference_steps=9,
            guidance_scale=0.0,
            generator=gen,
        ).images[0]

    print("\n=== OPERATOR SUMMARY ===")
    print(
        prof.key_averages(
            group_by_input_shape=True
        ).table(
            sort_by="cuda_time_total",
            row_limit=-1,
        )
    )

    # Chrome trace
    prof.export_chrome_trace(trace_path)

    # CSV
    events = prof.key_averages(group_by_input_shape=True)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "operator",
            "calls",
            "cpu_total_us",
            "cpu_self_us",
            "cuda_total_us",
            "cuda_self_us",
            "input_shapes",
        ])

        for event in events:
            writer.writerow([
                event.key,
                event.count,
                event.cpu_time_total,
                event.self_cpu_time_total,
                getattr(event, "device_time_total", 0.0),
                getattr(event, "self_device_time_total", 0.0),
                event.input_shapes,
            ])


    # Brief statistic:
    rows = []
    for e in events:
        rows.append({
            "operator": e.key,
            "calls": e.count,
            "cpu_total_us": e.cpu_time_total,
            "cpu_self_us": e.self_cpu_time_total,
            "device_total_us": getattr(e, "device_time_total", 0.0),
            "device_self_us": getattr(e, "self_device_time_total", 0.0),
            "input_shapes": str(e.input_shapes),
        })

    # Sort by accelerator/device time
    rows.sort(key=lambda x: x["device_total_us"], reverse=True)
    top = rows[:50]
    with open("profile_top50.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=top[0].keys())
        writer.writeheader()
        writer.writerows(top)

    print("Saved profile_top50.csv")
    return image

def generate_asset(objlist, N=1):
    for obj in objlist:
        prompt = obj.prompt()

        base_path = f"output/{obj.name}/{obj.nametyped}"
        dir_name = os.path.dirname(base_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(f"{base_path}.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"Saved {base_path}.txt")

        for i in range(N):
            current_seed = SEED + i
            gen = torch.Generator("cuda").manual_seed(current_seed)

            if PROFILER:
                trace_path = f"{base_path}_{current_seed}_trace.json"
                csv_path = f"{base_path}_{current_seed}_ops.csv"
                image = profile_generation(
                    pipe,
                    prompt,
                    gen,
                    trace_path,
                    csv_path,
                )
                print(f"Saved profiler trace: {trace_path}")
                print(f"Saved profiler CSV:   {csv_path}")
            else:
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
    #ArcherTower('Lvl1'),
    #ArcherTower('Lvl2'),
    #ArcherTower('Lvl3'),
    #ArcherTower('Lvl4'),
    #ArcherTower('Lvl5'),
    #ArcherTower('Lvl5-fire'),
    #ArcherTower('Lvl5-poison'),
    #HandTower('Lvl1'),
    #HandTower('Lvl2'),
    #RoundIcon(type='Lightning'),
    #RoundIcon(type='Poison'),
    #RoundIcon(type='Fire'),
    #RoundIcon(type='Rifle'),
    #RoundIcon(type='Cannon'),
    UnitOrc('Front'),
    #UnitOrc('Back'),
]
generate_asset(objlist, N=1)