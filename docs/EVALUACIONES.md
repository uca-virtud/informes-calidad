# Evaluaciones de la skill de autoinformes

Registro de las pruebas de la skill frente a autoinformes reales elaborados por las
coordinaciones. Cada evaluación se guarda en `evals/` y aquí se resumen sus resultados, las
lecciones aprendidas y su estado en la skill actual (`skills/uca-informes-calidad`).

## Método

Cada evaluación es un título de la ESI cuyo autoinforme de seguimiento del curso 2024/25
(convocatoria 2026) ya había elaborado y aprobado la coordinación. Se ejecutó la skill en
Claude Desktop y se pidió a la IA que cotejara su borrador con el documento humano.

Estructura de cada carpeta `evals/Eval n. <TÍTULO>/`:

| Carpeta | Contenido |
|---|---|
| `Datos de partida/` | Documentos aportados a la IA (autoinforme 23/24, memoria verificada, informe ACCUA). Los indicadores los extrajo la IA de LinceBI. |
| `Resultado obtenido por la IA/` | Borrador `.docx` generado. |
| `Resultado generado por Humano/` | Autoinforme aprobado por la CGC (referencia). |
| `Feedback proporcionado por la IA/` | Cotejo IA-humano redactado por la propia IA. |

En las evals 2 y 3 la carpeta de referencia se llama `Resutado generado por Humano/`.

Las evaluaciones se ejecutaron con la versión anterior de la skill
(`old-skills/autoinforme-seguimiento-uca`). Entre la eval 1 y las evals 2-3 la IA modificó
la skill con lo aprendido en la eval 1; esa versión es la que se conserva en `old-skills/`.

## Resultados

| Eval | Título | Datos de partida | Palabras IA / humano | PF IA / humano | PD IA / humano | `[PENDIENTE]` | Cotejo |
|---|---|---|---|---|---|---|---|
| 1 | GII | Autoinforme 23/24 + memoria | 5.518 / 26.359 (21 %) | 4 / 19 | 3 / 5 | 0 | Breve, no estructurado |
| 2 | GIA | Autoinforme 23/24 + memoria + informe ACCUA | 16.123 / 23.746 (68 %) | 20 / 14 | 14 / 4 | 6 | Medio |
| 3 | GIDIDP | Autoinforme 23/24 + memoria | 17.204 / 24.533 (70 %) | 19 / 16 | 16 / 1 | 3 | Detallado (≈230 celdas) |

PF/PD: códigos de puntos fuertes y débiles distintos encontrados en cada documento.

Se confirma la hipótesis de partida: **la eval 1 es claramente peor que la 2 y la 3**. Su
borrador tiene una quinta parte de la extensión del humano, apenas desarrolla puntos
fuertes y no incluye el análisis de calificaciones por asignatura. Las evals 2 y 3, ya con
la skill corregida, alcanzan unos dos tercios de la extensión humana y una coincidencia
alta en estructura, identificación, interpretaciones cualitativas e indicadores (≈91 % de
las celdas del Anexo I en la eval 3).

El problema dominante ha cambiado: en la eval 1 era **falta de contenido**; en las evals 2
y 3 es **exceso de puntos débiles** (14-16 frente a 1-4 de las coordinaciones) y
**discrepancias de datos** por la fuente y la fecha de extracción de LinceBI.

### Hallazgos por evaluación

**Eval 1 (GII).** Coinciden estructura, codificación PF/PD/AM y tasas de rendimiento,
éxito, evaluación y abandono. Faltaba el análisis de calificaciones por asignatura (6.3).
Graduación y eficiencia difieren por usar el entorno de pruebas (`datapru.uca.es`).

**Eval 2 (GIA).** Coinciden las 15 recomendaciones ACCUA, los objetivos de la memoria y la
interpretación de la baja graduación. Se repite el uso de `datapru`: graduación 16,4 %
frente a 7,5 % real. Quedaron pendientes datos que el humano sí tenía: créditos reconocidos
(787), prácticas curriculares (15 estudiantes) y la composición de la CGC (el humano remite
a la web). La IA detectó un error del humano (confunde quinquenios con sexenios).

**Eval 3 (GIDIDP).** Identificación 13/13. Las diferencias de datos se deben a la
volatilidad de la tasa de graduación entre marzo y julio, a que la IA consolidó la serie
histórica con el autoinforme anterior (la coordinación reextrae la serie en vivo) y a datos
internos del centro (plazas del doble título, convenios, tutores). La IA detectó cuatro
errores del humano: cohortes de egresados desplazadas un año, un valor de P04-13 fuera de
la escala 0-5, el objetivo del 50 % asignado a la tasa de éxito en vez de a la de
rendimiento y recomendaciones ACCUA renumeradas.

## Lecciones y estado en la skill

Estado: **Incorporada** (está en la skill actual), **Insuficiente** (está, pero una
evaluación posterior muestra que no basta) o **Pendiente**. Las lecciones L4-L14 se
incorporaron el 2 de octubre de 2026 y están pendientes de validar con una nueva ronda de
evaluaciones.

| # | Lección | Origen | Estado y dónde |
|---|---|---|---|
| L1 | Incluir el análisis de calificaciones por asignatura (6.3, `PorcentajeCalificaciones`) | Eval 1 | Incorporada (`SKILL.md`, `estilo-y-ejemplos.md`) |
| L2 | P01-03 (PTGAS) se analiza a nivel de centro | Eval 1 | Incorporada (`estilo-y-ejemplos.md`) |
| L3 | Objetivos de la memoria (§8.1) en tabla, respetando la tasa a la que se asocia cada uno | Evals 1 y 3 | Incorporada (`estilo-y-ejemplos.md`) |
| L4 | Extraer de producción (`data.uca.es`), no de pruebas (`datapru.uca.es`) | Evals 1 y 2 | Incorporada: comprobación del host antes de extraer y parada si es pruebas (`SKILL.md`); el script avisa si `extraccion.entorno` es `datapru` |
| L5 | Extraer toda la serie en vivo; el autoinforme anterior solo para columnas fuera de la ventana de cinco cursos y valores incoherentes | Eval 3 | Incorporada ("Regla de la serie histórica" en `mapa-indicadores-lincebi.md`, `SKILL.md`) |
| L6 | Registrar entorno y fecha de extracción; advertir de la volatilidad de P04-05 | Evals 2 y 3 | Incorporada (bloque `extraccion` del JSON; el script avisa si falta) |
| L7 | Ningún indicador de satisfacción por encima de 5; misma alineación de cohortes en título y centro | Eval 3 | Incorporada (aviso del script, comprobaciones del mapa y checklist) |
| L8 | Egresados: cinco últimas cohortes con datos (conv. 2026: `2019-20 … 2023-24`), análisis de la cohorte más reciente, nº de encuestas y egresados | Eval 3 | Incorporada: decidido por el responsable del proyecto; el script reetiqueta las cabeceras de la plantilla con `anios_egresados` |
| L9 | Entre 1 y 5 puntos débiles en total, solo los asumibles con acción propia | Eval 3 (y recuento de la 2) | Incorporada (`SKILL.md`, `guia-redaccion.md`, `estilo-y-ejemplos.md`) |
| L10 | Pedir al centro desde el inicio los datos internos (doble título, prácticas, convenios, tutores, créditos reconocidos, primer curso, rutas UCADrive) | Evals 2 y 3 | Incorporada (`SKILL.md`, `mapa-indicadores-lincebi.md`) |
| L11 | Créditos reconocidos desde LinceBI | Eval 2 | Incorporada con búsqueda alternativa; la ruta del mapa sigue sin verificar en LinceBI |
| L12 | Composición de la CGC: remitir a la web del título | Eval 2 | Incorporada (`SKILL.md`, `estilo-y-ejemplos.md`, `estructura-autoinforme.md`) |
| L13 | Evidencias en el seguimiento: rutas UCADrive por criterio y curso; enlaces externos para los Anexos 2 y 4 | Eval 3 | Incorporada (`estructura-autoinforme.md`) |
| L14 | Conservar la numeración original de las recomendaciones ACCUA | Eval 3 | Incorporada (`SKILL.md`, `estilo-y-ejemplos.md`) |
| L15 | Responsables y fechas concretos en el plan de mejora | Eval 1 | Incorporada como documento opcional (plan de mejora vivo) |

## Limitaciones de las evaluaciones actuales

- **Sin rúbrica común.** Cada cotejo tiene un formato y una profundidad distintos (la eval 1
  es un párrafo; la 3, un informe con tablas), así que no son comparables entre sí.
- **Autoevaluación.** La misma IA que genera el borrador juzga el resultado y, en la eval 1,
  modificó la skill sin revisión humana.
- **Referencia imperfecta.** El autoinforme humano contiene errores (evals 2 y 3); no puede
  tomarse como verdad absoluta celda a celda.
- **Datos no reproducibles.** Los valores de LinceBI cambian entre la aprobación (marzo) y
  la ejecución (julio), y no se registró el entorno ni la fecha de extracción.
- **Cobertura.** Solo seguimiento, solo grados de la ESI; no hay másteres, otros centros ni
  renovación de la acreditación.

## Cómo añadir una evaluación

1. Crea `evals/Eval n. <TÍTULO>/` con las cuatro subcarpetas del apartado Método.
2. Registra la versión de la skill, el cliente usado, el entorno de LinceBI y la fecha de
   extracción.
3. Haz el cotejo con la misma rúbrica para todas las evaluaciones.
4. Añade la fila a la tabla de resultados y actualiza el estado de las lecciones.
