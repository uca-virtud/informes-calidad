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
- Para evaluar la skill, sigue [`docs/evaluacion/procedimiento.md`](docs/evaluacion/procedimiento.md).
  No incorpores a la skill datos, frases ni nombres de los títulos usados como casos de
  evaluación, y no la modifiques durante una evaluación: las lecciones se proponen y las
  aprueba el responsable. Los ejemplos literales de la skill solo pueden proceder de
  títulos marcados como `excluido` en `docs/evaluacion/casos.csv`.
- No añadas pruebas automatizadas sin que el usuario haya dado su consentimiento.
- Mantén al día la web del proyecto, dos páginas estáticas en `web/`:
  - `index.html` (avance): las siete fases de `docs/VISION.md`. Cuando cambie el estado de
    una fase (en `docs/`, en la skill o comunicado por el usuario), actualízalo.
  - `evaluacion.html` (evaluación de la skill): cifras globales, sin detalle, tomadas de
    `evals/historial.md`; actualízalas tras cada ejecución. El texto de `SKILL.md` lo
    incrusta el workflow al publicar (marcador `SKILL_MD`); no lo copies a mano.
  - En ambas, cambia la fecha de «Última actualización» al modificarlas.
- En la web no se publican nunca datos personales (nombres, correos, teléfonos), documentos
  (PDF, DOCX, Excel) ni contenido de `docs/peticiones-cartera/`. La única excepción son los
  enlaces de `evaluacion.html` al material de revisión de las coordinaciones, que se guarda
  en el repositorio (`docs/evaluacion/material-coordinaciones/<caso>/`), no en la web.
- Para ver la web en local, abre `web/index.html` en el navegador. El despliegue lo hace
  `.github/workflows/pages.yml`, que cifra ambas páginas con StatiCrypt usando el secreto
  `SITE_PASSWORD` y falla si no existe. `web/.staticrypt.json` guarda la sal (no es secreta);
  no la cambies, o se invalidará el «Recordarme» de quienes ya accedieron.
- Los scripts de la skill necesitan `python-docx`, que no está en el Python del sistema;
  para probarlos crea un entorno virtual temporal.
- Para leer los PDF de `docs/`, usa `pypdf` en un entorno virtual temporal; `pdftotext`
  no está instalado.
