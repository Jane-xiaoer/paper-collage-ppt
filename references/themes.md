# 8 套经典配色(艺术史提炼 · 内置换肤 + 强调色滑杆)

**配色机制**:8 套主题的变量全部内置在 `template.html` 的 `body.t1..t8` 类里,deck 左下角自带「✂ 风格」换肤面板(观众也能一键切换,选择存 localStorage),面板底部带**强调色滑杆**——只改 accent 色相、饱和度/明度锁定主题原值(拖不出脏色),拖过的值按主题分别记忆。**作者只需要把 `<body class="tN">` 的 N 换成初始主题**——不再手工替换 `:root`。深色 field 主题(t4/t5/t8)的 `dark-field` class 由脚本自动追加,不用管。

规则:
- 作者按内容气质定一个**初始主题**;观众切换是 feature 不是 bug
- 用户给任意 hex → 委婉拒绝,让选 8 套;**用户给参考图 → 按图逐要素提色**(field/paper/ink/accent/第二强调),在 template 里加成 t9+,同步加进换肤面板按钮和(若深色)JS 的 DARK 集合
- 改/加主题只动 template 的 `body.tN` 块 + 面板按钮,别的 CSS 全走 var

## 主题总表

| # | 主题 | 出处 | 气质 | 适合 |
|---|------|------|------|------|
| t1 | 马蒂斯剪纸 | Matisse 剪纸时期 | 艺术、经典拼贴 | 默认。艺术/创意/通用 |
| t2 | 蒙德里安 | Mondrian 新造型主义 | 极简、原色 | 设计/科技/方法论 |
| t3 | 包豪斯 | Bauhaus 构成主义 | 复古印刷 | 设计史/工艺/宣言 |
| t4 | 中国大红剪纸 🌑 | 民间剪纸/年画 | 传统、有力量 | 节日/国风/文化 |
| t5 | 克莱因蓝色纸 🌑 | Yves Klein IKB | 强烈、宣言 | demo day/观点/造势 |
| t6 | 报纸黑白×印刷红 | 报纸/risograph | 冷静、编辑部 | 锐评/新闻感 |
| t7 | 苔绿清晨 | 自然写生 | 清爽、呼吸感 | 生活方式/可持续 |
| t8 | 午夜墨×薄荷 🌑 | 夜场霓虹 | 冷冽、高级 | 科技夜场/放映 |

🌑 = 深色 field(换肤脚本自动加 `dark-field`)

具体 hex 一律以 `template.html` 的 `body.tN` 块为准(唯一真相源,这里不重复抄一遍免得改岔)。

## 主题 → 插画联动

选定主题后,插画 prompt 的调色板段替换成对应描述:

| 主题 | 插画调色板描述(英文进 prompt) |
|------|------------------------------|
| t1 马蒂斯剪纸 | cream paper field, matisse-blue cut-outs, peach and leaf-green paper accents, deep navy ink |
| t2 蒙德里安 | white field, black cut-paper lines, primary red yellow and blue paper tiles |
| t3 包豪斯 | warm grey-cream field, vermilion mustard and steel-blue geometric paper shapes |
| t4 中国大红剪纸 | chinese vermilion-red paper field, cream cut-paper, gold accents, ink black details |
| t5 克莱因蓝色纸 | klein-blue paper field, cream cut-outs, one bright yellow accent |
| t6 报纸×印刷红 | newsprint white field, black-and-white halftone cut-outs, one printing-red accent |
| t7 苔绿清晨 | pale sage-green field, off-white paper, forest-green accents |
| t8 午夜墨×薄荷 | near-black ink field, warm cream paper pieces, one mint accent |
