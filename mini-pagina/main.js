// Contacto desde config.js y aparición suave de los bloques al scrollear.
(() => {
  const c = window.CONTACTO || {};
  const wa = `https://wa.me/${c.whatsapp}?text=${encodeURIComponent(c.mensaje || '')}`;
  document.querySelectorAll('[data-wa]').forEach((a) => { a.href = wa; });
  document.querySelectorAll('[data-phone]').forEach((p) => { p.textContent = c.telefono || ''; });

  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
})();
