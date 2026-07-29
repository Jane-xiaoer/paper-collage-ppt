# 插画生成(nano-banana · 剪纸纸艺配方)

PPT 的文字全部真 HTML,插画只负责「画面」。插画统一用 nano-banana(gemini-3-pro-image-preview,走 nano-image-generator skill),配方移植自 paper-collage-ad 的实战结论。

## 核心配方:拍一个真实的手工纸艺 diorama

**最大的质量杠杆是取景动词**:提示「插画/剪纸拼贴 illustration」→ 又平又丑;提示「**真实手工纸艺立体模型的微距实拍照片**」→ 有景深、有真实光影、有纸的质感。永远描述「一个被拍摄的实物」,不是「一张被画的图」。

Nano 是 Gemini 底子,要**完整自然语言句子**,不吃 Midjourney 关键词堆砌;它的强项是语义保持——你没点名的它不乱动,所以负面块和材质/光线的精确描述特别值钱。

## 七段结构(每张图都完整重写,生成器没有记忆)

1. **媒介与镜头**:Ultra-detailed macro photograph of a handcrafted, layered paper-craft diorama, shot with a macro lens at a subtle three-quarter angle, museum-quality miniature paper set — NOT a flat illustration.
2. **主体与场景**:一个动作 + 点名每个纸片角色/道具(物理语言:纸质小人、翻落的卡纸)。
3. **材质**:uncoated fibre paper with visible tooth, hand-cut + machine-cut + deckled edges, warm-white keylines, fine round-dot halftone as printed texture, layered planes with real air and cast shadows between them.
4. **光**:single warm directional key light(用场景里的纸台灯/纸窗户把光「合理化」), soft diffused fill, long cast shadows, a glow pooling on the hero, cool shadow tones.
5. **调色板**:按选定主题替换(**必须查 `themes.md` 底部的主题联动表**);任何多彩现实物体(app 图标/logo)一律重绘成同调色板的纸片,严禁真实光泽 logo。
6. **相机收尾**:shallow depth of field, macro bokeh, hero tack-sharp, photorealistic RAW look, breathing negative space.
7. **负面块**:no glossy realistic icons, no rainbow clutter, no flat even lighting, no digital-vector look, no CGI plastic shine, no cartoon anime, no oversaturation, no busy background, no text, no watermark.

**第 7 段必须加 "no text"**——PPT 插画里的文字一律由 HTML 出,AI 画的字必乱码。这是本 skill 和广告版配方唯一的硬差异。

## PPT 场景 → 比例/用法对照

| 落位 | 比例 | 说明 |
|------|------|------|
| 左文右图(Layout 5) | 4:3 | 主落位;第一张值得 reroll 到美并锁为风格锚 |
| 章节幕封背景件 | 1:1 | 可选:一个小纸艺物件代替大字纸片 |
| 全场底纹(慎用) | 16:9 | 只在封面/收尾,压暗 40% 当底 |

命名 `{页号}-{语义}.png` 放 `images/`(如 `05-case.png`)。封面(L1)是居中海报式,不放插画。

## 风格锚定(整份 deck 一个手作世界)

- 第一张(封面图)先出:reroll 到真的好看,**锁定为风格锚**
- 之后每张都带两个参考图:①风格锚 ②最相关的前一张;prompt 里完整重述材质/光线/调色板段
- 锚没定型前别批量生成;**别用一张不满意的旧图当参考**——nano 会把丑处原样保下来
- 美感自检(生成后逐张问):光有方向吗?调色板克制统一吗?有唯一主角和留白吗?纸层之间有互相投的影子吗?任何一个「否」→ 改 prompt 重来

## 复制起点(封面示例,马蒂斯剪纸主题)

```
Ultra-detailed macro photograph of a handcrafted layered paper-craft diorama,
shot with a macro lens at a subtle three-quarter angle, museum-quality miniature
paper set, NOT a flat illustration. A small paper figurine at a paper desk,
lifting a big cut-paper lightbulb above its head, loose paper scraps settling
around. Uncoated fibre paper with visible tooth, hand-cut and deckled edges,
warm-white keylines, fine round-dot halftone as printed texture, layered paper
planes with real air and soft cast shadows between them. A single warm key light
from a tiny paper desk lamp on the left, soft diffused fill, long cast shadows,
a warm glow pooling on the figurine, cool shadow tones. Palette: cream paper
field, matisse-blue cut-outs, peach and leaf-green paper accents, deep navy ink. Shallow
depth of field, macro bokeh, the figurine tack-sharp, photorealistic RAW look,
breathing negative space. No glossy realistic icons, no rainbow clutter, no flat
even lighting, no digital-vector look, no CGI plastic shine, no cartoon anime,
no oversaturation, no busy background, no text, no watermark. 4:3.
```
