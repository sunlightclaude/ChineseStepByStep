# 给 Codex 的任务：用 ElevenLabs 生成「Chinese Step by Step」的普通话录音

> 项目目录：`X:\【希腊人学汉语】`
> 现在 App 里没有录音的句子，会用手机自带的中文朗读代替；把录音放进 `docs\audio\` 后，App 自动改播真人录音。

## 要录什么

- `audio_src\female\*.txt`：女声，每个文件一句（拼音课的字词、医院急用句里病人说的话、身体部位、指示牌）
- `audio_src\male\*.txt`：男声，每个文件一句（医院急用句里「医生会说」的话）
- `audio_src\list.csv`：全部条目一览（id、声音、中文、拼音、英语），核对用
- 共 241 条、约 760 个字符（ElevenLabs 每月免费 1 万字符就够）

**文件名就是 App 里的音频 id，不要改名。** 生成的 mp3 必须叫 `<同名>.mp3`。

## 用的工具和声音

- 工具：`X:\AIWorkFlow\Audio\elevenlabs\tts\el_tts.py`（API key 已在同目录 `.env`）
- 模型：`eleven_multilingual_v2`（普通话声调稳定）
- 女声：**Shan Shan**（北京口音普通话）`ByhETIclHirOlWnWKhHc`
- 男声：**James Gao**（标准普通话）`4VZIsMPtgggwNg7OXbPY`

## 步骤

1. **先试 5 条，给用户听**（确认声音合适再全量生成）：
   把 `audio_src\female` 里这几条复制到一个临时目录试生成——妈、麻、马、骂（`list.csv` 里 pinyin 为 mā má mǎ mà 的四条）和「请叫救护车！」。
   ```
   python "X:\AIWorkFlow\Audio\elevenlabs\tts\el_tts.py" <临时目录> -o _el_try --voice ByhETIclHirOlWnWKhHc --model eleven_multilingual_v2
   ```
   重点听**四个声调是否清楚、不同**。不满意可以换声音（声音库：`X:\AIWorkFlow\Audio\elevenlabs\elevenlabs_Audios\data\voices.js`，筛 `l == "Chinese"`，优先 beijing / standard 口音，不要台湾口音）。

2. **全量生成**：
   ```
   python "X:\AIWorkFlow\Audio\elevenlabs\tts\el_tts.py" audio_src\female -o _el_out\female --voice ByhETIclHirOlWnWKhHc --model eleven_multilingual_v2
   python "X:\AIWorkFlow\Audio\elevenlabs\tts\el_tts.py" audio_src\male   -o _el_out\male   --voice 4VZIsMPtgggwNg7OXbPY --model eleven_multilingual_v2
   ```
   已经生成过的会自动跳过（断点续跑）。

3. **质检**：
   ```
   python "X:\AIWorkFlow\Audio\elevenlabs\tts\qa_whisper.py" _el_out\female --lang zh
   python "X:\AIWorkFlow\Audio\elevenlabs\tts\qa_whisper.py" _el_out\male --lang zh
   ```
   - 句子：识别结果和原文（去掉标点）应该一致，不一致的用 `--force` 单独重新生成那一条再查。
   - 单个字（拼音课）：语音识别会写成同音字，这正常；要核对的是**声调**。把四声组（如 mā má mǎ mà、bā pā、dà tà）列出来请用户逐组听，读错声调的重新生成（可以换个 seed：`--seed 2`）。

4. **放进 App**：把 `_el_out\female\*.mp3` 和 `_el_out\male\*.mp3` 复制到 `docs\audio\`（只要 mp3，不要 json）。

5. **检查数量**：
   ```
   python scripts\build.py
   ```
   最后一行应显示「已有录音 241 条」。

6. **发布**：把 `docs\sw.js` 第一行的 `VERSION` 加 1（例如 `cs-v1` → `cs-v2`，让手机更新缓存），然后
   ```
   git add -A && git commit -m "Add Mandarin audio (ElevenLabs)" && git push
   ```
   GitHub Pages 会自动发布 `docs\` 目录，几分钟后手机上刷新就能听到录音。

## 注意

- 不要修改 `content\` 和 `docs\data\content.js`；改了内容要重新跑 `python scripts\build.py`，id 会随文字变化。
- 不要把 `.env`（API key）复制进本项目或提交到 GitHub。
- `_el_out\` 是中间文件，不提交（已在 `.gitignore`）。
