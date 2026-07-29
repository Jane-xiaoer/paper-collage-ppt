#!/usr/bin/env python3
"""
剪纸拼贴 HTML deck → 可编辑 PPTX(混合导出)。

原理:装饰层(底纹/纸片/撕边/胶带)逐页截图当背景;文字从 DOM 里提取
位置/字号/颜色/旋转,在 PPTX 里生成**真正的文本框**叠在背景上——
风格与截图版一致,但每一段文字都可以在 PowerPoint/Keynote 里直接改。

用法:
    python3 export-pptx-editable.py deck.html                    # deck-editable.pptx
    python3 export-pptx-editable.py deck.html -o 分享.pptx --theme t15

边界(诚实声明):
- 改文字 ✅;改版式/换配色 ❌(回 HTML 改完重导)
- 剪贴字标题每个字压在一张烤死的纸片上:小改(等长换字)完美,
  大改字数会和纸片错位——标题大改请回 HTML
- 马克笔垫色(uline)烤在背景里,文字改长后垫色不跟随

依赖:Google Chrome + python-pptx。
"""
import argparse
import base64
import json
import math
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VW, VH = 1600, 900
EMU_PER_PX = 7620          # 12192000 EMU / 1600 px
PT_PER_PX = 72 / 120       # 1600px ↔ 13.33in → 120px/in

FORCE_FINAL = """
<style id="__pcx">
#skinbar,#dots,#pageno{display:none!important}
[data-drop]{opacity:1!important;transform:translateY(0) rotate(var(--rot,0deg)) scale(1)!important;transition:none!important}
*{transition:none!important;animation:none!important}
</style>
"""

COLLECT_JS = r"""
function __pcxCollect(mark){
  function angleOf(el, stopAt){
    let a = 0, n = el;
    while(n && n !== stopAt && n.nodeType === 1){
      const tr = getComputedStyle(n).transform;
      if(tr && tr !== 'none'){
        const m = tr.match(/matrix\(([-\d.e]+),\s*([-\d.e]+)/);
        if(m) a += Math.atan2(parseFloat(m[2]), parseFloat(m[1])) * 180 / Math.PI;
      }
      n = n.parentElement;
    }
    return a;
  }
  function hasDirectText(el){
    for(const c of el.childNodes)
      if(c.nodeType === 3 && c.textContent.trim()) return true;
    return false;
  }
  const out = [];
  document.querySelectorAll('#deck > .slide').forEach((slide, si) => {
    const srect = slide.getBoundingClientRect();
    const collected = [];
    const isIn = el => collected.some(c => c === el || c.contains(el));
    slide.querySelectorAll('*').forEach(el => {
      if(isIn(el)) return;
      if(['SCRIPT','STYLE','SVG','IMG'].includes(el.tagName)) return;
      let targets = null;
      if(el.classList.contains('chips')){
        targets = [...el.children].filter(c => c.tagName === 'SPAN' && c.innerText.trim());
        collected.push(el);
      } else if(hasDirectText(el)){
        targets = [el]; collected.push(el);
      }
      if(!targets) return;
      for(const t of targets){
        const r = t.getBoundingClientRect();
        if(r.width < 2 || r.height < 2) continue;
        const cs = getComputedStyle(t);
        const pad = ['Top','Right','Bottom','Left'].map(s => parseFloat(cs['padding'+s]) || 0);
        out.push({
          slide: si,
          text: t.innerText,
          cx: r.left + r.width/2 - srect.left,
          cy: r.top + r.height/2 - srect.top,
          w: t.offsetWidth, h: t.offsetHeight,
          rot: angleOf(t, slide.parentElement),
          size: parseFloat(cs.fontSize),
          lh: parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.2,
          weight: parseInt(cs.fontWeight) || 400,
          color: cs.color,
          align: cs.textAlign,
          family: cs.fontFamily.split(',')[0].replace(/["']/g,'').trim(),
          spacing: parseFloat(cs.letterSpacing) || 0,
          pad: pad,
        });
        if(mark){
          t.style.setProperty('color','transparent','important');
          t.style.setProperty('-webkit-text-fill-color','transparent','important');
          t.querySelectorAll('*').forEach(d => {
            d.style.setProperty('color','transparent','important');
            d.style.setProperty('-webkit-text-fill-color','transparent','important');
          });
        }
      }
    });
  });
  return out;
}
"""

EXTRACT_PAGE = COLLECT_JS + """
document.fonts.ready.then(() => {
  setTimeout(() => {
    const data = __pcxCollect(false);
    document.title = 'PCXDATA:' + btoa(unescape(encodeURIComponent(JSON.stringify(data))));
  }, 300);
});
"""

MASK_PAGE = COLLECT_JS + """
document.fonts.ready.then(() => { setTimeout(() => { __pcxCollect(true); document.title='PCXMASKED'; }, 300); });
"""

FONT_MAP = {
    "Noto Sans SC": "PingFang SC", "-apple-system": "PingFang SC",
    "Noto Serif SC": "Songti SC", "Ma Shan Zheng": "Kaiti SC",
    "STSongti-SC-Black": "Songti SC",
}


def run_chrome(args):
    return subprocess.run([CHROME, "--headless", "--disable-gpu", *args],
                          capture_output=True, text=False, timeout=180)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("-o", "--out")
    ap.add_argument("--theme", help="tN 配色编号")
    args = ap.parse_args()

    try:
        from pptx import Presentation
        from pptx.util import Emu, Pt
        from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
        from pptx.dml.color import RGBColor
        from pptx.oxml.ns import qn
    except ImportError:
        sys.exit("ERROR: 缺 python-pptx。安装:python3 -m pip install --user python-pptx")

    deck = Path(args.deck).expanduser().resolve()
    if not deck.exists():
        sys.exit(f"ERROR: 找不到 {deck}")
    html = deck.read_text()
    n = html.count('<section class="slide')
    if args.theme:
        html = re.sub(r'<body class="t\d+"', f'<body class="{args.theme}"', html, count=1)
        html = html.replace("localStorage.getItem(KEY)", "null")

    td = Path(tempfile.mkdtemp(prefix="pcx-"))

    # Pass 1: 提取文字几何
    (td/"extract.html").write_text(html.replace("</body>", FORCE_FINAL + "<script>" + EXTRACT_PAGE + "</script></body>"))
    r = run_chrome([f"--window-size={VW},{VH}", "--virtual-time-budget=10000",
                    "--dump-dom", f"file://{td}/extract.html"])
    m = re.search(rb"PCXDATA:([A-Za-z0-9+/=]+)", r.stdout)
    if not m:
        sys.exit("ERROR: 文字提取失败(dump-dom 无数据)")
    items = json.loads(base64.b64decode(m.group(1)).decode("utf-8"))
    print(f"  ✓ 提取 {len(items)} 个文本框 / {n} 页")

    # Pass 2: 文字透明化逐页截图
    (td/"mask.html").write_text(html.replace("</body>", FORCE_FINAL + "<script>" + MASK_PAGE + "</script></body>"))
    shots = []
    for i in range(1, n+1):
        png = td/f"s{i:02d}.png"
        run_chrome([f"--window-size={VW},{VH}", "--force-device-scale-factor=2",
                    "--virtual-time-budget=9000", "--hide-scrollbars",
                    f"--screenshot={png}", f"file://{td}/mask.html#{i}"])
        if not png.exists():
            sys.exit(f"ERROR: 第 {i} 页背景截图失败")
        try:  # PNG→JPEG:背景是照片质感,JPEG 体积小一个量级
            from PIL import Image
            jpg = td/f"s{i:02d}.jpg"
            Image.open(png).convert("RGB").save(jpg, "JPEG", quality=82)
            png.unlink(); png = jpg
        except ImportError:
            pass
        shots.append(png)
        print(f"  ✓ 背景 {i}/{n}")

    # Pass 3: 组装 PPTX
    prs = Presentation()
    prs.slide_width = Emu(12192000)
    prs.slide_height = Emu(6858000)
    blank = prs.slide_layouts[6]
    ALIGN = {"center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT, "justify": PP_ALIGN.JUSTIFY}

    for si in range(n):
        slide = prs.slides.add_slide(blank)
        slide.shapes.add_picture(str(shots[si]), 0, 0, width=prs.slide_width, height=prs.slide_height)
        for it in (x for x in items if x["slide"] == si):
            # 宽度加 8% 缓冲:不同渲染器字体度量有差,防止意外折行
            w, h = it["w"]*EMU_PER_PX*1.08 + 4*EMU_PER_PX, it["h"]*EMU_PER_PX
            left, top = it["cx"]*EMU_PER_PX - w/2, it["cy"]*EMU_PER_PX - h/2
            box = slide.shapes.add_textbox(Emu(int(left)), Emu(int(top)), Emu(int(w)), Emu(int(h)))
            box.rotation = it["rot"]
            tf = box.text_frame
            tf.word_wrap = True
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.margin_left = Emu(int(it["pad"][3]*EMU_PER_PX))
            tf.margin_right = Emu(int(it["pad"][1]*EMU_PER_PX))
            tf.margin_top = Emu(int(it["pad"][0]*EMU_PER_PX))
            tf.margin_bottom = Emu(int(it["pad"][2]*EMU_PER_PX))
            rgb = re.findall(r"\d+", it["color"])[:3]
            color = RGBColor(*(int(v) for v in rgb)) if len(rgb) == 3 else RGBColor(0,0,0)
            fam = FONT_MAP.get(it["family"], it["family"])
            lines = it["text"].split("\n")
            for li, line in enumerate(lines):
                p = tf.paragraphs[0] if li == 0 else tf.add_paragraph()
                p.alignment = ALIGN.get(it["align"], PP_ALIGN.LEFT)
                p.line_spacing = max(it["lh"]/it["size"], 0.9)
                run = p.add_run(); run.text = line
                f = run.font
                f.size = Pt(round(it["size"]*PT_PER_PX, 1))
                f.bold = it["weight"] >= 600
                f.color.rgb = color
                f.name = fam
                rPr = run._r.get_or_add_rPr()
                ea = rPr.find(qn("a:ea"))
                if ea is None:
                    ea = rPr.makeelement(qn("a:ea"), {}); rPr.append(ea)
                ea.set("typeface", fam)
                if it["spacing"]:
                    rPr.set("spc", str(int(it["spacing"]*PT_PER_PX*100)))

    out = Path(args.out).expanduser() if args.out else deck.with_name(deck.stem + "-editable.pptx")
    prs.save(out)
    print(f"  ✓ 可编辑 PPTX: {out}  ({out.stat().st_size//1024}KB, {len(items)} 个可编辑文本框)")


if __name__ == "__main__":
    main()
