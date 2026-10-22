# Lecciones de la evaluación de la skill de autoinformes

Registro versionado de lo que ha enseñado la evaluación de `skills/uca-informes-calidad`
frente a autoinformes reales: versiones de la skill y estado de cada lección. Aquí solo se
anotan lecciones generalizadas y la sigla de la ejecución (E01, E02…) que las origina o
valida; los resultados de cada ejecución están en `evals/historial.md` (solo local).

Cada ejecución sigue el [procedimiento de evaluación](PROCEDIMIENTO.md), que también define
[cómo se actualiza este documento](PROCEDIMIENTO.md#paso-6-registro-y-decisión-del-responsable)
y [los estados de una lección](PROCEDIMIENTO.md#después-de-la-ejecución-aplicar-lecciones).

## Versiones de la skill

v0 y v1 son la skill anterior (`old-skills/`, solo local), por eso no tienen commit.

| Versión | Commit | Cambios | Evaluada en |
|---|---|---|---|
| v0 | — | Skill anterior, inicial (línea base) | E01-GII |
| v1 | — | Skill anterior, modificada tras E01 (línea base) | E02-GIA, E03-GIDIDP |
| v2 | `d5ed099` | Skill nueva (`skills/uca-informes-calidad/`), con L4-L14 | E04-GII |
| v3 | `a3157b3` | + L16-L18 | E05-GIA |
| v4 | `2816f9e` | + L16b, L19-L22 | E06-GIDIDP |
| v5 | `4e6da0d` | + L23-L27 | E07-GH |
| v6 | `6f9f6cf` | + L11b, L28 | E08-GHUM |

Versión vigente: **v6** (`6f9f6cf`).

## Lecciones y estado en la skill

### Lecciones incorporadas

Rutas relativas a `skills/uca-informes-calidad/`; «checklist n» es el punto n de la lista de
verificación de `guia-redaccion.md`. Una lección insuficiente sigue en la skill hasta que el
responsable apruebe su refuerzo.

| # | Lección | Origen | Dónde está en la skill | Estado |
|---|---|---|---|---|
| L1 | Incluir el análisis de calificaciones por asignatura (6.3, `PorcentajeCalificaciones`) | E01 | `SKILL.md`, `estilo-y-ejemplos.md` | Incorporada |
| L2 | P01-03 (PTGAS) se analiza a nivel de centro | E01 | `estilo-y-ejemplos.md` | Incorporada |
| L3 | Objetivos de la memoria (§8.1) en tabla, respetando la tasa a la que se asocia cada uno | E01, E03 | `estilo-y-ejemplos.md` | Incorporada |
| L4 | Extraer de producción (`data.uca.es`), no de pruebas (`datapru.uca.es`) | E01, E02 | `SKILL.md` (comprobación del host antes de extraer y parada si es pruebas); el script avisa si `extraccion.entorno` es `datapru` | Incorporada el 2-10-2026; validada en E04 (producción comprobada y sin B3 en E04-E07) |
| L5 | Extraer toda la serie en vivo; el autoinforme anterior solo para columnas fuera de la ventana de cinco cursos y valores incoherentes | E03 | `mapa-indicadores-lincebi.md` («Regla de la serie histórica»), `SKILL.md` | Incorporada el 2-10-2026; validada en E04 (D2 = 2 en E04-E07) |
| L6 | Registrar entorno y fecha de extracción; advertir de la volatilidad de P04-05 | E02, E03 | Bloque `extraccion` del JSON; el script avisa si falta | Incorporada el 2-10-2026; validada en E04 |
| L7 | Ningún indicador de satisfacción por encima de 5; misma alineación de cohortes en título y centro | E03 | Aviso del script, comprobaciones del mapa y checklist | Incorporada el 2-10-2026; validada en E04 (sin B2 ni cohortes desalineadas en E04-E07) |
| L8 | Egresados: cinco últimas cohortes con datos (conv. 2026: `2019-20 … 2023-24`), análisis de la cohorte más reciente, nº de encuestas y egresados | E03 | El script reetiqueta las cabeceras de la plantilla con `anios_egresados` | Incorporada el 2-10-2026 por decisión del responsable; validada en E04 |
| L9 | Entre 1 y 5 puntos débiles en total, solo los asumibles con acción propia | E03 (y recuento de E02) | `SKILL.md`, `guia-redaccion.md`, `estilo-y-ejemplos.md` | Incorporada el 2-10-2026; validada en E04 (entre 2 y 4 PD en E04-E07) |
| L10 | Pedir al centro desde el inicio los datos internos (doble título, prácticas, convenios, tutores, créditos reconocidos, primer curso, rutas UCADrive) | E02, E03 | `SKILL.md`, `mapa-indicadores-lincebi.md` | Incorporada el 2-10-2026; sin evidencia: la evaluación no la ejercita, porque A no puede preguntar |
| L11 | Créditos reconocidos desde LinceBI | E02 | — (sustituida por L11b) | Incorporada el 2-10-2026; insuficiente en E04 (LinceBI no publica ese informe; confirmado en E05-E07) → L11b |
| L11b | Reformulación de L11: créditos reconocidos del curso como dato del centro; si el autoinforme anterior cita su fuente, reproducirla en el `[PENDIENTE]` | E04-E07 | `mapa-indicadores-lincebi.md` («Datos que no están en LinceBI»), `SKILL.md`, `estructura-autoinforme.md` | Incorporada el 4-10-2026; validada en E08 (reconocimientos del curso pedidos al centro como dato interno) |
| L12 | Composición de la CGC: remitir a la web del título | E02 | `SKILL.md`, `estilo-y-ejemplos.md`, `estructura-autoinforme.md` | Incorporada el 2-10-2026; validada en E04 |
| L13 | Evidencias en el seguimiento: rutas UCADrive por criterio y curso; enlaces externos para los Anexos II y IV | E03 | `estructura-autoinforme.md` | Incorporada el 2-10-2026; sin incidencias en E04; insuficiente en E06 (sin rutas ni marcadores de evidencias por criterio); sin incidencias en E07 |
| L14 | Conservar la numeración original de las recomendaciones ACCUA | E03 | `SKILL.md`, `estilo-y-ejemplos.md` | Incorporada el 2-10-2026; validada en E04 |
| L15 | Responsables y fechas concretos en el plan de mejora | E01 | Documento opcional «plan de mejora vivo» | Incorporada |
| L16 | Propuesta no es hecho: acciones, recomendaciones y texto modelo no se describen como realizados sin evidencia (C3) | E01-E04 | `guia-redaccion.md` (principios y checklist), `SKILL.md` (verificación) | Incorporada el 3-10-2026; insuficiente en E05 (texto modelo en negro conservado) → L16b |
| L16b | Refuerzo de L16: releer el texto modelo conservado en negro y contrastarlo con la memoria | E03-E05 | `guia-redaccion.md` (checklist 11), `SKILL.md` (verificación) | Incorporada el 3-10-2026; validada en E06 |
| L17 | La depuración cubre celdas de tablas y párrafos mixtos y conserva los `[PENDIENTE]` (C6) | E01-E04 | `scripts/depurar_instrucciones.py`, `SKILL.md` (paso 4b), checklist | Incorporada el 3-10-2026; validada en E05, tras corregir que vaciaba las etiquetas cortas en azul de las tablas |
| L18 | La habilitación profesional y demás datos de identidad se toman de la memoria | E04 (norma: memoria) | `guia-redaccion.md` | Incorporada el 3-10-2026; validada en E05 |
| L19 | Cero no es «sin dato»: sin guiones ambiguos; buscar en la entrada antes de dejar pendiente | E04, E05 | `guia-redaccion.md` (checklist 12), `SKILL.md` | Incorporada el 3-10-2026; validada en E06; insuficiente en E07 (guiones como 0 %; pendientes con dato en la entrada) y en E08 (guiones narrados como ausencia de actividad) |
| L20 | Anexos con fuente en LinceBI extraídos del informe previsto; un agregado o enlace genérico no basta (C5) | E01-E03, E05 | `guia-redaccion.md` (checklist 12) | Incorporada el 3-10-2026; insuficiente en E06 (Anexo IV con solo una selección) → L26 |
| L21 | Recomendaciones de informes ACCUA anteriores declaradas abiertas, con número y fecha (C4) | E01-E03, E05 | `guia-redaccion.md` (plan de mejora y checklist 13) | Incorporada el 3-10-2026; validada en E06 |
| L22 | Concluir solo lo que mide el indicador; sin generalizar sin comprobar (C2) | E01-E03, E05 | `guia-redaccion.md` (checklist 14) | Incorporada el 3-10-2026; insuficiente en E06 → L23 |
| L23 | Refuerzo de L22: adjetivos de evolución contrastados con toda la serie; objetivos de la memoria solo con su tasa, en todas las apariciones | E01-E03, E05, E06 | `guia-redaccion.md` (checklist 14) | Incorporada el 3-10-2026; insuficiente en E07 (evolución del centro con el signo cambiado; los objetivos de la memoria, correctos) y en E08 («mayoritariamente» con menos de la mitad; causa de una evolución atribuida sin fuente) |
| L24 | Contrastar los cursos comunes con el autoinforme anterior; sin analizar la evolución si hay diferencias sistemáticas | E05, E06 | `guia-redaccion.md` (principios y checklist 15) | Incorporada el 3-10-2026; validada en E07 |
| L25 | Ampliación de L16: estado conocido solo por el autoinforme anterior no es vigente; sin juzgar la eficacia sin implantación acreditada | E04, E06 | `guia-redaccion.md` | Incorporada el 3-10-2026; insuficiente en E07 (eficacia juzgada sin implantación acreditada) y en E08 (actividad del curso afirmada sin evidencia) |
| L26 | Refuerzo de L20: anexo completo o con enlace específico al informe íntegro, nunca condicionado | E01-E03, E06 | `guia-redaccion.md` | Incorporada el 3-10-2026; validada en E07 |
| L27 | Verificar restos de plantilla en negro: notas de cumplimentación, opciones alternativas, filas de ejemplo, enlaces pegados | E05, E06 | `guia-redaccion.md` (checklist 16), `SKILL.md` | Incorporada el 3-10-2026; insuficiente en E07 (notas de cumplimentación en la tabla del Anexo II) y en E08 (marcadores de plantilla y opciones alternativas en negro) |
| L28 | Resultados globales del 6.3 con seis cursos: el más antiguo, fuera de la ventana de LinceBI, del autoinforme anterior (C9) | E04, E05, E07 | `mapa-indicadores-lincebi.md` (años y regla de la serie histórica), `SKILL.md`, `estructura-autoinforme.md`, `guia-redaccion.md` (checklist 2) | Incorporada el 4-10-2026; validada en E08 (seis cursos, los dos más antiguos del autoinforme anterior) |

### Lecciones candidatas

Observadas en un solo título o sin respaldo suficiente según el
[filtro de admisión](PROCEDIMIENTO.md#reglas-contra-el-sobreajuste), por lo que aún no están en
la skill. Las que ya se incorporaron conservan su fila y remiten a su lección.

| # | Lección candidata | Observada en | Estado |
|---|---|---|---|
| C1 | Identificar cada valor por indicador, ámbito (título/centro) y curso; no completar series del centro con las del título | E01-E03 | Candidata: no se repite de forma grave desde E04 |
| C2 | Comprobar que cifras, comparaciones y adjetivos de evolución del texto coinciden con las tablas y con toda la serie | E01-E03, E05 | Incorporada como L22 |
| C3 | Distinguir propuestas de actuaciones ejecutadas: una acción del plan anterior no pasa a hecho sin evidencia | E01-E04 | Incorporada como L16 |
| C4 | Conciliar recomendaciones de ACCUA y puntos débiles con el plan de mejora, conservando referencias, responsables y plazos | E01-E03, E05 | Incorporada como L21 |
| C5 | No dar por completo un anexo vacío o con solo un enlace; extraer lo disponible o marcarlo pendiente | E01-E03, E05 | Incorporada como L20 |
| C6 | Revisar instrucciones y marcadores en todo el documento, incluidas tablas y portada | E01-E04 | Incorporada como L17 |
| C7 | Una fila por recomendación de ACCUA, aunque el informe no las numere | E07 | Candidata |
| C8 | Causas explicativas sin fuente redactadas como hipótesis | E07, E08 | Candidata: repetida en un segundo título; pendiente de decisión |
| C9 | Completar los seis cursos de resultados globales del 6.3 con el autoinforme anterior cuando LinceBI solo ofrece cinco | E04, E05, E07 | Incorporada como L28 |
| C10 | Comprobar el cálculo que respalda «mayoritariamente», «suficiente» y adjetivos semejantes | E08 | Candidata (afín a L23) |
| C11 | Agotar el informe que indica el mapa antes de declarar interna una tabla de un anexo | E08 | Candidata (afín a L20 y L26) |
| C12 | Cruzar «No procede» con la identificación del título (itinerarios, modalidades, menciones) | E08 | Candidata |
| C13 | Síntesis de sostenibilidad (7.6) con todos sus elementos: inserción, recursos y conclusión explícita | E08 | Candidata |
| C14 | Fechas del plan de mejora redactadas como propuesta, no como acordadas, y sin inicios anteriores a la redacción | E08 | Candidata |
| C15 | `rellenar_autoinforme.py` no debe avisar de escala 0-5 en las tasas de respuesta (P07-01), cuya etiqueta contiene «satisfacción» pero son porcentajes | E08 | Candidata (herramienta) |
| C16 | `depurar_instrucciones.py` deja en negro los restos de instrucciones mixtas («Rellenar solo en su caso: …», rutas de LinceBI de los anexos): avisar en el paso 4b o tratarlos en el script | E08 | Candidata (herramienta; afín a L17 y L27) |
