#!/usr/bin/env python3
"""
把 markdown 里的本地图片上传到微信公众号 CDN(media/uploadimg),
并把路径替换成返回的 mmbiz URL。wechat-publisher 的 publish.py 不管正文图,
这个脚本在 publish 之前跑一次,补上这个缺口。

用法:
    python3 upload-body-images.py /path/to/article.md            # 原地改写(留 .bak)
    python3 upload-body-images.py /path/to/article.md --dry-run  # 只列出要传哪些

约束(微信 uploadimg 接口):只收 jpg/png,单张 ≤1MB。超限自动用 sips 压一份再传。
AppID/Secret 复用 wechat-publisher 的配置(~/.config/wechat-publisher/config.yaml)。
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import uuid
from pathlib import Path


def load_config():
    candidates = [
        Path.home() / ".config/wechat-publisher/config.yaml",
        Path.home() / ".config/md2wechat/config.yaml",
    ]
    for cfg in candidates:
        if not cfg.exists():
            continue
        text = cfg.read_text()
        m_app = re.search(r'appid:\s*"([^"]+)"', text)
        m_sec = re.search(r'secret:\s*"([^"]+)"', text)
        if m_app and m_sec:
            return m_app.group(1), m_sec.group(1)
    sys.exit("ERROR: 找不到 AppID/Secret,先配置 ~/.config/wechat-publisher/config.yaml")


def get_token(appid: str, secret: str) -> str:
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
    with urllib.request.urlopen(url, timeout=15) as r:
        data = json.loads(r.read())
    if "access_token" not in data:
        sys.exit(f"ERROR: token 失败: {data}")
    return data["access_token"]


def ensure_uploadable(path: Path) -> Path:
    """uploadimg 只收 jpg/png ≤1MB;不合规就转/压一份临时文件。"""
    limit = 1024 * 1024
    suffix = path.suffix.lower()
    if suffix in (".jpg", ".jpeg", ".png") and path.stat().st_size <= limit:
        return path
    tmp = Path(tempfile.gettempdir()) / f"wxup-{uuid.uuid4().hex[:8]}.jpg"
    shutil.copy2(path, tmp)
    subprocess.run(
        ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "80",
         "--resampleWidth", "1080", str(tmp), "--out", str(tmp)],
        check=True, capture_output=True,
    )
    quality = 70
    while tmp.stat().st_size > limit and quality >= 30:
        subprocess.run(
            ["sips", "-s", "format", "jpeg", "-s", "formatOptions", str(quality),
             str(tmp), "--out", str(tmp)],
            check=True, capture_output=True,
        )
        quality -= 15
    if tmp.stat().st_size > limit:
        sys.exit(f"ERROR: {path.name} 压到 quality=30 还超 1MB,手动处理")
    return tmp


def upload_img(token: str, path: Path) -> str:
    path = ensure_uploadable(path)
    boundary = f"----wxup{uuid.uuid4().hex[:12]}"
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{path.name}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode() + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={token}",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    if "url" not in data:
        sys.exit(f"ERROR: uploadimg 失败 ({path.name}): {data}")
    return data["url"]


def collect_local_images(md_text: str, base: Path):
    """返回 [(原始引用串, 本地路径)],兼容 md 语法和 raw <img>。"""
    found = []
    for m in re.finditer(r'!\[[^\]]*\]\(([^)\s]+)[^)]*\)', md_text):
        found.append(m.group(1))
    for m in re.finditer(r'<img[^>]+src="([^"]+)"', md_text):
        found.append(m.group(1))
    out = []
    for ref in found:
        if ref.startswith(("http://", "https://", "data:")):
            continue
        p = Path(ref).expanduser()
        if not p.is_absolute():
            p = (base / ref).resolve()
        if not p.exists():
            sys.exit(f"ERROR: 正文引用的图片不存在: {ref} (解析为 {p})")
        out.append((ref, p))
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    md_path = Path(sys.argv[1]).expanduser().resolve()
    dry = "--dry-run" in sys.argv
    text = md_path.read_text()
    images = collect_local_images(text, md_path.parent)
    if not images:
        print("  ✓ 正文没有本地图片,无需上传")
        return
    print(f"  发现 {len(images)} 张本地图片:")
    for ref, p in images:
        print(f"    {ref}  ({p.stat().st_size // 1024}KB)")
    if dry:
        return
    appid, secret = load_config()
    token = get_token(appid, secret)
    shutil.copy2(md_path, md_path.with_suffix(md_path.suffix + ".bak"))
    done = {}
    for ref, p in images:
        if ref in done:
            continue
        url = upload_img(token, p)
        done[ref] = url
        print(f"  ✓ {ref} → {url}")
    for ref, url in done.items():
        text = text.replace(f"]({ref}", f"]({url}").replace(f'src="{ref}"', f'src="{url}"')
    md_path.write_text(text)
    print(f"  ✓ 已改写 {md_path.name}(备份 .bak)")


if __name__ == "__main__":
    main()
