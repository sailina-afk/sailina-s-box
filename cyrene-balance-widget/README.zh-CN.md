# 昔涟余额挂件 2.0（带动画）

[![已收录](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-zh.svg)](https://dsh.market/)

> 中文原文备份，英文版见 `README.md`。

打开客户端先播一段全屏开场动画（`assets/loading.mp4`，1440p / 60fps，约 20 MB，13.9 秒），播完淡出进入界面，
再过 2.5 秒播放「昔涟的问候」。

## 这一版的样子

| 项目 | 说明 |
|---|---|
| 加载动画 | 全屏播放 `loading.mp4`（2560×1440，H.264，60fps，约 20 MB），`object-fit: cover` 铺满 |
| 音效 | 保留原声，全程原音量；**最后 2.2 秒线性淡出**，动画多长声音就多长 |
| 结束 | 播完 overlay 900ms 淡出，页面自然渐显 |
| 问候 | 淡出完成 **2.5 秒**后播放 `assets/greeting.wav`（3.58 秒），同时轻提示一句 |
| 交互 | **没有跳过按钮、不请求全屏、不隐藏窗口按钮**——就是纯开场动画 |
| 兜底 | 带声播放被拦→静音重试；2.6 秒没起播（HEVC 解不了）→ 跳过；20 秒强制放行 |

## 挂件本体

- 形象：内置角色昔涟（610×610 透明底、底部对齐）
- 台词：25 句（`E:\昔涟.txt`），字号 6/7/8/9，随机出现
- 首次点击：余额面板；再点：随机台词
- 其余（音效、吸附、记账、泡泡编辑器）沿用 `dsh-whale-widget` 0.4.2

## 改东西

- **台词**：右键挂件 → 泡泡设置；或 `assets/whale-widget.js` 的 `BUBBLE_DEFAULT_ITEMS`；批量用 `tools/set-lines.py`
- **字号**：`tools/resize-lines.py`（改 `SIZE_MAP` 后重跑）
- **问候语音**：替换 `assets/greeting.wav`，刷新即生效
- **开场动画**：替换 `assets/loading.mp4`（建议 H.264，兼容性最好）

## 安装

`plugin_manager` → `install_bundle`，`target` 用本目录绝对路径。
无动画版在 `../no-animation/`（包名 `dsh-cyrene-whale-widget-noanim`），两版共用
`/dsh-whale/*` 路由与 `$DSH_HOME/.dshw-*.json`，同一时间只能启用一个。

## 素材来源

形象：用户提供的昔涟表情图；台词：`E:\昔涟.txt`；问候：`E:\直播录像与素材\昔涟的问候.wav`；
开场动画：`E:\直播录像与素材\昔涟.mp4`；上游 `dsh-whale-widget` v0.4.2（MIT）。
