// 离线：页面和数据先缓存；录音第一次播放时缓存，以后不联网也能听。改了文件就把 VERSION 加 1。
const VERSION = 'cs-v1';
const SHELL = ['./', 'index.html', 'style.css', 'app.js', 'data/content.js', 'manifest.webmanifest',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== VERSION && k !== 'cs-audio').map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  if (url.pathname.includes('/audio/')) {
    // 录音：有缓存用缓存；没有就下载并存起来（没录的返回 404，App 改用手机朗读）
    e.respondWith(caches.open('cs-audio').then((c) => c.match(e.request).then((hit) => hit || fetch(e.request).then((r) => {
      if (r.ok) c.put(e.request, r.clone());
      return r;
    }))));
    return;
  }
  // 页面和数据：先用网络拿最新的，断网时用缓存
  e.respondWith(fetch(e.request).then((r) => {
    if (r.ok) caches.open(VERSION).then((c) => c.put(e.request, r.clone()));
    return r;
  }).catch(() => caches.match(e.request).then((hit) => hit || caches.match('index.html'))));
});
