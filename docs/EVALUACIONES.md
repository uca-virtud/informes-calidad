# Evaluaciones de la skill de autoinformes

Registro versionado de las pruebas de `skills/uca-informes-calidad` frente a autoinformes
reales de las coordinaciones: resultados de cada ejecución y estado de las lecciones en la
skill. Los datos completos están en `evals/` (solo local); aquí solo se anotan cifras
agregadas y lecciones generalizadas.

Cada ejecución sigue el [procedimiento de evaluación](PROCEDIMIENTO.md), que también define
[cómo se actualiza este documento](PROCEDIMIENTO.md#paso-6-registro-y-decisión-del-responsable)
y [los estados de una lección](PROCEDIMIENTO.md#después-de-la-ejecución-aplicar-lecciones).

## Resumen de la serie

Notas de B con la rúbrica v2 (escala 0-2, media de D1-D7).

| Ejecución | Skill | Media | Bloqueantes |
|---|---|---|---|
| E01-GII | v0: anterior, inicial (línea base) | 0,57 | B1, B2, B3 |
| E02-GIA | v0.1: anterior, modificada tras E01 (línea base) | 1,00 | B2, B3 |
| E03-GIDIDP | v0.1: anterior, modificada tras E01 (línea base) | 1,29 | B1, B2, B3 |
| [E04-GII](#e04-gii-con-la-skill-actual) | v1 (`d5ed099`): actual | 1,43 | B1 |
| [E05-GIA](#e05-gia-con-l16-l18) | v2 (`a3157b3`): + L16-L18 | 1,43 | B1 |
| [E06-GIDIDP](#e06-gididp-con-l16b-y-l19-l22) | v3 (`2816f9e`): + L16b, L19-L22 | 1,57 | — |
| [E07-GH](#e07-gh-con-l23-l27) | v4 (`4e6da0d`): + L23-L27 | 1,57 | B1 |

Versión vigente, pendiente de evaluar: v5 (`6f9f6cf`): + L11b, L28. Cada versión nueva de la
skill recibe el siguiente número y se anota aquí con su commit.

Con la skill actual la media sube de 0,57-1,29 a 1,43-1,57 y los bloqueantes bajan de dos o
tres por caso a uno o ninguno.

## Lecciones y estado en la skill

### Lecciones incorporadas

Rutas relativas a `skills/uca-informes-calidad/`; «checklist n» es el punto n de la lista de
verificación de `guia-redaccion.md`.

| # | Lección | Origen | Dónde está en la skill | Estado |
|---|---|---|---|---|
| L1 | Incluir el análisis de calificaciones por asignatura (6.3, `PorcentajeCalificaciones`) | Eval 1 | `SKILL.md`, `estilo-y-ejemplos.md` | Incorporada |
| L2 | P01-03 (PTGAS) se analiza a nivel de centro | Eval 1 | `estilo-y-ejemplos.md` | Incorporada |
| L3 | Objetivos de la memoria (§8.1) en tabla, respetando la tasa a la que se asocia cada uno | Evals 1 y 3 | `estilo-y-ejemplos.md` | Incorporada |
| L4 | Extraer de producción (`data.uca.es`), no de pruebas (`datapru.uca.es`) | Evals 1 y 2 | `SKILL.md` (comprobación del host antes de extraer y parada si es pruebas); el script avisa si `extraccion.entorno` es `datapru` | Incorporada el 2-10-2026; validada en E04 (producción comprobada y sin B3 en E04-E07) |
| L5 | Extraer toda la serie en vivo; el autoinforme anterior solo para columnas fuera de la ventana de cinco cursos y valores incoherentes | Eval 3 | `mapa-indicadores-lincebi.md` («Regla de la serie histórica»), `SKILL.md` | Incorporada el 2-10-2026; validada en E04 (D2 = 2 en E04-E07) |
| L6 | Registrar entorno y fecha de extracción; advertir de la volatilidad de P04-05 | Evals 2 y 3 | Bloque `extraccion` del JSON; el script avisa si falta | Incorporada el 2-10-2026; validada en E04 |
| L7 | Ningún indicador de satisfacción por encima de 5; misma alineación de cohortes en título y centro | Eval 3 | Aviso del script, comprobaciones del mapa y checklist | Incorporada el 2-10-2026; validada en E04 (sin B2 ni cohortes desalineadas en E04-E07) |
| L8 | Egresados: cinco últimas cohortes con datos (conv. 2026: `2019-20 … 2023-24`), análisis de la cohorte más reciente, nº de encuestas y egresados | Eval 3 | El script reetiqueta las cabeceras de la plantilla con `anios_egresados` | Incorporada el 2-10-2026 por decisión del responsable; validada en E04 |
| L9 | Entre 1 y 5 puntos débiles en total, solo los asumibles con acción propia | Eval 3 (y recuento de la 2) | `SKILL.md`, `guia-redaccion.md`, `estilo-y-ejemplos.md` | Incorporada el 2-10-2026; validada en E04 (entre 2 y 4 PD en E04-E07) |
| L10 | Pedir al centro desde el inicio los datos internos (doble título, prácticas, convenios, tutores, créditos reconocidos, primer curso, rutas UCADrive) | Evals 2 y 3 | `SKILL.md`, `mapa-indicadores-lincebi.md` | Incorporada el 2-10-2026; sin evidencia: la evaluación no la ejercita, porque A no puede preguntar |
| L11 | Créditos reconocidos desde LinceBI | Eval 2 | Sustituida por L11b | Incorporada el 2-10-2026; insuficiente en E04 (LinceBI no publica ese informe; confirmado en E05-E07): → L11b |
| L11b | Reformulación de L11: créditos reconocidos del curso como dato del centro; si el autoinforme anterior cita su fuente, reproducirla en el `[PENDIENTE]` | E04-E07 | `mapa-indicadores-lincebi.md` («Datos que no están en LinceBI»), `SKILL.md`, `estructura-autoinforme.md` | Incorporada el 4-10-2026; validar en E08 |
| L12 | Composición de la CGC: remitir a la web del título | Eval 2 | `SKILL.md`, `estilo-y-ejemplos.md`, `estructura-autoinforme.md` | Incorporada el 2-10-2026; validada en E04 |
| L13 | Evidencias en el seguimiento: rutas UCADrive por criterio y curso; enlaces externos para los Anexos 2 y 4 | Eval 3 | `estructura-autoinforme.md` | Incorporada el 2-10-2026; insuficiente en E06 (sin rutas ni marcadores de evidencias por criterio); sin incidencias en E04 y E07 |
| L14 | Conservar la numeración original de las recomendaciones ACCUA | Eval 3 | `SKILL.md`, `estilo-y-ejemplos.md` | Incorporada el 2-10-2026; validada en E04 |
| L15 | Responsables y fechas concretos en el plan de mejora | Eval 1 | Documento opcional «plan de mejora vivo» | Incorporada |
| L16 | Propuesta no es hecho: acciones, recomendaciones y texto modelo no se describen como realizados sin evidencia (C3) | E03, E04 | `guia-redaccion.md` (principios y checklist), `SKILL.md` (verificación) | Incorporada el 3-10-2026; insuficiente en E05 (texto modelo en negro conservado) → L16b |
| L16b | Refuerzo de L16: releer el texto modelo conservado en negro y contrastarlo con la memoria | E03-E05 | `guia-redaccion.md` (checklist 11), `SKILL.md` (verificación) | Incorporada el 3-10-2026; validada en E06 |
| L17 | La depuración cubre celdas de tablas y párrafos mixtos y conserva los `[PENDIENTE]` (C6) | E01-E04 | `scripts/depurar_instrucciones.py`, `SKILL.md` (paso 4b), checklist | Incorporada el 3-10-2026; validada en E05, tras corregir que vaciaba las etiquetas cortas en azul de las tablas |
| L18 | La habilitación profesional y demás datos de identidad se toman de la memoria | E04 (norma: memoria) | `guia-redaccion.md` | Incorporada el 3-10-2026; validada en E05 |
| L19 | Cero no es «sin dato»: sin guiones ambiguos; buscar en la entrada antes de dejar pendiente | E04, E05 | `guia-redaccion.md` (checklist 12), `SKILL.md` | Incorporada el 3-10-2026; validada en E06; insuficiente en E07 (guiones como 0 %; pendientes con dato en la entrada) |
| L20 | Anexos con fuente en LinceBI extraídos del informe previsto; un agregado o enlace genérico no basta (C5) | E01-E03, E05 | `guia-redaccion.md` (checklist 12) | Incorporada el 3-10-2026; insuficiente en E06 (Anexo IV con solo una selección) → L26 |
| L21 | Recomendaciones de informes ACCUA anteriores declaradas abiertas, con número y fecha (C4) | E01-E03, E05 | `guia-redaccion.md` (plan de mejora y checklist 13) | Incorporada el 3-10-2026; validada en E06 |
| L22 | Concluir solo lo que mide el indicador; sin generalizar sin comprobar (C2) | E01-E03, E05 | `guia-redaccion.md` (checklist 14) | Incorporada el 3-10-2026; insuficiente en E06 → L23 |
| L23 | Refuerzo de L22: adjetivos de evolución contrastados con toda la serie; objetivos de la memoria solo con su tasa, en todas las apariciones | E01-E03, E05, E06 | `guia-redaccion.md` (checklist 14) | Incorporada el 3-10-2026; insuficiente en E07 (evolución del centro con el signo cambiado; los objetivos de la memoria, correctos) |
| L24 | Contrastar los cursos comunes con el autoinforme anterior; sin analizar la evolución si hay diferencias sistemáticas | E05, E06 | `guia-redaccion.md` (principios y checklist 15) | Incorporada el 3-10-2026; validada en E07 |
| L25 | Ampliación de L16: estado conocido solo por el autoinforme anterior no es vigente; sin juzgar la eficacia sin implantación acreditada | E04, E06 | `guia-redaccion.md` | Incorporada el 3-10-2026; insuficiente en E07 (eficacia juzgada sin implantación acreditada) |
| L26 | Refuerzo de L20: anexo completo o con enlace específico al informe íntegro, nunca condicionado | E01-E03, E06 | `guia-redaccion.md` | Incorporada el 3-10-2026; validada en E07 |
| L27 | Verificar restos de plantilla en negro: notas de cumplimentación, opciones alternativas, filas de ejemplo, enlaces pegados | E05, E06 | `guia-redaccion.md` (checklist 16), `SKILL.md` | Incorporada el 3-10-2026; insuficiente en E07 (notas de cumplimentación en la tabla del Anexo II) |
| L28 | Resultados globales del 6.3 con seis cursos: el más antiguo, fuera de la ventana de LinceBI, del autoinforme anterior (C9) | E04, E05, E07 | `mapa-indicadores-lincebi.md` (años y regla de la serie histórica), `SKILL.md`, `estructura-autoinforme.md`, `guia-redaccion.md` (checklist 2) | Incorporada el 4-10-2026; validar en E08 |

### Lecciones candidatas

Observadas en un título o sin respaldo suficiente según el
[filtro de admisión](PROCEDIMIENTO.md#reglas-contra-el-sobreajuste); aún no están en la skill.

| # | Lección candidata | Observada en | Estado |
|---|---|---|---|
| C1 | Identificar cada valor por indicador, ámbito (título/centro) y curso; no completar series del centro con las del título | E01-E03 | Candidata: no se repite de forma grave desde E04 |
| C2 | Comprobar que cifras, comparaciones y adjetivos de evolución del texto coinciden con las tablas y con toda la serie | E01-E03, E05 | Incorporada como L22 |
| C3 | Distinguir propuestas de actuaciones ejecutadas: una acción del plan anterior no pasa a hecho sin evidencia | E01-E04 | Incorporada como L16 |
| C4 | Conciliar recomendaciones de ACCUA y puntos débiles con el plan de mejora, conservando referencias, responsables y plazos | E01-E03, E05 | Incorporada como L21 |
| C5 | No dar por completo un anexo vacío o con solo un enlace; extraer lo disponible o marcarlo pendiente | E01-E03, E05 | Incorporada como L20 |
| C6 | Revisar instrucciones y marcadores en todo el documento, incluidas tablas y portada | E01-E04 | Incorporada como L17 |
| C7 | Una fila por recomendación de ACCUA, aunque el informe no las numere | E07 | Candidata |
| C8 | Causas explicativas sin fuente redactadas como hipótesis | E07 | Candidata |
| C9 | Completar los seis cursos de resultados globales del 6.3 con el autoinforme anterior cuando LinceBI solo ofrece cinco | E04, E05, E07 | Incorporada como L28 |

## Ejecuciones

### E04: GII con la skill actual

Primera ejecución completa del procedimiento (A `claude-opus-5.5` y B `gpt-6.1-sol`,
LinceBI `data.uca.es` el 3 de octubre de 2026). Media 1,43 frente a 0,57 en E01; D1-D3 pasan
de 0 a 2; desaparecen B2 y B3; las discrepancias S bajan de 13 a 7. Persisten C3 (B1:
actuaciones propuestas descritas como hechas) y C6, y aparece una habilitación profesional
deducida de las competencias en contra de la memoria. C1, C2, C4 y C5 no se repiten de forma
grave.

### E05: GIA con L16-L18

LinceBI cayó dos veces durante la extracción por un fallo del servidor MCP con llamadas
simultáneas (corregido en `lincebi-mcp`); la extracción se completó en dos tramos. Media
1,43, igual que E04; D1, D2 y D5 = 2. B1 por un texto modelo en negro conservado («se
imparte en varias modalidades») pese a L16. L17 funciona, pero vaciaba los encabezados en
azul de la tabla de calificaciones del 6.3: corregido el 3-10-2026 (las etiquetas cortas en
azul de las tablas se conservan). L18 sin incidencias. Se confirman en un segundo título C2,
C4 y C5 y el uso ambiguo de guiones de E04, que pasan a L19-L22.

### E06: GIDIDP con L16b y L19-L22

Sin incidencias con LinceBI tras la corrección del servidor. Media 1,57, sin bloqueantes;
D1, D2, D5 y D6 = 2. Funcionan L16b, L19 y L21. L20 y L22 se cumplen a medias: Anexo IV
solo con una selección «a completar si se requiere», adjetivos de evolución que la serie no
respalda y un objetivo de la memoria aplicado a otra tasa en un punto fuerte. Pasan a
L23-L27 las lecciones repetidas en dos títulos.

### E07: GH con L23-L27

Primer título fuera de la ESI (Facultad de Filosofía y Letras). Sin incidencias con LinceBI,
aunque no expone la relación nominal del PDI ni informes de créditos reconocidos o de
resultados de primer curso. Media 1,57, igual que E06; D1, D2, D5 y D6 = 2; D3, D4 y D7 = 1.
Extensión del 35 % frente a una referencia mucho más larga que las de la ESI, con 77
`[PENDIENTE]`. B1 porque los guiones de LinceBI se consignaron como 0 % y uno se narró como
ausencia de actividad, en contra de L19.

Funcionan L24 (series discrepantes con el autoinforme anterior advertidas sin analizar su
evolución), L26 (Anexo IV completo) y la parte de L23 sobre objetivos de la memoria. Se
quedan cortas L19 (también deja pendientes datos disponibles en la memoria y el autoinforme
anterior), L23 (una evolución del centro descrita con el signo cambiado), L25 (eficacia de
acciones juzgada sin implantación acreditada) y L27 (notas de cumplimentación en la tabla del
Anexo II). Nuevas candidatas, solo en este título: C7 y C8. `medir` avisa de tres frases de
la skill compartidas con referencias de casos (GH y GIDIDP), pendientes de revisar.

Decisión del responsable: pendiente.

## Antecedentes: evals 1-3 y línea base

### Método de las evals 1-3

Antes del procedimiento, cada evaluación fue un título de la ESI cuyo autoinforme de
seguimiento del curso 2024/25 (convocatoria 2026) ya había elaborado y aprobado la
coordinación. Se ejecutó la skill anterior (`old-skills/autoinforme-seguimiento-uca`) en
Claude Desktop y se pidió a la IA que cotejara su borrador con el documento humano. Entre la
eval 1 y las evals 2-3 la IA modificó la skill con lo aprendido en la eval 1; esa versión es
la que se conserva en `old-skills/`.

Se migraron al procedimiento como E01-GII, E02-GIA y E03-GIDIDP:

| Ubicación | Contenido |
|---|---|
| `evals/casos/<id>/entrada/` | Documentos aportados a la IA (autoinforme 23/24, memoria verificada, informe ACCUA en GIA). Los indicadores los extrajo la IA de LinceBI. |
| `evals/casos/<id>/referencia/` | Autoinforme aprobado por la CGC (referencia). |
| `evals/ejecuciones/E0n-<id>/` | Borrador `.docx` generado y cotejo original redactado por la propia IA (`cotejo-original.*`). En E02 se conserva también el borrador corregido tras el cotejo. |

### Resultados de las evals 1-3

| Eval | Título | Datos de partida | Palabras IA / humano | PF IA / humano | PD IA / humano | `[PENDIENTE]` | Cotejo |
|---|---|---|---|---|---|---|---|
| 1 | GII | Autoinforme 23/24 + memoria | 5.518 / 26.359 (21 %) | 4 / 19 | 3 / 5 | 0 | Breve, no estructurado |
| 2 | GIA | Autoinforme 23/24 + memoria + informe ACCUA | 16.123 / 23.746 (68 %) | 20 / 14 | 14 / 4 | 6 | Medio |
| 3 | GIDIDP | Autoinforme 23/24 + memoria | 17.204 / 24.533 (70 %) | 19 / 16 | 16 / 1 | 3 | Detallado (≈230 celdas) |

PF/PD: códigos de puntos fuertes y débiles distintos encontrados en cada documento.

La eval 1 es claramente peor que la 2 y la 3: su borrador tiene una quinta parte de la
extensión del humano, apenas desarrolla puntos fuertes y no incluye el análisis de
calificaciones por asignatura. Las evals 2 y 3, ya con la skill corregida, alcanzan unos dos
tercios de la extensión humana y una coincidencia alta en estructura, identificación,
interpretaciones cualitativas e indicadores (≈91 % de las celdas del Anexo I en la eval 3).

El problema dominante cambió: en la eval 1 era **falta de contenido**; en las evals 2 y 3,
**exceso de puntos débiles** (14-16 frente a 1-4 de las coordinaciones) y **discrepancias
de datos** por la fuente y la fecha de extracción de LinceBI.

- **Eval 1 (GII).** Coinciden estructura, codificación PF/PD/AM y tasas de rendimiento,
  éxito, evaluación y abandono. Faltaba el análisis de calificaciones por asignatura (6.3).
  Graduación y eficiencia difieren por usar el entorno de pruebas (`datapru.uca.es`).
- **Eval 2 (GIA).** Coinciden las 15 recomendaciones ACCUA, los objetivos de la memoria y la
  interpretación de la baja graduación. Se repite el uso de `datapru`: graduación 16,4 %
  frente a 7,5 % real. Quedaron pendientes datos que el humano sí tenía: créditos
  reconocidos (787), prácticas curriculares (15 estudiantes) y la composición de la CGC (el
  humano remite a la web). La IA detectó un error del humano (confunde quinquenios con
  sexenios).
- **Eval 3 (GIDIDP).** Identificación 13/13. Las diferencias de datos se deben a la
  volatilidad de la tasa de graduación entre marzo y julio, a que la IA consolidó la serie
  histórica con el autoinforme anterior (la coordinación reextrae la serie en vivo) y a
  datos internos del centro (plazas del doble título, convenios, tutores). La IA detectó
  cuatro errores del humano: cohortes de egresados desplazadas un año, un valor de P04-13
  fuera de la escala 0-5, el objetivo del 50 % asignado a la tasa de éxito en vez de a la de
  rendimiento y recomendaciones ACCUA renumeradas.

### Línea base con la rúbrica v2

El 3 de octubre de 2026 B (`gpt-6.1-sol`) puntuó E01-E03 con la rúbrica v2. D4-D7 obtuvieron
1 en los tres títulos.

| Ejecución | D1 | D2 | D3 | Media | Bloqueantes | Discrepancias S | Pendiente de revisión |
|---|---|---|---|---|---|---|---|
| E01-GII | 0 | 0 | 0 | 0,57 | B1, B2, B3 | 13 | 5 |
| E02-GIA | 2 | 0 | 1 | 1,00 | B2, B3 | 13 | 8 |
| E03-GIDIDP | 2 | 2 | 1 | 1,29 | B1, B2, B3 | 12 | 8 |

B3 aparece en todas porque no se registró el entorno (E02 usó además `datapru`). En D2, B
comprobó celda a celda menos del 80 % de coincidencia en E01 y E02 (series del título
copiadas en las tablas del centro y filas vacías), frente al 97 % que daba la métrica
automática, que desde entonces se presenta solo como cota superior. De estos tres títulos
salieron las candidatas C1-C6.

La línea base es optimista: `references/estilo-y-ejemplos.md` contenía entonces ejemplos
tomados de estos tres autoinformes de referencia (`medir` detectó 121 frases exclusivas de
los tres casos). El 3 de octubre de 2026 se sustituyeron por extractos de GIM (excluido de
la evaluación) o por plantillas con marcadores, así que desde E04 se mide la skill sin esa
fuga.

### Limitaciones de las evals 1-3 y cómo las resuelve el procedimiento

| Limitación | Respuesta del procedimiento |
|---|---|
| **Sin rúbrica común.** Cada cotejo tiene un formato y una profundidad distintos (la eval 1 es un párrafo; la 3, un informe con tablas). | Rúbrica cerrada D1-D7 y plantilla de cotejo fija; al cambiar la rúbrica se vuelven a puntuar las ejecuciones anteriores. |
| **Autoevaluación.** La misma IA genera y juzga y, en la eval 1, modificó la skill sin revisión humana. | Se mantiene el autocotejo (A) y se añade un corrector independiente de otra familia (B); solo el responsable aprueba cambios en la skill. |
| **Referencia imperfecta.** El autoinforme humano contiene errores (evals 2 y 3). | Causa **H** en las discrepancias: no penaliza y queda pendiente de revisión experta. |
| **Datos no reproducibles.** LinceBI cambia entre marzo y julio, y no se registró entorno ni fecha. | La ficha registra host y fecha de extracción; `datapru` es bloqueante (B3); las diferencias por volatilidad son causa **D**. |
| **Cobertura.** Solo seguimiento de grados de la ESI. | Catálogo `evals/casos.csv`; el siguiente título se elige por variedad (otro centro, máster, renovación). |
| **Fuga de casos en la skill.** Ejemplos de la skill tomados de los autoinformes de referencia inflan sus notas. | Aviso automático de huellas en `medir` y ejemplos solo de títulos excluidos (ver «Línea base con la rúbrica v2»). |
