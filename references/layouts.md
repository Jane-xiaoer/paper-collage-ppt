# 布局骨架(10 种 · 直接粘贴改文案,不要从零写 slide)

每个骨架都是完整的 `<section>`,粘进 `<main id="deck">` 即可。所有类名都在 `template.html` 的 `<style>` 里有定义——**不要发明新类名**,微调用 inline `style="..."`。

## Pre-flight 类名清单

`piece / tinted / kraft / inked / accent / straight / high / cut2 cut3 / pin / r0 r1 r2 r-1 r-2 / torn-strip torn-b torn-t / hills hill / chips (acc inkc tint kra) / halftone / dotfield / tape (tl tr tc neutral) / staple (sl sr) / kicker / h-hero / h-xl / h-md / h-hand / lead / body-s / label (paper accent) / uline / grid-2 / grid-3 / grid-7-5 / grid-5-7 / stack / card / card-nb / frame / ph / img-cap / steps / step / step-nb / step-title / step-desc / arrow-hand / stat / stat-nb / stat-unit / stat-note / scrap (dot star c-accent c-kraft c-ink c-tint) / data-drop`

## 页面节奏规划(挑布局前先做)

- 底色三档:默认 field(`class="slide"`)、深底纸(`slide deep`)、墨底(`slide ink halftone`)
- **连续 3 页以上同底色不允许**;8 页以上必须有 ≥1 个 `ink` 页;每 3-4 页一个深底呼吸页
- 生成后自检:`grep 'class="slide' index.html` 人工过节奏

## 手工感五铁律(所有布局通用)

1. **胶带/订书钉只能贴在 `.pin` 里 `.piece` 外**(贴进 piece 被剪掉)——见 paper-craft-css.md 铁律 1
2. **纸片永远微旋转**,同页角度正负交替,绝不全部摆正
3. **同页多张纸片剪裁轮廓不许全同**(默认/cut2/cut3 轮着用)
4. **阴影方向全场一致**(光从左上),不自写阴影
5. 每页至少一个手工痕迹(胶带/钉/纸屑/网点贴片/手写字/撕边),但 ≤3 种

## 版式怎么「选」

- **写稿时选**:下面 10 种骨架就是版式菜单,按每页内容挑(这是主要的选择方式)
- **改稿时翻面**:所有左右布局(grid-2/grid-7-5/grid-5-7)加 `.flip` 类即整页左右镜像——用户说「这页图放左边试试」时一个类搞定,不用重排
- **不做观众侧版式切换**:配色是氛围可以切(换肤面板),版式是叙事结构不该切——别给 deck 加版式切换按钮

## data-drop 入场规则

- 每页 3-6 个主要纸片按视觉顺序标 `data-drop="1".."6"`
- **带 r 类的必须同时写 `style="--rot:对应角度"`**(r0=-0.4deg / r1=1deg / r2=1.8deg / r-1=-1deg / r-2=-1.7deg),否则入场后旋转被清零
- 装饰 scrap/hills 不标(常驻)

---

## Layout 1 · 封面(居中海报式)

剪贴字居中放大 + 撕纸山景,封面不放插画(海报感靠字和山景撑,插画留给 L5/幕封)。

```html
<section class="slide">
  <div class="hills"><div class="hill torn-t"></div><div class="hill torn-t"></div><div class="hill torn-t"></div></div>
  <div class="dotfield" style="width:10vw;height:10vw;top:12vh;left:7vw"></div>
  <div class="scrap star c-accent" style="width:1.7vw;height:1.7vw;top:15vh;right:20vw;transform:rotate(12deg)"></div>
  <div class="scrap dot c-kraft" style="width:1vw;height:1vw;top:22vh;left:16vw"></div>
  <div class="stack" style="align-items:center;text-align:center;gap:3.2vh;position:relative;z-index:2">
    <span class="label accent r-1" data-drop="1" style="--rot:-1deg">KICKER 短语</span>
    <h1 class="h-hero chips" data-drop="2" style="font-size:6.2vw"><span>主</span><span>标</span><span class="acc">题</span><br><span class="tint">第</span><span>二</span><span>行</span></h1>
    <p class="lead" data-drop="3">一句话副标题。</p>
    <p class="body-s" data-drop="4" style="letter-spacing:.22em">讲者 · 日期 · 场合</p>
  </div>
</section>
```

## Layout 2 · 章节幕封(撕边大色块)

```html
<section class="slide ink halftone">
  <div class="grid-5-7">
    <div class="pin r-2 high" data-drop="1" style="--rot:-2deg">
      <div class="torn-b" style="background:var(--accent);padding:12vh 2vw 14vh;text-align:center">
        <span style="font-family:var(--serif);font-size:9vw;font-weight:900;color:var(--paper);line-height:1">壹</span>
      </div>
      <span class="tape tc neutral"></span>
    </div>
    <div class="stack">
      <span class="kicker" data-drop="2">CHAPTER ONE</span>
      <h2 class="h-xl chips" data-drop="3"><span>章</span><span class="acc">节</span><span>标</span><span>题</span></h2>
      <p class="lead" data-drop="4">一句话预告这一幕。</p>
    </div>
  </div>
</section>
```

## Layout 3 · 观点金句页(订书钉纸片 + 撕纸横带)

```html
<section class="slide deep">
  <div class="torn-strip" data-drop="1" style="position:absolute;left:-3vw;right:-3vw;top:56vh;height:9vh;background:var(--accent-paper);transform:rotate(-1.2deg);z-index:1"></div>
  <div class="stack" style="align-items:center;text-align:center;gap:3.6vh;position:relative;z-index:2">
    <span class="kicker" data-drop="1">ONE BIG IDEA</span>
    <div class="pin r-1 high" data-drop="2" style="--rot:-1deg;max-width:64vw">
      <div class="piece cut3" style="padding:5.5vh 4.5vw">
        <h2 class="h-xl" style="line-height:1.55">金句正文<span class="h-hand">,</span><br>核心词<span class="uline">垫纸条</span></h2>
      </div>
      <span class="staple sl"></span><span class="staple sr"></span>
    </div>
    <p class="body-s" data-drop="3" style="letter-spacing:.2em">—— 出处或注脚</p>
  </div>
</section>
```

## Layout 4 · 三卡并列(轮廓各不相同)

```html
<section class="slide">
  <div class="dotfield" style="width:10vw;height:10vw;bottom:8vh;right:6vw"></div>
  <div class="stack" style="gap:4.5vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">THREE THINGS</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">本页论点</h2>
    </div>
    <div class="grid-3" style="width:100%">
      <div class="pin r-1" data-drop="2" style="--rot:-1deg">
        <div class="piece card"><span class="card-nb">一</span><h3 class="h-md">要点</h3><p class="body-s">两三行短句。</p></div>
        <span class="staple sl"></span>
      </div>
      <div class="pin r1" data-drop="3" style="--rot:1deg">
        <div class="piece card tinted cut2"><span class="card-nb">二</span><h3 class="h-md">要点</h3><p class="body-s">中间换纸色。</p></div>
        <span class="tape tc"></span>
      </div>
      <div class="pin r-2" data-drop="4" style="--rot:-1.7deg">
        <div class="piece card cut3"><span class="card-nb">三</span><h3 class="h-md">要点</h3><p class="body-s">轮廓各不相同。</p></div>
      </div>
    </div>
  </div>
</section>
```

## Layout 5 · 左文右图

```html
<section class="slide">
  <div class="grid-2">
    <div class="stack">
      <span class="label r-1" data-drop="1" style="--rot:-1deg">CASE</span>
      <h2 class="h-xl" data-drop="2">故事标题</h2>
      <p class="lead" data-drop="3">两三行叙述,关键词<span class="uline">垫纸条</span>。</p>
    </div>
    <div class="pin r1 high" data-drop="3" style="--rot:1deg">
      <div class="piece frame cut2">
        <img src="images/05-case.png" alt="场景插画">
        <p class="img-cap" style="padding:0 1vw 1vh">图注一句话</p>
      </div>
      <span class="tape tr"></span>
    </div>
  </div>
</section>
```

## Layout 6 · 流程纸带

```html
<section class="slide deep">
  <div class="stack" style="gap:5vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">WORKFLOW</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">流程标题</h2>
    </div>
    <div class="steps" style="width:100%">
      <div class="piece step r-1" data-drop="2" style="--rot:-1deg">
        <span class="step-nb">01</span><span class="step-title">步骤名</span><span class="step-desc">一句话。</span>
      </div>
      <svg class="arrow-hand" data-drop="3" viewBox="0 0 60 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 14 C 20 6, 38 6, 52 12"/><path d="M45 5 L 53 12 L 43 16"/></svg>
      <div class="piece step cut2 r1" data-drop="3" style="--rot:1deg">
        <span class="step-nb">02</span><span class="step-title">步骤名</span><span class="step-desc">一句话。</span>
      </div>
      <svg class="arrow-hand" data-drop="4" viewBox="0 0 60 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 10 C 20 18, 38 18, 52 12"/><path d="M45 6 L 53 12 L 44 19"/></svg>
      <div class="piece step tinted cut3 r-2" data-drop="4" style="--rot:-1.5deg">
        <span class="step-nb">03</span><span class="step-title">步骤名</span><span class="step-desc">一句话。</span>
      </div>
    </div>
  </div>
</section>
```

## Layout 7 · 对比页(Before / After)

```html
<section class="slide" style="padding:0">
  <div style="display:grid;grid-template-columns:1fr 1fr;height:100%;position:relative">
    <div style="background:var(--field-deep);padding:10vh 4vw;display:flex;flex-direction:column;gap:2.6vh;justify-content:center">
      <span class="label r-1" data-drop="1" style="--rot:-1deg;align-self:flex-start">BEFORE</span>
      <h3 class="h-md" data-drop="2" style="font-size:1.9vw">旧的做法</h3>
      <div class="piece card r-1 cut2" data-drop="3" style="--rot:-1deg"><p class="body-s">痛点短句列出。</p></div>
    </div>
    <div style="padding:10vh 4vw;display:flex;flex-direction:column;gap:2.6vh;justify-content:center">
      <span class="label accent r1" data-drop="1" style="--rot:1deg;align-self:flex-start">AFTER</span>
      <h3 class="h-md" data-drop="2" style="font-size:1.9vw">新的做法</h3>
      <div class="piece card tinted r1 cut3" data-drop="4" style="--rot:1deg"><p class="body-s">对应改善,逐条呼应。</p></div>
    </div>
    <div class="piece accent r-2 high" data-drop="5" style="--rot:-1.7deg;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-1.7deg);padding:1.6vh 1.4vw;z-index:5">
      <span style="font-weight:900;font-size:1.3vw;letter-spacing:.1em">VS</span>
    </div>
  </div>
</section>
```

注:中缝 VS 纸片的 transform 写死在 style(--rot 动画和 translate 冲突),data-drop 只走透明度。

## Layout 8 · 数据大字报

```html
<section class="slide">
  <div class="stack" style="gap:4.5vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">NUMBERS</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">数据说明了什么</h2>
    </div>
    <div class="grid-3" style="width:100%">
      <div class="piece stat r-1" data-drop="2" style="--rot:-1deg">
        <span class="stat-nb">87<span class="stat-unit">%</span></span>
        <span class="stat-note">一句话解释</span>
      </div>
      <div class="piece stat inked cut2 r1" data-drop="3" style="--rot:1deg">
        <span class="stat-nb" style="color:var(--accent-paper)">3<span class="stat-unit">倍</span></span>
        <span class="stat-note" style="color:rgba(255,255,255,.7)">中间换墨底纸片</span>
      </div>
      <div class="piece stat cut3 r-2" data-drop="4" style="--rot:-1.7deg">
        <span class="stat-nb">10<span class="stat-unit">min</span></span>
        <span class="stat-note">一句话解释</span>
      </div>
    </div>
  </div>
</section>
```

## Layout 9 · 清单便签页

```html
<section class="slide deep">
  <div class="grid-5-7">
    <div class="stack">
      <span class="label r-1" data-drop="1" style="--rot:-1deg">CHECKLIST</span>
      <h2 class="h-xl" data-drop="2">交付前<br>过一遍</h2>
    </div>
    <div class="stack" style="gap:2vh;width:100%">
      <div class="piece r1" data-drop="3" style="--rot:1deg;padding:2.2vh 2vw;width:100%;display:flex;gap:1.2vw;align-items:center">
        <span class="h-hand" style="font-size:1.6vw">✓</span><p class="body-s" style="font-size:1.05vw">清单项一。</p>
      </div>
      <div class="piece tinted cut2 r-1" data-drop="4" style="--rot:-1deg;padding:2.2vh 2vw;width:100%;display:flex;gap:1.2vw;align-items:center">
        <span class="h-hand" style="font-size:1.6vw">✓</span><p class="body-s" style="font-size:1.05vw">清单项二。</p>
      </div>
      <div class="piece cut3 r2" data-drop="5" style="--rot:1.8deg;padding:2.2vh 2vw;width:100%;display:flex;gap:1.2vw;align-items:center">
        <span class="h-hand" style="font-size:1.6vw">✓</span><p class="body-s" style="font-size:1.05vw">清单项三。</p>
      </div>
    </div>
  </div>
</section>
```

## Layout 10 · 收束 CTA(剪贴字 + 山景)

```html
<section class="slide ink halftone">
  <div class="hills"><div class="hill torn-t"></div><div class="hill torn-t"></div><div class="hill torn-t"></div></div>
  <div class="scrap star c-tint" style="width:1.6vw;height:1.6vw;top:16vh;left:16vw;transform:rotate(-10deg)"></div>
  <div class="stack" style="align-items:center;text-align:center;gap:3.4vh;position:relative;z-index:2">
    <span class="kicker" data-drop="1">TAKEAWAY</span>
    <h2 class="h-hero chips" data-drop="2" style="font-size:4.4vw"><span>收</span><span>尾</span><span class="acc">金</span><span>句</span></h2>
    <div class="pin r1" data-drop="3" style="--rot:1deg">
      <div class="piece" style="padding:2.2vh 3vw"><p class="h-md" style="color:var(--ink)">CTA / 联系方式</p></div>
      <span class="tape tl"></span>
    </div>
    <p class="body-s" data-drop="4" style="letter-spacing:.24em">THANK YOU · 讲者名</p>
  </div>
</section>
```

---

## 页数规划参考

| 时长 | 页数 | 结构 |
|------|------|------|
| 10 分钟 | 8-10 页 | 封面 + 1 幕 + 收束 |
| 20 分钟 | 12-16 页 | 封面 + 2-3 幕(每幕幕封+2-4 内容页) + 收束 |
| 40 分钟 | 20-26 页 | 封面 + 3-4 幕 + 中场金句页 + 收束 |

叙事弧:钩子(封面/金句) → 定调(幕封) → 主体(L4/5/6/8 穿插) → 转折(L7 对比或 L3 金句) → 收束(L10)。
