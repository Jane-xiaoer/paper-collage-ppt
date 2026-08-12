# 好奇果冻 3D · 公众号配图规则

## 核心转换

将 3D Deck 的动态场景转成公众号静态配图：

1. 通过 `styles/haoqi-3d/demo.html?p=N&still=1&s=plus` 选择相关页面，保留静态渲染。
2. 或从 `styles/haoqi-3d/assets/clay/` 选择透明黏土 PNG，重新组合成单张信息图。
3. 图片中不生成任何文字；标题、数字和图注由 HTML 负责。
4. 让素材语义服务文章论点：相机对应记录，耳机对应聆听，手柄对应互动，植物对应生长，不要随机挑图。

## 尺寸

- 公众号头图：900×383，约 2.35:1；主角置于中央 60% 安全区。
- 正文主图：900×506，16:9；适合开头钩子和章节转场。
- 正文辅助图：900×675，4:3；适合单个物件或局部解释。
- 不使用竖版 9:16 作为正文默认图；本工作流以横图和方/近方构图为主。
- 单张上传前压缩到 ≤1MB。

## 生成/重组提示词

```text
A polished 3D clay illustration for a Chinese WeChat article, one clear semantic hero object: [OBJECT],
rounded toy-like geometry, handmade clay surface, saturated coral, lemon yellow, cobalt blue,
mint green and warm cream accents, soft studio lighting from upper left, gentle contact shadow,
clean warm ivory background, generous negative space around the object, editorial product illustration,
16:9 composition, no text, no letters, no logo, no watermark, no UI, no tiny details, no extra objects.
```

## 图位策略

| 文章位置 | 推荐素材 | 作用 |
|---|---|---|
| 开头钩子后 | balloon / rainbow / dop_heart | 先给情绪和记忆点 |
| 方法章节 | dop_cam / laptop / dop_phone | 把抽象方法落到动作 |
| 创作章节 | pop_boba / pop_boombox / pop_vinyl2 | 建立年轻、生活化气质 |
| 复盘章节 | cube / stack / ring | 表达结构、层级、迭代 |
| 结尾 CTA | girl_skate / girl_dance / pop_sneaker | 让文章轻快收束 |

## 封面裁切

先生成 21:9 或使用静态 Deck 截图，再裁成 900×383。主角不能贴近左右边缘；预留标题安全区，但不把标题烤进图里。
