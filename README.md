# MiaoBi-beta-v0.9 
这是妙笔的测试版本。妙笔，一个中文文生图模型，与经典的stable-diffusion 1.5版本拥有一致的结构，兼容现有的lora，controlnet，T2I-Adapter等主流插件。

This is the beta version of MiaoBi, a chinese text-to-image model, following the classical structure of sd-v1.5, compatible with existing mainstream plugins such as Lora, Controlnet, T2I Adapter, etc.

## Diffusers
```py
from diffusers import StableDiffusionPipeline
import torch
model_id = "AIXI-AIGC/miaobi"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "一只穿着铠甲的猫"
image = pipe(prompt).images[0]  
image.save("铠甲猫.png")
```

## Weights
权重文件将会在下周开源。

we are working hard to get better result, and the checkpoint will be released as soon as possible.


## MiaoBi-beta-v0.9 Chinese Example

一只精致的陶瓷猫咪雕像，全身绘有精美的传统花纹，眼睛仿佛会发光。 ![](examples/fig1.png)


动漫风格的风景画，有山脉、湖泊，也有繁华的小镇子，色彩鲜艳，光影效果明显。 ![](examples/fig2.png)


极具真实感的复杂农村的老人肖像，黑白。 ![](examples/fig3.png)


红烧狮子头 ![](examples/fig4.png)


车水马龙的上海街道，春节，舞龙舞狮。 ![](examples/fig5.png)


枯藤老树昏鸦，小桥流水人家。水墨画。 ![](examples/fig6.png)



## Limitations
受限于算力与中文数据集规模的问题，现阶段妙笔的表现力可能逊色于商用模型，我们正在拓展我们的算力资源，以及收集更大规模的数据，期待妙笔的未来表现。

Due to limitations in computing power and the size of Chinese datasets, the performance of Miaobi may be inferior to commercial models at this stage. We are expanding our computing resources and collecting larger scale data, looking forward to the future performance of Miaobi.


