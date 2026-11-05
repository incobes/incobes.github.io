from pathlib import Path
import json,html,re
ROOT=Path(__file__).parent; OUT=ROOT/'docs'; members=json.loads((ROOT/'members.json').read_text())
# Corrección editorial de una ficha con encabezado distinto en el documento original.
members[4]['bio']='Soy licenciado en Psicología por el ITESO, maestro y doctor en Ciencias del Comportamiento por la Universidad de Guadalajara. Mi investigación experimental integra principios del análisis de la conducta con la psicología ecológica: elección, orientación y memoria espacial, affordances y variabilidad conductual. Soy responsable del Laboratorio de Sistemas Conductuales del Centro de Investigación en Conducta y Cognición Comparada.'
institutions_short=['UAEH','UAEM','UABC','UAEM','UdeG','UAEM','UNAM','Tecnológico de Monterrey','UdeG','Simon Fraser University','UABC','COGNOS','CETYS Universidad','CETYS Universidad','UABC','CETYS Universidad','UABC','UNAM','UAEH']
for m,short in zip(members,institutions_short):m['short_aff']=short
eng=[
 'Researcher in cognitive and experimental psychology. His interests include problematic gaming, involuntary cognitive processes, psychometrics, EEG and eye tracking.',
 'Researcher with a background in physics and EEG hyperscanning. Her work connects quantitative methods with brain and behavioral sciences.',
 'Researcher in cognitive and behavioral sciences. His work explores experimental approaches to cognition and behavior.',
 'Researcher working across cognitive and behavioral sciences, with an interest in interdisciplinary collaboration.',
 'Professor at the University of Guadalajara. His experimental research connects behavior analysis and ecological psychology, including choice, spatial orientation and affordances.',
 'Researcher working in behavioral and cognitive sciences, with interests in experimental and interdisciplinary approaches.',
 'Researcher at UNAM working in cognitive and behavioral sciences.',
 'Researcher at Tecnológico de Monterrey studying emotion and decision making with experimental methods, neurophysiology and artificial intelligence.',
 'Postdoctoral researcher at the University of Guadalajara. His research examines neurotransmitters, psychoactive substances and addiction-related behavior.',
 'Postdoctoral researcher at Simon Fraser University. He uses multimodal neuroimaging to study brain aging and early Alzheimer’s disease.',
 'Researcher at UABC with interests in neuropsychological assessment, cognitive stimulation, EEG and eye tracking.',
 'Researcher in mental health and addictions with interests in neurophysiological biomarkers and noninvasive neuromodulation.',
 'Researcher at CETYS studying face perception, neuroimaging, psychometrics and open science.',
 'Researcher at CETYS studying aggression, early stress, neuropsychological intervention, sport and music in cognition.',
 'Researcher at UABC working on neurocognitive development, maternal mental health and cognition in vulnerable contexts.',
 'Researcher at CETYS studying early adversity, neuropsychological development, epilepsy, stress and sleep.',
 'Professor-researcher at UABC working on cognitive and emotional processes through EEG and eye tracking, including biomarkers of gaming in childhood.',
 'Academic technician at UNAM’s Faculty of Psychology. His research studies language prediction, acquisition and bilingualism with eye tracking, EEG and computational analyses.',
 'Professor-researcher at UAEH studying cognition and emotion, inhibitory control and the validation of affective stimuli using EEG and eye tracking.'
]
# Contactos profesionales publicados en las fichas entregadas para la página.
contacts=json.loads((ROOT/'public_contacts.json').read_text(encoding='utf-8'))
for m,c in zip(members,contacts):m.update(c)
navs={'es':[('about','La red'),('research','Investigación'),('people','Integrantes'),('events','Actividades'),('publications','Publicaciones'),('resources','Recursos'),('members','Miembros')], 'en':[('about','About'),('research','Research'),('people','People'),('events','Events'),('publications','Publications'),('resources','Resources'),('members','Members')]}
def h(x):return html.escape(str(x),quote=True)
def slugify(x):return re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-')
def tx(lang,es,en):return es if lang=='es' else en
def icon(kind):
 # SVG icons are local inline assets, inspired by the reference's icon blocks.
 paths={'nodes':'<circle cx="12" cy="5" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="19" cy="18" r="2"/><path d="M11 7 6 16M13 7l5 9M7 18h10"/>','brain':'<path d="M12 3c-2-2-6-.5-6 2.5C3 5 2 8 4 10c-2 2-1 5 1 6 0 3 3 5 6 3V5m1-2c2-2 6-.5 6 2.5 3-.5 4 2.5 2 4.5 2 2 1 5-1 6 0 3-3 5-6 3V5"/>','lab':'<path d="M8 3h8M10 3v7l-5 8a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-8V3M8 15h8"/>','spark':'<path d="m12 2 2.2 7.8L22 12l-7.8 2.2L12 22l-2.2-7.8L2 12l7.8-2.2L12 2Z"/>','calendar':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4M17 3v4M3 10h18"/>','book':'<path d="M12 6c-2-2-6-2-9-1v14c3-1 7-1 9 1 2-2 6-2 9-1V5c-3-1-7-1-9 1Zm0 0v14"/>','arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>','globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c-5 5-5 13 0 18m0-18c5 5 5 13 0 18"/>'}
 return f'<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths[kind]}</svg>'
def btn(url,text,variant=''):return f'<a class="btn {variant}" href="{url}">{text} <span aria-hidden="true">↗</span></a>'
def mail_icon():return '<svg aria-hidden="true" width="23" height="23" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
def heading(lang,kicker,title,description=''):return f'<div class="section-heading reveal"><div><div class="eyebrow">{kicker}</div><h2>{title}</h2></div>'+ (f'<p>{description}</p>' if description else '')+'</div>'
def network_svg():
 return '''<svg class="network-bg" aria-hidden="true" viewBox="0 0 1600 700" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#96d9ec" stroke-width="1" opacity=".35"><path d="M1010 75 1180 185 1390 90 1510 300 1340 405 1460 630M1010 75 965 315 1150 420 1340 405M965 315 820 140 620 260M1150 420 940 600 700 510"/><circle cx="1310" cy="320" r="240"/><circle cx="1310" cy="320" r="300" stroke-dasharray="3 14"/></g><g fill="#67ccdb" opacity=".9"><circle cx="1010" cy="75" r="5"/><circle cx="1180" cy="185" r="6"/><circle cx="1390" cy="90" r="5"/><circle cx="1510" cy="300" r="5"/><circle cx="1340" cy="405" r="7"/><circle cx="1150" cy="420" r="5"/><circle cx="965" cy="315" r="5"/></g></svg>'''
def page(lang,key,title,body,show_footer=True):
 other='en' if lang=='es' else 'es';link=lambda k:f'{lang}-{k}.html';key_for_switch=key
 if key.startswith('person-'):key_for_switch=key
 nav=''.join(f'<a href="{link(k)}" class="{("active " if k==key else "")+("member-link" if k=="members" else "")}">{label}</a>' for k,label in navs[lang])
 doc=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#173b5d"><meta name="description" content="INCOBES — Interdisciplinary Network for Cognitive and Behavioral Sciences"><title>{h(title)} | INCOBES</title><link rel="stylesheet" href="assets/style.css"><script defer src="assets/site.js"></script></head><body><div class="topbar"></div><header class="site-header"><div class="container head-inner"><a class="brand" href="{link('index')}" aria-label="INCOBES — {tx(lang,'Inicio','Home')}"><span class="brand-symbol"><img src="assets/incobes-logo.png" alt=""></span><span>INCOBES</span></a><button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="{tx(lang,'Abrir menú','Open menu')}">☰</button><nav id="site-nav" class="site-nav" aria-label="{tx(lang,'Navegación principal','Main navigation')}">{nav}<a class="language" href="{other}-{key_for_switch}.html" lang="{other}" hreflang="{other}" aria-label="{tx(lang,'Ver en inglés','View in Spanish')}">{other.upper()}</a></nav></div></header><main class="site-main">{body}</main><footer class="site-footer"><div class="container"><div class="footer-grid footer-feature"><div class="footer-identity"><a href="{link('index')}" aria-label="INCOBES — {tx(lang,'Inicio','Home')}"><img src="assets/incobes-logo-white.png" alt="INCOBES" class="footer-logo"></a><p>{tx(lang,'Red de Investigación Interdisciplinaria de Ciencias Cognitivas y de la Conducta.','Interdisciplinary Network for Cognitive and Behavioral Sciences.')}</p></div><div><div class="footer-icon">{icon('globe')}</div><h3>{tx(lang,'La red','The network')}</h3><p>{tx(lang,'Colaboración académica internacional en cognición, conducta y neurociencias.','International academic collaboration in cognition, behavior and neuroscience.')}</p><a href="{link('institutions')}">{tx(lang,'Explorar adscripciones','Explore affiliations')} ↗</a></div><div><div class="footer-icon">✉</div><h3>{tx(lang,'Contacto','Contact')}</h3><p><a href="mailto:incobes@gmail.com">incobes@gmail.com</a></p><div class="footer-links"><a href="{link('people')}">{tx(lang,'Integrantes','People')}</a><a href="{link('events')}">{tx(lang,'Actividades','Events')}</a><a href="{link('resources')}">{tx(lang,'Recursos','Resources')}</a></div></div></div><div class="footer-affiliations"><span>{tx(lang,'Adscripciones de las personas fundadoras','Founders’ affiliations')}</span><div class="affiliation-logos"><img src="assets/uaeh.png" alt="UAEH" loading="lazy"><img src="assets/unam.svg" alt="UNAM" loading="lazy"><img src="assets/uabc.png" alt="UABC" loading="lazy"></div></div><div class="foot-bottom">© 2026 INCOBES</div></div></footer></body></html>'''
 if not show_footer:
  start=doc.index('<footer class="site-footer">')
  end=doc.index('</footer>',start)+len('</footer>')
  doc=doc[:start]+doc[end:]
 (OUT/f'{lang}-{key}.html').write_text(doc,encoding='utf-8')
def top(lang,kicker,title,lead=''):return f'<section class="page-hero compact on-dark"><div class="container"><div class="eyebrow">{kicker}</div><h1>{title}</h1>'+ (f'<p class="lead">{lead}</p>' if lead else '') + '</div></section>'
def person_card(lang,i,m):
 pic=f'<img src="{m["img"]}" loading="lazy" alt="{h(m["name"])}">' if m['img'] else '<div class="placeholder" aria-label="Portrait pending">✣</div>'
 status=tx(lang,'Estudiante','Student') if m['status']=='student' else tx(lang,'Investigador/a','Researcher')
 return f'<article class="portrait-card reveal" data-search="{h(m["name"]+" "+m["aff"]+" "+status)}"><a href="{lang}-person-{i}.html" aria-label="{h(m["name"])}"><div class="image-wrap" data-cursor-label="{tx(lang,'Ver perfil','View profile')}">{pic}<span class="round-link" aria-hidden="true">↗</span></div><div class="card-body"><span class="person-status">{status}</span><h3>{h(m["name"])}</h3><p>{h(m["short_aff"])}</p></div></a></article>'
projects=[('Biomarcadores y videojuegos','Gaming and biomarkers','Biomarcadores neurofisiológicos, cognitivos y conductuales del uso problemático de videojuegos en niños de edad escolar.','Neurophysiological, cognitive and behavioral biomarkers of problematic gaming in school-age children.'),('Expresiones faciales infantiles','Child facial expressions','Validación mexicana del conjunto Child Affective Facial Expressions.','Mexican validation of the Child Affective Facial Expressions set.'),('Normas psicolingüísticas','Psycholinguistic norms','Desarrollo de normas psicolingüísticas del español de México.','Development of psycholinguistic norms for Mexican Spanish.'),('Forward Flow Project','Forward Flow Project','','')]
def project_cards(lang,limit=4):
 return '<div class="project-grid">'+''.join(f'<article class="project-card reveal"><div class="eyebrow">{tx(lang,"Proyecto de la red","Network project")}</div><span class="project-number">0{i+1}</span><h3>{h(p[0 if lang=="es" else 1])}</h3>'+(f'<p>{h(p[2 if lang=="es" else 3])}</p>' if p[2 if lang=="es" else 3] else '')+'</article>' for i,p in enumerate(projects[:limit]))+'</div>'

# The graph shows the affiliation selected for each member in this directory.
INSTITUTIONS=[('UNAM','Universidad Nacional Autónoma de México'),('UABC','Universidad Autónoma de Baja California'),('UAEH','Universidad Autónoma del Estado de Hidalgo'),('UAEM','Universidad Autónoma del Estado de Morelos'),('UdeG','Universidad de Guadalajara'),('CETYS','CETYS Universidad'),('Tec de Monterrey','Tecnológico de Monterrey'),('Simon Fraser University','Simon Fraser University'),('COGNOS','COGNOS · Terapia Cognitivo Conductual')]
AFFILIATION_LOOKUP={'Tec de Monterrey':'Tecnológico de Monterrey','Simon Fraser University':'Simon Fraser University','CETYS':'CETYS Universidad'}
INSTITUTION_LOGOS={'UNAM':'unam.svg','UABC':'uabc-seal.png','UAEH':'uaeh.svg','UAEM':'uaem.png','UdeG':'udg.svg','CETYS':'cetys.png','Tec de Monterrey':'itesm.svg','Simon Fraser University':'sfu.png','COGNOS':'cognos.jpg'}
NETWORK_POSITIONS=[
 ('UAEH',245,155,[(130,100),(365,100)]),
 ('UNAM',700,135,[(570,70),(830,70)]),
 ('UABC',1140,160,[(1015,65),(1270,65),(1020,275),(1270,275)]),
 ('UAEM',1180,445,[(1060,560),(1260,555),(1310,380)]),
 ('UdeG',1055,695,[(935,790),(1190,790)]),
 ('CETYS',720,695,[(580,790),(840,790),(720,565)]),
 ('Tec de Monterrey',360,700,[(225,735)]),
 ('Simon Fraser University',165,435,[(80,535)]),
 ('COGNOS',475,430,[(480,545)]),
]
# SVG image frames keep faces visible in wide, full-body source portraits.
NETWORK_PHOTO_FRAMES={4:(-50,-36,100,94),7:(-51,-27,110,88),17:(-86,-62,180,135)}
def person_initials(name):
 words=re.sub(r'^(Dr\.?|Dra\.?)\s+','',name).split()
 return ''.join(part[0].upper() for part in (words[0],words[-1])) if words else '•'
def network_graph(lang):
 T=lambda es,en:tx(lang,es,en)
 cx,cy=700,425
 edges=[];institutions=[];people=[]
 for n,(code,x,y,spots) in enumerate(NETWORK_POSITIONS):
  aff=AFFILIATION_LOOKUP.get(code,code)
  cohort=[(i,m) for i,m in enumerate(members) if m['short_aff']==aff]
  group=slugify(code)
  mx,my=(cx+x)/2,(cy+y)/2
  curve=22 if n%2 else -22
  edges.append(f'<path class="map-edge map-spoke" data-network-group="{group}" d="M{cx} {cy} Q{mx+curve} {my-curve} {x} {y}"/>')
  for j,(i,m) in enumerate(cohort):
   px,py=spots[j] if j<len(spots) else (x+80+(j-len(spots))*35,y+110)
   edges.append(f'<path class="map-edge map-membership" data-network-group="{group}" d="M{x} {y} L{px} {py}"/>')
   name=h(m['name'])
   if m.get('img'):
    fx,fy,fw,fh=NETWORK_PHOTO_FRAMES.get(i,(-26,-26,52,52))
    portrait=(f'<clipPath id="network-photo-{i}"><circle r="26"/></clipPath>'
              f'<image href="{h(m["img"])}" x="{fx}" y="{fy}" width="{fw}" height="{fh}" preserveAspectRatio="xMidYMid slice" clip-path="url(#network-photo-{i})" aria-hidden="true"/>')
   else:
    portrait=f'<text class="map-person-initials" text-anchor="middle" dominant-baseline="central">{h(person_initials(m["name"]))}</text>'
   people.append(f'<a class="map-person" href="{lang}-person-{i}.html" data-network-group="{group}" data-network-title="{name}" data-network-meta="{h(aff)}" data-cursor-label="{T("Ver perfil","View profile")}" aria-label="{name} · {h(aff)}"><title>{name}</title><g transform="translate({px} {py})"><circle class="map-person-halo" r="34"/><circle class="map-person-disc" r="27"/>{portrait}<circle class="map-person-ring" r="27"/></g></a>')
  logo=INSTITUTION_LOGOS.get(code)
  mark=f'<image href="assets/{logo}" x="-58" y="-35" width="116" height="70" preserveAspectRatio="xMidYMid meet"/>' if logo else f'<text class="map-initials" text-anchor="middle" dominant-baseline="central">{h(code[:2].upper())}</text>'
  count=T('integrante' if len(cohort)==1 else 'integrantes','member' if len(cohort)==1 else 'members')
  label='Simon Fraser' if code=='Simon Fraser University' else code
  institutions.append(f'<a class="map-institution" href="#{slugify(code)}" data-network-group="{group}" data-network-title="{h(code)}" data-network-meta="{len(cohort)} {count}" data-cursor-label="{T("Ver integrantes","View members")}" aria-label="{h(code)}, {len(cohort)} {count}"><title>{h(aff)}</title><g transform="translate({x} {y})"><rect class="map-institution-glow" x="-73" y="-51" width="146" height="102" rx="24"/><rect class="map-institution-disc" x="-66" y="-44" width="132" height="88" rx="18"/>{mark}<text class="map-institution-label" y="68" text-anchor="middle">{h(label)}</text></g></a>')
 svg=f'''<svg class="network-map" viewBox="0 0 1400 850" xmlns="http://www.w3.org/2000/svg" role="group" aria-label="{T('Grafo de instituciones e integrantes','Graph of institutions and members')}"><desc>{T('Selecciona un nodo para abrir su ficha. Las líneas muestran la adscripción elegida para cada integrante de este directorio.','Select a node to open its record. Lines show the affiliation selected for each member in this directory.')}</desc><defs><pattern id="map-dots" width="35" height="35" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#9fd6e4" opacity=".18"/></pattern></defs><rect width="1400" height="850" fill="url(#map-dots)"/><g class="map-edges" aria-hidden="true">{''.join(edges)}</g><g class="map-core" transform="translate({cx} {cy})" aria-hidden="true"><circle class="map-core-glow" r="77"/><circle class="map-core-disc" r="62"/><image href="assets/incobes-logo-white.png" x="-46" y="-46" width="92" height="92"/></g>{''.join(institutions)}{''.join(people)}</svg>'''
 return f'''<section class="network-section" id="conexiones"><div class="container"><div class="network-heading"><div class="eyebrow">01 / {T('CONEXIONES','CONNECTIONS')}</div><h2>{T('Instituciones y personas conectadas.','Connected institutions and people.')}</h2><p>{T('Explora las adscripciones de los integrantes y abre sus perfiles desde el grafo.','Explore members’ affiliations and open their profiles from the graph.')}</p></div><p class="network-mobile-hint">{T('Desliza para explorar el grafo. El directorio completo aparece después.','Swipe to explore the graph. The full directory follows.')}</p><div class="network-map-scroll" role="region" tabindex="0" aria-label="{T('Grafo desplazable de instituciones e integrantes','Scrollable graph of institutions and members')}">{svg}<div class="network-tooltip" aria-hidden="true"></div></div><div class="network-utility"><div class="network-feedback"><span>{T('EXPLORA LA RED','EXPLORE THE NETWORK')}</span><strong>{T('Selecciona un nodo para ver sus vínculos.','Select a node to see its connections.')}</strong></div><div class="map-legend"><span><i class="legend-affiliation"></i>{T('Adscripción','Affiliation')}</span></div></div></div></section>'''

def network_jump(lang,label,extra_class):
 return f'<a class="network-jump {extra_class}" href="{lang}-institutions.html#conexiones"><span class="network-jump-icon" aria-hidden="true">{icon("nodes")}</span><span class="network-jump-label">{h(label)}</span><span class="network-jump-arrow" aria-hidden="true">↗</span></a>'

# The circular artwork on Inicio is the existing decorative network_svg() and
# emblem-art. It represents the idea of connection, not verified relationships.
ABOUT = {
 'es': {
  'title':'Una comunidad que surge de la colaboración.',
  'lead':'INCOBES nace de la experiencia de investigadores que encontraron en el intercambio de conocimientos y perspectivas una manera de enriquecer sus propias líneas de investigación y construir nuevas oportunidades de trabajo conjunto.',
  'origin_title':'Nuestro origen',
  'origin':[
   'INCOBES surgió de la colaboración entre tres investigadores que coincidieron en el Instituto de Neurociencias de la Universidad de Guadalajara y que, al continuar sus trayectorias en distintas instituciones, mantuvieron sus vínculos académicos.',
   'En los últimos tres años, estas colaboraciones dieron lugar a publicaciones científicas, participación en comités de tesis, estancias académicas e intercambios mediante conferencias. La incorporación de colegas de otras instituciones y disciplinas amplió las posibilidades de trabajo conjunto.',
   'Esta experiencia nos llevó a reconocer el valor de conectar nuestras redes individuales de colaboración. Así comenzó a tomar forma INCOBES: una comunidad donde cada investigador puede mantener sus propios intereses y, al mismo tiempo, contribuir con sus conocimientos y recursos a los proyectos de otros.'
  ],
  'philosophy_title':'Nuestra filosofía',
  'philosophy':[
   'Creemos que la investigación se fortalece cuando existe apertura para compartir conocimientos, cuestionar ideas y aprender de perspectivas diferentes.',
   'INCOBES busca construir una comunidad científica horizontal, flexible y basada en la confianza, donde el diálogo crítico y constructivo, la colaboración responsable y las relaciones personales sean tan importantes como los resultados académicos.',
   'Promovemos la diversidad disciplinaria, la integración de métodos, la ciencia abierta y el intercambio responsable de conocimientos, datos y herramientas. La participación es voluntaria y las coordinaciones pueden rotar entre integrantes. Nuestra organización facilita colaboraciones que surgen de intereses compartidos, respetando la autonomía de cada persona.'
  ],
  'outlook_title':'Lo que buscamos construir',
  'outlook_lead':'Queremos que los intereses compartidos se traduzcan en oportunidades concretas de investigación, formación e intercambio científico.',
  'goals':[
   'Proyectos y publicaciones científicas en colaboración.',
   'Intercambio de métodos, conocimientos y recursos.',
   'Formación estudiantil mediante tesis y estancias.',
   'Encuentros, seminarios y discusión académica.',
   'Divulgación, ciencia abierta y reproducibilidad.',
   'Vínculos entre instituciones, disciplinas y países.'
  ],
  'outlook_note':'Hoy, la mayoría de los integrantes pertenece a instituciones mexicanas y existe una participación internacional inicial. Aspiramos a ampliar esos vínculos sin perder el espíritu cercano, abierto y colaborativo que dio origen a la iniciativa.',
  'founder_label':'Iniciativa impulsada por:',
  'founder_names':'Armando Q. Angulo-Chavira, Luis Llamas-Alonso y Vladimir Huerta-Chávez.'
 },
 'en': {
  'title':'A community born from collaboration.',
  'lead':'INCOBES grew from the experience of researchers who found that sharing knowledge and perspectives could enrich their own research and create new opportunities to work together.',
  'origin_title':'Our origins',
  'origin':[
   'INCOBES began with three researchers who met at the Institute of Neuroscience of the University of Guadalajara. As their careers took them to different institutions, they continued to collaborate.',
   'Over the past three years, these collaborations have led to scientific publications, thesis committee work, academic visits and exchanges through conferences. Colleagues from other institutions and disciplines joined in, expanding the possibilities for working together.',
   'This experience showed us the value of connecting our individual collaboration networks. INCOBES began to take shape as a community where researchers can pursue their own interests while contributing their knowledge and resources to the projects of others.'
  ],
  'philosophy_title':'Our philosophy',
  'philosophy':[
   'We believe research grows stronger when people are open to sharing knowledge, questioning ideas and learning from different perspectives.',
   'INCOBES aims to be a horizontal, flexible scientific community built on trust, where constructive scientific dialogue, responsible collaboration and personal relationships matter as much as academic results.',
   'We encourage disciplinary diversity, the integration of methods, open science and responsible sharing of knowledge, data and tools. Participation is voluntary and coordination roles may rotate among members. Our organization makes room for collaboration based on shared interests while respecting each person’s autonomy.'
  ],
  'outlook_title':'What we hope to build',
  'outlook_lead':'We want shared interests to become concrete opportunities for research, education and scientific exchange.',
  'goals':[
   'Collaborative research projects and publications.',
   'Exchange of methods, knowledge and resources.',
   'Student training through theses and academic visits.',
   'Meetings, seminars and scientific discussion.',
   'Outreach, open science and reproducibility.',
   'Connections across institutions, disciplines and countries.'
  ],
  'outlook_note':'Most members are currently based at Mexican institutions, with early international participation. We hope to expand those connections while preserving the close, open and collaborative spirit that started the initiative.',
  'founder_label':'Initiated by:',
  'founder_names':'Armando Q. Angulo-Chavira, Luis Llamas-Alonso and Vladimir Huerta-Chávez.'
 }
}
def paragraphs(items):
 return ''.join(f'<p>{h(item)}</p>' for item in items)

for lang in ('es','en'):
 T=lambda a,b:tx(lang,a,b)
 about_url=f'{lang}-about.html'
 cta=btn(about_url,T('Conoce INCOBES','Discover INCOBES'),'light')
 terms=['COGNICIÓN','CONDUCTA','NEUROCIENCIAS','CIENCIA ABIERTA','COLABORACIÓN'] if lang=='es' else ['COGNITION','BEHAVIOR','NEUROSCIENCE','OPEN SCIENCE','COLLABORATION']
 ticker_items=''.join(f'<span>{h(term)} <b aria-hidden="true">✳</b></span>' for term in terms)
 ticker=f'<div class="home-ticker" aria-hidden="true"><div class="home-ticker-track">{ticker_items*2}</div></div>'
 hero=f'''<section class="hero home-hero on-dark">{network_svg()}<div class="container"><div class="hero-content"><div class="eyebrow">{T('RED ACADÉMICA INTERDISCIPLINARIA','INTERDISCIPLINARY ACADEMIC NETWORK')}</div><h1>{T('Distintas perspectivas para comprender un mundo complejo.','Different perspectives to understand a complex world.')}</h1><p class="lead">{T('INCOBES es una red académica internacional que busca conectar investigadores de distintas disciplinas y regiones del mundo para intercambiar conocimientos, integrar perspectivas y promover nuevas formas de colaboración científica.','INCOBES is an international academic network that seeks to connect researchers from different disciplines and regions of the world to exchange knowledge, integrate perspectives and encourage new forms of scientific collaboration.')}</p><div class="btn-row">{cta}</div></div><div class="hero-art emblem-art" aria-hidden="true"><div class="orbit"></div><div class="emblem-halo"></div><img class="emblem" src="assets/incobes-logo-white.png" alt=""><span class="spark-dot d1"></span><span class="spark-dot d2"></span><span class="spark-dot d3"></span></div></div></section>'''
 hero=hero.removesuffix('</section>')+ticker+'</section>'
 page(lang,'index',T('Inicio','Home'),hero,show_footer=False)
 c=ABOUT[lang]
 about=top(lang,T('INCOBES / LA RED','INCOBES / ABOUT'),h(c['title']),h(c['lead']))
 about+=f'''<section class="about-editorial"><div class="container about-columns"><article class="about-column reveal"><span class="eyebrow">01 / {T('ORIGEN','ORIGINS')}</span><h2>{h(c['origin_title'])}</h2>{paragraphs(c['origin'])}</article><article class="about-column reveal"><span class="eyebrow">02 / {T('FILOSOFÍA','PHILOSOPHY')}</span><h2>{h(c['philosophy_title'])}</h2>{paragraphs(c['philosophy'])}</article></div></section>'''
 goals=''.join(f'<li><span aria-hidden="true">{i:02d}</span><span>{h(goal)}</span></li>' for i,goal in enumerate(c['goals'],1))
 network_link=network_jump(lang,T('Ver grafo de instituciones e integrantes','View the institutions and members graph'),'about-network-link')
 about+=f'''<section class="about-outlook"><div class="container"><div class="about-outlook-heading reveal"><div><span class="eyebrow">03 / {T('OBJETIVOS','AIMS')}</span><h2>{h(c['outlook_title'])}</h2></div><p>{h(c['outlook_lead'])}</p></div><ul class="about-goals reveal">{goals}</ul><p class="about-outlook-note">{h(c['outlook_note'])}</p>{network_link}<p class="about-founder-credit"><strong>{h(c['founder_label'])}</strong> {h(c['founder_names'])}</p></div></section>'''
 page(lang,'about',T('La red','About'),about)
 research=top(lang,T('INCOBES / INVESTIGACIÓN','INCOBES / RESEARCH'),T('Investigación','Research'))+f'<section class="section"><div class="container">{heading(lang,T("01 / PROYECTOS","01 / PROJECTS"),T("Proyectos de la red.","Network projects."))}{project_cards(lang)}</div></section>'
 page(lang,'research',T('Investigación','Research'),research)
 for directory_key,status in [('people','researcher'),('students','student')]:
  cohort=[(i,m) for i,m in enumerate(members) if m['status']==status]
  directory_title=T('Investigadores','Researchers') if status=='researcher' else T('Estudiantes','Students')
  tabs=f'<nav class="section-tabs community-tabs" aria-label="{T("Tipos de integrantes","Member categories")}"><a href="{lang}-people.html" class="{"selected" if status=="researcher" else ""}">{T("Investigadores","Researchers")}</a><a href="{lang}-students.html" class="{"selected" if status=="student" else ""}">{T("Estudiantes","Students")}</a></nav>'
  cards=''.join(person_card(lang,i,m) for i,m in cohort)
  empty=f'<div class="catalog-empty directory-empty"><div class="icon">{icon("nodes")}</div><h3>{T("Primeros perfiles en camino","First profiles on the way")}</h3><p>{T("Los estudiantes aparecerán aquí cuando se integren a la red.","Student members will appear here as they join the network.")}</p></div>' if not cohort else ''
  directory_link=network_jump(lang,T('Ver grafo de integrantes e instituciones','View the people and institutions graph'),'directory-network-link')
  directory=top(lang,T('INCOBES / INTEGRANTES','INCOBES / PEOPLE'),T('Integrantes','People'))+f'<section class="section"><div class="container">{tabs}{directory_link}<div class="search-row"><div><div class="eyebrow">{T("01 / DIRECTORIO","01 / DIRECTORY")}</div><h2 class="directory-title">{directory_title}</h2><p class="count-label"><span id="people-count">{len(cohort)}</span> {T("perfiles","profiles")}</p></div><label><span class="sr-only">{T("Buscar integrantes","Search members")}</span><input id="people-search" type="search" placeholder="{T("Buscar por nombre o institución","Search name or institution")}" aria-label="{T("Buscar integrantes","Search members")}"></label></div><div class="people-grid">{cards}</div>{empty}</div></section>'
  page(lang,directory_key,T('Integrantes','People'),directory)
 for i,m in enumerate(members):
  bio=m['bio'] if lang=='es' else eng[i]
  photo=f'<img src="{m["img"]}" alt="{h(m["name"])}">' if m['img'] else '<div class="placeholder">✣</div>'
  link_defs=[('orcid','ORCID','orcid.png'),('scholar','Google Scholar','scholar.png'),('researchgate','ResearchGate','researchgate.png')]
  links=''.join(f'<a class="academic-link" href="{h(m[key])}" target="_blank" rel="noopener noreferrer" aria-label="{label}" title="{label}"><img src="assets/{img}" alt=""><span>{label}</span></a>' for key,label,img in link_defs if m.get(key))
  if m.get('github'):
   links+=f'<a class="academic-link" href="{h(m["github"])}" target="_blank" rel="noopener noreferrer" aria-label="GitHub" title="GitHub"><span class="academic-monogram" aria-hidden="true">GH</span><span>GitHub</span></a>'
  # Professional email is supplied for the webpage. Phone numbers belong only in the future private directory.
  mail=f'<span class="email-copy-wrap"><button type="button" class="academic-link email-copy" data-copy-email="{h(m["email"])}" aria-label="{T("Copiar correo de","Copy email for")} {h(m["name"])}">{mail_icon()}</button><span class="copy-tooltip" role="status" aria-live="polite" aria-atomic="true"></span></span>' if m['email'] else ''
  back_page='students' if m['status']=='student' else 'people'
  status_label=T('ESTUDIANTE','STUDENT') if m['status']=='student' else T('INVESTIGADOR/A','RESEARCHER')
  aff=T('Unidad de neurociencias nbt, COGNOS','nbt Neuroscience Unit, COGNOS') if m['name']=='Edgar Omar Herrera Hernández' else m['aff']
  profile=top(lang,T('INCOBES / INTEGRANTES','INCOBES / PEOPLE'),h(m['name']),h(aff))+f'<section class="section"><div class="container profile"><div class="profile-image reveal">{photo}</div><div class="reveal"><a class="back-link" href="{lang}-{back_page}.html">← {T("Todos los integrantes","All members")}</a><div class="eyebrow">{T("PERFIL","PROFILE")} · {status_label}</div><h2>{T("Semblanza","Biography")}</h2><p class="bio">{h(bio) if bio else T("Semblanza en preparación.","Biography in preparation.")}</p><div class="academic-links">{links}{mail}</div></div></div></section>'
  page(lang,f'person-{i}',m['name'],profile)
 events_data=json.loads((ROOT/'events.json').read_text(encoding='utf-8'))
 upcoming=[e for e in events_data if e.get('status')=='upcoming']
 def event_link(url,label):
  return f'<a href="{h(url)}" target="_blank" rel="noopener noreferrer">{label} ↗</a>' if url else ''
 def event_card(e,carousel=False):
  title=e.get('title_es' if lang=='es' else 'title_en') or e.get('title_es') or ''
  poster=e.get('poster','')
  art=f'<img src="{h(poster)}" alt="{h(title)}" loading="lazy">' if poster else f'<div class="event-poster-fallback">{icon("calendar")}<span>INCOBES</span></div>'
  details=''.join(event_link(e.get(key,''),T(es,en)) for key,es,en in [('program','Programa','Program'),('stream','Transmisión','Stream'),('materials','Materiales','Materials')])
  date=h(e.get('date_label_es' if lang=='es' else 'date_label_en') or e.get('date',''))
  return f'<article class="event-card reveal" data-search="{h(title+" "+e.get("type_es"," ")+" "+date)}"><div class="event-art">{art}</div><div class="event-info"><span class="eyebrow">{date}</span><h3>{h(title)}</h3><p>{h(e.get("summary_es" if lang=="es" else "summary_en", ""))}</p><div class="event-links">{details}</div></div></article>'
 slides=''.join(f'<div class="carousel-slide" id="event-slide-{i}">{event_card(e,True)}</div>' for i,e in enumerate(upcoming))
 carousel=f'<div class="event-carousel" data-carousel aria-label="{T("Próximos eventos","Upcoming events")}"><div class="carousel-controls"><button type="button" data-prev aria-label="{T("Evento anterior","Previous event")}">←</button><span class="carousel-status" aria-live="polite">1 / {len(upcoming)}</span><button type="button" data-next aria-label="{T("Evento siguiente","Next event")}">→</button></div><div class="carousel-track">{slides}</div></div>' if upcoming else f'<div class="event-empty"><div class="event-placeholder-art">{network_svg()}<img src="assets/incobes-logo-white.png" alt=""></div><div><div class="eyebrow">INCOBES / {T("PRÓXIMAMENTE","COMING SOON")}</div><h3>{T("Próximas actividades","Upcoming events")}</h3><p>{T("Publicaremos carteles y fechas en cuanto estén confirmados.","Posters and dates will appear here once confirmed.")}</p></div></div>'
 gallery=''.join(event_card(e) for e in events_data)
 events=top(lang,T('INCOBES / ACTIVIDADES','INCOBES / EVENTS'),T('Actividades','Events'))+f'<section class="section"><div class="container">{heading(lang,T("01 / PRÓXIMAMENTE","01 / NEXT"),T("En agenda","On the calendar"))}{carousel}</div></section><section class="section event-archive"><div class="container">{heading(lang,T("02 / ARCHIVO","02 / ARCHIVE"),T("Todas las actividades","All events"),T("Encuentra carteles, programas, transmisiones y materiales cuando estén disponibles.","Find posters, programs, streams and materials when available."))}<label class="event-search-label"><span class="sr-only">{T("Buscar actividades","Search events")}</span><input id="event-search" type="search" placeholder="{T("Buscar actividades","Search events")}" aria-label="{T("Buscar actividades","Search events")}"></label><div class="event-grid">{gallery}</div><p class="notice event-no-results" {"hidden" if gallery else ""}>{T("Aún no hay actividades para mostrar. Las fichas se publicarán cuando la red confirme su información.","There are no events to show yet. Event details will be published once confirmed by the network.")}</p></div></section>'
 page(lang,'events',T('Actividades','Events'),events)
 resource_types=[('all',T('Todos','All')),('protocol',T('Protocolos','Protocols')),('instrument',T('Instrumentos','Instruments')),('code',T('Código','Code')),('data',T('Datos','Data')),('template',T('Plantillas','Templates'))]
 resource_data=json.loads((ROOT/'resources.json').read_text(encoding='utf-8'))
 resource_labels=dict(resource_types)
 if any(item['type'] not in resource_labels or item['type']=='all' for item in resource_data):
  raise ValueError('Unknown resource type')
 resource_cards=''.join(f'<article class="tool-card reveal" data-type="{h(r["type"])}" data-search="{h(" ".join(str(r.get(k,"")) for k in ("title_es","title_en","description_es","description_en")))}"><span class="tool-type">{resource_labels[r["type"]]}</span><h3>{h(r.get("title_es" if lang=="es" else "title_en",""))}</h3><p>{h(r.get("description_es" if lang=="es" else "description_en",""))}</p><a href="{h(r["url"])}" target="_blank" rel="noopener noreferrer">{T("Abrir recurso","Open resource")} ↗</a></article>' for r in resource_data)
 resource_filters=''.join(f'<button class="filter-pill {"selected" if key=="all" else ""}" type="button" data-resource-filter="{key}" aria-pressed="{str(key=="all").lower()}">{label}</button>' for key,label in resource_types)
 resources=top(lang,T('INCOBES / RECURSOS','INCOBES / RESOURCES'),T('Recursos','Resources'))+f'<section class="section"><div class="container">{heading(lang,T("01 / HERRAMIENTAS","01 / TOOLBOX"),T("Herramientas para investigar","Tools for research"))}<div class="catalog-controls"><div class="filter-row" aria-label="{T("Tipos de recurso","Resource types")}">{resource_filters}</div><label class="catalog-search"><span class="sr-only">{T("Buscar recursos","Search resources")}</span><input id="resource-search" type="search" placeholder="{T("Buscar recursos","Search resources")}" aria-label="{T("Buscar recursos","Search resources")}"></label></div><div class="resource-results">{resource_cards}</div><div class="catalog-empty" {"hidden" if resource_cards else ""}><div class="icon">{icon("lab")}</div><h3>{T("Primeros recursos en camino","First resources on the way")}</h3><p>{T("Protocolos, instrumentos, código, datos y plantillas abiertos aparecerán aquí.","Open protocols, instruments, code, data and templates will appear here.")}</p></div><div class="catalog-contribute"><div><h3>{T("¿Tienes una herramienta para compartir?","Have a tool to share?")}</h3><p>{T("Envíanos su enlace, licencia y una breve descripción.","Send us its link, license and a short description.")}</p></div>{btn("mailto:incobes@gmail.com?subject="+T("Recurso%20para%20INCOBES","Resource%20for%20INCOBES"),T("Proponer recurso","Suggest a resource"))}</div></div></section>'
 publication_types=[('all',T('Todos','All')),('article',T('Artículos','Articles')),('preprint',T('Preprints','Preprints')),('forthcoming',T('En prensa','Forthcoming')),('conference',T('Ponencias','Conference papers')),('chapter',T('Capítulos','Book chapters')),('book',T('Libros','Books')),('thesis',T('Tesis','Theses'))]
 publications_data=json.loads((ROOT/'publications.json').read_text(encoding='utf-8'))
 allowed_types={kind for kind,_ in publication_types if kind!='all'}
 for publication in publications_data:
  if publication['type'] not in allowed_types or len(set(publication['network_contributors'])) < (1 if publication['type']=='thesis' else 2):
   raise ValueError('Publications require a recognized type and two distinct INCOBES contributors, or one contributor for a thesis')
 publication_filters=''.join(f'<button class="filter-pill {"selected" if key=="all" else ""}" type="button" data-publication-filter="{key}" aria-pressed="{str(key=="all").lower()}">{label}</button>' for key,label in publication_types)
 publication_item_labels={'article':T('Artículo','Article'),'preprint':'Preprint','forthcoming':T('En prensa','Forthcoming'),'conference':T('Ponencia','Conference paper'),'chapter':T('Capítulo de libro','Book chapter'),'book':T('Libro','Book'),'thesis':T('Tesis','Thesis')}
 publication_cards=''.join(f'<article class="publication reveal" data-type="{h(item["type"])}" data-search="{h(item["citation"]+" "+item["year"]+" "+" ".join(item["network_contributors"]))}"><div class="year">{h(item["year"])}</div><div><div class="pub-type">{publication_item_labels[item["type"]]}</div><h3 class="citation">{h(item["citation"])}</h3><a href="{h(item["url"])}" target="_blank" rel="noopener noreferrer">{T("Ver publicación","View publication")} ↗</a></div></article>' for item in publications_data)
 publications=top(lang,T('INCOBES / PUBLICACIONES','INCOBES / OUTPUTS'),T('Publicaciones','Publications'))+f'<section class="section"><div class="container">{heading(lang,T("01 / PRODUCCIÓN","01 / OUTPUTS"),T("Producción colaborativa","Collaborative work"))}<div class="catalog-controls"><div class="filter-row" aria-label="{T("Tipos de publicación","Publication types")}">{publication_filters}</div><label class="catalog-search"><span class="sr-only">{T("Buscar publicaciones","Search publications")}</span><input id="publication-search" type="search" placeholder="{T("Buscar por autor, título o año","Search author, title or year")}" aria-label="{T("Buscar publicaciones","Search publications")}"></label></div><div class="publication-list">{publication_cards}</div><p class="notice publication-no-results" hidden>{T("No hay publicaciones en esta selección.","No publications match this selection.")}</p></div></section>'
 page(lang,'publications',T('Publicaciones','Publications'),publications)
 # Old thesis links open the publication catalogue with the thesis category selected.
 (OUT/f'{lang}-theses.html').write_text(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={lang}-publications.html?type=thesis"><title>{T("Tesis","Theses")} | INCOBES</title><a href="{lang}-publications.html?type=thesis">{T("Tesis","Theses")}</a></html>',encoding='utf-8')
 institution_cards=[]
 for code,full in INSTITUTIONS:
  short=AFFILIATION_LOOKUP.get(code,code)
  full_label=T('COGNOS · Terapia Cognitivo Conductual','COGNOS · Cognitive Behavioral Therapy') if code=='COGNOS' else full
  mark=f'<img src="assets/{INSTITUTION_LOGOS[code]}" alt="" loading="lazy">' if code in INSTITUTION_LOGOS else f'<span aria-hidden="true">{h(code[:2].upper())}</span>'
  member_links=''.join(f'<a href="{lang}-person-{i}.html">{h(m["name"])} ↗</a>' for i,m in enumerate(members) if m['short_aff']==short)
  institution_cards.append(f'<article class="institution reveal" id="{slugify(code)}"><div class="institution-heading"><div class="institution-mark">{mark}</div><b>{h(code)}</b></div><p>{h(full_label)}</p><div class="institution-people">{member_links}</div></article>')
 institutions_html=top(lang,T('INCOBES / INSTITUCIONES','INCOBES / INSTITUTIONS'),T('Instituciones representadas','Institutions represented'))
 institutions_html+=network_graph(lang)
 institutions_html+=f'<section class="section institution-directory" id="directorio"><div class="container">{heading(lang,T("02 / DIRECTORIO","02 / DIRECTORY"),T("Directorio de instituciones","Institution directory"))}<div class="institution-grid">{"".join(institution_cards)}</div></div></section>'
 page(lang,'institutions',T('Instituciones','Institutions'),institutions_html)
 page(lang,'resources',T('Recursos','Resources'),resources)
 private=top(lang,T('INCOBES / MIEMBROS','INCOBES / MEMBERS'),T('Acceso de integrantes','Member access'))+f'<section class="section"><div class="container member-gateway"><div><div class="eyebrow">01 / {T("COMUNIDAD","COMMUNITY")}</div><h2>{T("Un espacio para colaborar","A space to collaborate")}</h2><div class="gateway-list"><div>{icon("spark")}<span>{T("Propuestas de investigación","Research proposals")}</span></div><div>{icon("lab")}<span>{T("Equipos, técnicas y acceso a poblaciones","Equipment, methods and participant access")}</span></div><div>{icon("nodes")}<span>{T("Contacto directo entre integrantes","Direct contact between members")}</span></div></div></div><div class="access-card"><div class="access-symbol">{icon("nodes")}</div><span class="status-pill">{T("Solo para integrantes autorizados","Authorized members only")}</span><h3>{T("Ingresa a tu cuenta","Sign in to your account")}</h3><a class="btn" href="https://incobes-members.incobes.workers.dev/" target="_blank" rel="noopener noreferrer">{T("Acceder al espacio","Access member space")} ↗</a><div class="access-divider"></div><p>{T("¿Quieres integrarte a la red?","Would you like to join the network?")}</p><a class="access-join" href="{lang}-join.html">{T("Conoce los requisitos","See the requirements")} ↗</a></div></div></section>'
 join=top(lang,T('INCOBES / INTEGRARSE','INCOBES / JOIN'),T('Integrarse a la red','Join the network'))+f'<section class="section"><div class="container"><nav class="section-tabs" aria-label="{T("Secciones de miembros","Member sections")}"><a href="{lang}-members.html">{T("Colaboración interna","Internal collaboration")}</a><a class="selected" href="{lang}-join.html">{T("Integrarse a la red","Join the network")}</a></nav><div class="text-grid join-grid"><div><div class="eyebrow">01 / {T("POSTULACIÓN","APPLICATION")}</div><h2>{T("Tu interés es el punto de partida.","Start with your interests.")}</h2><p class="lead">{T("Investigadores y estudiantes pueden integrarse a la colaboración interdisciplinaria en cognición, conducta y neurociencias.","Researchers and students can join interdisciplinary work across cognition, behavior and neuroscience.")}</p><div class="join-steps"><div><b>01</b><p>{T("Prepara una carta de intención breve con tus intereses y motivos para integrarte.","Prepare a short letter of intent describing your interests and reasons for joining.")}</p></div><div><b>02</b><p>{T("Incluye tu nombre, institución o programa de estudios, intereses y una síntesis de tu trayectoria académica.","Include your name, institution or degree program, interests and a short academic background.")}</p></div><div><b>03</b><p>{T("Envía la carta y tu información académica al correo de la red.","Email the letter and academic information to the network.")}</p></div></div></div><div class="join-panel"><div class="icon">{icon("book")}</div><h3>{T("Enviar solicitud","Send an application")}</h3><p>{T("Adjunta la carta de intención y un CV o síntesis académica.","Attach your letter of intent and a CV or academic summary.")}</p>{btn("mailto:incobes@gmail.com?subject="+T("Solicitud%20de%20integraci%C3%B3n%20a%20INCOBES","INCOBES%20membership%20application"),T("Escribir al correo de la red","Email the network"))}<p class="join-email">incobes@gmail.com</p></div></div></div></section>'
 page(lang,'join',T('Integrarse','Join'),join)
 page(lang,'members',T('Miembros','Members'),private)
(OUT/'index.html').write_text('<!doctype html><html lang="es"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=es-index.html"><title>INCOBES</title><a href="es-index.html">Español</a> / <a href="en-index.html">English</a></html>')
print('Wrote',len(list(OUT.glob('*.html'))),'pages')
