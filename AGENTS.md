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
- Mantén al día la web de avance del proyecto: una única página estática, `web/index.html`.
  Cuando cambie el estado de una fase o haya un avance relevante (en `docs/`, en la skill o
  comunicado por el usuario), actualiza el estado de la fase, añade una entrada en
  «Novedades» y cambia la fecha de «Última actualización».
- En la web no se publican nunca datos personales (nombres, correos, teléfonos), documentos
  (PDF, DOCX, Excel) ni contenido de `docs/peticiones-cartera/`: solo el avance resumido.
- Para ver la web en local, abre `web/index.html` en el navegador. El despliegue lo hace
  `.github/workflows/pages.yml`, que la cifra con StatiCrypt usando el secreto `SITE_PASSWORD`
  y falla si no existe. `web/.staticrypt.json` guarda la sal (no es secreta); no la cambies,
  o se invalidará el «Recordarme» de quienes ya accedieron.
- Los scripts de la skill necesitan `python-docx`, que no está en el Python del sistema;
  para probarlos crea un entorno virtual temporal.
- Para leer los PDF de `docs/`, usa `pypdf` en un entorno virtual temporal; `pdftotext`
  no está instalado.
