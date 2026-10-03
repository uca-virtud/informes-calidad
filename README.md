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

`web/index.html` es una página estática que muestra el avance del proyecto a los colectivos
implicados de la UCA. Al hacer push a `main`, `.github/workflows/pages.yml` la cifra con una
contraseña compartida (StatiCrypt, secreto `SITE_PASSWORD`) y la publica en GitHub Pages.
Para verla en local, abre `web/index.html` en el navegador.

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `skills/uca-informes-calidad/` | Skill vigente (seguimiento y renovación de la acreditación). |
| `old-skills/autoinforme-seguimiento-uca/` | Versión anterior de la skill, solo de seguimiento, usada en las evaluaciones. Solo local. |
| `evals/` | Evaluaciones: `casos/<id>/` (entrada y autoinforme humano de referencia), `ejecuciones/Enn-<id>/` (ficha, borrador, cotejos y métricas) e `historial.md`. Solo local: contiene documentos con datos personales. |
| `tools/evaluacion/` | Script `evaluacion.py` (`nueva`, `medir`) del [procedimiento de evaluación](docs/evaluacion/procedimiento.md). |
| `samples/` | Autoinformes reales de ejemplo (seguimiento y renovación). Solo local. |
| `docs/` | Visión del proyecto, evaluaciones (`docs/evaluacion/`: procedimiento, rúbrica, plantillas y catálogo de casos), y, solo en local, peticiones de cartera de los centros y solicitud de la fase 1 al SI. |
| `web/` | Página web de avance del proyecto, publicada en GitHub Pages con contraseña. |