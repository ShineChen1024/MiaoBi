import cv2
from PIL import Image
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
import torch
import numpy as np
from diffusers.utils import load_image
from transformers import AutoTokenizer

# image = load_image("https://huggingface.co/lllyasviel/sd-controlnet-canny/blob/main/images/bird.png")

image = load_image("./bird.png")
image = np.array(image)

low_threshold = 100
high_threshold = 200

image = cv2.Canny(image, low_threshold, high_threshold)
image = image[:, :, None]
image = np.concatenate([image, image, image], axis=2)
image = Image.fromarray(image)

controlnet = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16)

tokenizer = AutoTokenizer.from_pretrained("checkpoints/miaobi_beta0.9/tokenizer",  trust_remote_code=True)
pipe = StableDiffusionControlNetPipeline.from_pretrained("checkpoints/miaobi_beta0.9", controlnet=controlnet,torch_dtype=torch.float16)
pipe.to("cuda")

image = pipe("小麻雀", image, num_inference_steps=20).images[0]
image.save('小麻雀.png')