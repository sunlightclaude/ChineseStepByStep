"""预备阶段 P1–P8：拼音、声调、汉字基础。讲解用英语，发音难点拿希腊语里相近的音作对照。
每个 sounds 组里的条目：(拼音, 汉字, 英语意思)。音频按汉字读（单个字的声调由字决定）。
drill=True 的组会自动出"听音选拼音"的练习题。"""

LESSONS = [
    {
        'id': 'P1', 'title': 'The sounds of Chinese', 'zh': '汉语的声音',
        'goal': 'Understand what a tone is, and hear the four tones.',
        'blocks': [
            ('text', """Every Chinese syllable has three parts: an **initial** (the first consonant), a **final** (the vowel part) and a **tone**.

**ma** → initial **m** + final **a** + a tone.

Chinese has **four tones** plus a light **neutral tone**. The tone is the *pitch* of your voice — high, rising, low or falling — and it changes the meaning of the word."""),
            ('tones', None),
            ('greek', """**For Greek speakers:** Greek has *stress* (ο τόνος): one syllable in a word is louder — *μήλο / μηλό*. Chinese tones are different: **every single syllable** has its own pitch shape, and the pitch, not the loudness, changes the meaning. Don't put "Greek stress" on Chinese words; instead, sing each syllable with its own melody."""),
            ('sounds', {'title': 'Four tones on "ma"', 'drill': True, 'items': [
                ('mā', '妈', 'mother'), ('má', '麻', 'hemp'), ('mǎ', '马', 'horse'), ('mà', '骂', 'to scold')]}),
            ('text', """**The six simple finals**

| Pinyin | Sounds like | Note |
|---|---|---|
| **a** | Greek **α** | mouth wide open |
| **o** | Greek **ο** with very round lips | almost "uo" |
| **e** | *no Greek equivalent* | say **ο** but spread your lips, like a quiet "uh" |
| **i** | Greek **ι** | |
| **u** | Greek **ου** | lips very round |
| **ü** | *no Greek equivalent* | say **ι**, then round your lips like **ου** without moving the tongue (like French *u*, German *ü*) |"""),
            ('sounds', {'title': 'Tones on other syllables', 'drill': True, 'items': [
                ('bā', '八', 'eight'), ('bá', '拔', 'to pull'), ('bǎ', '把', 'to hold'), ('bà', '爸', 'dad')]}),
            ('sounds', {'title': 'yi — wu — yu', 'drill': True, 'items': [
                ('yī', '一', 'one'), ('yí', '姨', 'aunt'), ('yǐ', '椅', 'chair'), ('yì', '亿', 'hundred million'),
                ('wǔ', '五', 'five'), ('wù', '雾', 'fog'), ('yú', '鱼', 'fish'), ('yǔ', '雨', 'rain')]}),
            ('sounds', {'title': 'e', 'drill': True, 'items': [
                ('é', '鹅', 'goose'), ('è', '饿', 'hungry')]}),
            ('text', """**The neutral tone** is short and light, with no tone mark. It usually comes after another syllable:"""),
            ('sounds', {'title': 'Neutral tone', 'drill': False, 'items': [
                ('māma', '妈妈', 'mum'), ('bàba', '爸爸', 'dad'), ('gēge', '哥哥', 'elder brother')]}),
        ],
        'hanzi': {'title': 'What is a Chinese character?', 'text': """Chinese characters began as **pictures**. Many simple characters still look like the thing they mean. You will learn about 300 characters in this course — they are built from a small number of parts.""",
                  'items': [('人', 'rén', 'person', 'a person walking'), ('口', 'kǒu', 'mouth', 'an open mouth'),
                            ('日', 'rì', 'sun; day', 'the sun'), ('月', 'yuè', 'moon; month', 'a crescent moon'),
                            ('山', 'shān', 'mountain', 'three peaks'), ('水', 'shuǐ', 'water', 'flowing water')]},
    },
    {
        'id': 'P2', 'title': 'Initials 1: b p m f d t n l', 'zh': '声母（一）',
        'goal': 'Hear and say the difference between b–p and d–t (aspiration).',
        'blocks': [
            ('text', """The most important new idea for Greek speakers: **aspiration**.

In Chinese, **p t k** are said with a strong puff of air (put your hand in front of your mouth — you should feel it). **b d g** have **no** puff of air.

The letters **b d g do not mean voiced sounds** like Greek μπ ντ γκ. They are voiceless, just without the puff."""),
            ('greek', """**For Greek speakers — good news:** your Greek **π** and **τ** are already exactly Chinese **b** and **d**!

- Chinese **b** ≈ Greek **π** (in *πάω*) — not Greek **β** (which is *v*), not **μπ**
- Chinese **d** ≈ Greek **τ** (in *τα*) — not **ντ**
- Chinese **p** = Greek **π** + a puff of air (*π-χ*)
- Chinese **t** = Greek **τ** + a puff of air
- **m n l f** are like Greek **μ ν λ φ**"""),
            ('sounds', {'title': 'b or p?', 'drill': True, 'items': [
                ('bā', '八', 'eight'), ('pā', '趴', 'to lie on stomach'), ('bù', '不', 'not'), ('pù', '铺', 'shop'),
                ('bō', '波', 'wave'), ('pō', '坡', 'slope')]}),
            ('sounds', {'title': 'd or t?', 'drill': True, 'items': [
                ('dà', '大', 'big'), ('tà', '踏', 'to step'), ('dī', '低', 'low'), ('tī', '踢', 'to kick'),
                ('dù', '肚', 'belly'), ('tù', '兔', 'rabbit')]}),
            ('sounds', {'title': 'm f n l', 'drill': True, 'items': [
                ('mā', '妈', 'mother'), ('fā', '发', 'to send'), ('nǐ', '你', 'you'), ('lǐ', '里', 'inside'),
                ('nǚ', '女', 'woman'), ('lǜ', '绿', 'green')]}),
        ],
        'hanzi': {'title': 'Strokes 1', 'text': """Every character is written with a few basic **strokes**. The first five:""",
                  'items': [('一', 'héng', 'horizontal stroke 横', 'left → right'), ('丨', 'shù', 'vertical stroke 竖', 'top → bottom'),
                            ('丿', 'piě', 'left-falling stroke 撇', 'top-right → bottom-left'), ('丶', 'diǎn', 'dot 点', 'short, top → down-right'),
                            ('㇏', 'nà', 'right-falling stroke 捺', 'top-left → bottom-right'),
                            ('十', 'shí', 'ten', 'horizontal, then vertical'), ('大', 'dà', 'big', 'a person with arms open'), ('八', 'bā', 'eight', 'left-falling, then right-falling')]},
    },
    {
        'id': 'P3', 'title': 'Initials 2: g k h · j q x', 'zh': '声母（二）',
        'goal': 'Say g–k and j–q, and the new sounds j q x.',
        'blocks': [
            ('greek', """- Chinese **g** ≈ Greek **κ** (in *καλά*), no puff of air; **k** = **κ** + a puff of air
- Chinese **h** ≈ Greek **χ** in *χαρά* — often a little lighter"""),
            ('sounds', {'title': 'g k h', 'drill': True, 'items': [
                ('gē', '哥', 'elder brother'), ('kē', '科', 'department'), ('hē', '喝', 'to drink'),
                ('gǔ', '古', 'ancient'), ('kǔ', '苦', 'bitter'), ('hǔ', '虎', 'tiger')]}),
            ('text', """**j q x** are made with the **flat middle of the tongue** against the hard palate, with the tip of the tongue down behind the lower teeth. They only come before **i** and **ü**.

- **x** ≈ Greek **χ** in *χέρι*, but with the tongue further forward — between **σ** and that **χ**
- **j** ≈ a quick, soft "τσ" with the tongue flat (no puff of air)
- **q** = **j** + a puff of air

After **j q x** the letter **u** is really **ü**: *ju* = jü, *qu* = qü, *xu* = xü."""),
            ('sounds', {'title': 'j q x', 'drill': True, 'items': [
                ('jī', '鸡', 'chicken'), ('qī', '七', 'seven'), ('xī', '西', 'west'),
                ('jiā', '家', 'home'), ('qián', '钱', 'money'), ('xiè', '谢', 'thank'),
                ('jù', '句', 'sentence'), ('qù', '去', 'to go'), ('xū', '需', 'to need')]}),
        ],
        'hanzi': {'title': 'Strokes 2 and stroke order', 'text': """More strokes, and the **rules of stroke order** (the order matters — it makes your writing fast and readable):

1. Horizontal before vertical: 十
2. Left-falling before right-falling: 人 八
3. Top to bottom: 三
4. Left to right: 川
5. Outside before inside: 月
6. Inside before closing the box: 日 国
7. Middle before the two sides: 小 水""",
                  'items': [('三', 'sān', 'three', 'top to bottom'), ('川', 'chuān', 'river', 'left to right'),
                            ('小', 'xiǎo', 'small', 'middle first'), ('国', 'guó', 'country', 'inside before closing'),
                            ('了', 'le', '(grammar word)', 'horizontal-turn, then vertical hook')]},
    },
    {
        'id': 'P4', 'title': 'Initials 3: z c s · zh ch sh r', 'zh': '声母（三）',
        'goal': 'Say z–c, and tell flat (z c s) from curled (zh ch sh) sounds.',
        'blocks': [
            ('greek', """- Chinese **z** ≈ Greek **τσ** in *τσάι* (no puff of air) — **not** the voiced τζ
- Chinese **c** = **τσ** + a puff of air
- Chinese **s** ≈ Greek **σ**"""),
            ('sounds', {'title': 'z c s', 'drill': True, 'items': [
                ('zì', '字', 'character'), ('cì', '次', 'time (occurrence)'), ('sì', '四', 'four'),
                ('zǎo', '早', 'early'), ('cǎo', '草', 'grass'), ('sǎo', '扫', 'to sweep')]}),
            ('text', """**zh ch sh r** — curl the tip of your tongue **up and back** behind the ridge of your upper teeth. Greek has no such sounds.

- **zh** ≈ like **z** but with the tongue curled
- **ch** = **zh** + a puff of air
- **sh** ≈ English *sh*, tongue curled
- **r** ≈ English *r* in *run* — **not** the rolled Greek **ρ**!

⚠️ After **z c s zh ch sh r**, the letter **i** is **not** Greek **ι**: it is a buzzing sound that just continues the consonant. *si* sounds like "sss", *shi* like "shrr"."""),
            ('sounds', {'title': 'zh ch sh r', 'drill': True, 'items': [
                ('zhī', '知', 'to know'), ('chī', '吃', 'to eat'), ('shī', '诗', 'poem'), ('rì', '日', 'sun'),
                ('zhǎo', '找', 'to look for'), ('chǎo', '炒', 'to stir-fry'), ('shǎo', '少', 'few'), ('ròu', '肉', 'meat')]}),
            ('sounds', {'title': 'Flat or curled?', 'drill': True, 'items': [
                ('sì', '四', 'four'), ('shí', '十', 'ten'), ('zì', '字', 'character'), ('zhì', '治', 'to treat (illness)'),
                ('cā', '擦', 'to wipe'), ('chā', '插', 'to insert')]}),
        ],
        'hanzi': {'title': 'Radicals 1', 'text': """Most characters are made of a **radical** (a part that hints at the meaning) plus other parts. Learn to spot these:""",
                  'items': [('亻', 'rén', 'person', 'in 你 他 们 住'), ('口', 'kǒu', 'mouth', 'in 吃 喝 叫 吗'),
                            ('女', 'nǚ', 'woman', 'in 妈 好 她 姐'), ('子', 'zǐ', 'child', 'in 字 学 孩'),
                            ('木', 'mù', 'tree; wood', 'in 林 椅 本')]},
    },
    {
        'id': 'P5', 'title': 'Compound finals', 'zh': '复韵母',
        'goal': 'Glide smoothly through ai ei ao ou and the finals with i u ü.',
        'blocks': [
            ('text', """A compound final is **one syllable** that glides from one vowel to another. Don't break it into two syllables.

| Final | Sounds like |
|---|---|
| **ai** | *άι* in *τσάι* |
| **ei** | *έι* in *λέι* (one syllable) |
| **ao** | *άου* — one syllable |
| **ou** | *όου* — one syllable |
| **ia / ie / iao / iu** | start with a quick **ι** |
| **ua / uo / uai / ui** | start with a quick **ου** |
| **üe** | start with **ü** |

Spelling notes: **iou** is written **iu** (*liù*), **uei** is written **ui** (*duì*)."""),
            ('sounds', {'title': 'ai ei ao ou', 'drill': True, 'items': [
                ('ài', '爱', 'to love'), ('běi', '北', 'north'), ('hǎo', '好', 'good'), ('kǒu', '口', 'mouth')]}),
            ('sounds', {'title': 'Finals with i u ü', 'drill': True, 'items': [
                ('jiā', '家', 'home'), ('xiè', '谢', 'thank'), ('xiǎo', '小', 'small'), ('liù', '六', 'six'),
                ('huā', '花', 'flower'), ('wǒ', '我', 'I'), ('kuài', '快', 'fast'), ('shuǐ', '水', 'water'),
                ('duì', '对', 'correct'), ('xué', '学', 'to study')]}),
        ],
        'hanzi': {'title': 'Radicals 2', 'text': """Radicals usually sit on the left or on top and change shape a little:""",
                  'items': [('氵', 'shuǐ', 'water', 'in 河 海 汉 洗'), ('扌', 'shǒu', 'hand', 'in 打 拿 找'),
                            ('讠', 'yán', 'speech', 'in 说 话 语 请'), ('心 / 忄', 'xīn', 'heart', 'in 想 您 忙 快'),
                            ('日', 'rì', 'sun', 'in 时 明 星 早')]},
    },
    {
        'id': 'P6', 'title': 'Nasal finals: -n and -ng', 'zh': '鼻韵母',
        'goal': 'Hear and say the difference between -n and -ng.',
        'blocks': [
            ('text', """Chinese syllables can end in **-n** or **-ng** — and the difference changes the meaning.

- **-n**: the tip of the tongue touches behind the upper teeth, like Greek **ν**
- **-ng**: the **back** of the tongue rises to the soft palate, like the **γγ** in *Άγγλος* — but stop before the **γ/κ** sound"""),
            ('greek', """Greek words almost never end in **-ng**, so at first **-ng** may sound like **-n** to you. Listen to the pairs below many times; the vowel before **-ng** also sounds darker and deeper."""),
            ('sounds', {'title': '-n or -ng?', 'drill': True, 'items': [
                ('shān', '山', 'mountain'), ('shāng', '伤', 'wound'), ('fàn', '饭', 'meal'), ('fàng', '放', 'to put'),
                ('lín', '林', 'forest'), ('líng', '零', 'zero'), ('qián', '钱', 'money'), ('qiáng', '墙', 'wall'),
                ('chuán', '船', 'boat'), ('chuáng', '床', 'bed')]}),
            ('sounds', {'title': 'More nasal finals', 'drill': True, 'items': [
                ('rén', '人', 'person'), ('lěng', '冷', 'cold'), ('yún', '云', 'cloud'), ('yòng', '用', 'to use'),
                ('xīn', '心', 'heart'), ('xīng', '星', 'star')]}),
        ],
        'hanzi': {'title': 'Radicals 3', 'text': '',
                  'items': [('辶', 'zǒu', 'walking', 'in 这 还 远 近 进'), ('宀', 'mián', 'roof', 'in 家 字 安'),
                            ('艹', 'cǎo', 'grass; plant', 'in 花 茶 菜 药'), ('钅', 'jīn', 'metal', 'in 钱 铁 银'),
                            ('饣', 'shí', 'food', 'in 饭 饿 馆')]},
    },
    {
        'id': 'P7', 'title': 'Spelling rules and tone changes', 'zh': '拼写规则和变调',
        'goal': 'Read pinyin correctly and apply the tone-change rules.',
        'blocks': [
            ('text', """**Spelling rules**

- A syllable that starts with **i** is written with **y**: i → *yi*, ia → *ya*, ie → *ye*
- A syllable that starts with **u** is written with **w**: u → *wu*, ua → *wa*, uo → *wo*
- **ü** alone is written **yu**; after **j q x y** the dots are dropped (*qù, yú*), after **n l** they stay (*nǚ, lǜ*)
- **iou → iu**, **uei → ui**, **uen → un**
- The tone mark goes on **a** or **e** if there is one; in **ou** it goes on **o**; otherwise on the last vowel (*liù, duì*)

⚠️ Pinyin uses Latin letters, but **not with their Greek-reader values**: **c** = τσ + puff, **q** = soft τσ + puff, **x** ≈ σ/χ of *χέρι*, **z** = τσ, **h** = χ."""),
            ('text', """**Tone changes (sandhi)** — the written tone stays the same in dictionaries, but in speech:

1. **Third + third → second + third**: 你好 *nǐ hǎo* is said *ní hǎo*
2. **不 bù** becomes **bú** before a fourth tone: 不是 *bú shì*, 不要 *bú yào*
3. **一 yī** becomes **yí** before a fourth tone (一个 *yí ge*), and **yì** before tones 1, 2, 3 (一天 *yì tiān*, 一年 *yì nián*, 一起 *yìqǐ*)
4. **-儿 (erhua)**: in northern Chinese, some words end with an *r* sound: 哪儿 *nǎr*, 一点儿 *yìdiǎnr*"""),
            ('sounds', {'title': 'Tone changes in real words', 'drill': True, 'items': [
                ('nǐ hǎo', '你好', 'hello'), ('hěn hǎo', '很好', 'very good'), ('bú shì', '不是', 'is not'),
                ('bù hǎo', '不好', 'not good'), ('yí ge', '一个', 'one (of something)'), ('yì tiān', '一天', 'one day'),
                ('yìqǐ', '一起', 'together'), ('nǎr', '哪儿', 'where')]}),
        ],
        'hanzi': {'title': 'How characters are built', 'text': """Most characters are combinations of parts, arranged in a few patterns:""",
                  'items': [('你', 'nǐ', 'you', 'left–right: 亻 + 尔'), ('好', 'hǎo', 'good', 'left–right: 女 + 子'),
                            ('字', 'zì', 'character', 'top–bottom: 宀 + 子'), ('学', 'xué', 'to study', 'top–bottom'),
                            ('国', 'guó', 'country', 'enclosed: 囗 + 玉'), ('问', 'wèn', 'to ask', 'half-enclosed: 门 + 口')]},
    },
    {
        'id': 'P8', 'title': 'Putting it together', 'zh': '综合练习',
        'goal': 'Count from 1 to 10 and use classroom phrases.',
        'blocks': [
            ('text', """Numbers are a perfect tone exercise — say them slowly and exaggerate each tone."""),
            ('sounds', {'title': 'Numbers 1–10', 'drill': True, 'items': [
                ('yī', '一', 'one'), ('èr', '二', 'two'), ('sān', '三', 'three'), ('sì', '四', 'four'), ('wǔ', '五', 'five'),
                ('liù', '六', 'six'), ('qī', '七', 'seven'), ('bā', '八', 'eight'), ('jiǔ', '九', 'nine'), ('shí', '十', 'ten')]}),
            ('sounds', {'title': 'Classroom phrases', 'drill': False, 'items': [
                ('Lǎoshī hǎo!', '老师好！', 'Hello, teacher!'), ('Xièxie!', '谢谢！', 'Thank you!'), ('Bú kèqi.', '不客气。', "You're welcome."),
                ('Duìbuqǐ.', '对不起。', 'Sorry.'), ('Méi guānxi.', '没关系。', "It doesn't matter."),
                ('Wǒ bù dǒng.', '我不懂。', "I don't understand."), ('Qǐng zài shuō yí biàn.', '请再说一遍。', 'Please say it again.'),
                ('Qǐng shuō màn yìdiǎnr.', '请说慢一点儿。', 'Please speak more slowly.')]}),
        ],
        'hanzi': {'title': 'Review: 30 first characters', 'text': """You can now recognise these characters. Tap each one to hear it.""",
                  'items': [(c, p, e, '') for c, p, e in [
                      ('一', 'yī', 'one'), ('二', 'èr', 'two'), ('三', 'sān', 'three'), ('四', 'sì', 'four'), ('五', 'wǔ', 'five'),
                      ('六', 'liù', 'six'), ('七', 'qī', 'seven'), ('八', 'bā', 'eight'), ('九', 'jiǔ', 'nine'), ('十', 'shí', 'ten'),
                      ('人', 'rén', 'person'), ('口', 'kǒu', 'mouth'), ('日', 'rì', 'sun'), ('月', 'yuè', 'moon'), ('山', 'shān', 'mountain'),
                      ('水', 'shuǐ', 'water'), ('大', 'dà', 'big'), ('小', 'xiǎo', 'small'), ('中', 'zhōng', 'middle'), ('国', 'guó', 'country'),
                      ('你', 'nǐ', 'you'), ('我', 'wǒ', 'I'), ('他', 'tā', 'he'), ('好', 'hǎo', 'good'), ('女', 'nǚ', 'woman'),
                      ('子', 'zǐ', 'child'), ('不', 'bù', 'not'), ('是', 'shì', 'to be'), ('家', 'jiā', 'home'), ('学', 'xué', 'to study')]]},
    },
]
