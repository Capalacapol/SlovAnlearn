/* SlovAnLearn display preferences — independent from student progress and Supabase. */
(function () {
  'use strict';
  const STORAGE_KEY = 'slovanlearn-display-mode';
  const root = document.documentElement;
  const toggle = document.getElementById('themeToggle');
  const meta = document.querySelector('meta[name="theme-color"]');

  function storedMode() {
    try { return localStorage.getItem(STORAGE_KEY) === 'dark' ? 'dark' : 'light'; }
    catch (_) { return root.getAttribute('data-atlas-theme') === 'dark' ? 'dark' : 'light'; }
  }

  function setMode(mode, persist) {
    const dark = mode === 'dark';
    if (dark) root.setAttribute('data-atlas-theme', 'dark');
    else root.removeAttribute('data-atlas-theme');
    if (meta) meta.setAttribute('content', dark ? '#101b2d' : '#f5f7fc');
    if (toggle) {
      const label = dark ? 'Light mode' : 'Dark mode';
      const explanation = dark ? 'Switch to light mode' : 'Switch to dark mode';
      toggle.setAttribute('aria-label', explanation);
      toggle.setAttribute('title', explanation);
      toggle.setAttribute('aria-pressed', String(dark));
      const icon = toggle.querySelector('.theme-toggle-icon');
      const text = toggle.querySelector('.theme-toggle-label');
      if (icon) icon.textContent = dark ? '☀' : '☾';
      if (text) text.textContent = label;
    }
    if (persist) {
      try { localStorage.setItem(STORAGE_KEY, dark ? 'dark' : 'light'); } catch (_) { /* Storage may be disabled. */ }
    }
  }

  setMode(storedMode(), false);
  if (toggle) {
    toggle.addEventListener('click', function () {
      setMode(root.getAttribute('data-atlas-theme') === 'dark' ? 'light' : 'dark', true);
    });
  }
  window.addEventListener('storage', function (event) {
    if (event.key === STORAGE_KEY || event.key === null) setMode(storedMode(), false);
  });
})();
