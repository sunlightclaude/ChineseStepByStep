# Chinese Step by Step · 一步一步学中文

Learn Mandarin Chinese from zero — a web app (PWA) for Greek speakers, with explanations in English.
Works on iPhone and Android: open the website in Safari / Chrome and choose **Add to Home Screen**; it then works like an app, also offline.

**Version 1 contains**
- Stage 0: Pinyin and tones (lessons P1–P8) — tones, aspiration, j q x, zh ch sh r, -n / -ng, tone changes, first 30 characters, with tips for Greek speakers
- Listening practice (hear → choose the pinyin) and record-and-compare with a pitch curve
- Hospital phrases: about 70 emergency phrases, body parts and hospital signs, with a big-text mode to show the doctor

Lessons 1–50 (daily life and a hospital unit) will follow.

## Project layout (中文说明)

| 目录 | 内容 |
|---|---|
| `docs/` | 网页版 App（GitHub Pages 直接发布这个目录） |
| `docs/audio/` | 普通话录音 `<id>.mp3`；没有录音的句子 App 用手机自带朗读 |
| `content/` | 课程内容源文件（拼音课、医院急用句） |
| `scripts/build.py` | 由内容生成 `docs/data/content.js` 和要录的音（`audio_src/`） |
| `audio_src/` | 要录的音，每个 txt 一句；生成方法见 `CODEX_生成音频.md` |
| `设计方案.md`、`课程架构.md` | 设计方案和完整课程架构 |
