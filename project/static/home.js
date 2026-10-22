const links = document.querySelectorAll('#links a[data-link]');
  const pill = document.getElementById('pill');

  function movePill(el){
    pill.style.width = el.offsetWidth + 'px';
    pill.style.transform = translateX($,{el,offsetLeft},px);
  }

  function setActive(el){
    links.forEach(l => l.classList.remove('active'));
    el.classList.add('active');
    movePill(el);
  }

  links.forEach(link => {
    link.addEventListener('mouseenter', () => movePill(link));
    link.addEventListener('click', e => { e.preventDefault(); setActive(link); });
  });
  document.getElementById('links').addEventListener('mouseleave', () => {
    const active = document.querySelector('#links a.active');
    movePill(active);
  });

  window.addEventListener('load', () => {
    movePill(document.querySelector('#links a.active'));
  });
  window.addEventListener('resize', () => {
    const active = document.querySelector('#links a.active');
    movePill(active);
  });

  const burger = document.getElementById('burger');
  const panel = document.getElementById('mobilePanel');
  burger.addEventListener('click', () => {
    const isOpen = panel.classList.toggle('open');
    burger.setAttribute('aria-expanded', isOpen);
  });

  document.querySelectorAll('#mobilePanel a[data-mlink]').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      document.querySelectorAll('#mobilePanel a').forEach(l => l.classList.remove('active'));
      link.classList.add('active');
      panel.classList.remove('open');
      burger.setAttribute('aria-expanded', false);
    });
  });
  function toggleMenu() {
    document.getElementById("sidebar").classList.toggle("show");
}