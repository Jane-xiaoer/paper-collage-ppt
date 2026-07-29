# 剪纸 CSS 工艺手册(v2)

template.html 的剪纸感来自一套固定「工艺」。v2 的核心升级:**纸片不再是笔直矩形**——不规则手剪轮廓、撕边大色块、层叠撕纸山景、剪贴字。改样式/加组件前读这份。

## 工艺分解

| 效果 | 实现 | 在哪 |
|------|------|------|
| 手剪轮廓 | 12 点微抖 `clip-path` 三档(`--cut` 默认 / `.cut2` / `.cut3`),白 keyline 宽度随轮廓抖动=手剪白边 | `.piece` 默认全带 |
| 纸片阴影 | **filter drop-shadow 双层**(`--lift-f/--lift-f-high`,box-shadow 会被 clip-path 剪掉所以必须用 filter) | `.piece`/`.torn-*` |
| 纸片受光面 | `.piece::before` 左上白→右下微沉的对角渐变(纸不是完全平的) | 所有纸片 |
| 纸片纤维 | `.piece::after` SVG 噪点(每张纸自带纹理,叠在全局颗粒之上) | 所有纸片 |
| 撕边大色块 | `.torn-b`(只撕下边)/`.torn-strip`(上下都撕)/`.torn-t`(只撕上边) | 章节块/横带/山景 |
| 撕纸山景 | `.hills`>3×`.hill.torn-t`,三层撕纸地平线,负 y 向 drop-shadow 出层叠 AO | 封面/收尾页底部 |
| 剪贴字 | `.chips span` 每字一张小纸片,nth-child 交替旋转,`.acc/.inkc/.tint/.kra` 换色 | 大标题(最强剪纸信号) |
| 和纸胶带 | `.tape`(颜色自动跟 `--accent-rgb`),`.tl/.tr/.tc` 三位 | `.pin` 里 |
| 订书钉 | `.staple`(`.sl/.sr`),半框+圆角模拟钉脚 | `.pin` 里 |
| 网点贴片 | `.dotfield` 圆形渐隐 halftone 补丁 | 空旷角落 |
| 纸星星 | `.scrap.star` 五角星 clip-path 纸屑 | 装饰 |
| 手工微旋转 | `.r0/.r1/.r2/.r-1/.r-2`(±0.4°~1.8°) | 所有纸片 |
| 纸浆斑驳 | `body::before` 大尺度低频 turbulence + 四角轻晕影(纸的色调不均匀) | 全局 |
| 纸片纤维方向 | `.piece::after` 细噪点 + 93° 隐约纤维纹;`::before` 加 inset 边缘吃光 | 所有纸片 |
| 撕纸块纹理 | `.torn-strip/.torn-b/.hill` 的 `::after` 纸浆噪点 | 撕边色块/山景 |
| 内置换肤 | `body.t1..t14` 主题类 + `#skinbar` 面板(观众可切,localStorage 记住;深色主题 JS 自动加 dark-field)+ **强调色滑杆**(只改 accent 色相,S/L 锁主题原值,按主题记忆;Jane 2026-07-28 终版拍板保留) | 全局 |
| 定格入场 | `steps(4/5)` 逐格「贴」上来 | `[data-drop]` |

## 六条不许动的工艺铁律

1. **胶带/订书钉必须贴在 `.pin` 包裹层里、`.piece` 外面**。贴进 piece 会被 clip-path 剪掉。结构:`<div class="pin r1" data-drop..><div class="piece...">内容</div><span class="tape tl"></span></div>`——旋转/入场标在 pin 上,`.high`/`.cut2` 标在哪层都行(CSS 变量会继承)。
2. **阴影 = 光从左上来**,全走 `--lift-f`/`--lift-f-high` 变量;唯一例外是山景的负 y 阴影(层叠 AO,已内置)。
3. **旋转只用预设五档**;胶带例外(±42deg)。
4. **同页三张以上纸片,剪裁轮廓不许全同**——cut 默认/cut2/cut3 轮着用。
5. **半调/网点是质感不是花纹**:透明度 ≤0.14,dotfield 每页 ≤1 个。
6. **steps() 不许换成 ease**。平滑=数字幻灯片,逐格=手工定格,这是分水岭。

## 剪贴字(chips)用法

```html
<h1 class="h-hero chips" data-drop="2"><span>把</span><span>想</span><span>法</span><span class="acc">剪</span><span>下</span><span>来</span></h1>
```

- 只给**大标题**用(封面/幕封/金句/CTA),正文标题用普通字——满屏 chips 会吵
- 每页 chips 里带色纸片(acc/inkc/tint/kra)≤3 张,其余留白纸
- 断行手动 `<br>`,每行 ≤7 字

## 深色 field 主题机制

`body.dark-field` 时:裸文字(直接躺在 field 上的)自动翻成 `--field-text`,纸片上的文字翻回 `--ink`;`.uline` 换成半透明 accent 垫色。主题需额外定义 `--field-text/--field-text-soft`(见 themes.md 标 🌑 的主题)。

## 常见微调(允许)

- 内边距/字号:inline style,单位 vw/vh
- 浮更高:加 `.high`;别自写阴影
- 撕边幅度:动 clip-path 点位 y 值 ±3% 以内
- 新纸色:优先 `.tinted/.kraft/.inked/.accent` 四档

## 已知边界

- clip-path 锯齿在 4K 大屏显直线段,观感尚可;别用 SVG filter url(#) 做真撕边(Safari 不稳)
- 字体走 Google Fonts CDN,断网降级系统字体;重要场合先联网打开一次
- `--rot` 与 data-drop:入场动画会重算 transform,旋转必须写进 `style="--rot:..."`,只挂 .r 类会被清零
- 大量 drop-shadow 在低端机可能掉帧;单页 `.piece` 控制在 8 张以内
