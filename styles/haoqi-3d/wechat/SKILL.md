---
name: haoqi-3d-wechat
version: 0.1.0
description: This skill should be used when the user asks to "用 3D 卡通风做公众号", "做一个好奇果冻风公众号排版", "把这篇文章排成 3D 卡通风", "做 3D 黏土风公众号版面", or requests a WeChat Official Account article using the Haoqi 3D / cute clay / jelly visual language. Produces WeChat-safe static HTML and image guidance; does not run Three.js inside the article.
---

# 好奇果冻 3D · 公众号排版 Skill

将文章排成明亮、年轻、有 3D 卡通记忆点的微信公众号正文。保留好奇果冻 3D 的视觉语言，但将 WebGL 场景转换为微信可渲染的静态 PNG 与 inline HTML。Three.js 只用于生成、截图或挑选素材，不进入公众号正文。

## 适用边界

触发于 3D 卡通公众号、黏土风公众号、果冻 3D 文章、年轻化视觉排版等请求。用户只要网页 PPT 时，走仓库根目录的多风格 PPT 工作流；用户要剪纸/卡纸公众号时，走现有公众号剪纸工作流。用户明确要求混搭时，先说明两套视觉语言的差异，再只在章节边界混搭，不把两套组件随机交叉。

## 工作流

### 1. 对齐文章与输出

完整文章已提供时直接分析；只有主题时，最多询问受众、文章目的和期望长度，其余采用合理假设并明确记录。确定：标题、摘要、封面图、正文 2–5 张图、章节数量、CTA 与是否只生成预览还是创建微信草稿。

将文章拆成：钩子 → 解释 → 方法/案例 → 复盘 → CTA。每个段落只承担一个信息任务。优先短句、具体动作和读者收益，避免连续的风格自嗨描述。

### 2. 建立 3D 视觉预算

先为每章选择语义素材，再决定版式：

- `hero`：一件承担记忆点的主物件或人物，通常占图片主体 30–60%。
- `support`：最多两件帮助解释论点的物件。
- `accent`：最多一件小型符号、贴纸或颜色节点。

使用 `references/haoqi-3d-wechat-images.md` 选择 balloon、camera、phone、gamepad、plant、skate 等素材。不要用随机黏土物件填空；物件必须对应记录、互动、成长、迭代等语义。

采用暖象牙、果冻蓝、珊瑚橙、柠檬黄、薄荷绿和深墨色的角色分工。避免整篇只用蓝色，也不要把 PPT 的蓝色渐变直接当成公众号底色。

### 3. 制作静态图片

使用已有 Deck 页面作为构图参考：

```text
styles/haoqi-3d/demo.html?p=0&still=1&s=plus
```

使用 `still=1` 关闭动画，截取干净静态图；或从 `styles/haoqi-3d/assets/clay/` 取透明 PNG，重新组合信息图。图片中不放中文、标题、数字、Logo 或关键说明，全部文字由正文 HTML 承载。按照 `references/haoqi-3d-wechat-images.md` 输出：头图 900×383，正文主图 900×506 或 900×675，单张不超过 1MB。

正文图片使用图片相框或 3D 卡片组件承托，不将图片直接散落在段落之间。上传前运行：

```bash
python3 scripts/upload-body-images.py article.md --dry-run
```

需要发布时再去掉 `--dry-run`，将本地图替换为微信 CDN URL。不要把 AppSecret 写进文章、skill 或示例文件。

### 4. 生成微信安全 HTML

读取 `references/haoqi-3d-wechat-components.md`。使用主题：

```text
assets/wechat-themes/haoqi-3d.json
```

组件只能使用适合微信的简单标签和 inline style。带 `background-image` 的面板外层必须是 styled `<section>`；微信可能清掉 styled `<div>` 的背景图。禁止 `flex`、`grid`、绝对定位、脚本、外链 CSS、WebGL、canvas、SVG、滤镜和混合模式。

保持以下组件节制：

- 开场卡：每篇 1 个。
- 黏土知识卡：每个大章节最多 2 个。
- 数据/对比卡：最多 2 个。
- CTA：结尾 1 个。
- 正文配图：每个大章节最多 1 张。

让主题默认的 h1/h2/h3/p 负责大部分排版，不让卡片变成每段文字的背景。每个正文 `<p>` 明确设置颜色。列表项之间压紧标签，避免公众号把换行识别为空 bullet。

### 5. 预览、验证和草稿

先生成 dry-run HTML，再用移动宽度预览；不要把 Chrome 预览当成微信最终结果。运行：

```bash
python3 scripts/validate-haoqi-wechat.py article.md
```

逐项检查 `references/haoqi-3d-wechat-checklist.md`。确认图片引用存在、禁止 CSS/HTML 特性未出现、图片大小合规。必要时使用 wechat-publisher 的 `publish.py` 走官方 API 创建草稿；先预检 token，只有 API 返回成功才报告草稿已创建。不要改走第三方 SaaS 或浏览器搬运发布。

### 6. 交付说明

交付时列出：文章 Markdown、dry-run HTML、封面图、正文图、主题 JSON、验证结果和微信草稿状态。明确说明：动态 3D 已转换为静态图片；修改文字在 Markdown/HTML 中完成，修改 3D 构图需要重新截图或重新组图。

## Additional Resources

- **`references/haoqi-3d-wechat-components.md`** — 微信安全的 3D 卡片、开场、步骤、数据和 CTA 组件。
- **`references/haoqi-3d-wechat-images.md`** — 静态 3D 图片、尺寸、裁切、语义素材和提示词规则。
- **`references/haoqi-3d-wechat-checklist.md`** — 公众号交付前的内容、视觉、HTML 和发布检查清单。
- **`assets/wechat-themes/haoqi-3d.json`** — 可供 wechat-publisher 注入的主题 JSON。
- **`examples/wechat-3d/article.md`** — 一篇可复制的示例文章结构。
- **`scripts/validate-haoqi-wechat.py`** — 检查微信禁用标签、CSS 能力、图片大小和本地引用。
