from diffusers import StableDiffusionPipeline
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("checkpoints/miaobi_beta0.9/tokenizer",  trust_remote_code=True)
pipe = StableDiffusionPipeline.from_pretrained("checkpoints/miaobi_beta0.9")

pipe.to("cuda")
prompt = "一只穿着铠甲的猫"
image = pipe(prompt).images[0]
image.save("铠甲猫.png")
