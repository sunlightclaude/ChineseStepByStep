"""把 content/ 里写好的课程内容生成 App 数据和"要录的音"清单。
输出：
  docs/data/content.js          App 读的数据（window.CONTENT）
  audio_src/female/<id>.txt    要用女声生成的句子（每个文件一句，el_tts.py 按文件名出 <id>.mp3）
  audio_src/male/<id>.txt      要用男声生成的句子（医生 / 护士说的话）
  audio_src/list.csv           全部条目一览：id, 声音, 中文, 拼音, 英语
音频 id 由中文文本决定（同一句只录一次）。生成好的 mp3 放进 docs/audio/<id>.mp3，App 就会播真人录音；
没有录音的句子 App 用手机自带的中文朗读代替。
用法: python scripts/build.py"""
import csv, hashlib, json, os, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'content'))
import pinyin as PY
import hospital as HO

audio = {}          # id -> {voice, text, py, en}


def aid(text, voice='female', py='', en=''):
    """音频 id：中文文本的短哈希。单个字后面加句号，单字更容易读出完整的声调。"""
    spoken = text if len(text) > 1 or text[-1:] in '。！？' else text + '。'
    h = 'a' + hashlib.md5((voice + '|' + spoken).encode('utf-8')).hexdigest()[:10]
    audio.setdefault(h, {'voice': voice, 'text': spoken, 'py': py, 'en': en})
    return h


def tone_of(py):
    """单音节拼音的声调 1–4，轻声 / 多音节返回 0。"""
    s = unicodedata.normalize('NFD', py.lower())
    if len(py.split()) > 1:
        return 0
    marks = {'̄': 1, '́': 2, '̌': 3, '̀': 4}
    for ch in s:
        if ch in marks:
            return marks[ch]
    return 0


def build():
    lessons = []
    for L in PY.LESSONS:
        blocks = []
        for kind, data in L['blocks']:
            if kind in ('text', 'greek'):
                blocks.append({'t': kind, 'md': data})
            elif kind == 'tones':
                blocks.append({'t': 'tones', 'items': [
                    {'py': p, 'hz': h, 'en': e, 'tone': tone_of(p), 'a': aid(h, py=p, en=e)}
                    for p, h, e in [('mā', '妈', 'mother'), ('má', '麻', 'hemp'), ('mǎ', '马', 'horse'), ('mà', '骂', 'to scold')]]})
            elif kind == 'sounds':
                blocks.append({'t': 'sounds', 'title': data['title'], 'drill': data['drill'], 'items': [
                    {'py': p, 'hz': h, 'en': e, 'tone': tone_of(p), 'a': aid(h, py=p, en=e)} for p, h, e in data['items']]})
        hz = L['hanzi']
        items = []
        for t in hz['items']:
            if t[0] == 'part':
                # 笔画 / 偏旁：不是字，不发音；显示它的名称（横、三点水、走之旁……）
                _, sym, name, name_py, e, n = t
                items.append({'hz': sym, 'part': True, 'name': name, 'py': name_py, 'en': e, 'note': n, 'a': None})
            else:
                c, p, e, n = t
                items.append({'hz': c, 'py': p, 'en': e, 'note': n, 'a': aid(c, py=p, en=e)})
        hanzi = {'title': hz['title'], 'md': hz['text'], 'items': items}
        lessons.append({'id': L['id'], 'title': L['title'], 'zh': L['zh'], 'goal': L['goal'], 'blocks': blocks, 'hanzi': hanzi})

    groups = []
    for g in HO.GROUPS:
        voice = 'male' if g.get('doctor') else 'female'
        groups.append({'id': g['id'], 'title': g['title'], 'zh': g['zh'], 'icon': g['icon'], 'doctor': bool(g.get('doctor')),
                       'items': [{'hz': h, 'py': p, 'en': e, 'a': aid(h.replace('……', ''), voice, p, e)} for h, p, e in g['items']]})
    body = [{'hz': h, 'py': p, 'en': e, 'icon': i, 'a': aid(h, py=p, en=e)} for h, p, e, i in HO.BODY]
    signs = [{'hz': h, 'py': p, 'en': e, 'a': aid(h, py=p, en=e)} for h, p, e in HO.SIGNS]

    data = {'version': 1, 'lessons': lessons, 'hospital': {'groups': groups, 'body': body, 'signs': signs}}
    os.makedirs(os.path.join(ROOT, 'docs', 'data'), exist_ok=True)
    with open(os.path.join(ROOT, 'docs', 'data', 'content.js'), 'w', encoding='utf-8') as f:
        f.write('window.CONTENT=')
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        f.write(';')

    # 要录的音
    for voice in ('female', 'male'):
        d = os.path.join(ROOT, 'audio_src', voice)
        os.makedirs(d, exist_ok=True)
        keep = {f'{k}.txt' for k, v in audio.items() if v['voice'] == voice}
        for old in os.listdir(d):
            if old.endswith('.txt') and old not in keep:
                os.remove(os.path.join(d, old))
        for k, v in audio.items():
            if v['voice'] == voice:
                with open(os.path.join(d, k + '.txt'), 'w', encoding='utf-8') as f:
                    f.write(v['text'])
    with open(os.path.join(ROOT, 'audio_src', 'list.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['id', 'voice', 'text', 'pinyin', 'english'])
        for k, v in sorted(audio.items(), key=lambda kv: (kv[1]['voice'], kv[1]['py'])):
            w.writerow([k, v['voice'], v['text'], v['py'], v['en']])
    n_chars = sum(len(v['text']) for v in audio.values())
    have = {f[:-4] for f in os.listdir(os.path.join(ROOT, 'docs', 'audio'))} if os.path.isdir(os.path.join(ROOT, 'docs', 'audio')) else set()
    print(f'课程 {len(lessons)} 课，医院急用句 {sum(len(g["items"]) for g in groups)} 句，身体部位 {len(body)}，指示牌 {len(signs)}')
    print(f'要录的音 {len(audio)} 条（女声 {sum(1 for v in audio.values() if v["voice"] == "female")}，男声 {sum(1 for v in audio.values() if v["voice"] == "male")}），'
          f'共 {n_chars} 个字符；已有录音 {len(have & set(audio))} 条')


if __name__ == '__main__':
    build()
