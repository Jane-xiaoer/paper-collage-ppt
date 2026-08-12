#!/usr/bin/env python3
"""Validate a Haoqi 3D WeChat article before conversion/upload."""
from pathlib import Path
import re
import sys

BANNED = [
    r"<script\b", r"<style\b", r"<canvas\b", r"<svg\b", r"<video\b",
    r"display\s*:\s*(?:flex|grid)", r"position\s*:\s*(?:absolute|fixed)",
    r"(?:^|[;\s])float\s*:", r"mix-blend-mode", r"\bfilter\s*:",
    r"three\.module|three\.core|OrbitControls|WebGL",
]

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate-haoqi-wechat.py article.md")
    path = Path(sys.argv[1]).expanduser().resolve()
    text = path.read_text()
    errors = []
    for pat in BANNED:
        if re.search(pat, text, re.I):
            errors.append(f"banned pattern: {pat}")
    for ref in re.findall(r"!\[[^]]*\]\(([^)\s]+)", text):
        if not re.match(r"https?://|data:", ref):
            image = (path.parent / ref).resolve()
            if not image.exists():
                errors.append(f"missing markdown image: {ref}")
            elif image.stat().st_size > 1024 * 1024:
                errors.append(f"image over 1MB: {ref} ({image.stat().st_size // 1024}KB)")
    for ref in re.findall(r'<img[^>]+src=["\']([^"\']+)', text, re.I):
        if not re.match(r"https?://|data:", ref):
            image = (path.parent / ref).resolve()
            if not image.exists():
                errors.append(f"missing HTML image: {ref}")
            elif image.stat().st_size > 1024 * 1024:
                errors.append(f"image over 1MB: {ref} ({image.stat().st_size // 1024}KB)")
    if re.search(r"<section[^>]+background-image", text, re.I) is None and "background-image" in text:
        errors.append("background-image must be on a styled <section>")
    if errors:
        print("FAIL")
        print("\n".join(f"- {e}" for e in errors))
        raise SystemExit(1)
    print(f"PASS {path.name}: no banned WeChat patterns and all local images are present/under 1MB")

if __name__ == "__main__":
    main()
