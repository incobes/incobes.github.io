# INCOBES — versión 10

Sitio público bilingüe de páginas independientes, preparado para GitHub Pages. Todo el contenido de `docs/` es público.

## Publicar y editar

Descomprime el ZIP y sube la carpeta `incobes` completa a un repositorio de GitHub. En **Settings → Pages**, selecciona **Deploy from a branch → main → /docs**. Para revisarlo localmente, abre `docs/index.html` (redirige a español). Tras editar los datos o el generador, ejecuta `python build_site.py` desde `incobes` y sube de nuevo `docs/`.

## Organización

- **Inicio:** portada de una pantalla en escritorio, con texto breve, botón hacia «La red», el motivo circular animado original y la cinta de áreas de conocimiento en el borde inferior. La cinta aparece solamente en Inicio. El motivo representa la idea de conexión; no afirma relaciones de colaboración específicas. En pantallas pequeñas la portada admite desplazamiento.
- **La red:** origen, filosofía, objetivos, mención discreta de Armando Q. Angulo-Chavira, Luis Llamas-Alonso y Vladimir Huerta-Chávez y enlace al grafo institucional. Las fotos y fichas de los fundadores permanecen en Integrantes.
- **Investigación:** proyectos de la red.
- **Integrantes:** investigadores y estudiantes con el mismo directorio, separados por estatus, con buscador, perfiles individuales y enlace al grafo. Aún no hay fichas estudiantiles.
- **Actividades:** carrusel de próximos carteles y galería buscable con programa, transmisión y materiales opcionales.
- **Publicaciones:** búsqueda y filtros de artículos, preprints, trabajos en prensa, ponencias, capítulos, libros y tesis.
- **Recursos:** catálogo buscable de protocolos, instrumentos, código, datos y plantillas.
- **Miembros:** entrada visual a futuras cuentas y enlace único a Integrarse. El acceso privado aún no está activo.
- **Instituciones:** grafo interactivo y directorio de adscripciones. El grafo vincula a las 19 personas del directorio con sus nueve adscripciones mostradas y permite abrir perfiles y fichas institucionales. Los nodos personales muestran las fotografías disponibles; Cynthia Torres González conserva iniciales mientras no haya fotografía. Las líneas representan adscripciones del directorio, no colaboraciones científicas comprobadas. Los logotipos proporcionados de UNAM, UABC, UAEH, UAEM, UdeG, CETYS, Tecnológico de Monterrey, Simon Fraser University y COGNOS aparecen con el mismo tratamiento visual. Edgar Omar Herrera Hernández figura bajo COGNOS. En teléfonos el grafo se desplaza horizontalmente y el directorio completo aparece a continuación.

El icono de sobre en los perfiles copia la dirección profesional y muestra una confirmación breve junto al icono. El cursor interactivo se desactiva en pantallas táctiles y con preferencia de movimiento reducido.

## Datos editables

`members.json` contiene los perfiles (`status`: `researcher` o `student`), con nombre, adscripción, semblanza y foto. Los contactos y enlaces públicos están en `public_contacts.json`, en el mismo orden. Las semblanzas breves inglesas se encuentran en `build_site.py`. Si agregas perfiles, actualiza las adscripciones cortas y traducciones allí antes de regenerar el sitio.

Las posiciones y logotipos del grafo se definen en `NETWORK_POSITIONS` e `INSTITUTION_LOGOS`, dentro de `build_site.py`. Si cambia una adscripción, revisa también `institutions_short` y la ficha correspondiente. El grafo destaca vínculos al pasar el puntero o enfocar un nodo con el teclado. Los enlaces al grafo en «La red» e «Integrantes» usan un botón destacado. La cinta y las transiciones respetan la preferencia de movimiento reducido.

`publications.json` define año, tipo, referencia, enlace y participantes de la red. El generador exige dos integrantes distintos para trabajos de colaboración y al menos un integrante para una tesis. `events.json` y `resources.json` siguen vacíos hasta recibir registros públicos confirmados; el generador contiene sus formatos.

## Espacio privado

GitHub Pages no protege archivos del repositorio. Miembros sólo es una entrada visual; su botón de ingreso está desactivado hasta conectar autenticación y almacenamiento externos. Propuestas, teléfonos y capacidades privadas deben quedar fuera de `docs/`. Los avisos a la cuenta de la red y tres fundadores se configurarán en una etapa posterior.

## Antes de publicar

Confirma el correo de la red, el formato de carta de intención y el uso previsto de cada logotipo. Revisa nombres, adscripciones, fotografías y publicaciones. Las fotos de fundadores proceden del primer sitio proporcionado y los demás retratos de sus fichas. Esta versión no publica cuentas ni contenidos privados.
