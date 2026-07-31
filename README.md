# 小耳剪纸风 · Xiaoer Paper Collage PPT

把一份大纲变成「剪纸拼贴」风格的单文件网页 PPT:内容像剪好的纸片一张张贴在纸面上,翻页时逐格「贴」上来(定格动画手感)。An agent skill by **Xiaoer(小耳)** that turns an outline into a paper-collage style single-file HTML deck.

## 特性

- **单文件 HTML**:双击浏览器即放映(←→ / 滚轮 / 触屏 / 圆点导航),断网可用
- **14 套艺术史经典配色**:马蒂斯剪纸 / 蒙德里安 / 包豪斯 / 中国大红剪纸 / 克莱因蓝 / 报纸黑白×印刷红 / 苔绿清晨 / 午夜墨×薄荷 / 莫奈睡莲 / 梵高星夜 / 北斋浪 / 莫兰迪 / 敦煌壁画 / 波普艺术——观众可用左下「✂ 风格」面板一键换肤,附强调色滑杆(只改色相,拖不出脏色)
- **20 种布局骨架**:封面 / 目录 / 幕封 / 金句 / 三卡 / 左文右图(.flip 镜像)/ 流程 / 对比 / 数据 / 清单 / 时间轴 / 团队 / 双栏 / 四宫格 / 表格 / 全幅大图 / 问答 / 进度 / 图解 / 收束
- **剪纸工艺系统**:手剪轮廓纸片、剪贴字标题(每字一张小纸片)、撕纸山景、和纸胶带、订书钉、半调网点、三层纸质感
- **文字全部真 HTML**:永不乱码;插画由 nano-banana 按「实拍纸艺 diorama」配方生成(可选)
- **可编辑 PPTX 导出**:`python3 scripts/export-pptx-editable.py deck.html --theme t3`——三层分解(背景/纸片独立图形/真文本框),在 PowerPoint 里改字、挪纸片、拉纸片都行

## 用法

这是一个 agent skill(Claude Code / Codex / 任意支持 SKILL.md 的框架):把本仓库放进 skills 目录,对 agent 说「用剪纸风格做个分享」。手动使用:复制 `assets/template.html`,按 `references/layouts.md` 挑布局填内容即可。

## 结构

```
SKILL.md          ← agent 工作流(必读入口)
assets/template.html   ← 完整可运行模板(10 示例页 = 布局全菜单)
references/       ← 配色 / 布局 / 工艺 / 插画配方 / 检查清单
scripts/export-pptx-editable.py ← HTML → 可编辑 PPTX(三层分解)
```

## 公众号工作流(v1.2 新增)

同一套剪纸语言的公众号排版+配图:两套主题 JSON(`assets/wechat-themes/`,暖色浅底 / **艺术史海报深色版**:深炭底+米卡宋体撕边标题条+藏蓝芥黄砖红)、真纸组件库(`references/wechat-components.md`)、正文图上传脚本(`scripts/upload-body-images.py`)。主题里的 `{{asset:*}}` 占位符用你自己的公众号 CDN 资产替换(生成管线见组件库文档,素材源在姊妹仓 [paper-collage-cardstock](https://github.com/Jane-xiaoer/paper-collage-cardstock))。

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
