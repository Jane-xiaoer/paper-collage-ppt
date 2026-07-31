# 布局骨架(20 种 · 直接粘贴改文案,不要从零写 slide)

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

- **写稿时选**:下面 20 种骨架就是版式菜单,按每页内容挑(这是主要的选择方式)
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

## Layout 11 · 目录页(Agenda)

开场后放全片地图。左标题右四行编号纸条,行数 3-5 可增删。

```html
<section class="slide deep">
  <div class="grid-5-7">
    <div class="stack">
      <span class="kicker" data-drop="1">AGENDA</span>
      <h2 class="h-xl chips" data-drop="2"><span>目</span><span class="acc">录</span></h2>
      <p class="lead" data-drop="2">今天讲四件事。</p>
    </div>
    <div class="stack" style="gap:2vh;width:100%">
      <div class="piece" data-drop="3" style="--rot:.5deg;transform:rotate(.5deg);padding:2vh 2vw;width:100%;display:flex;gap:1.4vw;align-items:center">
        <span class="step-nb">01</span><p class="body-s" style="font-size:1.1vw;font-weight:700;color:var(--ink)">第一章标题</p>
      </div>
      <div class="piece tinted cut2" data-drop="4" style="--rot:-.5deg;transform:rotate(-.5deg);padding:2vh 2vw;width:100%;display:flex;gap:1.4vw;align-items:center">
        <span class="step-nb">02</span><p class="body-s" style="font-size:1.1vw;font-weight:700;color:var(--ink)">第二章标题</p>
      </div>
      <div class="piece cut3" data-drop="5" style="--rot:.6deg;transform:rotate(.6deg);padding:2vh 2vw;width:100%;display:flex;gap:1.4vw;align-items:center">
        <span class="step-nb">03</span><p class="body-s" style="font-size:1.1vw;font-weight:700;color:var(--ink)">第三章标题</p>
      </div>
      <div class="piece" data-drop="6" style="--rot:-.4deg;transform:rotate(-.4deg);padding:2vh 2vw;width:100%;display:flex;gap:1.4vw;align-items:center">
        <span class="step-nb">04</span><p class="body-s" style="font-size:1.1vw;font-weight:700;color:var(--ink)">第四章标题</p>
      </div>
    </div>
  </div>
</section>
```

## Layout 12 · 时间轴(Timeline)

项目历程/发展史。一条撕纸横轴,节点纸片上下交替;节点 3-5 个。

```html
<section class="slide">
  <div class="stack" style="gap:1.2vh">
    <span class="kicker" data-drop="1">TIMELINE</span>
    <h2 class="h-md" data-drop="1" style="font-size:2.4vw">从想法到发布</h2>
  </div>
  <div style="position:relative;width:100%;height:50vh;margin-top:2vh">
    <div class="torn-strip" style="position:absolute;left:-2vw;right:-2vw;top:47%;height:4.5vh;transform:rotate(-.5deg);background-color:var(--accent-paper)"></div>
    <div class="piece r-1" data-drop="2" style="--rot:-1deg;position:absolute;left:3%;bottom:56%;width:18vw;padding:2vh 1.4vw">
      <span class="step-nb">2024</span>
      <p class="body-s" style="margin-top:.6vh">节点事件一,一两句。</p>
    </div>
    <div class="piece tinted cut2 r1" data-drop="3" style="--rot:1deg;position:absolute;left:28%;top:56%;width:18vw;padding:2vh 1.4vw">
      <span class="step-nb">2025</span>
      <p class="body-s" style="margin-top:.6vh">节点事件二,一两句。</p>
    </div>
    <div class="piece cut3 r-2" data-drop="4" style="--rot:-1.7deg;position:absolute;left:53%;bottom:56%;width:18vw;padding:2vh 1.4vw">
      <span class="step-nb">2026</span>
      <p class="body-s" style="margin-top:.6vh">节点事件三,一两句。</p>
    </div>
    <div class="piece r1" data-drop="5" style="--rot:1deg;position:absolute;left:78%;top:56%;width:18vw;padding:2vh 1.4vw">
      <span class="step-nb">未来</span>
      <p class="body-s" style="margin-top:.6vh">下一步,一两句。</p>
    </div>
    <div class="scrap dot c-accent" style="width:1vw;height:1vw;left:10%;top:46%;position:absolute"></div>
    <div class="scrap dot c-ink" style="width:1vw;height:1vw;left:35%;top:46%;position:absolute"></div>
    <div class="scrap dot c-accent" style="width:1vw;height:1vw;left:60%;top:46%;position:absolute"></div>
    <div class="scrap dot c-kraft" style="width:1vw;height:1vw;left:85%;top:46%;position:absolute"></div>
  </div>
</section>
```

## Layout 13 · 人物/团队页

讲人:团队、嘉宾、用户画像。三列头像纸framed+名字纸条;头像用 nano 纸艺人像或真实照片。

```html
<section class="slide">
  <div class="stack" style="gap:4vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">TEAM</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">三个人,三件事</h2>
    </div>
    <div class="grid-3" style="width:100%">
      <div class="stack" style="gap:1.6vh;align-items:center">
        <div class="pin r-1" data-drop="2" style="--rot:-1deg;width:80%">
          <div class="piece frame"><div class="ph" style="aspect-ratio:1/1">13-p1.png · 人像</div></div>
          <span class="tape tc"></span>
        </div>
        <span class="label paper r1" data-drop="2" style="--rot:1deg">姓名一</span>
        <p class="body-s" style="text-align:center">一句话:负责什么/什么来头。</p>
      </div>
      <div class="stack" style="gap:1.6vh;align-items:center">
        <div class="pin r1" data-drop="3" style="--rot:1deg;width:80%">
          <div class="piece frame cut2"><div class="ph" style="aspect-ratio:1/1">13-p2.png · 人像</div></div>
          <span class="staple sl"></span>
        </div>
        <span class="label r-1" data-drop="3" style="--rot:-1deg">姓名二</span>
        <p class="body-s" style="text-align:center">一句话介绍。</p>
      </div>
      <div class="stack" style="gap:1.6vh;align-items:center">
        <div class="pin r-2" data-drop="4" style="--rot:-1.7deg;width:80%">
          <div class="piece frame cut3"><div class="ph" style="aspect-ratio:1/1">13-p3.png · 人像</div></div>
          <span class="tape tr"></span>
        </div>
        <span class="label accent r1" data-drop="4" style="--rot:1deg">姓名三</span>
        <p class="body-s" style="text-align:center">一句话介绍。</p>
      </div>
    </div>
  </div>
</section>
```

## Layout 14 · 双栏要点

两组并列内容(非对立,对立用 L7):如「原理 / 实践」「适合 / 不适合」。

```html
<section class="slide">
  <div class="stack" style="gap:4vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">TWO SIDES</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">本页论点</h2>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3vw;width:100%">
      <div class="piece card r-1" data-drop="2" style="--rot:-1deg;gap:1.8vh">
        <h3 class="h-md" style="color:var(--accent)">左栏标题</h3>
        <p class="body-s">· 要点一,短句。</p>
        <p class="body-s">· 要点二,短句。</p>
        <p class="body-s">· 要点三,短句。</p>
      </div>
      <div class="piece card tinted cut2 r1" data-drop="3" style="--rot:1deg;gap:1.8vh">
        <h3 class="h-md">右栏标题</h3>
        <p class="body-s">· 要点一,短句。</p>
        <p class="body-s">· 要点二,短句。</p>
        <p class="body-s">· 要点三,短句。</p>
      </div>
    </div>
  </div>
</section>
```

## Layout 15 · 四宫格

四要点/SWOT/矩阵。四张卡角度正负交替;做 SWOT 时每卡标题换 S/W/O/T。

```html
<section class="slide deep">
  <div class="stack" style="gap:3.5vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">FOUR THINGS</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">本页论点</h2>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4vh 2.4vw;width:100%">
      <div class="piece card r-1" data-drop="2" style="--rot:-1deg;padding:2.6vh 1.8vw">
        <span class="card-nb" style="font-size:1.8vw">一</span>
        <h3 class="h-md" style="font-size:1.3vw">要点标题</h3>
        <p class="body-s">一两句说明。</p>
      </div>
      <div class="piece tinted cut2 card r1" data-drop="3" style="--rot:1deg;padding:2.6vh 1.8vw">
        <span class="card-nb" style="font-size:1.8vw">二</span>
        <h3 class="h-md" style="font-size:1.3vw">要点标题</h3>
        <p class="body-s">一两句说明。</p>
      </div>
      <div class="piece cut3 card r2" data-drop="4" style="--rot:1.8deg;padding:2.6vh 1.8vw">
        <span class="card-nb" style="font-size:1.8vw">三</span>
        <h3 class="h-md" style="font-size:1.3vw">要点标题</h3>
        <p class="body-s">一两句说明。</p>
      </div>
      <div class="piece card r-2" data-drop="5" style="--rot:-1.7deg;padding:2.6vh 1.8vw">
        <span class="card-nb" style="font-size:1.8vw">四</span>
        <h3 class="h-md" style="font-size:1.3vw">要点标题</h3>
        <p class="body-s">一两句说明。</p>
      </div>
    </div>
  </div>
</section>
```

## Layout 16 · 表格页

对比参数/价格表/规格。表头墨纸条,数据行米卡纸条;列数 2-4,行数 ≤4(再多换常规 PPT)。

```html
<section class="slide">
  <div class="stack" style="gap:4vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">TABLE</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">一张表说清楚</h2>
    </div>
    <div class="stack" style="gap:1.6vh;width:100%">
      <div class="piece inked" data-drop="2" style="--rot:-.3deg;transform:rotate(-.3deg);padding:1.8vh 2vw;width:100%;display:flex">
        <span class="step-title" style="flex:1.4;color:var(--paper)">维度</span>
        <span class="step-title" style="flex:1;color:var(--paper)">方案 A</span>
        <span class="step-title" style="flex:1;color:var(--accent-paper)">方案 B(推荐)</span>
      </div>
      <div class="piece" data-drop="3" style="--rot:.35deg;transform:rotate(.35deg);padding:1.8vh 2vw;width:100%;display:flex">
        <span class="body-s" style="flex:1.4;font-weight:700;color:var(--ink)">行一</span>
        <span class="body-s" style="flex:1">数值</span>
        <span class="body-s" style="flex:1;font-weight:700;color:var(--accent)">数值</span>
      </div>
      <div class="piece cut2" data-drop="4" style="--rot:-.35deg;transform:rotate(-.35deg);padding:1.8vh 2vw;width:100%;display:flex">
        <span class="body-s" style="flex:1.4;font-weight:700;color:var(--ink)">行二</span>
        <span class="body-s" style="flex:1">数值</span>
        <span class="body-s" style="flex:1;font-weight:700;color:var(--accent)">数值</span>
      </div>
      <div class="piece cut3" data-drop="5" style="--rot:.3deg;transform:rotate(.3deg);padding:1.8vh 2vw;width:100%;display:flex">
        <span class="body-s" style="flex:1.4;font-weight:700;color:var(--ink)">行三</span>
        <span class="body-s" style="flex:1">数值</span>
        <span class="body-s" style="flex:1;font-weight:700;color:var(--accent)">数值</span>
      </div>
    </div>
  </div>
</section>
```

## Layout 17 · 全幅大图页

一张图就是主角:成品展示/氛围图/大截图。图占 78%,左上标签右下图注。

```html
<section class="slide deep">
  <div class="stack" style="align-items:center;gap:2.4vh">
    <div class="pin r0 high" data-drop="1" style="--rot:-.4deg;width:76vw">
      <div class="piece frame"><div class="ph" style="aspect-ratio:16/8.2">17-hero.png · 全幅大图 16:9</div></div>
      <span class="tape tl"></span><span class="tape tr"></span>
    </div>
    <div style="display:flex;justify-content:space-between;width:76vw;align-items:center">
      <span class="label accent r-1" data-drop="2" style="--rot:-1deg">SHOWCASE</span>
      <p class="img-cap" data-drop="2" style="margin:0">图注:一句话说明这张图。</p>
    </div>
  </div>
</section>
```

## Layout 18 · 问答页(Q&A)

FAQ/预判听众疑问。Q=强调纸条,A=纸片;2-3 组。

```html
<section class="slide">
  <div class="grid-5-7">
    <div class="stack">
      <span class="kicker" data-drop="1">Q &amp; A</span>
      <h2 class="h-xl" data-drop="1">你可能想问</h2>
    </div>
    <div class="stack" style="gap:2.6vh;width:100%">
      <div class="stack" style="gap:1vh;width:100%">
        <span class="label accent r-1" data-drop="2" style="--rot:-1deg">Q1 · 这个问题怎么办?</span>
        <div class="piece r1" data-drop="3" style="--rot:1deg;padding:2vh 2vw;width:100%">
          <p class="body-s" style="font-size:1.02vw">回答两三行,直接给结论,别绕。</p>
        </div>
      </div>
      <div class="stack" style="gap:1vh;width:100%">
        <span class="label accent r1" data-drop="4" style="--rot:1deg">Q2 · 另一个高频疑问?</span>
        <div class="piece tinted cut2 r-1" data-drop="5" style="--rot:-1deg;padding:2vh 2vw;width:100%">
          <p class="body-s" style="font-size:1.02vw">回答两三行。</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

## Layout 19 · 进度/里程碑页

项目汇报:完成度、阶段进展。撕纸条当进度条填充;3-4 条。

```html
<section class="slide deep">
  <div class="stack" style="gap:4vh">
    <div class="stack" style="gap:1.2vh">
      <span class="kicker" data-drop="1">PROGRESS</span>
      <h2 class="h-md" data-drop="1" style="font-size:2.4vw">走到哪了</h2>
    </div>
    <div class="stack" style="gap:2.8vh;width:100%">
      <div class="stack" data-drop="2" style="gap:1.3vh;width:100%">
        <div style="display:flex;justify-content:space-between;width:100%"><span class="step-title">阶段一 · 设计</span><span class="stat-unit" style="color:inherit">100%</span></div>
        <div class="piece straight" style="width:100%;height:3.6vh;padding:0;transform:rotate(-.3deg)"><div class="torn-strip" style="background-color:var(--accent);width:100%;height:100%"></div></div>
      </div>
      <div class="stack" data-drop="3" style="gap:1.3vh;width:100%">
        <div style="display:flex;justify-content:space-between;width:100%"><span class="step-title">阶段二 · 开发</span><span class="stat-unit" style="color:inherit">70%</span></div>
        <div class="piece straight" style="width:100%;height:3.6vh;padding:0;transform:rotate(.35deg)"><div class="torn-strip" style="background-color:var(--accent);width:70%;height:100%"></div></div>
      </div>
      <div class="stack" data-drop="4" style="gap:1.3vh;width:100%">
        <div style="display:flex;justify-content:space-between;width:100%"><span class="step-title">阶段三 · 上线</span><span class="stat-unit" style="color:inherit">30%</span></div>
        <div class="piece straight" style="width:100%;height:3.6vh;padding:0;transform:rotate(-.35deg)"><div class="torn-strip" style="background-color:var(--kraft);width:30%;height:100%"></div></div>
      </div>
    </div>
  </div>
</section>
```

## Layout 20 · 图解页(大图+编号讲解)

讲一张截图/一个界面/一张架构图:左大图右编号要点,要点对应图上位置。

```html
<section class="slide">
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:3.5vw;align-items:center;height:100%">
    <div class="pin r-1 high" data-drop="1" style="--rot:-1deg">
      <div class="piece frame"><div class="ph">20-shot.png · 大截图/架构图 4:3</div></div>
      <span class="tape tl"></span>
    </div>
    <div class="stack" style="gap:2.2vh">
      <span class="kicker" data-drop="2">HOW IT WORKS</span>
      <h2 class="h-md" data-drop="2" style="font-size:2vw">看这三处</h2>
      <div class="piece r1" data-drop="3" style="--rot:1deg;padding:1.8vh 1.6vw;width:100%;display:flex;gap:1.2vw;align-items:flex-start">
        <span class="step-nb">1</span><p class="body-s">第一处在图里什么位置,说明什么。</p>
      </div>
      <div class="piece tinted cut2 r-1" data-drop="4" style="--rot:-1deg;padding:1.8vh 1.6vw;width:100%;display:flex;gap:1.2vw;align-items:flex-start">
        <span class="step-nb">2</span><p class="body-s">第二处,一两句。</p>
      </div>
      <div class="piece cut3 r2" data-drop="5" style="--rot:1.8deg;padding:1.8vh 1.6vw;width:100%;display:flex;gap:1.2vw;align-items:flex-start">
        <span class="step-nb">3</span><p class="body-s">第三处,一两句。</p>
      </div>
    </div>
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

叙事弧:钩子(L1 封面) → 地图(L11 目录) → 定调(L2 幕封) → 主体(L4/5/6/8/12-20 按内容型挑) → 转折(L7 对比或 L3 金句) → 收束(L10)。

**按内容型选版式**:讲要点→L4/L14/L15;讲过程→L6/L12/L19;讲数据→L8/L16;讲图→L5/L17/L20;讲人→L13;答疑→L18。
