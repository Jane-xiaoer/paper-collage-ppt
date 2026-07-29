# 公众号配图(nano-banana · 纸艺 diorama 配方)

配方本体与 `paper-collage-ppt/references/image-prompts.md` 完全同源(七段结构:媒介与镜头/主体/材质/光/调色板/相机收尾/负面块),这里只写公众号特有的差异。**先读那份拿完整配方,再回来看这页。**

## 公众号特有规则

1. **一律横屏或方图,严禁竖图**(Jane 铁律:公众号不放竖屏素材)。正文插画 16:9 或 4:3。
2. **负面块必须含 no text**——文字信息全部由排版承载,AI 画字必乱码。
3. **调色板固定「暖象牙精品」**(warm ivory field, muted coral accent, soft charcoal and warm greys, natural kraft),和 paper-collage 主题的 #F3EDE2/#E4573D 纸面严丝合缝。手作/幕后类文章可换「牛皮纸工坊」(natural kraft-brown field, cream paper pieces, deep coffee ink, one persimmon-red accent),但一篇文章只用一套。
4. **数量克制**:封面 1 张 + 正文 2-4 张(每个大章节最多 1 张)。图是呼吸口,不是段落插花。

## 封面(发布时用)

- 公众号头图比例 **2.35:1**(900×383)。nano 按 **21:9** 生成,再居中裁到 900×383:
  ```bash
  sips -c 383 900 cover-raw.png --out cover-2.35.jpg
  ```
  (先 `sips --resampleWidth 900`,再裁高度;构图时把主角放正中 60% 安全区,两侧只留纸面留白)
- 次图(转发小图)1:1:从封面主角区居中裁方即可。
- 封面构图建议:一个纸艺主角 + 大面积暖纸留白,微距浅景深;别塞满。

## 正文插画选位

按文章结构挑 2-4 个「视觉可承载」的位置:

| 位置 | 画什么 | 比例 |
|------|--------|------|
| 开头钩子后 | 全文核心隐喻的纸艺场景(风格锚,先出这张) | 16:9 |
| 每个大章节 | 该章节的一个具体动作/物件,纸艺化 | 16:9 或 4:3 |
| 结尾 CTA 前 | 收束意象(纸艺小人挥手/合上的纸盒...) | 16:9 |

所有正文图生成后:
1. 套 `components.md` 的「图片相框」组件插入 md
2. 发布前跑 `scripts/upload-body-images.py` 换成微信 CDN URL
