# 小耳 PPT 风格馆 · Xiaoer Deck Style Gallery

把一份大纲变成有完整视觉语言的网页 PPT。项目从「小耳剪纸风」起步，现在加入「好奇果冻 3D」，并采用独立风格目录继续扩展更多 3D 方向。An agent skill by **Xiaoer(小耳)** for creating expressive HTML presentation decks in multiple visual styles.

## 选择风格

通过 [`style-gallery.html`](./style-gallery.html) 进入风格馆，或访问 GitHub Pages（启用后：<https://jane-xiaoer.github.io/paper-collage-ppt/>）。也可以直接打开对应模板：

| 风格 | 视觉特征 | 适合 | 入口 |
|---|---|---|---|
| **小耳剪纸风** | 手剪纸片、艺术史配色、定格贴入 | 故事、课程、生活方式分享 | [`assets/template.html`](./assets/template.html) |
| **好奇果冻 3D** | 半透果冻字、黏土多巴胺物件、技术网格 | 设计、创意、年轻化产品演示 | [`styles/haoqi-3d/demo.html`](./styles/haoqi-3d/demo.html) |

> 好奇 3D 使用 ES Modules，需要通过 HTTP 服务预览：`python3 -m http.server 8788`。

## 剪纸风特性

- **单文件 HTML**:双击浏览器即放映(←→ / 滚轮 / 触屏 / 圆点导航),断网可用
- **14 套艺术史经典配色**:马蒂斯剪纸 / 蒙德里安 / 包豪斯 / 中国大红剪纸 / 克莱因蓝 / 报纸黑白×印刷红 / 苔绿清晨 / 午夜墨×薄荷 / 莫奈睡莲 / 梵高星夜 / 北斋浪 / 莫兰迪 / 敦煌壁画 / 波普艺术——观众可用左下「✂ 风格」面板一键换肤,附强调色滑杆(只改色相,拖不出脏色)
- **20 种布局骨架**:封面 / 目录 / 幕封 / 金句 / 三卡 / 左文右图(.flip 镜像)/ 流程 / 对比 / 数据 / 清单 / 时间轴 / 团队 / 双栏 / 四宫格 / 表格 / 全幅大图 / 问答 / 进度 / 图解 / 收束
- **剪纸工艺系统**:手剪轮廓纸片、剪贴字标题(每字一张小纸片)、撕纸山景、和纸胶带、订书钉、半调网点、三层纸质感
- **文字全部真 HTML**:永不乱码;插画由 nano-banana 按「实拍纸艺 diorama」配方生成(可选)
- **可编辑 PPTX 导出**：剪纸用 `python3 scripts/export-pptx-editable.py deck.html --theme t3`；好奇 3D 用 `python3 scripts/export-haoqi-pptx-editable.py path/to/deck.html --scheme plus`。好奇 3D 自动发现任意页数，并可通过 `registerPptx3D(...)` 将用户新增的任意 Three.js 主体拆为独立透明对象；两者均保留真文本框与可继续编辑的结构。

## 用法

这是一个 agent skill（Claude Code / Codex / 任意支持 SKILL.md 的框架）。把本仓库放进 skills 目录后，可以说：

- 「用小耳剪纸风做个分享」
- 「用好奇果冻 3D 做一个设计类 deck」
- 「先让我从现有 PPT 风格里选一个」

手动使用：先打开 `style-gallery.html` 选风格。剪纸风复制 `assets/template.html`；3D 风格按对应目录的 `README.md` 使用。

## 结构

```text
style-gallery.html          ← 风格选择入口
SKILL.md                    ← agent 路由与工作流
assets/template.html        ← 小耳剪纸风完整模板
styles/
├── README.md               ← 新风格扩展规范
└── haoqi-3d/
    ├── demo.html           ← 20 页好奇果冻 3D 示例
    ├── picker.html         ← 3D 素材筛选台
    ├── README.md           ← 使用方法与设计约束
    ├── wechat/SKILL.md     ← 好奇 3D 卡通公众号工作流
    ├── assets/             ← 风格专属素材
    └── vendor/             ← 本地 Three.js 运行时
references/                 ← 剪纸风配色 / 布局 / 工艺 / 检查清单
scripts/export-pptx-editable.py       ← 剪纸 HTML → 可编辑 PPTX
scripts/export-haoqi-pptx-editable.py ← 好奇 3D HTML → 可编辑 PPTX
```

## 公众号工作流

### 剪纸风公众号

同一套剪纸语言的公众号排版+配图：两套主题 JSON（`assets/wechat-themes/`，暖色浅底 / 艺术史海报深色版）、真纸组件库（`references/wechat-components.md`）和正文图上传脚本（`scripts/upload-body-images.py`）。

### 好奇果冻 3D 卡通公众号

读取 [`styles/haoqi-3d/wechat/SKILL.md`](./styles/haoqi-3d/wechat/SKILL.md)。该工作流把 3D Deck 的动态场景转换成微信安全的静态 PNG + inline HTML：Three.js 只用于制作和截取素材，不进入正文；主题为 `assets/wechat-themes/haoqi-3d.json`；组件规则在 `references/haoqi-3d-wechat-components.md`；配图尺寸、语义素材和提示词在 `references/haoqi-3d-wechat-images.md`；交付前运行 `python3 scripts/validate-haoqi-wechat.py article.md`。

所有正文图片都应在发布前用 `scripts/upload-body-images.py` 上传为微信 CDN URL。主题里的 `{{asset:*}}` 占位符使用自己的公众号 CDN 资产替换，不将 AppSecret 写入仓库。

## 血统

视觉体系来自 [paper-collage-ad](https://github.com/Jane-xiaoer/paper-collage-ad-codex)(剪纸拼贴广告视频 skill)的实战配方。两条硬教训直接继承:AI 渲染文字必乱码,精确内容一律真 HTML;工艺正确 ≠ 好看,美感层绝不能省。


## 关于小耳 · About Xiaoer

这套「小耳剪纸风」由 **小耳(Xiaoer)** 设计制作——一个用 AI 做点好玩的的独立创作者。

- 🏠 主站:[xiaoerai.xyz](https://xiaoerai.xyz)
- 🧰 工具墙:[tools.xiaoerai.xyz](https://tools.xiaoerai.xyz)
- 🐦 X:[@xiaoerzhan](https://x.com/xiaoerzhan)
- 💻 GitHub:[@Jane-xiaoer](https://github.com/Jane-xiaoer)

姊妹项目:[paper-collage-ad](https://github.com/Jane-xiaoer/paper-collage-ad-codex)(剪纸广告视频)· [paper-collage-ppt](https://github.com/Jane-xiaoer/paper-collage-ppt)(轻量版)· [paper-collage-cardstock](https://github.com/Jane-xiaoer/paper-collage-cardstock)(卡纸版)

Made with 👂 by 小耳

## License

MIT © Jane-xiaoer
