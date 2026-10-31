const menu=document.querySelector('.menu-toggle');const nav=document.querySelector('.site-nav');if(menu&&nav){menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});}
const obs=window.IntersectionObserver?new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}})},{threshold:.08}):null;document.querySelectorAll('.reveal').forEach(el=>obs?obs.observe(el):el.classList.add('visible'));
const search=document.querySelector('#people-search');if(search){search.addEventListener('input',()=>{const q=search.value.toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');document.querySelectorAll('.portrait-card').forEach(el=>{const t=el.dataset.search.toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');el.hidden=!t.includes(q)});const count=document.querySelector('#people-count');if(count)count.textContent=String(document.querySelectorAll('.portrait-card:not([hidden])').length)})}
const eventSearch=document.querySelector('#event-search');if(eventSearch){eventSearch.addEventListener('input',()=>{const q=eventSearch.value.toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');const cards=[...document.querySelectorAll('.event-grid .event-card')];cards.forEach(el=>{const t=el.dataset.search.toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');el.hidden=!t.includes(q)});const empty=document.querySelector('.event-no-results');if(empty)empty.hidden=cards.some(el=>!el.hidden);});}
document.querySelectorAll('[data-carousel]').forEach(carousel=>{const track=carousel.querySelector('.carousel-track'),slides=[...carousel.querySelectorAll('.carousel-slide')],status=carousel.querySelector('.carousel-status');if(!track||slides.length<2){carousel.querySelector('.carousel-controls')?.remove();return;}let current=0;const move=delta=>{current=(current+delta+slides.length)%slides.length;slides[current].scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth',inline:'start',block:'nearest'});if(status)status.textContent=`${current+1} / ${slides.length}`;};carousel.querySelector('[data-prev]')?.addEventListener('click',()=>move(-1));carousel.querySelector('[data-next]')?.addEventListener('click',()=>move(1));});
const normalize=s=>s.toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
for(const [inputId,buttonAttr,cardSelector,emptySelector] of [['publication-search','data-publication-filter','.publication-list .publication','.publication-no-results'],['resource-search','data-resource-filter','.resource-results .tool-card','.catalog-empty']]){
  const input=document.getElementById(inputId);if(!input)continue;
  const buttons=[...document.querySelectorAll(`[${buttonAttr}]`)];const cards=[...document.querySelectorAll(cardSelector)];const empty=document.querySelector(emptySelector);let current='all';
  if(inputId==='publication-search'){
    const requested=new URLSearchParams(location.search).get('type');
    if(buttons.some(button=>button.getAttribute(buttonAttr)===requested))current=requested;
    buttons.forEach(button=>{const selected=button.getAttribute(buttonAttr)===current;button.classList.toggle('selected',selected);button.setAttribute('aria-pressed',String(selected));});
  }
  function filter(){const q=normalize(input.value.trim());cards.forEach(card=>card.hidden=!(current==='all'||card.dataset.type===current)||!normalize(card.dataset.search||'').includes(q));if(empty)empty.hidden=cards.some(card=>!card.hidden);}
  buttons.forEach(button=>button.addEventListener('click',()=>{current=button.getAttribute(buttonAttr);buttons.forEach(b=>{const selected=b===button;b.classList.toggle('selected',selected);b.setAttribute('aria-pressed',String(selected));});filter();}));
  input.addEventListener('input',filter);
  filter();
}
let copyToastTimer;
document.querySelectorAll('.email-copy').forEach(button=>button.addEventListener('click',async()=>{
  const email=button.dataset.copyEmail,lang=document.documentElement.lang,feedback=button.closest('.email-copy-wrap')?.querySelector('.copy-tooltip');let copied=false;
  try{if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(email);copied=true;}}catch{}
  if(!copied){const field=document.createElement('textarea');field.value=email;field.style.position='fixed';field.style.opacity='0';document.body.appendChild(field);field.select();try{copied=document.execCommand('copy');}catch{}field.remove();}
  if(feedback){
    feedback.textContent=copied?(lang==='es'?'Correo copiado':'Email copied'):(lang==='es'?`No se pudo copiar: ${email}`:`Could not copy: ${email}`);
    feedback.classList.add('show');clearTimeout(copyToastTimer);
    copyToastTimer=setTimeout(()=>feedback.classList.remove('show'),3500);
  }
}));
document.querySelectorAll('.network-map').forEach(map=>{
  const section=map.closest('.network-section');
  const feedback=section?.querySelector('.network-feedback strong');
  const scrollBox=section?.querySelector('.network-map-scroll');
  const tooltip=section?.querySelector('.network-tooltip');
  if(scrollBox&&matchMedia('(max-width:700px)').matches)scrollBox.scrollLeft=(scrollBox.scrollWidth-scrollBox.clientWidth)/2;
  const defaultText=feedback?.textContent||'';
  const related=[...map.querySelectorAll('[data-network-group]')];
  const clear=()=>{
    map.classList.remove('is-focused');
    related.forEach(el=>el.classList.remove('is-connected','is-dimmed'));
    if(feedback)feedback.textContent=defaultText;
    tooltip?.classList.remove('show');
  };
  map.querySelectorAll('a[data-network-group]').forEach(link=>{
    const focus=()=>{
      const groups=new Set(link.dataset.networkGroup.split(/\s+/));
      map.classList.add('is-focused');
      related.forEach(el=>{
        const connected=el.dataset.networkGroup.split(/\s+/).some(group=>groups.has(group));
        el.classList.toggle('is-connected',connected);
        el.classList.toggle('is-dimmed',!connected);
      });
      const detail=[link.dataset.networkTitle,link.dataset.networkMeta].filter(Boolean).join(' · ');
      if(feedback)feedback.textContent=detail;
      if(tooltip&&scrollBox){
        const node=link.getBoundingClientRect(),box=scrollBox.getBoundingClientRect();
        const x=node.left+node.width/2-box.left;
        const above=node.top-box.top-53;
        tooltip.textContent=detail;
        tooltip.style.left=`${Math.max(145,Math.min(x,box.width-145))}px`;
        tooltip.style.top=`${above<8?node.bottom-box.top+10:above}px`;
        tooltip.classList.add('show');
      }
    };
    link.addEventListener('pointerenter',focus);
    link.addEventListener('focus',focus);
    link.addEventListener('pointerleave',clear);
    link.addEventListener('blur',clear);
  });
});
// The pointer remains native on touch devices, reduced-motion preferences and form controls.
if (matchMedia('(hover:hover) and (pointer:fine) and (prefers-reduced-motion:no-preference)').matches) {
  const follower=document.createElement('div'); follower.className='cursor-follower'; follower.setAttribute('aria-hidden','true'); follower.innerHTML='<span></span>'; document.body.appendChild(follower); document.body.classList.add('custom-cursor');
  let x=-100,y=-100,frame=0;
  const paint=()=>{follower.style.transform=`translate3d(${x}px,${y}px,0) translate(-50%,-50%)`;frame=0};
  document.addEventListener('pointermove',e=>{
    if(e.pointerType!=='mouse')return;x=e.clientX;y=e.clientY;
    if(!frame)frame=requestAnimationFrame(paint);
    const form=e.target.closest('input,textarea,select,[contenteditable]');
    follower.classList.toggle('active',!form);
    const label=e.target.closest('[data-cursor-label]');
    follower.classList.toggle('label',!!label);
    follower.classList.toggle('hover',!label&&!!e.target.closest('a,button'));
    follower.classList.toggle('dark',!!e.target.closest('.hero,.dark-section,.page-hero,.site-footer'));
    follower.firstElementChild.textContent=label?.dataset.cursorLabel||'';
  },{passive:true});
  document.addEventListener('pointerleave',()=>follower.classList.remove('active'));
  window.addEventListener('blur',()=>follower.classList.remove('active'));
}
