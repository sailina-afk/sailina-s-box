# Cyrene Balance Widget 2.0 (Animated)

[![Listed on DSH Market](https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/badge-listed-en.svg)](https://dsh.market/)

On client startup it plays a full-screen opening animation (`assets/loading.mp4`, 1440p / 60fps, ~20 MB, 13.9 s),
fades out into the UI, and 2.5 seconds later plays "Cyrene's Greeting".

## What this build does

| Item | Details |
|---|---|
| Loading animation | Full-screen `loading.mp4` (2560×1440, H.264, 60fps, ~20 MB) with `object-fit: cover` |
| Audio | Original soundtrack kept at full volume; **linear fade-out over the last 2.2 s** — the sound lasts exactly as long as the animation |
| Exit | Overlay fades out over 900 ms, the page fades in naturally |
| Greeting | **2.5 s after** the fade-out completes, `assets/greeting.wav` (3.58 s) plays together with a short toast |
| Interaction | **No skip button, no fullscreen request, no hiding of window buttons** — just a plain opening animation |
| Fallbacks | Autoplay with sound blocked → retry muted; not playing within 2.6 s → skip; hard release at 20 s |

## The widget itself

- Character: built-in Cyrene sprite (610×610, transparent, bottom-aligned)
- Lines: 25 quotes, font sizes 6/7/8/9, shown at random
- First click: balance panel; next click: a random quote
- Everything else (sound effects, snapping, accounting, bubble editor) comes from `dsh-whale-widget` 0.4.2

## Customising

- **Lines**: right-click the widget → bubble settings; or `BUBBLE_DEFAULT_ITEMS` in `assets/whale-widget.js`; batch via `tools/set-lines.py`
- **Font size**: `tools/resize-lines.py` (edit `SIZE_MAP`, then re-run)
- **Greeting audio**: replace `assets/greeting.wav`, refresh to apply
- **Opening animation**: replace `assets/loading.mp4` (H.264 recommended for widest compatibility)

## Install

`plugin_manager` → `install_bundle`, with `target` set to this directory's absolute path.
The no-animation build lives in `../no-animation/` (package `dsh-cyrene-whale-widget-noanim`). Both share the
`/dsh-whale/*` routes and `$DSH_HOME/.dshw-*.json`, so only one can be enabled at a time.

## Asset credits

Character: Cyrene sticker provided by the user; lines and greeting voice: user-provided;
opening animation: user-provided 4K source, re-encoded to 1440p60 H.264;
upstream `dsh-whale-widget` v0.4.2 (MIT, see `LICENSE` and `README.upstream.md`).
