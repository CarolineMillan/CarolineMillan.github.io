// Dark mode toggle
const toggle = document.getElementById('mode-toggle');

// Apply stored mode on load
if (localStorage.getItem('darkMode') === 'true') {
  document.body.classList.add('dark');
  toggle.textContent = '☀️';
}

toggle.addEventListener('click', () => {
  const isDark = document.body.classList.toggle('dark');
  localStorage.setItem('darkMode', isDark);
  toggle.textContent = isDark ? '☀️' : '🌙';
});