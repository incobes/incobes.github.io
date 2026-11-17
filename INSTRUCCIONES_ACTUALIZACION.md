# Actualización de INCOBES

Esta entrega contiene archivos para dos repositorios. No se requiere una migración de D1 ni se incluyen tokens.

## Portal privado (`incobes-members`)

1. En el repositorio privado, reemplaza los archivos de `src/` incluidos en `INCOBES_actualizacion_portal_privado.zip` y agrega `GUIA_PUBLICACION_PERFILES.md`.
2. Conserva las variables y secretos de Cloudflare existentes. No hace falta cambiar el enlace con D1 ni la configuración de Access.
3. Guarda los cambios en la rama conectada a Workers. Revisa **Deployments** y confirma que el nuevo despliegue quede en estado Ready.

La actualización muestra errores de validación más claros, contadores de caracteres para semblanza y capacidades, y el aviso de revisión de fotos/logotipos. No publica fotos directamente.

## Sitio público (`incobes.github.io`)

1. En el repositorio público, reemplaza `build_site.py`, `members.json`, `resources.json` y `README.md` por los incluidos en `INCOBES_actualizacion_sitio_publico.zip`.
2. Reemplaza las páginas correspondientes de `docs/` incluidas en el ZIP: fichas `es-person-*`, `en-person-*` y `es-resources.html`, `en-resources.html`.
3. Elimina `public_contacts.json` del repositorio. El directorio deja de publicar correos y enlaces personales; el contacto general de INCOBES permanece.
4. Guarda los cambios en la rama que publica GitHub Pages.

Los recursos de ANEW y completamiento abren los minisitios que ya existen en `angulo-chavira.github.io`; esta actualización no crea otro sitio.

## Drive de recepción

El portal ya indica a los integrantes que soliciten el enlace de la carpeta de revisión por correo a INCOBES. La carpeta real no está enlazada en esta entrega porque no se proporcionó su URL. Cuando exista una carpeta específica en el Drive compartido, administración puede compartir su enlace con las personas integrantes. Los archivos se revisan y publican sólo después de verificar autorización.
