# MiaoBi-beta
这是妙笔的测试版本。妙笔，一个中文文生图模型，与经典的stable-diffusion 1.5版本拥有一致的结构，兼容现有的lora，controlnet，T2I-Adapter等主流插件及其权重。

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

一只精致的陶瓷猫咪雕像，全身绘有精美的传统花纹，眼睛仿佛会发光。 

![](examples/fig1.png)


动漫风格的风景画，有山脉、湖泊，也有繁华的小镇子，色彩鲜艳，光影效果明显。 

![](examples/fig2.png)


极具真实感的复杂农村的老人肖像，黑白。  

![](examples/fig3.png)


红烧狮子头 

![](examples/fig4.png)


车水马龙的上海街道，春节，舞龙舞狮。 

![](examples/fig5.png)


枯藤老树昏鸦，小桥流水人家。水墨画。 

![](examples/fig6.png)



## Limitations
妙笔的训练数据包含Laion-5B中的中文子集（经过清洗过滤），Midjourney相关的开源数据（将英文提示词翻译成中文），以及我们收集的一批数十万的caption数据。由于整个数据集大量缺少成语与古诗词数据，所以对成语与古诗词的理解可能存在偏差，对中国的名胜地标建筑数据的缺少以及大量的英译中数据，可能会导致出现一些对象的混乱，如果有以上较高数据质量的伙伴，希望能完善该项目，请与我们联系，我们根据提供的数据提供全新的版本。所有的模型均在8张4090显卡上完成训练，我们正在拓展我们的机器资源获得更优的结果，敬请期待。

Due to limitations in computing power and the size of Chinese datasets, the performance of Miaobi may be inferior to commercial models at this stage. We are expanding our computing resources and collecting larger scale data, looking forward to the future performance of Miaobi.


