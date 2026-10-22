# Informes de calidad — UCA

Automatización asistida de la preparación de informes de calidad de títulos oficiales
de la Universidad de Cádiz.

## Documentación

- [Visión del proyecto](docs/VISION.md): contexto, objetivo y fases.
- [Skill de autoinformes](skills/uca-informes-calidad/SKILL.md): procedimiento de
  elaboración, recursos y criterios de entrega.
- [Procedimiento de evaluación](docs/PROCEDIMIENTO.md): cómo se evalúa la skill frente a
  autoinformes reales, paso a paso.
- [Lecciones](docs/LECCIONES.md): versiones de la skill y lecciones aprendidas en su
  evaluación, con su estado.
- [Instrucciones para agentes](AGENTS.md): reglas de trabajo de los agentes de IA en este
  repositorio.

## Estructura del repositorio

Las carpetas marcadas como *solo local* contienen datos personales o documentos internos y
no se versionan.

| Carpeta | Contenido |
|---|---|
| `skills/uca-informes-calidad/` | Skill vigente (seguimiento y renovación de la acreditación). |
| `.github/skills/preparar-caso/` | Skill de proyecto que prepara un caso de evaluación a partir del nombre del título, buscando sus documentos en la web del centro. |
| `dist/` | Zip de la skill para instalarla en Claude; se descarga desde `asistente.html`. Se regenera con `python3 tools/empaquetar_skill.py`. |
| `tools/empaquetar_skill.py` | Script que genera el zip de `dist/` a partir de la skill vigente. |
| `tools/evaluacion/` | Script `evaluacion.py` (`enlaces`, `caso`, `nueva`, `medir`, `valoracion`) del procedimiento de evaluación. |
| `docs/` | Visión, procedimiento de evaluación y lecciones. |
| `docs/evaluacion/` | Rúbrica y plantillas de cotejo y ficha. |
| `docs/peticiones-cartera/` | Peticiones de cartera de los centros y solicitud de la fase 1 al Sistema de Información (modelo de datos e informe de indicadores del Anexo I). *Solo local.* |
| `evals/casos.csv` | Catálogo de casos de evaluación. |
| `evals/casos/<id>/` | Por cada caso: documentos de entrada (`entrada/`), autoinforme humano de referencia (`referencia/`) y procedencia de los documentos (`fuentes.json` y `fuentes.md`). |
| `evals/ejecuciones/Enn-<id>/` | Por cada ejecución: ficha, borrador, cotejos, métricas y, si se envió a la coordinación, `rubrica-valoracion.xlsx`. Las hojas devueltas (`valoracion-coordinacion*.xlsx`) son *solo locales*. |
| `evals/historial.md` | Resultados y relato de cada ejecución. *Solo local.* |
| `samples/` | Autoinformes reales de ejemplo (seguimiento y renovación). *Solo local.* |
| `old-skills/autoinforme-seguimiento-uca/` | Versión anterior de la skill, solo de seguimiento, usada en las primeras evaluaciones. *Solo local.* |
| `web/` | Web del proyecto (ver abajo). |

## Web del proyecto

`web/` contiene cuatro páginas estáticas para los colectivos implicados de la UCA:

- `index.html`: avance del proyecto por fases.
- `asistente.html`: qué es el asistente, cómo funciona (agente de IA, skill y MCP de LinceBI),
  lecciones aprendidas en cada versión y descarga de la skill en zip.
- `procedimiento.html`: cómo se evalúa la skill: proceso de evaluación y rúbrica.
- `evaluacion.html`: resultados de la evaluación: resumen de cifras al principio, evolución de la nota,
  tabla por ejecución (nota de cada aspecto, media, errores graves y ficha resumida),
  próximos pasos y material para que las coordinaciones la revisen.

Al hacer push a `main`, `.github/workflows/pages.yml` cifra las cuatro páginas con una
contraseña compartida (StatiCrypt, secreto `SITE_PASSWORD`; sin él el despliegue falla) y las
publica en GitHub Pages. Para verlas en local, abre
`web/index.html` en el navegador.
