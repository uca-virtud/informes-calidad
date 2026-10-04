# Informes de calidad — UCA

Automatización asistida de la preparación de informes de calidad de títulos oficiales
de la Universidad de Cádiz.

## Documentación

- [Visión del proyecto](docs/VISION.md): contexto, objetivo y fases.
- [Skill de autoinformes](skills/uca-informes-calidad/SKILL.md): procedimiento de
  elaboración, recursos y criterios de entrega.
- [Evaluaciones](docs/EVALUACIONES.md): resultados de la skill frente a autoinformes
  reales, lecciones aprendidas y su estado.
- Solicitud de la fase 1 al Sistema de Información (`docs/peticiones-cartera/`, no se
  versiona): modelo de datos e informe agregado de indicadores del Anexo I.

## Web de avance del proyecto

`web/` contiene dos páginas estáticas para los colectivos implicados de la UCA:
`index.html`, con el avance del proyecto por fases, y `evaluacion.html`, con los resultados
globales de la evaluación de la skill, su texto y el material para que las coordinaciones la
revisen. Al hacer push a `main`, `.github/workflows/pages.yml` incrusta `SKILL.md` en la
página de evaluación, cifra ambas con una contraseña compartida (StatiCrypt, secreto
`SITE_PASSWORD`) y las publica en GitHub Pages. Para verlas en local, abre `web/index.html`
en el navegador.

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `skills/uca-informes-calidad/` | Skill vigente (seguimiento y renovación de la acreditación). |
| `old-skills/autoinforme-seguimiento-uca/` | Versión anterior de la skill, solo de seguimiento, usada en las evaluaciones. Solo local. |
| `evals/` | Evaluaciones: `casos/<id>/` (entrada y autoinforme humano de referencia), `ejecuciones/Enn-<id>/` (ficha, borrador, cotejos y métricas) e `historial.md`. Solo local: contiene documentos con datos personales. |
| `tools/evaluacion/` | Script `evaluacion.py` (`enlaces`, `caso`, `nueva`, `medir`) del [procedimiento de evaluación](docs/evaluacion/procedimiento.md). |
| `.github/skills/preparar-caso/` | Skill de proyecto que prepara un caso de evaluación a partir del nombre del título, buscando sus documentos en la web del centro. |
| `samples/` | Autoinformes reales de ejemplo (seguimiento y renovación). Solo local. |
| `docs/` | Visión del proyecto, evaluaciones (`docs/evaluacion/`: procedimiento, rúbrica, plantillas, catálogo de casos y `material-coordinaciones/`, con el borrador de la IA, el autoinforme de la coordinación y la rúbrica de valoración en Excel de cada título), y, solo en local, peticiones de cartera de los centros y solicitud de la fase 1 al SI. |
| `web/` | Web del proyecto (avance y evaluación), publicada en GitHub Pages con contraseña. |