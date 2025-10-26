// Theme toggle (persist in localStorage)
const root = document.documentElement;
const btn = document.getElementById('theme-toggle');
const stored = localStorage.getItem('site-theme');
if(stored) root.setAttribute('data-theme', stored);
else {
  // default follow system pref (optional)
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  root.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
}

btn.addEventListener('click', () => {
  const cur = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', cur);
  localStorage.setItem('site-theme', cur);
});
