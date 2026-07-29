# Paper Collage PPT · 剪纸拼贴演示

把一份大纲变成「剪纸拼贴」风格的单文件网页 PPT:内容像剪好的纸片一张张贴在纸面上,翻页时逐格「贴」上来(定格动画手感)。An agent skill that turns an outline into a paper-collage style single-file HTML deck.

## 特性

- **单文件 HTML**:双击浏览器即放映(←→ / 滚轮 / 触屏 / 圆点导航),断网可用
- **8 套艺术史经典配色**:马蒂斯剪纸 / 蒙德里安 / 包豪斯 / 中国大红剪纸 / 克莱因蓝 / 报纸黑白×印刷红 / 苔绿清晨 / 午夜墨×薄荷——观众可用左下「✂ 风格」面板一键换肤,附强调色滑杆(只改色相,拖不出脏色)
- **10 种布局骨架**:封面(居中海报式)/ 幕封 / 金句 / 三卡 / 左文右图(支持 .flip 镜像)/ 流程 / 对比 / 数据 / 清单 / 收束
- **剪纸工艺系统**:手剪轮廓纸片、剪贴字标题(每字一张小纸片)、撕纸山景、和纸胶带、订书钉、半调网点、三层纸质感
- **文字全部真 HTML**:永不乱码;插画由 nano-banana 按「实拍纸艺 diorama」配方生成(可选)
- **一键导出 PPTX**:`python3 scripts/export-pptx.py deck.html --theme t3`

## 用法

这是一个 agent skill(Claude Code / Codex / 任意支持 SKILL.md 的框架):把本仓库放进 skills 目录,对 agent 说「用剪纸风格做个分享」。手动使用:复制 `assets/template.html`,按 `references/layouts.md` 挑布局填内容即可。

## 结构

```
SKILL.md          ← agent 工作流(必读入口)
assets/template.html   ← 完整可运行模板(10 示例页 = 布局全菜单)
references/       ← 配色 / 布局 / 工艺 / 插画配方 / 检查清单
scripts/export-pptx.py ← HTML → 16:9 PPTX
```

## 血统

视觉体系来自 [paper-collage-ad](https://github.com/Jane-xiaoer/paper-collage-ad-codex)(剪纸拼贴广告视频 skill)的实战配方。两条硬教训直接继承:AI 渲染文字必乱码,精确内容一律真 HTML;工艺正确 ≠ 好看,美感层绝不能省。

## License

MIT © Jane-xiaoer
