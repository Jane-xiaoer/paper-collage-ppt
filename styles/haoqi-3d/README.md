# 好奇果冻 3D · Haoqi Jelly 3D

一套面向设计、创意和年轻化产品演示的 3D 网页 PPT 风格。

## 视觉语言

- 淡蓝天空底与斜向暖光
- 半透明、带清漆高光的果冻手写字
- 多巴胺黏土人物与生活物件
- 复古印刷贴纸
- 外露的网格、十字、坐标和进度条
- 大标题 / 中支撑 / 小点缀三级视觉重量
- 素材从画外飘入，落位后缓慢呼吸

## 使用

本风格使用 ES Modules，需通过本地 HTTP 服务预览：

```bash
cd paper-collage-ppt
python3 -m http.server 8788 --bind 127.0.0.1
```

打开：

- Deck：<http://127.0.0.1:8788/styles/haoqi-3d/demo.html>
- 素材筛选台：<http://127.0.0.1:8788/styles/haoqi-3d/picker.html>

操作：

- `←` / `→`、空格、Page Up / Page Down 翻页
- 滚轮或点击翻页
- 底部切换“规范 / 进阶 / 前卫”三档材质
- URL 参数 `?p=0&s=plus`：指定页码和材质方案
- URL 参数 `&still=1`：关闭动画，适合截图导出

## 结构

```text
demo.html              # 20 页完整示例
picker.html            # 48 件黏土素材 + 9 件复古贴纸筛选台
assets/clay/           # 透明 PNG 黏土素材
assets/fonts/          # 果冻字路径数据
assets/stickers/retro/ # 复古贴纸
vendor/                # 本地 Three.js 与 addons
```

## 设计约束

1. 每页先确定 PPT 信息类型，再选择 3D 素材。
2. 每页最多一个 hero、两个 support 和一个 sticker。
3. hero 宽度约 22–38vw，support 8–15vw，accent 3–7vw。
4. 贴纸必须咬住标题、网格或实物边缘，不悬空做水印。
5. 章节页和金句页允许极简，不为“热闹”而堆素材。
6. `hello` 是封面招牌；内页不重复滥用。
7. 不使用紫色，保持蓝、暖光和高饱和黏土物件的关系。

## 来源与授权

本目录中的页面、代码和项目内素材作为本仓库的一部分按根目录 `LICENSE` 发布。Three.js 运行时遵循其原始 MIT License。
