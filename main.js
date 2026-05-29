/* ═══════════════════════════════════════════════
   INCOBES – main.js (Consolidado)
═══════════════════════════════════════════════ */

const i18n = {
  // Navegación
  nav_home:          { es: 'Inicio',         en: 'Home' },
  nav_events:        { es: 'Eventos',        en: 'Events' },
  nav_publications:  { es: 'Publicaciones',  en: 'Publications' },
  nav_members:       { es: 'Miembros',       en: 'Members' },
  nav_resources:     { es: 'Recursos',       en: 'Resources' },
  nav_universities:  { es: 'Universidades',  en: 'Universities' },
  nav_theses:        { es: 'Tesis',          en: 'Theses' },
  nav_blog:          { es: 'Blog',           en: 'Blog' },

  // Footer
  footer_desc: { es: 'Red de investigadores comprometidos con la excelencia científica y la colaboración internacional.', en: 'Network of researchers committed to scientific excellence and international collaboration.' },
  footer_copy: { es: 'Todos los derechos reservados.', en: 'All rights reserved.' },

  // Hero y Misión (Index)
  hero_title:    { es: 'Red Internacional de Investigadores', en: 'International Researchers Network' },
 hero_subtitle: { 
    es: 'Una plataforma colaborativa global que conecta expertos en neurociencias, psicología, ciencia de datos e ingeniería para crear modelos integradores del comportamiento humano.', 
    en: 'A global collaborative platform connecting experts in neuroscience, psychology, data science, and engineering to create integrative models of human behavior.' 
  },
  hero_btn1: { es: 'Conoce la red', en: 'Explore the network' },
  hero_btn2: { es: 'Ver publicaciones', en: 'View publications' },
  events_label:  { es: 'Destacados', en: 'Featured' },
  events_title:  { es: 'Eventos Recientes', en: 'Recent Events' },
  events_viewall:{ es: 'Ver todos', en: 'View all' },
  events_readmore:{ es: 'Leer más', en: 'Read more' },

  // ── Quiénes Somos ──
  about_label: { es: 'Nuestra Red', en: 'Our Network' },
  about_intro_text: { 
    es: 'INCOBES nace para trascender las fronteras disciplinarias. Conectamos expertos en psicofisiología, neuropsicología, ciencia de datos e ingeniería biomédica para crear modelos integradores de la mente y el comportamiento humano a través de una plataforma colaborativa global.', 
    en: 'INCOBES was created to transcend disciplinary boundaries. We connect experts in psychophysiology, neuropsychology, data science, and biomedical engineering to create integrative models of the human mind and behavior through a global collaborative platform.' 
  },
  
  about_mission_title: { es: 'Misión', en: 'Mission' },
  about_mission_text: { 
    es: 'Fomentar el intercambio científico y proyectos conjuntos entre investigadores y estudiantes, impulsando la innovación metodológica y la difusión abierta del conocimiento.', 
    en: 'To foster scientific exchange and joint projects among researchers and students, driving methodological innovation and the open dissemination of knowledge.' 
  },

  about_vision_title: { es: 'Visión', en: 'Vision' },
  about_vision_text: { 
    es: 'Ser el referente global de colaboración interdisciplinaria donde la ciencia fluya sin fronteras institucionales e inspire a las futuras generaciones de científicos.', 
    en: 'To be the global reference for interdisciplinary collaboration where science flows without institutional borders and inspires future generations of scientists.' 
  },

  // Valores
  val_1_title: { es: 'Rigor', en: 'Rigor' },
  val_1_desc:  { es: 'Transparencia y altos estándares.', en: 'Transparency and high standards.' },
  val_2_title: { es: 'Apertura', en: 'Openness' },
  val_2_desc:  { es: 'Ciencia abierta y participativa.', en: 'Open and participatory science.' },
  val_3_title: { es: 'Sinergia', en: 'Synergy' },
  val_3_desc:  { es: 'Integración interdisciplinaria.', en: 'Interdisciplinary integration.' },
  
  about_mem_title: { es: 'Membresía', en: 'Membership' },
  about_mem_text: { 
    es: 'Nuestra red es ágil e interinstitucional. Invitamos a profesionales y estudiantes a participar en eventos, proponer proyectos y difundir mejores prácticas en investigación reproducible.', 
    en: 'Our network is agile and inter-institutional. We invite professionals and students to participate in events, propose projects, and disseminate best practices in reproducible research.' 
  },

  // Miembros
  members_page_title: { es: 'Nuestros Miembros', en: 'Our Members' },
  members_page_sub:   { es: 'Conoce a la red de investigadores', en: 'Meet the research network' },
  member1_role: { es: 'Profesor-Investigador, UABC | Miembro INCOBES', en: 'Professor-Researcher, UABC | INCOBES Member' },
  member1_bio: { es: 'Doctor en Ciencia del Comportamiento (Neurociencias) por la UDG. Es Responsable del Laboratorio de Psicofisiología Cognitiva y Afectiva en la UABC e investigador SNII Nivel I. Sus líneas de investigación se centran en los biomarcadores neurofisiológicos del uso de videojuegos en la infancia y la psicofisiología de procesos cognitivos y emocionales mediante EEG y eye-tracking.', en: 'PhD in Behavioral Science (Neuroscience) from UDG. He is the Head of the Cognitive and Affective Psychophysiology Lab at UABC and a SNII Level I researcher. His research focuses on neurophysiological biomarkers of video game use in childhood and the psychophysiology of cognitive and emotional processes using EEG and eye-tracking.' },
  member2_role: { es: 'Doctor en Psicología (UNAM) | Miembro INCOBES', en: 'PhD in Psychology (UNAM) | INCOBES Member' },
  member2_bio: { es: 'Doctor en Psicología (Neurociencias de la Conducta) por la UNAM. Ha realizado estancias en la Universidad de Oxford y la Universitat Pompeu Fabra. Su investigación se enfoca en la predicción lingüística, adquisición del lenguaje y bilingüismo, utilizando medidas experimentales (eye-tracking, EEG) y análisis computacionales.', en: 'PhD in Psychology (Behavioral Neuroscience) from UNAM. He has completed academic stays at the University of Oxford and Universitat Pompeu Fabra. His research focuses on linguistic prediction, language acquisition, and bilingualism, using experimental measures (eye-tracking, EEG) and computational analysis.' },
  member3_role: { es: 'Profesor-Investigador, UAEH | Miembro INCOBES', en: 'Professor-Researcher, UAEH | INCOBES Member' },
  member3_bio: { es: 'Doctor en Ciencia del Comportamiento (Neurociencias) por la UDG. Es miembro del SNII (Nivel Candidato) y Profesor-Investigador en la UAEH. Su investigación se centra en la interacción cognición-emoción, mecanismos de control inhibitorio y la validación de estímulos afectivos mediante electroencefalografía y eye-tracking.', en: 'PhD in Behavioral Science (Neuroscience) from UDG. He is a member of the SNII (Candidate Level) and a Professor-Researcher at UAEH. His research focuses on cognition-emotion interaction, inhibitory control mechanisms, and the validation of affective stimuli using EEG and eye-tracking.' },

  // Publicaciones
  pubs_page_title: { es: 'Publicaciones', en: 'Publications' },
  pubs_page_sub:   { es: 'Producción científica de los miembros de INCOBES', en: 'Scientific production of INCOBES members' },
  pubsTitle:       { es: 'Artículos de revista', en: 'Journal Articles' },

  // ── Universidades ──
  uni_page_title: { es: 'Universidades Participantes', en: 'Participating Universities' },
  uni_page_sub: { es: 'Instituciones vinculadas a nuestra red de investigación', en: 'Institutions linked to our research network' },
};

const NAV_LINKS = [
  { key: 'nav_home',         href: 'index.html',        page: 'index' },
  { key: 'nav_events',       href: 'events.html',       page: 'events' },
  { key: 'nav_publications', href: 'publications.html', page: 'publications' },
  { key: 'nav_members',      href: 'members.html',      page: 'members' },
  { key: 'nav_resources',    href: 'resources.html',    page: 'resources' },
  { key: 'nav_universities', href: 'universities.html', page: 'universities' },
  { key: 'nav_theses',       href: 'theses.html',       page: 'theses' },
  { key: 'nav_blog',         href: 'blog.html',         page: 'blog' }
];

const PAGE = (() => {
  const p = location.pathname.split('/').pop() || 'index.html';
  return p.replace('.html', '') || 'index';
})();

let lang = localStorage.getItem('incobes_lang') || 'es';

function t(key) { return i18n[key]?.[lang] ?? key; }

function setLang(l) {
  lang = l;
  localStorage.setItem('incobes_lang', lang);
  applyTranslations();
  updateLangBtn();
}

function toggleLang() { setLang(lang === 'es' ? 'en' : 'es'); }

function applyTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      el.placeholder = t(el.dataset.i18n);
    } else {
      el.textContent = t(el.dataset.i18n);
    }
  });
  document.documentElement.lang = lang;
}

function updateLangBtn() {
  const flagImg = document.getElementById('flag-icon');
  if (lang === 'es') {
    document.querySelectorAll('.lang-text').forEach(el => el.textContent = 'EN');
    if (flagImg) flagImg.src = 'img/usa.jpg';
  } else {
    document.querySelectorAll('.lang-text').forEach(el => el.textContent = 'ES');
    if (flagImg) flagImg.src = 'img/mx.jpg';
  }
}

async function loadComponent(id, file) {
  const el = document.getElementById(id);
  if (!el) return;
  const res = await fetch(file);
  el.innerHTML = await res.text();
}

function buildNav() {
  const navHTML = NAV_LINKS.map(({ key, href, page }) =>
    `<a href="${href}" class="${page === PAGE ? 'active' : ''}" data-i18n="${key}">${t(key)}</a>`
  ).join('');

  const nav = document.getElementById("nav-links");
  const mobile = document.getElementById("mobile-nav");
  if (nav) nav.innerHTML = navHTML;
  if (mobile) mobile.innerHTML = navHTML;

  const footer = document.getElementById("footer-links");
  if (footer) {
    footer.innerHTML = NAV_LINKS.slice(0,4).map(({ key, href }) =>
      `<li><a href="${href}" data-i18n="${key}">${t(key)}</a></li>`
    ).join('');
  }
}

function setYear() {
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
}

function initUI() {
  const langBtn = document.getElementById('lang-toggle');
  if (langBtn) langBtn.addEventListener('click', toggleLang);

  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobile-nav');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileNav.classList.toggle('open');
    });
  }
}

window.copyEmail = function(email) {
  navigator.clipboard.writeText(email).then(() => {
    const toast = document.getElementById('toast-notification');
    if (toast) {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3000);
    }
  }).catch(err => console.error('Error al copiar: ', err));
};

async function injectLayout() {
  await loadComponent("header-slot", "header.html");
  await loadComponent("footer-slot", "footer.html");
  buildNav();
  applyTranslations();
  updateLangBtn();
  setYear();
  initUI();
}

document.addEventListener("DOMContentLoaded", injectLayout);