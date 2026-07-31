---
name: paper-collage-ppt
description: 生成「剪纸拼贴 / 手工纸艺」风格的横向翻页网页 PPT(单 HTML 文件):14 套艺术史经典配色 + deck 内置一键换肤面板 + 强调色滑杆 + 20 种布局(封面/目录/幕封/金句/三卡/图文/流程/对比/数据/清单/时间轴/团队/双栏/四宫格/表格/大图/问答/进度/图解/收尾),文字全部真 HTML 永不乱码,可导出可编辑 PPTX。当用户说"剪纸 PPT""剪纸风演示""拼贴风 PPT""纸艺幻灯片""paper collage deck"时使用。
---

# Paper Collage PPT · 剪纸拼贴演示

把一份大纲或文章变成「剪纸拼贴」风格的单文件网页 PPT:所有内容像剪好的纸片一张张贴在纸面上,翻页时逐格「贴」上来(定格动画手感),需要画面的页面配 nano 生成的手工纸艺插画。

**血统**:视觉体系来自 `paper-collage-ad`(剪纸广告视频 skill)的实战配方——「实拍纸艺 diorama」美学、克制调色板、暖光投影;工程骨架借鉴 `guizang-ppt-skill` 的单文件 HTML 路线。两条硬教训直接继承:①AI 渲染文字必乱码,精确内容一律真 HTML;②工艺正确 ≠ 好看,美感层(光/色/主次/留白)绝不能省。

## 何时用 / 不用

**合适**:分享会、课程、产品故事、手作/生活方式主题、任何想要「温暖、手工、有记忆点」的演讲;公众号文章改讲稿。
**不合适**:大表格/密集图表(用常规 PPT)、严肃商务汇报(风格太俏皮)、需要多人协作编辑的场合。

## 工作流

### Step 1 · 对齐(动手前,最多 3 问)

用户给了完整大纲/文章 → 跳过直接 Step 2。只给了主题 → 最多问 3 个问题:①讲给谁听、什么场合?②时长(定页数:10 分钟≈8-10 页,20 分钟≈12-16 页)?③有没有现成素材/硬约束?其余自己做合理假设并在回复里说明。

### Step 2 · 大纲与节奏

按叙事弧搭骨架:钩子 → 定调 → 主体 → 转折 → 收束(页数分配见 `references/layouts.md` 尾部)。同时列出**每页的底色节奏**(field / deep / ink),规则在 layouts.md「页面节奏规划」——无连续 3 页同底色,每 3-4 页一个深底呼吸页。大纲 + 节奏表先给用户确认再动手写 HTML。

### Step 3 · 定初始主题(14 套艺术史配色,内置换肤+滑杆)

读 `references/themes.md` 总表,按内容气质推荐**初始主题**,把模板 `<body class="tN">` 换成对应编号即可——14 套变量和左下角「✂ 风格」换肤面板都内置在模板里,观众/用户随时一键切换(深色主题的 dark-field 由脚本自动处理)。**不接受自定义 hex、不许混搭**;用户给参考图 → 按图逐要素提色加成 t15+(方法在 themes.md 开头)。

### Step 4 · 拷模板 + 填布局

```bash
mkdir -p "项目/XXX/ppt/images"
cp <SKILL_DIR>/assets/template.html "项目/XXX/ppt/index.html"
```

template.html 完整可运行,内置 7 个示例页展示全部工艺。然后:

1. 立刻替换 `<title>` 等 `[必填]` 占位
2. 打开 `references/layouts.md`,按大纲从 **20 种布局骨架**里挑,整段粘贴改文案——**不要从零写 slide,不要发明新类名**
3. 纸片工艺(手剪轮廓/pin 包裹/剪贴字/撕边/山景/data-drop 入场)的规矩在 layouts.md 顶部「手工感五铁律」和 `references/paper-craft-css.md` 六条铁律,写每页时遵守
4. 微调只改 inline style(vw/vh 单位)

### Step 5 · 配插画(可选)

**先拍板配色,再生成插画**:排版出来后让用户用左下换肤面板实景试 14 套、定下最终主题,然后再生成插画——插画调色板是生成时烤死的,不会跟着换肤,这个顺序能保证图和版面永远同色系。之后读 `references/image-prompts.md`,用 nano-image-generator 按「实拍纸艺 diorama」七段配方生成。要点:封面是居中海报式不放图,插画主要落位在 L5 左文右图/幕封;先出第一张插画 reroll 到美并锁为风格锚,后续图带锚做参考;调色板跟主题联动(themes.md 底部对照表);**prompt 负面块必须含 no text**。没有 GEMINI key 或用户不要图 → 全 deck 纯排版也成立(模板的纸片体系不依赖插画)。

### Step 6 · 自检

逐项过 `references/checklist.md`(P0 全过才能交)。跑一遍自检命令,并用无头 Chrome 截 2-3 页人眼看一遍美感:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --window-size=1600,900 --virtual-time-budget=5000 \
  --screenshot=/tmp/check.png "file://$(pwd)/index.html#3"
```

### Step 7 · 交付

`open index.html` 直接帮用户打开(不要给路径让用户自己找);说明操作:键盘 ←→ / 滚轮 / 触屏滑动 / 底部圆点,URL 带 `#页号` 可直达。

**要 PPTX?** 用户要 PowerPoint 文件时:

```bash
python3 <SKILL_DIR>/scripts/export-pptx-editable.py deck.html --theme t15 -o 分享.pptx
```

**三层分解导出**:背景=底纹装饰截图;**每张纸片=独立图片形状**(可选中/拖动/拉伸,纹理跟着变);文字=真文本框(位置/字号/颜色/旋转对位)。所以在 PowerPoint/Keynote 里:改字 ✅、挪纸片 ✅、文字变长把纸片拉大 ✅——版式可以继续调。边界:换配色/加新页回 HTML 重导;纯 CSS 色块元素(轻量版少数)仍烤在背景;马克笔垫色不跟随文字。依赖 python-pptx + 本机 Chrome。

## 资源导览

```
paper-collage-ppt/
├── SKILL.md                      ← 你在读
├── assets/
│   └── template.html             ← 完整可运行模板 v2(7 示例页 = 工艺全展示)
├── scripts/
│   ├── export-pptx.py            ← HTML deck → 16:9 PPTX(逐页截图,可 --theme 指定配色)
└── references/
    ├── themes.md                 ← 14 套艺术史配色总表 + 换肤/滑杆机制 + 插画调色板联动表
    ├── layouts.md                ← 20 种布局骨架 + 节奏规划 + 手工感五铁律
    ├── paper-craft-css.md        ← 剪纸 CSS 工艺分解(v2) + 六条不许动的铁律
    ├── image-prompts.md          ← nano 纸艺 diorama 配方(PPT 版,强制 no text)
    └── checklist.md              ← P0/P1/P2 交付检查清单
```


**加载顺序**:SKILL.md → (Step 2 后) themes.md → layouts.md → 动手写页 → (要配图) image-prompts.md → checklist.md。paper-craft-css.md 在需要微调样式或加组件时查。

## 设计哲学

1. **一页一件事** — 每页一个论点、一个视觉动作;贪多就拆页
2. **文字是内容,插画是气氛** — 真 HTML 文字承载全部信息,拿掉所有插画 deck 依然成立
3. **手工感来自不完美** — 微旋转、逐格入场、胶带纸屑;但不完美是设计出来的,五档旋转之外的随意才是真乱
4. **克制优于堆料** — 一套调色板、留白 ≥40%、每页手工痕迹 ≤3 种
5. **工艺正确只是及格,美感层才是分数** — 光的方向、色的克制、主次与留白,每页都要过美感自检
