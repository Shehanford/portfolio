// main.js - interactions: fade-in on scroll, modal, theme toggle, project modal content

document.addEventListener('DOMContentLoaded', function() {

  // Fade-in observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) e.target.classList.add('show');
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.fade').forEach(el => observer.observe(el));

  // Theme toggle (persist)
  const themeToggle = document.getElementById('theme-toggle');
  const stored = localStorage.getItem('site-theme');
  if (stored === 'dark') document.documentElement.classList.add('dark');

  themeToggle && themeToggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    localStorage.setItem('site-theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  });

  // Projects modal
  const projects = JSON.parse(document.getElementById('__projects').textContent || '[]');
  const modal = document.getElementById('project-modal');
  const modalContent = document.getElementById('modal-content');
  const modalClose = document.getElementById('modal-close');

  function openProject(id) {
    const p = projects.find(x => x.id === id);
    if (!p) return;
    modalContent.innerHTML = `
      <h3>${p.title}</h3>
      <p class="muted">${p.short}</p>
      <div style="margin-top:12px">${p.detail || ''}</div>
    `;
    modal.classList.add('show');
    modal.setAttribute('aria-hidden', 'false');
  }

  document.querySelectorAll('.js-open-project').forEach(btn => {
    btn.addEventListener('click', (ev) => {
      openProject(btn.dataset.id);
    });
  });

  modalClose && modalClose.addEventListener('click', () => {
    modal.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('show');
      modal.setAttribute('aria-hidden', 'true');
    }
  });

  // Smooth anchor scrolling
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', function(e){
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({behavior:'smooth', block:'start'});
      }
    });
  });

});
