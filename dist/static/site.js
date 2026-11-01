const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('is-open');
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
});
navigation.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});
const copyButton = document.querySelector('#copy-email');
let copyReset;
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText('jaswanthjanga506@gmail.com');
    copyButton.textContent = 'Email copied ✓';
    document.querySelector('#copy-status').textContent = 'Email address copied to clipboard.';
    clearTimeout(copyReset);
    copyReset = setTimeout(() => { copyButton.textContent = 'Copy email ⧉'; }, 3000);
  } catch {
    document.querySelector('#copy-status').textContent = 'Unable to copy automatically. Select the email address above to copy it.';
    copyButton.textContent = 'Please select the email above to copy';
  }
});
const navLinks = [...navigation.querySelectorAll('a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          if (link.getAttribute('href') === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
    }
  }, { rootMargin: '-15% 0px -30% 0px', threshold: 0 });
  navLinks.forEach(link => observer.observe(document.querySelector(link.getAttribute('href'))));
}
