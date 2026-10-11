"""医院急用句速查：大号汉字 + 拼音 + 英语 + 发音。第一天就能用，不按课程顺序。
每句：(汉字, 拼音, 英语)。'doctor': True 的一组是医生 / 护士说的话（男声），其余是病人说的（女声）。"""

GROUPS = [
    {'id': 'help', 'title': 'Emergency', 'zh': '求救', 'icon': '🚨', 'items': [
        ('救命！', 'Jiùmìng!', 'Help!'),
        ('请叫救护车！', 'Qǐng jiào jiùhùchē!', 'Please call an ambulance!'),
        ('请打一二零。', 'Qǐng dǎ yāo èr líng.', 'Please call 120 (ambulance).'),
        ('我需要医生。', 'Wǒ xūyào yīshēng.', 'I need a doctor.'),
        ('很急！', 'Hěn jí!', "It's urgent!"),
        ('请带我去医院。', 'Qǐng dài wǒ qù yīyuàn.', 'Please take me to the hospital.'),
        ('我的地址是……', 'Wǒ de dìzhǐ shì……', 'My address is …'),
    ]},
    {'id': 'lang', 'title': "I don't speak Chinese", 'zh': '不会说中文', 'icon': '💬', 'items': [
        ('我不会说中文。', 'Wǒ bú huì shuō Zhōngwén.', "I can't speak Chinese."),
        ('你会说英语吗？', 'Nǐ huì shuō Yīngyǔ ma?', 'Can you speak English?'),
        ('我是希腊人。', 'Wǒ shì Xīlà rén.', "I'm Greek."),
        ('请写下来。', 'Qǐng xiě xiàlai.', 'Please write it down.'),
        ('请说慢一点儿。', 'Qǐng shuō màn yìdiǎnr.', 'Please speak more slowly.'),
        ('请用手机翻译。', 'Qǐng yòng shǒujī fānyì.', 'Please translate with your phone.'),
        ('我听不懂。', 'Wǒ tīng bu dǒng.', "I don't understand."),
    ]},
    {'id': 'pain', 'title': 'Where it hurts', 'zh': '哪里不舒服', 'icon': '🤕', 'items': [
        ('我不舒服。', 'Wǒ bù shūfu.', "I don't feel well."),
        ('我这里疼。', 'Wǒ zhèlǐ téng.', 'It hurts here. (point)'),
        ('我头疼。', 'Wǒ tóu téng.', 'I have a headache.'),
        ('我肚子疼。', 'Wǒ dùzi téng.', 'I have a stomach ache.'),
        ('我胸口疼。', 'Wǒ xiōngkǒu téng.', 'I have chest pain.'),
        ('我嗓子疼。', 'Wǒ sǎngzi téng.', 'I have a sore throat.'),
        ('我牙疼。', 'Wǒ yá téng.', 'I have a toothache.'),
        ('我背疼。', 'Wǒ bèi téng.', 'My back hurts.'),
        ('我呼吸困难。', 'Wǒ hūxī kùnnan.', "I can't breathe well."),
    ]},
    {'id': 'symptom', 'title': 'Symptoms', 'zh': '症状', 'icon': '🌡️', 'items': [
        ('我发烧了。', 'Wǒ fāshāo le.', 'I have a fever.'),
        ('我咳嗽。', 'Wǒ késou.', 'I have a cough.'),
        ('我头晕。', 'Wǒ tóu yūn.', 'I feel dizzy.'),
        ('我想吐。', 'Wǒ xiǎng tù.', 'I feel sick (want to vomit).'),
        ('我吐了。', 'Wǒ tù le.', 'I vomited.'),
        ('我拉肚子。', 'Wǒ lā dùzi.', 'I have diarrhoea.'),
        ('我流血了。', 'Wǒ liú xiě le.', "I'm bleeding."),
        ('我摔倒了。', 'Wǒ shuāidǎo le.', 'I fell down.'),
        ('已经两天了。', 'Yǐjīng liǎng tiān le.', 'It has been two days.'),
        ('从昨天开始。', 'Cóng zuótiān kāishǐ.', 'Since yesterday.'),
    ]},
    {'id': 'history', 'title': 'Allergies and medical history', 'zh': '过敏和病史', 'icon': '📋', 'items': [
        ('我对青霉素过敏。', 'Wǒ duì qīngméisù guòmǐn.', "I'm allergic to penicillin."),
        ('我对这个药过敏。', 'Wǒ duì zhège yào guòmǐn.', "I'm allergic to this medicine."),
        ('我有糖尿病。', 'Wǒ yǒu tángniàobìng.', 'I have diabetes.'),
        ('我有高血压。', 'Wǒ yǒu gāoxuèyā.', 'I have high blood pressure.'),
        ('我有心脏病。', 'Wǒ yǒu xīnzàngbìng.', 'I have a heart condition.'),
        ('我有哮喘。', 'Wǒ yǒu xiàochuǎn.', 'I have asthma.'),
        ('我怀孕了。', 'Wǒ huáiyùn le.', "I'm pregnant."),
        ('我在吃这个药。', 'Wǒ zài chī zhège yào.', "I'm taking this medicine."),
    ]},
    {'id': 'register', 'title': 'At the hospital', 'zh': '挂号和看病', 'icon': '🏥', 'items': [
        ('在哪儿挂号？', 'Zài nǎr guàhào?', 'Where do I register?'),
        ('我要看急诊。', 'Wǒ yào kàn jízhěn.', 'I need the emergency department.'),
        ('我要挂号。', 'Wǒ yào guàhào.', 'I want to register (to see a doctor).'),
        ('这是我的护照。', 'Zhè shì wǒ de hùzhào.', 'This is my passport.'),
        ('要等多长时间？', 'Yào děng duō cháng shíjiān?', 'How long do I have to wait?'),
        ('洗手间在哪儿？', 'Xǐshǒujiān zài nǎr?', 'Where is the toilet?'),
    ]},
    {'id': 'doctor', 'title': 'What the doctor says', 'zh': '医生会说', 'icon': '🩺', 'doctor': True, 'items': [
        ('你哪儿不舒服？', 'Nǐ nǎr bù shūfu?', "What's wrong? / Where does it hurt?"),
        ('多长时间了？', 'Duō cháng shíjiān le?', 'How long has it been?'),
        ('疼得厉害吗？', 'Téng de lìhai ma?', 'Does it hurt a lot?'),
        ('你对什么过敏吗？', 'Nǐ duì shénme guòmǐn ma?', 'Are you allergic to anything?'),
        ('张嘴。', 'Zhāng zuǐ.', 'Open your mouth.'),
        ('深呼吸。', 'Shēn hūxī.', 'Breathe deeply.'),
        ('请躺下。', 'Qǐng tǎng xià.', 'Please lie down.'),
        ('先量一下体温。', 'Xiān liáng yíxià tǐwēn.', "First let's take your temperature."),
        ('你要验血。', 'Nǐ yào yàn xiě.', 'You need a blood test.'),
        ('你要拍个片子。', 'Nǐ yào pāi ge piānzi.', 'You need an X-ray.'),
        ('你要住院。', 'Nǐ yào zhùyuàn.', 'You need to stay in hospital.'),
        ('先去交费。', 'Xiān qù jiāo fèi.', 'Go and pay first.'),
    ]},
    {'id': 'medicine', 'title': 'Medicine and paying', 'zh': '拿药和交费', 'icon': '💊', 'items': [
        ('一天吃几次？', 'Yì tiān chī jǐ cì?', 'How many times a day?'),
        ('一次吃几片？', 'Yí cì chī jǐ piàn?', 'How many tablets each time?'),
        ('饭前还是饭后？', 'Fàn qián háishi fàn hòu?', 'Before or after meals?'),
        ('药房在哪儿？', 'Yàofáng zài nǎr?', 'Where is the pharmacy?'),
        ('在哪儿交钱？', 'Zài nǎr jiāo qián?', 'Where do I pay?'),
        ('可以用信用卡吗？', 'Kěyǐ yòng xìnyòngkǎ ma?', 'Can I pay by credit card?'),
        ('我有保险。', 'Wǒ yǒu bǎoxiǎn.', 'I have insurance.'),
        ('请给我收据。', 'Qǐng gěi wǒ shōujù.', 'Please give me a receipt.'),
    ]},
    {'id': 'level', 'title': 'How much it hurts', 'zh': '疼痛程度', 'icon': '📈', 'items': [
        ('有点儿疼。', 'Yǒudiǎnr téng.', 'It hurts a little.'),
        ('很疼。', 'Hěn téng.', 'It hurts a lot.'),
        ('非常疼。', 'Fēicháng téng.', 'It hurts very much.'),
        ('疼得受不了。', 'Téng de shòu bu liǎo.', "The pain is unbearable."),
        ('现在好一点儿了。', 'Xiànzài hǎo yìdiǎnr le.', "It's a bit better now."),
    ]},
]

# 身体部位：(汉字, 拼音, 英语, 图标)
BODY = [
    ('头', 'tóu', 'head', '🙂'), ('眼睛', 'yǎnjing', 'eye', '👁️'), ('耳朵', 'ěrduo', 'ear', '👂'), ('鼻子', 'bízi', 'nose', '👃'),
    ('嘴', 'zuǐ', 'mouth', '👄'), ('牙', 'yá', 'tooth', '🦷'), ('嗓子', 'sǎngzi', 'throat', '🗣️'), ('脖子', 'bózi', 'neck', '🧣'),
    ('胸口', 'xiōngkǒu', 'chest', '🫁'), ('心脏', 'xīnzàng', 'heart', '❤️'), ('肚子', 'dùzi', 'belly; stomach', '🫃'), ('背', 'bèi', 'back', '🔙'),
    ('腰', 'yāo', 'lower back; waist', '⬅️'), ('手', 'shǒu', 'hand', '✋'), ('胳膊', 'gēbo', 'arm', '💪'), ('腿', 'tuǐ', 'leg', '🦵'),
    ('脚', 'jiǎo', 'foot', '🦶'), ('皮肤', 'pífū', 'skin', '🖐️'),
]

# 医院里的指示牌：(汉字, 拼音, 英语)
SIGNS = [
    ('急诊', 'jízhěn', 'Emergency'), ('挂号', 'guàhào', 'Registration'), ('收费处', 'shōufèichù', 'Cashier / Payment'),
    ('内科', 'nèikē', 'Internal medicine'), ('外科', 'wàikē', 'Surgery'), ('儿科', 'érkē', 'Paediatrics (children)'),
    ('妇科', 'fùkē', 'Gynaecology'), ('牙科', 'yákē', 'Dentistry'), ('眼科', 'yǎnkē', 'Ophthalmology (eyes)'),
    ('药房', 'yàofáng', 'Pharmacy'), ('化验室', 'huàyànshì', 'Laboratory (tests)'), ('住院部', 'zhùyuànbù', 'Inpatient department'),
    ('出口', 'chūkǒu', 'Exit'), ('洗手间', 'xǐshǒujiān', 'Toilet'),
]
