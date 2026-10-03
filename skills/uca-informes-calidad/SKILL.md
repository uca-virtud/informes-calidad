---
name: uca-informes-calidad
description: >-
  Ayuda a redactar y cumplimentar los autoinformes de calidad de títulos oficiales
  (Grado/Máster) de la Universidad de Cádiz según el modelo ACCUA/DEVA: el
  Autoinforme de Seguimiento y el Autoinforme Global de Renovación de la
  Acreditación. Úsala siempre que el usuario mencione "autoinforme", "seguimiento
  del título", "informe de seguimiento", "ACCUA", "DEVA", "renovación de la
  acreditación", criterios/subcriterios de calidad, indicadores ISGC (P01-P07),
  tasas de rendimiento/éxito/abandono/graduación, puntos fuertes y débiles, plan de
  mejora, o quiera rellenar las plantillas oficiales UCA. Extrae indicadores de
  LinceBI (data.uca.es), integra archivos aportados por el usuario y entrega los
  documentos en Word (.docx) respetando las plantillas oficiales.
---

# Autoinformes de calidad de títulos — Universidad de Cádiz (ACCUA/DEVA)

## Qué hace esta skill

Guía la elaboración de dos tipos de autoinforme de un título oficial de la UCA, que
comparten criterios, subcriterios, indicadores ISGC y estilo de redacción:

- **Seguimiento**: anual. Entrega un único `.docx` basado en la plantilla oficial, con
  análisis, puntos fuertes/débiles, plan de mejora y anexos.
- **Renovación de la acreditación**: analiza todo el periodo desde la última
  acreditación y se presenta en la plataforma web de ACCUA. Entrega un `.docx` por
  criterio (plantillas de la Unidad de Calidad) y un `.docx` con el Anexo I de
  indicadores, listos para volcar en la plataforma.

En ambos casos recopila los indicadores ISGC (desde LinceBI o desde archivos que aporte
el usuario), rellena de forma determinista las tablas y ayuda a redactar el análisis.

El resultado es un **borrador de trabajo** para la coordinación del título y la
Comisión de Garantía de Calidad (CGC): revisa siempre los datos y la redacción antes
de presentarlo a ACCUA.

## Cuándo usarla

Cuando el usuario pida elaborar, actualizar, revisar o cumplimentar un autoinforme de
seguimiento o de renovación de la acreditación de un grado o máster de la UCA, analizar
indicadores de calidad de un título, redactar puntos fuertes/débiles o un plan de
mejora, o rellenar las plantillas oficiales.

## Antes de empezar: tipo de informe

Pregunta primero **qué tipo de autoinforme** es (seguimiento o renovación de la
acreditación), salvo que el usuario ya lo haya dicho. Si es **renovación**, sigue
`references/estructura-renovacion.md` para la estructura, los documentos que hay que
pedir y la redacción específica; el resto de esta skill se aplica igual salvo donde
se indique.

## Datos que necesitas

Pregunta (con `AskUserQuestion` si falta) por:

1. **Título y centro**: denominación exacta del Grado/Máster, centro/s, ID Ministerio,
   curso académico de implantación, web, modalidad, si es título doble/conjunto,
   última renovación de acreditación.
2. **Curso y convocatoria** del autoinforme (p. ej. curso 2024/25, convocatoria 2026).
   Determina los años de las columnas de las tablas de indicadores.
3. **Origen de los indicadores**: LinceBI (recomendado) y/o archivos aportados por el
   usuario (Excel/PDF descargados de data.uca.es o UCADRIVE).
4. **¿Va a Seguimiento ACCUA o solo seguimiento interno?** (solo en seguimiento).
   Algunos apartados y evidencias (asignaturas representativas, TFG/TFM, pruebas de
   evaluación) solo aplican a los títulos que se presentan a ACCUA. En la renovación
   aplican siempre.

### Documentos a solicitar al usuario (paso obligatorio)

En la **renovación**, la lista de documentos es la de `references/estructura-renovacion.md`
(todos los autoinformes e informes de ACCUA del periodo). En el **seguimiento**:

LinceBI aporta lo cuantitativo (indicadores ISGC, tasas, calificaciones, personal
académico). Lo cualitativo e histórico NO está en LinceBI y hay que pedírselo al usuario.
**Al iniciar el autoinforme, solicita explícitamente estos dos documentos con
`AskUserQuestion`** (con selección múltiple):

- **El autoinforme de seguimiento del curso anterior** — *clave*. Es la fuente más útil:
  además de dar continuidad al análisis y permitir comentar la evolución, **ya contiene la
  tabla de recomendaciones de ACCUA** (con todas las subsanaciones y recomendaciones aún
  vivas) y **el plan de mejora anterior con sus acciones**. De él se extrae directamente lo
  necesario para el **Criterio 2** y el **Plan de Mejora** (arrastrando las recomendaciones
  hasta que ACCUA las dé por cerradas y los puntos débiles no resueltos).
- **La memoria verificada del título** (o su enlace web) — *clave*. Aporta los datos de la
  identificación (curso de implantación, modalidad, nº de plazas) y, sobre todo, los
  **objetivos de las tasas** (rendimiento, éxito, graduación, abandono, eficiencia) con los
  que comparar los indicadores en los **Criterios 3 y 6**.

Documentos adicionales, solo si se quiere afinar o verificar (opcionales): el **plan de
mejora vivo** del título (para responsables y fechas exactos de cada acción) y el **informe
de ACCUA** original (para confirmar que no hay recomendaciones posteriores al último
autoinforme). Suelen ser innecesarios si se dispone del autoinforme anterior.

**Pide también, en la misma pregunta inicial, los datos internos del centro** que no
están en LinceBI y que las coordinaciones sí incluyen: plazas del título doble; prácticas
curriculares (créditos y plazas ofertadas, estudiantes que las han realizado por curso,
convenios con plazas y tutores, tutores académicos con su dedicación); créditos
reconocidos y resultados de primer curso si no aparecen en LinceBI; y las rutas de
UCADrive de las evidencias de cada criterio. Lo que no se aporte queda `[PENDIENTE]`.

Para la **composición de la CGC** (criterio 2) no hace falta pedir la lista de miembros:
remite a la página de la CGC en la web del título o del centro, como hacen las
coordinaciones.

Si el usuario no aporta alguno, genera igualmente un borrador con todas las tablas de
indicadores rellenas y el análisis cuantitativo, dejando los apartados afectados marcados
como `[PENDIENTE: aportar …]` y avisando de qué ha quedado pendiente y por qué.

No inventes datos. Si un indicador o dato no está disponible, déjalo marcado como
`[PENDIENTE: …]` para que el usuario lo complete.

## Flujo de trabajo

### 1. Entender la estructura
Lee `references/estructura-autoinforme.md`. Contiene el orden exacto de criterios,
subcriterios, tablas y anexos de la plantilla, y qué se espera en cada apartado. En la
renovación, lee además `references/estructura-renovacion.md` (diferencias, plantillas por
criterio, subcriterio 2.4 y esquema del JSON).

### 2. Obtener los indicadores
Lee `references/mapa-indicadores-lincebi.md`. Mapea cada indicador ISGC a su ruta en
LinceBI y a la tabla/celda de la plantilla.

- **Desde LinceBI**: usa las herramientas `lincebi_*`. Busca el informe con
  `lincebi_search_resources` (filtra `types=["REPORT_PRD"]`), resuelve parámetros con
  `lincebi_get_report_parameters` (normalmente título/plan y curso), y extrae datos con
  `lincebi_get_report_data`. LinceBI requiere VPN/sesión UCA: si no responde, avisa al
  usuario y continúa con los archivos que aporte o deja `[PENDIENTE]`.
- **Desde archivos**: si el usuario aporta Excel/CSV/PDF, extrae los valores por
  indicador y año. Para Excel usa la skill `xlsx`; para PDF, la skill `pdf`.

Reúne los valores en un JSON de datos (ver esquema en
`references/mapa-indicadores-lincebi.md`).

**Entorno de producción obligatorio.** Antes de extraer, comprueba el host de LinceBI
(por ejemplo, en el `viewerUrl` que devuelve `lincebi_get_report_data`): debe ser
`data.uca.es`. Si es `datapru.uca.es` (pruebas), **detente** y avisa al usuario: sus
valores no son los definitivos (en las evaluaciones, la tasa de graduación llegó a
duplicarse). Registra el entorno y la fecha en el bloque `extraccion` del JSON.

**Serie en vivo.** Extrae de LinceBI todos los cursos de cada tabla, no solo el último;
usa el autoinforme anterior únicamente para las columnas que LinceBI ya no muestra y
para valores vivos incoherentes, según la "Regla de la serie histórica" del mapa. Las
cohortes de egresados son las cinco últimas con datos (convocatoria 2026:
`2019-20 … 2023-24`).

Extrae también el informe `PorcentajeCalificaciones` (por curso, centro y plan): es la
base del **Anexo IV** y del análisis de calificaciones por asignatura del **Criterio 6.3**
(asignaturas con más suspensos/no presentados y asignaturas de excelencia).

### 3. Rellenar la plantilla (parte determinista)
Ejecuta el script para volcar identificación e indicadores en el `.docx` sin tocar el
formato oficial:

```bash
python scripts/rellenar_autoinforme.py \
  --plantilla assets/plantilla_autoinforme_seguimiento.docx \
  --datos <ruta_al_datos.json> \
  --salida <ruta_salida.docx>
```

El script rellena la tabla de identificación, las tablas de indicadores (ISGC
P01–P07, con las cabeceras de años del JSON) y, si se aportan, las tablas de puntos
fuertes/débiles y el plan de mejora. Revisa los `AVISO` que imprime: falta de entorno o
fecha de extracción, entorno de pruebas, valores de satisfacción fuera de la escala 0-5
o tablas cuyo número de columnas no coincide con los años del JSON.

En la **renovación**, usa en su lugar:

```bash
python scripts/rellenar_renovacion.py \
  --plantillas assets/plantillas_renovacion \
  --plantilla-indicadores assets/plantilla_autoinforme_seguimiento.docx \
  --datos <ruta_al_datos.json> \
  --salida-dir <carpeta_salida>
```

Genera `Criterio_1.docx` … `Criterio_7.docx` (ficha de identificación, denominación,
puntos fuertes por curso, puntos débiles con impacto, tablas de recomendaciones del
criterio 2 y tabla de evidencias) y `Anexo_I_Indicadores.docx`. Ejemplo de datos en
`assets/ejemplo_datos_renovacion.json`.

### 4. Redactar el análisis (parte guiada)
Lee `references/guia-redaccion.md` y, sobre todo, `references/estilo-y-ejemplos.md`, que
recoge el estilo real de la coordinación: el micro-formato de análisis por indicador, la
estructura de cada subcriterio (reproducir la directriz → narrativa → indicadores →
anexo), la codificación de puntos fuertes/débiles y acciones (`PF/PD/AM-<CENTRO>-crit.n`),
el manejo de "No procede", la comparación con los objetivos de la memoria y el aviso de
cohortes/participación en egresados.

Para los apartados institucionales comunes a la UCA (SGC, servicios de orientación,
CAU/BAU/SIRE, Campus Virtual, DOCENTIA, ORI…), parte de `assets/bloques_reutilizables_uca.md`
y adapta solo lo específico del título/centro, verificando versiones y fechas.

Sobre el `.docx` generado, sustituye los textos entre corchetes (instrucciones de
cumplimentación) por el análisis real de cada subcriterio, apoyándote en los indicadores
obtenidos y comentando su **evolución**. Usa la skill `docx` para editar el documento con
fidelidad. En el seguimiento, el objetivo es **un único documento**: integra el análisis
dentro de cada criterio (no en un anexo aparte). En la renovación, redacta cada criterio
en su `.docx`, analizando el periodo completo de acreditación.

### 4b. Depurar instrucciones (documento único y limpio)
Cuando el análisis esté redactado, elimina el texto de instrucciones/directrices de la
plantilla ejecutando:

```bash
python scripts/depurar_instrucciones.py --entrada <borrador.docx> --salida <final.docx>
```

Borra los párrafos en rojo (instrucciones) y azul (directrices ACCUA), los que van entre
corchetes `[ … ]` y los marcadores `XXXX`, también dentro de las tablas, y en los párrafos
mixtos quita solo los fragmentos en rojo o azul. Conserva el texto en negro (análisis),
las tablas y los `[PENDIENTE: …]`. Revisa el resultado para asegurarte de que no se ha
eliminado contenido útil.
En la renovación, ejecútalo sobre cada `Criterio_n.docx`.

El script `rellenar_autoinforme.py` también vuelca la **tabla de recomendaciones de
ACCUA** (Criterio 2) si aportas en el JSON el bloque `accua`:
`{"fecha": "...", "items": [{"rec": "Subsanación/Recomendación ...", "accion": "..."}]}`.
Extrae estos datos del último informe de ACCUA y del autoinforme anterior, **conservando
la numeración original** de cada recomendación tal como figura en el informe de ACCUA.

### 5. Puntos fuertes/débiles y plan de mejora
En el **seguimiento**, cada criterio cierra con puntos fuertes y débiles **de este
autoinforme** (no de años anteriores). Cada punto débil debe enlazar con una acción de
mejora, y todas las acciones se consolidan en el Plan de Mejora final, que además debe
incluir todas las recomendaciones vivas del último informe ACCUA.

**Pocos puntos débiles y asumibles.** Las coordinaciones declaran entre 1 y 5 puntos
débiles en todo el autoinforme, no uno por cada indicador a la baja. Propón como punto
débil solo lo que la coordinación puede abordar con una acción propia; los indicadores
desfavorables con causa externa o ya cubiertos por una recomendación de ACCUA se
analizan en el texto y, si procede, se siguen en el plan de mejora. Si detectas más
debilidades, preséntalas al usuario en el resumen como candidatas, no en las tablas.

En la **renovación** no hay plan de mejora final: los puntos fuertes y débiles recogen los
de **todos los autoinformes del periodo**, por curso, y cada punto débil indica su
propuesta de mejora y el **impacto** observado en los indicadores.

### 6. Verificación
Antes de entregar, comprueba: que las columnas de años coinciden con la convocatoria y
las de egresados con las cinco últimas cohortes; que los indicadores proceden de
producción y la fecha de extracción está indicada; que ningún indicador de satisfacción
supera 5 y que título y centro alinean igual las cohortes; que no queda texto de
instrucciones (rojo/azul) ni marcadores `XXXX`; que cada punto débil tiene acción de
mejora; que los indicadores citados en el análisis coinciden con las tablas del Anexo 1;
que ninguna acción propuesta o texto modelo figura como realizado sin evidencia.
Relee `references/guia-redaccion.md` (checklist final) y, en la renovación, el checklist
de `references/estructura-renovacion.md`.

## Entrega

Guarda el autoinforme cumplimentado en `.docx` (en la renovación, los siete criterios y
el Anexo I) y preséntalo al usuario. Recuerda que es un borrador para revisión de la
coordinación y la CGC.
