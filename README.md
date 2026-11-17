# INCOBES — versión 13

Sitio público bilingüe de páginas independientes, preparado para GitHub Pages. Todo el contenido de `docs/` es público.

## Publicar y editar

Descomprime el ZIP y sube la carpeta `incobes` completa a un repositorio de GitHub. En **Settings → Pages**, selecciona **Deploy from a branch → main → /docs**. Para revisarlo localmente, abre `docs/index.html` (redirige a español). Tras editar los datos o el generador, ejecuta `python build_site.py` desde `incobes` y sube de nuevo `docs/`.

## Organización

- **Inicio:** portada de una pantalla en escritorio, con texto breve, botón hacia «La red», el motivo circular animado original y la cinta de áreas de conocimiento en el borde inferior. La cinta aparece solamente en Inicio. El motivo representa la idea de conexión; no afirma relaciones de colaboración específicas. En pantallas pequeñas la portada admite desplazamiento.
- **La red:** origen, filosofía, objetivos, mención discreta de Armando Q. Angulo-Chavira, Luis Llamas-Alonso y Vladimir Huerta-Chávez y enlace al grafo institucional. Las fotos y fichas de los fundadores permanecen en Integrantes.
- **Investigación:** proyectos de la red.
- **Integrantes:** investigadores y estudiantes con el mismo directorio, separados por estatus, con buscador, perfiles individuales y enlace al grafo. Las fichas muestran semblanza y adscripción; el contacto y la invitación a integrarse se canalizan por INCOBES.
- **Actividades:** carrusel de próximos carteles y galería buscable con programa, transmisión y materiales opcionales.
- **Publicaciones:** búsqueda y filtros de artículos, preprints, trabajos en prensa, ponencias, capítulos, libros y tesis.
- **Recursos:** catálogo buscable de protocolos, instrumentos, código, datos y plantillas.
- **Miembros:** la introducción y las tres formas de participación comparten un solo encabezado. Debajo aparecen la solicitud de incorporación por correo y el acceso al futuro espacio privado. No hay pestañas ni página separada de «Cómo integrarse».
- **Instituciones:** grafo interactivo y directorio de adscripciones. El grafo vincula a las 19 personas del directorio con sus nueve adscripciones mostradas y permite abrir perfiles y fichas institucionales. Los nodos personales muestran las fotografías disponibles; Cynthia Torres González conserva iniciales mientras no haya fotografía. Las líneas representan adscripciones del directorio, no colaboraciones científicas comprobadas. Los logotipos proporcionados de UNAM, UABC, UAEH, UAEM, UdeG, CETYS, Tecnológico de Monterrey, Simon Fraser University y COGNOS aparecen con el mismo tratamiento visual. Edgar Omar Herrera Hernández figura bajo COGNOS. En teléfonos el grafo se desplaza horizontalmente y el directorio completo aparece a continuación.

Los perfiles públicos ya no incluyen correo, teléfono ni enlaces a cuentas académicas o personales. Cada ficha dirige a «Miembros» para que el interés y las solicitudes lleguen a INCOBES.

## Datos editables

`members.json` contiene los perfiles (`status`: `researcher` o `student`), con nombre, adscripción, semblanza en español e inglés (`bio`, `bio_en`) y foto. Editar estos datos no requiere cambiar `build_site.py`. Las fotos aprobadas se guardan en `docs/assets/` y se referencian con una ruta como `assets/miembros/nombre.webp`.

Las posiciones y logotipos del grafo se definen en `NETWORK_POSITIONS` e `INSTITUTION_LOGOS`, dentro de `build_site.py`. Si cambia una adscripción, revisa también `institutions_short` y la ficha correspondiente. El grafo destaca vínculos al pasar el puntero o enfocar un nodo con el teclado. Los enlaces al grafo en «La red» e «Integrantes» usan un botón destacado. La cinta y las transiciones respetan la preferencia de movimiento reducido.

`publications.json` define año, tipo, referencia, enlace y participantes de la red. El generador exige dos integrantes distintos para trabajos de colaboración y al menos un integrante para una tesis. `resources.json` contiene enlaces a los minisitios ANEW y de completamiento de oraciones, alojados en el sitio de Armando. `events.json` sigue vacío hasta recibir actividades públicas confirmadas.

Los archivos recibidos para perfiles públicos deben revisarse y aprobarse antes de publicarse. No se publica automáticamente ningún archivo recibido en Drive.

## Espacio privado

GitHub Pages no protege archivos del repositorio. El botón «Solicitar incorporación» prepara un correo a `incobes@gmail.com` con asunto y campos sugeridos; no envía ni almacena la solicitud automáticamente. La incorporación se acuerda tras conversar con la persona interesada. El botón «Acceder al espacio de miembros» permanece desactivado mientras no exista una aplicación privada autenticada. Una vez desplegada y protegida con Cloudflare Access, configura su URL HTTPS con `INCOBES_PRIVATE_APP_URL` al generar el sitio: `INCOBES_PRIVATE_APP_URL=https://<dirección-real> python3 build_site.py` (en PowerShell: `$env:INCOBES_PRIVATE_APP_URL='https://<dirección-real>'; python build_site.py`). Una URL inválida detiene la generación. Si no se configura, se genera el botón desactivado. Regenera y publica `docs/` después de activar el acceso.

Propuestas, teléfonos y capacidades privadas deben quedar fuera de `docs/`. La visibilidad de los datos de contacto será optativa cuando exista el directorio privado. Los avisos a la cuenta de la red y tres fundadores se configurarán en una etapa posterior. La propuesta de arquitectura para Cloudflare está en `PROPUESTA_ESPACIO_PRIVADO.md`; aún no se han creado Worker, D1, Access ni R2 para INCOBES.

## Antes de publicar

Confirma el correo de la red y el uso previsto de cada logotipo. Revisa nombres, adscripciones, fotografías y publicaciones. Las fotos de fundadores proceden del primer sitio proporcionado y los demás retratos de sus fichas. Esta versión no publica cuentas ni contenidos privados.
