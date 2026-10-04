# Instrucciones para agentes

Repositorio de la skill que redacta autoinformes de calidad de títulos de la Universidad de
Cádiz y de su evaluación frente a autoinformes reales. Contexto, objetivo y fases:
[`docs/VISION.md`](docs/VISION.md). Escribe en español de España, salvo que el usuario pida
otro idioma.

## Dónde está cada cosa

Cada contenido vive en una sola fuente: enlázala en lugar de copiarla.

| Tarea | Fuente |
|---|---|
| Elaborar o revisar un autoinforme | [`skills/uca-informes-calidad/SKILL.md`](skills/uca-informes-calidad/SKILL.md) y las referencias que indique su flujo |
| Preparar un caso de evaluación a partir del nombre de un título | [`.github/skills/preparar-caso/SKILL.md`](.github/skills/preparar-caso/SKILL.md) |
| Evaluar la skill: ejecución, registro de resultados y material para las coordinaciones | [`docs/PROCEDIMIENTO.md`](docs/PROCEDIMIENTO.md) |
| Resultados de las evaluaciones y estado de las lecciones | [`docs/EVALUACIONES.md`](docs/EVALUACIONES.md) |
| Estructura del repositorio y funcionamiento de la web | [`README.md`](README.md) |

## Cambiar la skill

- La skill cambia solo con lecciones aprobadas por el responsable y fuera de una evaluación:
  durante una ejecución queda congelada y las lecciones se proponen.
- Cumple las [reglas contra el sobreajuste](docs/PROCEDIMIENTO.md#reglas-contra-el-sobreajuste):
  los ejemplos literales proceden solo de títulos con `conjunto = excluido` en
  `evals/casos.csv`.
- En el mismo cambio, actualiza `SKILL.md`, las referencias afectadas y la tabla de lecciones
  de `docs/EVALUACIONES.md`.

## Datos personales

`evals/`, `samples/`, `old-skills/` y `docs/peticiones-cartera/` contienen datos personales y
solo existen en local (`.gitignore`). De ellos llegan al repositorio y a la web únicamente
cifras agregadas, lecciones generalizadas y el material aprobado del paso 7 del
procedimiento.

La web publica solo el avance y cifras globales. Nunca publica datos personales (nombres,
correos, teléfonos), documentos (PDF, DOCX, Excel) ni contenido de
`docs/peticiones-cartera/`. Única excepción: los enlaces de `evaluacion.html` al material de
`docs/evaluacion/material-coordinaciones/`, que está en el repositorio, no en `web/`.

## Web

- `web/index.html` refleja el estado de las siete fases de `docs/VISION.md`: actualízalo
  cuando cambie una fase (en `docs/`, en la skill o porque lo comunique el usuario).
- `web/evaluacion.html` (resultados) se actualiza tras cada ejecución (pasos 6 y 7 del
  procedimiento). `web/procedimiento.html` explica el proceso y la rúbrica: actualízalo cuando
  cambien en `docs/PROCEDIMIENTO.md`. `web/asistente.html` explica qué es el asistente y cómo
  funciona: actualízalo cuando cambien la skill o el MCP. El texto de `SKILL.md` lo incrusta el workflow en
  el marcador `SKILL_MD` de `web/asistente.html` al publicar.
- Cada versión nueva de la skill recibe el siguiente número (v7, v8…) en `docs/EVALUACIONES.md`
  y en la línea temporal de `web/evaluacion.html`.
- Al modificar una página, cambia su fecha de «Última actualización».
- La sal de `web/.staticrypt.json` es fija (no es secreta): cambiarla invalida el
  «Recordarme» de quienes ya accedieron.

## Entorno

- Comprueba que un comando exista en el repositorio antes de usarlo o documentarlo.
- Pide consentimiento al usuario antes de añadir pruebas automatizadas.
- El Python del sistema no trae las librerías necesarias y no hay `pdftotext`. Usa un entorno
  virtual temporal con `python-docx` para los scripts de la skill, `pypdf` para leer PDF y
  `tools/evaluacion/requirements.txt` para `evaluacion.py`.
