# Instrucciones para agentes

## Referencias

- Consulta [`docs/VISION.md`](docs/VISION.md) para el contexto y el estado del proyecto.
- Para elaborar o revisar un autoinforme, sigue
  [`skills/uca-informes-calidad/SKILL.md`](skills/uca-informes-calidad/SKILL.md);
  consulta sus referencias según el flujo definido allí.
- Escribe en español de España, salvo que el usuario solicite otro idioma.

## Criterios de trabajo

- Mantén cada contenido en su fuente: visión en `docs/VISION.md`, procedimiento en la
  skill y sus referencias, e instrucciones de trabajo aquí.
- Antes de usar o documentar comandos de build, pruebas o despliegue, comprueba que
  existan en el repositorio.
- Al cambiar una skill, actualiza las referencias afectadas junto con su documento
  principal, y el estado de las lecciones en [`docs/EVALUACIONES.md`](docs/EVALUACIONES.md).
- No añadas pruebas automatizadas sin que el usuario haya dado su consentimiento.
- Mantén al día el sitio web del proyecto (`web/`, MkDocs). `VISION.md`, `EVALUACIONES.md`
  y la solicitud de la fase 1 se incluyen desde `docs/` y se actualizan solos. Cuando cambie
  el estado de una fase, la skill o cualquier documento de `docs/`, revisa `web/docs/index.md`,
  `hoja-de-ruta.md`, `como-funciona.md` y `colectivos.md`, y añade una entrada fechada en
  `novedades.md`. Si creas un documento en `docs/` que deba publicarse, inclúyelo en `web/`
  y añádelo al `nav` de `web/mkdocs.yml`.
- En el sitio no se publican nunca datos personales (nombres, correos, teléfonos) ni
  documentos (PDF, DOCX, Excel): solo resúmenes y métricas. El hook `web/hooks/proteccion.py`
  exige la contraseña, cifra todas las páginas y bloquea los documentos, pero no detecta datos
  personales: revísalos tú.
- Para previsualizar el sitio, crea un entorno virtual temporal con `web/requirements.txt` y
  ejecuta `SITE_PASSWORD=<contraseña de prueba> mkdocs serve` en `web/`. El despliegue lo
  hace `.github/workflows/pages.yml` con el secreto `SITE_PASSWORD`.
- Los scripts de la skill necesitan `python-docx`, que no está en el Python del sistema;
  para probarlos crea un entorno virtual temporal.
- Para leer los PDF de `docs/`, usa `pypdf` en un entorno virtual temporal; `pdftotext`
  no está instalado.
