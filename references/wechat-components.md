# 剪纸组件库(公众号版 · 真纸资产,raw HTML 直接嵌进 md)

> **2026-07-29 起为真纸资产版**(Jane 实测拍板:CSS 平色块「不够剪纸」)。所有纸片/标题条/分隔用实拍卡纸 PNG(微信 CDN 永久地址),颜色预烘焙(微信不认 blend-mode)。
> `{{asset:名字}}` 为占位符——用你自己的公众号凭证按下述管线生成资产并替换(素材源在姊妹仓 paper-collage-cardstock 的 assets/paper/);补新资产走 `references/`(卡纸配方)→ PIL multiply 预染色+quantize(≤1MB)→ uploadimg 上传→回填 json。主题 JSON(h1/h2/h3/blockquote)也已用这些资产。

## 微信管线硬约束(违反=组件被剥/穿帮)

1. **只能用 `<div>/<b>/<img>`**;class/id/section/span 全被 sanitize 剥。主题表内标签自定义 style 会被注入抢位。
2. **不用 position:absolute / float**;叠放用负 margin。
3. **撕边 PNG 下严禁 box-shadow**——阴影跟矩形盒子走,撕边外露出直角阴影必穿帮;要浮起感靠资产自带的边缘烘焙。
4. **面板一律 `background-image:url(资产);background-size:100% 100%`**,颜色换资产不换 background-color(没有 blend-mode)。
5. 正文插画先 `scripts/upload-body-images.py` 传 CDN。

## 1 · 金句大纸卡(真胶带 + 米卡面板)

```html
<div style="text-align:center;margin:32px 0;">
<img src="{{asset:tape}}" style="width:92px;display:block;margin:0 auto -16px;transform:rotate(-4deg);position:relative;z-index:2;">
<div style="background-image:url({{asset:panel-cream}});background-size:100% 100%;padding:34px 30px;margin:0 10px;transform:rotate(-0.8deg);">
<b style="font-size:17px;line-height:1.9;color:#201C18;font-weight:900;">金句正文</b>
</div>
</div>
```

## 2 · 序号步骤纸片(米卡/芥黄交替)

```html
<div style="margin:26px 0;">
<div style="background-image:url({{asset:panel-cream}});background-size:100% 100%;padding:24px 24px;margin:0 8px 14px;transform:rotate(-0.6deg);">
<b style="font-size:20px;color:#D94F2B;font-weight:900;">01</b>&nbsp;&nbsp;<b style="font-size:15px;color:#201C18;">步骤标题</b>
<div style="font-size:14px;line-height:1.8;color:#6A6157;margin-top:6px;">一两句说明。</div>
</div>
<div style="background-image:url({{asset:panel-mustard}});background-size:100% 100%;padding:24px 24px;margin:0 8px 14px;transform:rotate(0.6deg);">
<b style="font-size:20px;color:#A2452A;font-weight:900;">02</b>&nbsp;&nbsp;<b style="font-size:15px;color:#201C18;">步骤标题</b>
<div style="font-size:14px;line-height:1.8;color:#6A5A42;margin-top:6px;">一两句说明。</div>
</div>
</div>
```

(角度正负交替;米卡/芥黄交替;件数不限但 ≤5)

## 3 · 牛皮纸便签(提示/注意)

```html
<div style="background-image:url({{asset:panel-kraft}});background-size:100% 100%;padding:26px 24px;margin:26px 10px;transform:rotate(0.5deg);">
<b style="font-size:14px;color:#8A4B2E;letter-spacing:2px;">✂ 注意</b>
<div style="font-size:14px;line-height:1.85;color:#57482F;margin-top:8px;">提示内容两三行以内。</div>
</div>
```

## 4 · 图片相框(正文插画统一用,米卡面板托底)

```html
<div style="background-image:url({{asset:panel-cream}});background-size:100% 100%;padding:22px 22px 16px;margin:28px 6px;transform:rotate(0.6deg);">
<img src="images/xx.jpg" style="display:block;width:100%;" alt="">
<div style="font-size:12px;color:#9C8F79;letter-spacing:2px;text-align:center;padding:6px 0 4px;">图注一句话</div>
</div>
```

相邻两个相框旋转方向相反。

## 5 · 撕纸分隔条

```html
<div style="background-image:url({{asset:strip-tan}});background-size:100% 100%;height:24px;margin:36px 4px;transform:rotate(-0.4deg);"></div>
```

## 6 · 文末落款(黑撕边条)

```html
<div style="text-align:center;margin:40px 0 16px;">
<div style="display:inline-block;background-image:url({{asset:bar-ink}});background-size:100% 100%;color:#F5EFE2;font-size:13px;letter-spacing:3px;padding:11px 24px;transform:rotate(-1deg);">小耳 · 用 AI 做点好玩的</div>
</div>
```

## 使用节制

金句纸卡 ≤2、便签 ≤2、步骤片 ≤1 组、撕纸分隔 ≤3。组件是重音不是背景音——大部分段落让主题默认排版(黑撕边 h2 条/米卡 h3 条/panel 引用卡都已是真纸)说话。
