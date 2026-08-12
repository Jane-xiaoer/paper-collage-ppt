# 风格扩展目录

每套视觉风格放在独立目录中，避免 CSS、运行时和素材互相污染。

```text
styles/
└── <style-id>/
    ├── README.md       # 风格定位、使用方法、设计约束
    ├── demo.html       # 可直接运行的完整示例
    ├── picker.html     # 可选：素材筛选台
    ├── assets/         # 风格专属素材
    └── vendor/         # 可选：本地运行时依赖
```

## 新增风格约定

1. `demo.html` 必须离线可运行，不依赖私有 API。
2. 精确文字使用真 HTML，不把文字烤进生成图片。
3. 风格素材只放在自己的目录中。
4. 必须提供 1600×900 的视觉回归检查。
5. 在根目录 `style-gallery.html` 注册入口。
6. 在根目录 `README.md` 的风格表中补充定位和适用场景。
7. 风格必须是一套完整视觉语言，而不是只换颜色。

## 当前风格

| ID | 名称 | 入口 |
|---|---|---|
| `paper-collage` | 小耳剪纸风 | `../assets/template.html` |
| `haoqi-3d` | 好奇果冻 3D | `./haoqi-3d/demo.html` |
| `haoqi-3d-wechat` | 好奇果冻 3D · 公众号排版 | `./haoqi-3d/wechat/SKILL.md` |
