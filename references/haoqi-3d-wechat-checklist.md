# 好奇果冻 3D 公众号交付检查清单

## 内容

- [ ] 标题有情绪钩子或具体收益，不写“关于 3D 风格的思考”。
- [ ] 每段只推进一个观点，删掉纯过渡句。
- [ ] hero、support、accent 与文章语义对应。
- [ ] 正文保留真 HTML 文字，图片不承载关键信息。

## 视觉

- [ ] 主色使用暖象牙、果冻蓝、珊瑚橙、柠檬黄、薄荷绿；蓝不是大面积唯一颜色。
- [ ] 开头有一个明确的 3D 视觉锚点。
- [ ] 每个大章节最多一张正文主图。
- [ ] 同一篇文章不混用剪纸真纸组件和 3D 卡通组件，除非用户明确要求混搭。
- [ ] 不让图片与标题争夺同一视觉层级。

## 微信 HTML

- [ ] 无 `script`、`style`、外链 CSS、Three.js、canvas、SVG、video。
- [ ] 无 `display:flex`、`display:grid`、`position:absolute`、`position:fixed`、`float`、`filter`、`mix-blend-mode`。
- [ ] 带 `background-image` 的面板外层使用 styled `<section>`，不用 styled `<div>`。
- [ ] 每个 `<p>` 明确设置 `color`。
- [ ] 列表项之间没有多余换行；`<li>` 内没有多余 `<p>` 包裹。
- [ ] 所有正文图片是 PNG/JPG，单张 ≤1MB；图片引用已替换为微信 CDN URL。
- [ ] HTML 只保留微信允许的 inline style。

## 发布

- [ ] 先运行 `md2wechat convert` 或 wechat-publisher 的 dry-run。
- [ ] 本地移动宽度预览通过。
- [ ] 先推草稿，不直接发布。
- [ ] 用微信后台/手机确认背景图、字号、列表、图片比例。
- [ ] 只有 API 返回 `media_id` 或明确成功，才报告草稿已创建。
