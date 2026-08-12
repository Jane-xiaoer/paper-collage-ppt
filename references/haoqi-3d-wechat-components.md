# 好奇果冻 3D · 公众号组件库

公众号正文不能运行 Three.js、WebGL、ES Modules 或 CSS 动画。3D 风格的正确转换是：**用 Three.js 生成/截取静态 PNG，再用微信安全 HTML 排版**。文字始终是真 HTML。

## 微信兼容硬约束

1. 组件只使用 `<section>`、`<div>`、`<b>`、`<img>`、`<br>`；不要使用 `class`、`id`、`span`、`style` 标签、外链 CSS。
2. 需要显示 `background-image` 的面板，外层必须使用带 inline style 的 `<section>`；微信正文可能清掉 `<div>` 上的背景图。
3. 不使用 `display:flex`、`display:grid`、`position:absolute`、`position:fixed`、`float`、`mix-blend-mode`、`filter` 或 CSS animation。
4. 每段正文显式写 `color`；图片使用 `display:block;width:100%;height:auto`。
5. 纸面背景、面板背景、阴影和纹理必须预烘焙进 PNG；不要指望微信支持 Three.js 材质或浏览器特效。
6. 原始 PNG 先压缩到微信接口要求的单张 ≤1MB，再通过 `upload-body-images.py` 上传 CDN。

## 1. 3D 开场卡

```html
<section style="background-image:url({{asset:panel-blue}});background-size:100% 100%;padding:24px 20px;margin:28px 4px;">
<img src="images/balloon.png" style="display:block;width:58%;margin:0 auto 12px;" alt="彩色黏土热气球">
<b style="display:block;text-align:center;color:#FFF8E8;font-size:22px;line-height:1.45;">把复杂的东西，讲得更有趣</b>
<div style="text-align:center;color:#FFDAA9;font-size:13px;line-height:1.7;margin-top:8px;">HAOQI 3D VISUAL LANGUAGE</div>
</section>
```

## 2. 黏土知识卡

```html
<section style="background:#FFFFFF;padding:20px 18px;margin:24px 4px;border:1px solid #DCE8F2;">
<img src="images/pop_pad.png" style="display:block;width:34%;margin:0 0 10px;" alt="黏土游戏手柄">
<b style="display:block;color:#425FC9;font-size:16px;line-height:1.5;">01 · 先建立一个视觉锚点</b>
<div style="color:#3F4652;font-size:14px;line-height:1.85;margin-top:6px;">一页只解决一个问题。让 hero 资产承担记忆点，让正文负责解释。</div>
</section>
```

## 3. 三栏替代方案：不用 flex/grid

微信环境不可靠时，用连续 block 卡片模拟三栏，不追求桌面端并排：

```html
<section style="margin:26px 0;">
<div style="background:#FFF0D6;padding:18px;margin:0 0 10px;">
<b style="color:#EF7650;font-size:20px;">01</b><br><b style="color:#151A22;font-size:15px;">颜色先行</b>
<div style="color:#5E6878;font-size:14px;line-height:1.8;margin-top:5px;">先定角色色，再选素材。</div>
</div><div style="background:#DCE8F2;padding:18px;margin:0 0 10px;">
<b style="color:#425FC9;font-size:20px;">02</b><br><b style="color:#151A22;font-size:15px;">层级清楚</b>
<div style="color:#5E6878;font-size:14px;line-height:1.8;margin-top:5px;">hero、support、accent 各司其职。</div>
</div>
</section>
```

## 4. 数据/对比卡

```html
<section style="background:#151A22;padding:22px 20px;margin:28px 4px;">
<b style="display:block;color:#FFF8E8;font-size:17px;line-height:1.5;">一页的视觉预算</b>
<div style="color:#FFDAA9;font-size:14px;line-height:2;margin-top:10px;">1 个 hero　·　2 个 support　·　1 个 accent</div>
<div style="color:#B7C4D6;font-size:13px;line-height:1.8;margin-top:6px;">减少无意义的物件，保留真正帮助理解的物件。</div>
</section>
```

## 5. 结尾 CTA

```html
<section style="text-align:center;background:#F6C66B;padding:26px 20px;margin:34px 4px;">
<img src="images/girl_skate.png" style="display:block;width:30%;margin:0 auto 8px;" alt="滑板黏土人物">
<b style="display:block;color:#151A22;font-size:20px;line-height:1.5;">下一篇，继续玩</b>
<div style="color:#5E4B35;font-size:13px;line-height:1.8;margin-top:6px;">小耳 · 用 AI 做点好玩的</div>
</section>
```

## 使用节制

开场卡 1 个、知识卡每章最多 2 个、数据/对比卡最多 2 个、CTA 1 个。正文配图每个大章节最多 1 张。3D 资产是视觉锚，不是每一段文字旁边都放一个玩具。
