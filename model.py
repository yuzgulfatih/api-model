from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt: str, negative_prompt: str = None):
    """Verilen prompta göre stable diffusion ile görsel üretimi."""
    image = pipe(prompt, negative_prompt=negative_prompt).images[0]
    return image
