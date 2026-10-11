// Chinese Step by Step —— 希腊人学汉语（网页版 App，iPhone / 安卓都能用，加到主屏幕后可离线）
(function () {
  'use strict';
  const C = window.CONTENT;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* 隐私模式下存不了，不影响使用 */ } },
  };
  function toast(msg, ms) {
    const t = $('toast'); t.textContent = msg; t.classList.remove('hidden');
    clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.add('hidden'), ms || 2000);
  }
  let slow = store.get('cs_slow', false);
  const toneClass = (t) => 'tone' + (t || 0);

  // ---------------------------------------------------------------- 发音
  // 有录音（audio/<id>.mp3）就播录音；没有就用手机自带的中文朗读
  const missing = new Set(store.get('cs_missing', []));
  let player = null;
  function zhVoice() {
    const vs = (window.speechSynthesis && speechSynthesis.getVoices()) || [];
    return vs.find((v) => /zh[-_]CN/i.test(v.lang)) || vs.find((v) => /^zh/i.test(v.lang)) || null;
  }
  if (window.speechSynthesis) speechSynthesis.onvoiceschanged = () => {};
  function speak(text) {
    if (!window.speechSynthesis) { toast('No Chinese voice on this device'); return; }
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'zh-CN';
    const v = zhVoice(); if (v) u.voice = v;
    u.rate = slow ? 0.55 : 0.85;
    speechSynthesis.speak(u);
  }
  function play(id, text, el) {
    if (player) { player.pause(); player = null; }
    if (window.speechSynthesis) speechSynthesis.cancel();
    document.querySelectorAll('.playing').forEach((x) => x.classList.remove('playing'));
    if (el) { el.classList.add('playing'); setTimeout(() => el.classList.remove('playing'), 1500); }
    if (!id || missing.has(id)) { speak(text); return; }
    const a = new Audio('audio/' + id + '.mp3');
    a.playbackRate = slow ? 0.7 : 1;
    player = a;
    a.onerror = () => { missing.add(id); store.set('cs_missing', [...missing].slice(-500)); if (player === a) speak(text); };
    a.play().catch(() => { if (player === a) speak(text); });
  }

  // ---------------------------------------------------------------- 简单的 Markdown（粗体、斜体、表格、列表、段落）
  function inline(s) {
    return esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\*(.+?)\*/g, '<i>$1</i>');
  }
  function md(src) {
    const lines = String(src || '').split('\n');
    let html = '', i = 0;
    while (i < lines.length) {
      const l = lines[i];
      if (/^\s*\|/.test(l)) {
        const rows = [];
        while (i < lines.length && /^\s*\|/.test(lines[i])) { rows.push(lines[i]); i++; }
        const cells = (r) => r.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
        const body = rows.filter((r) => !/^[\s|:-]+$/.test(r));          // 去掉 |---|---| 分隔行
        const head = cells(body[0]);
        html += '<table><tr>' + head.map((c) => `<th>${inline(c)}</th>`).join('') + '</tr>'
          + body.slice(1).map((r) => '<tr>' + cells(r).map((c) => `<td>${inline(c)}</td>`).join('') + '</tr>').join('') + '</table>';
        continue;
      }
      if (/^\s*(-|\d+\.)\s+/.test(l)) {
        const ordered = /^\s*\d+\./.test(l);
        const items = [];
        while (i < lines.length && /^\s*(-|\d+\.)\s+/.test(lines[i])) { items.push(lines[i].replace(/^\s*(-|\d+\.)\s+/, '')); i++; }
        html += (ordered ? '<ol>' : '<ul>') + items.map((x) => `<li>${inline(x)}</li>`).join('') + (ordered ? '</ol>' : '</ul>');
        continue;
      }
      if (l.trim()) {
        const para = [];
        while (i < lines.length && lines[i].trim() && !/^\s*(\||-\s|\d+\.\s)/.test(lines[i])) { para.push(lines[i]); i++; }
        html += `<p>${para.map(inline).join('<br>')}</p>`;
        continue;
      }
      i++;
    }
    return html;
  }

  // ---------------------------------------------------------------- 路由（#/、#/lesson/P1、#/quiz/P1、#/hospital）
  function go(hash) { if (location.hash !== hash) location.hash = hash; else render(); }
  window.addEventListener('hashchange', render);
  $('back').onclick = () => { if (history.length > 1) history.back(); else go('#/'); };
  $('slowBtn').onclick = () => { slow = !slow; store.set('cs_slow', slow); $('slowBtn').classList.toggle('on', slow); toast(slow ? 'Slow audio: on' : 'Slow audio: off'); };
  $('slowBtn').classList.toggle('on', slow);

  function setTop(title, back) {
    $('title').textContent = title;
    $('back').classList.toggle('hidden', !back);
    window.scrollTo(0, 0);
  }

  function render() {
    const h = location.hash || '#/';
    let m;
    if ((m = h.match(/^#\/lesson\/(\w+)/))) return renderLesson(m[1]);
    if ((m = h.match(/^#\/quiz\/(\w+)/))) return renderQuiz(m[1]);
    if (h.startsWith('#/hospital')) return renderHospital();
    return renderHome();
  }

  // ---------------------------------------------------------------- 首页
  function renderHome() {
    setTop('Chinese Step by Step', false);
    const done = store.get('cs_done', []);
    $('view').innerHTML = `
      <div class="hero"><h2>欢迎！ Welcome!</h2>
        <p class="big">Learn Mandarin Chinese from zero. Explanations in English, with tips for Greek speakers. 🇬🇷 → 🇨🇳</p></div>
      <button class="card tile" data-go="#/hospital"><span class="em">🏥</span>
        <span class="t"><b>Hospital phrases</b><span>Emergency Chinese you can use from day one — show it to the doctor</span></span><span class="chev">›</span></button>
      <h3>Stage 0 · Pinyin and tones（拼音和声调）</h3>
      <div class="card">${C.lessons.map((L) => `
        <button class="lesson-row ${done.includes(L.id) ? 'done' : ''}" data-go="#/lesson/${L.id}">
          <span class="no">${done.includes(L.id) ? '✓' : esc(L.id)}</span>
          <span class="t">${esc(L.title)}<span>${esc(L.zh)} · ${esc(L.goal)}</span></span><span class="chev">›</span></button>`).join('')}</div>
      <p class="note">Lessons 1–50 (greetings, shopping, transport, hospital…) are coming in the next versions.</p>
      <p class="note">Tip: on iPhone, tap <b>Share → Add to Home Screen</b> to use this like an app, also offline.</p>`;
  }

  // ---------------------------------------------------------------- 课
  function toneSvg() {
    // 五度标调：1 = 低，5 = 高
    const shapes = { 1: [[0, 5], [1, 5]], 2: [[0, 3], [1, 5]], 3: [[0, 2], [0.5, 1], [1, 4]], 4: [[0, 5], [1, 1]] };
    const W = 520, H = 196, pad = 30;
    const x = (t, k) => pad + k * 125 + t * 95, y = (v) => H - 18 - (v - 1) * 34;   // 5 度 = 顶部 y≈40，留出标签位置
    let g = '';
    for (let v = 1; v <= 5; v++) g += `<line x1="${pad - 6}" x2="${W - 10}" y1="${y(v)}" y2="${y(v)}" stroke="currentColor" stroke-opacity=".12"/>`;
    [1, 2, 3, 4].forEach((t, k) => {
      const pts = shapes[t].map(([tt, v]) => `${x(tt, k)},${y(v)}`).join(' ');
      g += `<polyline points="${pts}" fill="none" stroke="var(--t${t})" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>`
        + `<text x="${x(0.5, k)}" y="16" text-anchor="middle" font-size="15" fill="var(--t${t})" font-weight="700">Tone ${t}</text>`;
    });
    return `<svg class="tones-svg" viewBox="0 0 ${W} ${H}" role="img" aria-label="The four tones">${g}</svg>`;
  }

  function sndCard(it) {
    return `<div class="snd" data-a="${it.a || ''}" data-hz="${esc(it.hz)}"><div class="hz">${esc(it.hz)}</div>`
      + `<div class="py ${toneClass(it.tone)}">${esc(it.py)}</div><div class="en">${esc(it.en || '')}</div>`
      + `<div class="acts"><button data-play aria-label="Play">▶</button>${it.tone ? '<button data-rec aria-label="Record and compare">🎙</button>' : ''}</div></div>`;
  }

  let curItems = {};
  function renderLesson(id) {
    const L = C.lessons.find((x) => x.id === id); if (!L) return go('#/');
    setTop(`${L.id} · ${L.title}`, true);
    curItems = {};
    let html = `<div class="goal">🎯 ${esc(L.goal)}</div>`;
    let nDrill = 0;
    L.blocks.forEach((b) => {
      if (b.t === 'text') html += `<div class="md">${md(b.md)}</div>`;
      else if (b.t === 'greek') html += `<div class="greek md">${md(b.md)}</div>`;
      else if (b.t === 'tones') {
        html += `<h3>The four tones</h3><div class="card">${toneSvg()}<div class="tone-keys">`
          + b.items.map((it) => { curItems[it.a] = it; return `<button class="snd-lite" data-a="${it.a}" data-hz="${esc(it.hz)}"><b class="${toneClass(it.tone)}">${esc(it.py)}</b><span>${esc(it.hz)} · ${esc(it.en)}</span></button>`; }).join('')
          + '</div><p class="note">Tone 1 high and flat · Tone 2 rising · Tone 3 low (dips, then rises) · Tone 4 falling sharply</p></div>';
      } else if (b.t === 'sounds') {
        if (b.drill) nDrill += b.items.length;
        html += `<h3>${esc(b.title)}</h3><div class="grid">` + b.items.map((it) => { curItems[it.a] = it; return sndCard(it); }).join('') + '</div>';
      }
    });
    const H = L.hanzi;
    html += `<h2>汉字 · ${esc(H.title)}</h2><div class="md">${md(H.md)}</div><div class="grid">`
      + H.items.map((it) => { if (it.a) curItems[it.a] = it; return `<div class="snd" data-a="${it.a || ''}" data-hz="${esc(it.hz)}"><div class="hz">${esc(it.hz)}</div>`
        + `<div class="py">${esc(it.py)}</div><div class="en">${esc(it.en)}</div>${it.note ? `<div class="en">${esc(it.note)}</div>` : ''}`
        + (it.a ? '<div class="acts"><button data-play aria-label="Play">▶</button></div>' : '') + '</div>'; }).join('') + '</div>';
    const done = store.get('cs_done', []).includes(L.id);
    html += `<div class="row-btns">${nDrill ? `<button class="btn" data-go="#/quiz/${L.id}">✍️ Practice (${Math.min(10, nDrill)} questions)</button>` : ''}`
      + `<button class="btn ghost" id="doneBtn">${done ? '✓ Done' : 'Mark as done'}</button></div>`;
    $('view').innerHTML = html;
    $('doneBtn').onclick = () => {
      const d = store.get('cs_done', []).filter((x) => x !== L.id);
      if (!done) d.push(L.id);
      store.set('cs_done', d); renderLesson(id);
    };
  }

  // ---------------------------------------------------------------- 练习：听音选拼音
  function shuffle(a) { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  function renderQuiz(id, only) {
    const L = C.lessons.find((x) => x.id === id); if (!L) return go('#/');
    setTop(`${L.id} · Practice`, true);
    const groups = L.blocks.filter((b) => b.t === 'sounds' && b.drill);
    let pool = [];
    groups.forEach((g) => g.items.forEach((it) => pool.push({ it, group: g })));
    if (only) pool = pool.filter((q) => only.includes(q.it.a));
    const qs = shuffle(pool).slice(0, 10);
    let k = 0, score = 0;
    const wrong = [];
    function show() {
      if (k >= qs.length) {
        $('view').innerHTML = `<div class="card" style="text-align:center"><h2>${score} / ${qs.length}</h2>`
          + `<p>${score === qs.length ? 'Perfect! 太好了！' : 'Keep going — listen again to the ones you missed.'}</p>`
          + `<div class="row-btns" style="justify-content:center">${wrong.length ? '<button class="btn" id="again">Practise the mistakes</button>' : ''}`
          + `<button class="btn ghost" id="more">New round</button><button class="btn ghost" data-go="#/lesson/${L.id}">Back to lesson</button></div></div>`;
        if (wrong.length) $('again').onclick = () => renderQuiz(id, wrong.map((q) => q.it.a));
        $('more').onclick = () => renderQuiz(id);
        return;
      }
      const q = qs[k];
      const opts = shuffle([q.it, ...shuffle(q.group.items.filter((x) => x.py !== q.it.py)).slice(0, 3)]);
      $('view').innerHTML = `<div class="quiz-top"><span>Question ${k + 1} / ${qs.length}</span><span>✓ ${score}</span></div>`
        + `<p style="text-align:center;margin:10px 0 0">Listen. Which one do you hear?</p>`
        + `<div class="quiz-play"><button id="qPlay" aria-label="Play">▶</button></div>`
        + `<div class="opts">${opts.map((o) => `<button data-py="${esc(o.py)}">${esc(o.py)}</button>`).join('')}</div><div class="quiz-fb" id="qFb"></div>`;
      const say = () => play(q.it.a, q.it.hz);
      $('qPlay').onclick = say; say();
      document.querySelectorAll('.opts button').forEach((b) => {
        b.onclick = () => {
          if (document.querySelector('.opts .ok')) return;
          const right = b.dataset.py === q.it.py;
          if (right) score++; else wrong.push(q);
          document.querySelectorAll('.opts button').forEach((x) => x.classList.toggle('ok', x.dataset.py === q.it.py));
          if (!right) b.classList.add('bad');
          $('qFb').innerHTML = `<b style="font-size:26px">${esc(q.it.hz)}</b> <span class="${toneClass(q.it.tone)}">${esc(q.it.py)}</span> · ${esc(q.it.en)}`
            + `<div class="row-btns" style="justify-content:center;margin:10px 0 0"><button class="btn" id="qNext">Next ›</button></div>`;
          $('qNext').onclick = () => { k++; show(); };
        };
      });
    }
    show();
  }

  // ---------------------------------------------------------------- 医院急用句
  let hosFilter = 'help';
  function renderHospital() {
    setTop('Hospital phrases · 医院', true);
    const H = C.hospital;
    curItems = {};
    const chips = H.groups.map((g) => [g.id, `${g.icon} ${g.title}`]).concat([['body', '🧍 Body'], ['signs', '🪧 Signs'], ['all', 'All']]);
    $('view').innerHTML = `<input class="search" id="hsearch" type="search" placeholder="Search in English or Chinese… (e.g. fever, pain)" autocomplete="off">`
      + `<div class="chips" id="hchips">${chips.map(([k, n]) => `<button data-k="${k}" class="${k === hosFilter ? 'on' : ''}">${esc(n)}</button>`).join('')}</div>`
      + `<div id="hlist"></div><p class="note">Tap ⛶ to show a phrase in big letters to the doctor or nurse. 🔊 plays it aloud.</p>`;
    const draw = () => {
      const q = $('hsearch').value.trim().toLowerCase();
      let rows = [];
      H.groups.forEach((g) => g.items.forEach((it) => rows.push({ it, g: g.id, doctor: g.doctor, head: `${g.icon} ${g.title} · ${g.zh}` })));
      H.body.forEach((it) => rows.push({ it, g: 'body', head: '🧍 Body · 身体', icon: it.icon }));
      H.signs.forEach((it) => rows.push({ it, g: 'signs', head: '🪧 Signs in the hospital · 指示牌' }));
      if (q) rows = rows.filter((r) => (r.it.hz + ' ' + r.it.py + ' ' + r.it.en).toLowerCase().includes(q));
      else if (hosFilter !== 'all') rows = rows.filter((r) => r.g === hosFilter);
      let html = '', head = null;
      rows.forEach((r) => {
        curItems[r.it.a] = r.it;
        if (r.head !== head) { if (head !== null) html += '</div>'; head = r.head; html += `<h3>${esc(head)}</h3><div class="card">`; }
        html += `<div class="phr"><div class="m"><div class="hz">${r.icon ? esc(r.icon) + ' ' : ''}${esc(r.it.hz)}${r.doctor ? '<span class="doctor-tag">doctor</span>' : ''}</div>`
          + `<div class="py">${esc(r.it.py)}</div><div class="en">${esc(r.it.en)}</div></div>`
          + `<div class="b"><button data-say="${r.it.a}" aria-label="Play">🔊</button><button data-showit="${r.it.a}" aria-label="Show big">⛶</button></div></div>`;
      });
      if (head !== null) html += '</div>';
      $('hlist').innerHTML = html || '<p class="note">Nothing found.</p>';
    };
    $('hsearch').oninput = draw;
    $('hchips').onclick = (e) => { const b = e.target.closest('[data-k]'); if (!b) return; hosFilter = b.dataset.k; $('hsearch').value = '';
      document.querySelectorAll('#hchips button').forEach((x) => x.classList.toggle('on', x === b)); draw(); };
    draw();
  }

  let showing = null;
  function showBig(it) {
    showing = it;
    $('showHz').textContent = it.hz; $('showPy').textContent = it.py; $('showEn').textContent = it.en;
    $('show').classList.remove('hidden');
  }
  $('showPlay').onclick = () => showing && play(showing.a, showing.hz);
  $('showClose').onclick = () => $('show').classList.add('hidden');

  // ---------------------------------------------------------------- 跟读：录音 + 音高曲线
  let recItem = null, recBlob = null, recUrl = null;
  const MODEL = { 1: [[0, 5], [1, 5]], 2: [[0, 3], [1, 5]], 3: [[0, 2], [0.45, 1], [1, 4]], 4: [[0, 5], [1, 1]] };
  function openRec(it) {
    recItem = it; recBlob = null;
    $('recHz').textContent = it.hz; $('recPy').textContent = it.py; $('recPy').className = 'rec-py ' + toneClass(it.tone);
    $('recMine').disabled = true; $('recMsg').textContent = 'Listen, then press ● and say it.';
    $('rec').classList.remove('hidden');
    drawPitch(null);
  }
  function drawPitch(track) {
    const cv = $('recCanvas'), g = cv.getContext('2d');
    const W = cv.width, H = cv.height, pad = 24;
    g.clearRect(0, 0, W, H);
    const css = getComputedStyle(document.documentElement);
    const y = (v) => H - pad - (v - 1) / 4 * (H - 2 * pad), x = (t) => pad + t * (W - 2 * pad);
    g.strokeStyle = 'rgba(128,128,128,.25)'; g.lineWidth = 1;
    for (let v = 1; v <= 5; v++) { g.beginPath(); g.moveTo(pad, y(v)); g.lineTo(W - pad, y(v)); g.stroke(); }
    const m = MODEL[recItem && recItem.tone];
    if (m) {
      g.strokeStyle = css.getPropertyValue('--muted') || '#888'; g.lineWidth = 6; g.setLineDash([12, 8]); g.lineCap = 'round';
      g.beginPath(); m.forEach(([t, v], i) => (i ? g.lineTo(x(t), y(v)) : g.moveTo(x(t), y(v)))); g.stroke(); g.setLineDash([]);
    }
    if (track && track.length > 2) {
      g.strokeStyle = css.getPropertyValue('--accent') || '#c8102e'; g.lineWidth = 5; g.lineJoin = 'round';
      g.beginPath(); track.forEach(([t, v], i) => (i ? g.lineTo(x(t), y(v)) : g.moveTo(x(t), y(v)))); g.stroke();
    }
  }
  // 自相关法估计音高（75–500 Hz），返回 [[时间 0–1, 音高 1–5]]
  function pitchTrack(buf) {
    const sr = buf.sampleRate, d = buf.getChannelData(0);
    const win = Math.round(sr * 0.04), hop = Math.round(sr * 0.01);
    const minLag = Math.floor(sr / 500), maxLag = Math.floor(sr / 75);
    let peak = 0; for (let i = 0; i < d.length; i++) peak = Math.max(peak, Math.abs(d[i]));
    const out = [];
    for (let s = 0; s + win + maxLag < d.length; s += hop) {
      let rms = 0; for (let i = 0; i < win; i++) rms += d[s + i] * d[s + i];
      rms = Math.sqrt(rms / win);
      if (rms < peak * 0.12) continue;
      let best = 0, bestLag = 0, e0 = 0;
      for (let i = 0; i < win; i++) e0 += d[s + i] * d[s + i];
      for (let lag = minLag; lag <= maxLag; lag++) {
        let c = 0, e1 = 0;
        for (let i = 0; i < win; i++) { c += d[s + i] * d[s + i + lag]; e1 += d[s + i + lag] * d[s + i + lag]; }
        const r = c / Math.sqrt(e0 * e1 + 1e-9);
        if (r > best) { best = r; bestLag = lag; }
      }
      if (best > 0.6) out.push([s / sr, 12 * Math.log2(sr / bestLag / 100)]);
    }
    if (out.length < 3) return null;
    // 去掉跳变（倍频错误），时间归一到 0–1，音高按本人音域映射到 1–5
    const st = out.map((p) => p[1]).sort((a, b) => a - b);
    const med = st[Math.floor(st.length / 2)];
    const clean = out.filter((p) => Math.abs(p[1] - med) < 9);
    const t0 = clean[0][0], t1 = clean[clean.length - 1][0] || t0 + 1e-3;
    return clean.map(([t, v]) => [(t - t0) / (t1 - t0 || 1), Math.max(1, Math.min(5, 3 + (v - med) / 3))]);
  }
  let mediaRec = null;
  $('recGo').onclick = async () => {
    if (mediaRec && mediaRec.state === 'recording') { mediaRec.stop(); return; }
    if (!navigator.mediaDevices || !window.MediaRecorder) { toast('Recording is not supported in this browser'); return; }
    let stream;
    try { stream = await navigator.mediaDevices.getUserMedia({ audio: true }); } catch (e) { toast('Please allow the microphone'); return; }
    const chunks = [];
    mediaRec = new MediaRecorder(stream);
    mediaRec.ondataavailable = (e) => chunks.push(e.data);
    mediaRec.onstop = async () => {
      stream.getTracks().forEach((t) => t.stop());
      $('recGo').textContent = '● Record';
      recBlob = new Blob(chunks, { type: mediaRec.mimeType || 'audio/mp4' });
      if (recUrl) URL.revokeObjectURL(recUrl);
      recUrl = URL.createObjectURL(recBlob);
      $('recMine').disabled = false;
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const buf = await ctx.decodeAudioData(await recBlob.arrayBuffer());
        const tr = pitchTrack(buf);
        drawPitch(tr);
        $('recMsg').textContent = tr ? 'Red = your voice. Compare its shape with the dashed model line.' : 'I could not hear a clear voice — try again a little louder.';
      } catch (e) { $('recMsg').textContent = 'Recorded. Tap "Mine" to listen.'; }
    };
    mediaRec.start();
    $('recGo').textContent = '■ Stop';
    $('recMsg').textContent = 'Recording… say it now, then press Stop.';
    setTimeout(() => { if (mediaRec && mediaRec.state === 'recording') mediaRec.stop(); }, 3000);
  };
  $('recPlay').onclick = () => recItem && play(recItem.a, recItem.hz);
  $('recMine').onclick = () => { if (recUrl) new Audio(recUrl).play(); };
  $('recClose').onclick = () => { if (mediaRec && mediaRec.state === 'recording') mediaRec.stop(); $('rec').classList.add('hidden'); };

  // ---------------------------------------------------------------- 点击
  document.addEventListener('click', (e) => {
    const g = e.target.closest('[data-go]'); if (g) { go(g.dataset.go); return; }
    const card = e.target.closest('.snd, .snd-lite');
    if (e.target.closest('[data-rec]') && card) { const it = curItems[card.dataset.a]; if (it) { play(it.a, it.hz); openRec(it); } return; }
    if (card) { const it = curItems[card.dataset.a]; play(card.dataset.a || null, it ? it.hz : card.dataset.hz, card); return; }
    const s = e.target.closest('[data-say]'); if (s) { const it = curItems[s.dataset.say]; if (it) play(it.a, it.hz); return; }
    const sh = e.target.closest('[data-showit]'); if (sh) { const it = curItems[sh.dataset.showit]; if (it) showBig(it); }
  });

  // ---------------------------------------------------------------- 离线
  if ('serviceWorker' in navigator && location.protocol === 'https:') {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }
  render();
})();
