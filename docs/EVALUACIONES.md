# Evaluaciones de la skill de autoinformes

Registro de las pruebas de la skill frente a autoinformes reales elaborados por las
coordinaciones. Cada evaluación se guarda en `evals/` y aquí se resumen sus resultados, las
lecciones aprendidas y su estado en la skill actual (`skills/uca-informes-calidad`).

Desde octubre de 2026 las evaluaciones siguen el
[procedimiento sistemático](evaluacion/procedimiento.md): un título por ejecución, rúbrica
cerrada, autocotejo más segundo corrector de otra familia de modelos y métricas calculadas
por `tools/evaluacion/evaluacion.py`. Las evals 1-3 se han migrado como línea base
E01-GII, E02-GIA y E03-GIDIDP (`evals/ejecuciones/`), y su historial está en
`evals/historial.md`.

## Método

Cada evaluación es un título de la ESI cuyo autoinforme de seguimiento del curso 2024/25
(convocatoria 2026) ya había elaborado y aprobado la coordinación. Se ejecutó la skill en
Claude Desktop y se pidió a la IA que cotejara su borrador con el documento humano.

Sus documentos están ahora en la estructura del procedimiento:

| Ubicación | Contenido |
|---|---|
| `evals/casos/<id>/entrada/` | Documentos aportados a la IA (autoinforme 23/24, memoria verificada, informe ACCUA en GIA). Los indicadores los extrajo la IA de LinceBI. |
| `evals/casos/<id>/referencia/` | Autoinforme aprobado por la CGC (referencia). |
| `evals/ejecuciones/E0n-<id>/` | Borrador `.docx` generado y cotejo original redactado por la propia IA (`cotejo-original.*`). En E02 se conserva también el borrador corregido tras el cotejo. |

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

### Línea base con la rúbrica (v2)

El 3 de octubre de 2026 el segundo corrector (B, `gpt-6.1-sol`) puntuó E01-E03 con la
rúbrica v2. Escala 0-2; D4-D7 obtuvieron 1 en los tres títulos.

| Ejecución | D1 | D2 | D3 | Media | Bloqueantes | Discrepancias S | Pendiente de revisión |
|---|---|---|---|---|---|---|---|
| E01-GII | 0 | 0 | 0 | 0,57 | B1, B2, B3 | 13 | 5 |
| E02-GIA | 2 | 0 | 1 | 1,00 | B2, B3 | 13 | 8 |
| E03-GIDIDP | 2 | 2 | 1 | 1,29 | B1, B2, B3 | 12 | 8 |

B3 aparece en todas porque no se registró el entorno (E02 usó además `datapru`). En D2, B
comprobó celda a celda menos del 80 % de coincidencia en E01 y E02 (series del título
copiadas en las tablas del centro y filas vacías), frente al 97 % que daba la métrica
automática, que desde entonces se presenta solo como cota superior.

Lecciones candidatas observadas en los tres títulos (pendientes de comprobar con la skill
actual en E04-E06 antes de incorporarlas):

| # | Lección candidata |
|---|---|
| C1 | Identificar cada valor por indicador, ámbito (título/centro) y curso; no completar series del centro con las del título. |
| C2 | Comprobar que cifras, comparaciones y adjetivos de evolución del texto coinciden con las tablas y con toda la serie. |
| C3 | Distinguir propuestas de actuaciones ejecutadas: una acción del plan anterior no pasa a hecho sin evidencia. Persiste en E04 → incorporada como L16. |
| C4 | Conciliar recomendaciones de ACCUA y puntos débiles con el plan de mejora, conservando referencias, responsables y plazos. |
| C5 | No dar por completo un anexo vacío o con solo un enlace; extraer lo disponible o marcarlo pendiente. |
| C6 | Revisar instrucciones y marcadores en todo el documento, incluidas tablas y portada. Persiste en E04 → incorporada como L17. |

### E04: GII con la skill actual

Primera ejecución completa del procedimiento (A `claude-opus-5.5` y B `gpt-6.1-sol`,
LinceBI `data.uca.es` el 3 de octubre de 2026). Media 1,43 frente a 0,57 en E01; D1-D3 pasan
de 0 a 2; desaparecen B2 y B3; las discrepancias S bajan de 13 a 7. Persisten C3 (B1:
actuaciones propuestas descritas como hechas) y C6, y aparece una habilitación profesional
deducida de las competencias en contra de la memoria. C1, C2, C4 y C5 no se repiten de forma
grave en E04; siguen como candidatas hasta E05-E06.

### E05: GIA con L16-L18

LinceBI cayó dos veces durante la extracción por un fallo del servidor MCP con llamadas
simultáneas (corregido en `lincebi-mcp`); la extracción se completó en dos tramos. Media
1,43, igual que E04; D1, D2 y D5 = 2; B1 por un texto modelo en negro conservado («se
imparte en varias modalidades») pese a L16. L17 funciona, pero vaciaba los encabezados
en azul de la tabla de calificaciones del 6.3: corregido el 3-10-2026 (las etiquetas
cortas en azul de las tablas se conservan). L18 sin incidencias. Se confirman en un segundo
título C2, C4 y C5 y el uso ambiguo de guiones de E04, que pasan a L19-L22.

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
| L16 | Propuesta no es hecho: acciones, recomendaciones y texto modelo no se describen como realizados sin evidencia | E03, E04 | Incorporada el 3-10-2026 (`guia-redaccion.md`, principios y checklist; `SKILL.md`, verificación); validar en E05 |
| L17 | La depuración cubre celdas de tablas y párrafos mixtos y conserva los `[PENDIENTE]` | E01-E04 | Incorporada el 3-10-2026 (`scripts/depurar_instrucciones.py`, `SKILL.md` 4b, checklist); validar en E05 |
| L18 | La habilitación profesional y demás datos de identidad se toman de la memoria | E04 (norma: memoria) | Incorporada el 3-10-2026 (`guia-redaccion.md`); sin incidencias en E05 |
| L16b | Refuerzo de L16: releer el texto modelo conservado en negro y contrastarlo con la memoria | E03-E05 | Incorporada el 3-10-2026 (`guia-redaccion.md`, checklist 11; `SKILL.md`, verificación); validar en E06 |
| L19 | Cero no es «sin dato»: sin guiones ambiguos; buscar en la entrada antes de dejar pendiente | E04, E05 | Incorporada el 3-10-2026 (`guia-redaccion.md`, checklist 12; `SKILL.md`); validar en E06 |
| L20 | Anexos con fuente en LinceBI extraídos del informe previsto; un agregado o enlace genérico no basta (C5) | E01-E03, E05 | Incorporada el 3-10-2026 (`guia-redaccion.md`, checklist 12); validar en E06 |
| L21 | Recomendaciones de informes ACCUA anteriores declaradas abiertas, con número y fecha (C4) | E01-E03, E05 | Incorporada el 3-10-2026 (`guia-redaccion.md`, plan de mejora y checklist 13); validar en E06 |
| L22 | Concluir solo lo que mide el indicador; sin generalizar sin comprobar (C2) | E01-E03, E05 | Incorporada el 3-10-2026 (`guia-redaccion.md`, checklist 14); validar en E06 |

## Limitaciones de las evals 1-3 y cómo las resuelve el procedimiento

| Limitación | Respuesta del procedimiento |
|---|---|
| **Sin rúbrica común.** Cada cotejo tiene un formato y una profundidad distintos (la eval 1 es un párrafo; la 3, un informe con tablas). | Rúbrica cerrada D1-D7 y plantilla de cotejo fija; al cambiar la rúbrica se vuelven a puntuar las ejecuciones anteriores. |
| **Autoevaluación.** La misma IA genera y juzga y, en la eval 1, modificó la skill sin revisión humana. | Se mantiene el autocotejo (A) y se añade un corrector independiente de otra familia (B); solo el responsable aprueba cambios en la skill. |
| **Referencia imperfecta.** El autoinforme humano contiene errores (evals 2 y 3). | Causa **H** en las discrepancias: no penaliza y queda pendiente de revisión experta. |
| **Datos no reproducibles.** LinceBI cambia entre marzo y julio, y no se registró entorno ni fecha. | La ficha registra host y fecha de extracción; `datapru` es bloqueante (B3); las diferencias por volatilidad son causa **D**. |
| **Cobertura.** Solo seguimiento de grados de la ESI. | Catálogo `docs/evaluacion/casos.csv`; el siguiente título se elige por variedad (otro centro, máster, renovación). |
| **Fuga de casos en la skill.** `references/estilo-y-ejemplos.md` contiene ejemplos tomados de los autoinformes de la ESI que se usan como referencia (`medir` detecta 121 frases exclusivas de los tres casos), lo que puede inflar sus notas. | Aviso automático de huellas en `medir`. Resuelto el 3 de octubre de 2026: los extractos se sustituyeron por otros de GIM (excluido de la evaluación) o por plantillas con marcadores. La línea base E01-E03 se obtuvo con la skill anterior y es optimista; E04 medirá ya la skill sin fuga. |

## Cómo añadir una evaluación

Sigue [docs/evaluacion/procedimiento.md](evaluacion/procedimiento.md).
