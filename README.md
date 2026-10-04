# Informes de calidad — UCA

Automatización asistida de la preparación de informes de calidad de títulos oficiales
de la Universidad de Cádiz.

## Documentación

- [Visión del proyecto](docs/VISION.md): contexto, objetivo y fases.
- [Skill de autoinformes](skills/uca-informes-calidad/SKILL.md): procedimiento de
  elaboración, recursos y criterios de entrega.
- [Procedimiento de evaluación](docs/PROCEDIMIENTO.md): cómo se evalúa la skill frente a
  autoinformes reales, paso a paso.
- [Evaluaciones](docs/EVALUACIONES.md): resultados de cada ejecución, lecciones aprendidas y
  su estado en la skill.
- [Instrucciones para agentes](AGENTS.md): reglas de trabajo de los agentes de IA en este
  repositorio.

## Estructura del repositorio

Las carpetas marcadas como *solo local* contienen datos personales o documentos internos y
no se versionan.

| Carpeta | Contenido |
|---|---|
| `skills/uca-informes-calidad/` | Skill vigente (seguimiento y renovación de la acreditación). |
| `.github/skills/preparar-caso/` | Skill de proyecto que prepara un caso de evaluación a partir del nombre del título, buscando sus documentos en la web del centro. |
| `tools/evaluacion/` | Script `evaluacion.py` (`enlaces`, `caso`, `nueva`, `medir`) del procedimiento de evaluación. |
| `docs/` | Visión, procedimiento y registro de evaluaciones. |
| `docs/evaluacion/` | Rúbrica, plantillas de cotejo y ficha, y `material-coordinaciones/<caso>/` (borrador de la IA, autoinforme de la coordinación y rúbrica de valoración en Excel de cada título). |
| `docs/peticiones-cartera/` | Peticiones de cartera de los centros y solicitud de la fase 1 al Sistema de Información (modelo de datos e informe de indicadores del Anexo I). *Solo local.* |
| `evals/` | Catálogo de casos (`casos.csv`), `casos/<id>/` (entrada y autoinforme humano de referencia), `ejecuciones/Enn-<id>/` (ficha, borrador, cotejos y métricas) e `historial.md`. *Solo local.* |
| `samples/` | Autoinformes reales de ejemplo (seguimiento y renovación). *Solo local.* |
| `old-skills/autoinforme-seguimiento-uca/` | Versión anterior de la skill, solo de seguimiento, usada en las primeras evaluaciones. *Solo local.* |
| `web/` | Web del proyecto (ver abajo). |

## Web del proyecto

`web/` contiene dos páginas estáticas para los colectivos implicados de la UCA:

- `index.html`: avance del proyecto por fases.
- `evaluacion.html`: seguimiento de la evaluación de la skill para los implicados: resumen de
  resultados, proceso de evaluación, rúbrica, evolución de la nota, tabla por ejecución (nota
  de cada aspecto, media, errores graves y ficha resumida), lecciones aprendidas en cada
  versión, próximos pasos, texto de la skill y material para que las coordinaciones la revisen.

Al hacer push a `main`, `.github/workflows/pages.yml` incrusta `SKILL.md` en la página de
evaluación, cifra ambas con una contraseña compartida (StatiCrypt, secreto `SITE_PASSWORD`;
sin él el despliegue falla) y las publica en GitHub Pages. Para verlas en local, abre
`web/index.html` en el navegador.
