---
name: uca-informes-calidad
description: >-
  Ayuda a redactar y cumplimentar los autoinformes de calidad de títulos oficiales
  (Grado/Máster) de la Universidad de Cádiz según el modelo de ACCUA (antes DEVA): el
  Autoinforme de Seguimiento y el Autoinforme Global de Renovación de la
  Acreditación. Úsala siempre que el usuario mencione "autoinforme", "seguimiento
  del título", "informe de seguimiento", "ACCUA", "DEVA", "renovación de la
  acreditación", criterios/subcriterios de calidad, indicadores ISGC (P01-P07),
  tasas de rendimiento/éxito/abandono/graduación, puntos fuertes y débiles, plan de
  mejora, o quiera rellenar las plantillas oficiales UCA. Extrae indicadores de
  LinceBI (data.uca.es), integra archivos aportados por el usuario y entrega los
  documentos en Word (.docx) respetando las plantillas oficiales.
---

# Autoinformes de calidad de títulos — Universidad de Cádiz (ACCUA)

## Qué hace esta skill

Guía la elaboración de dos tipos de autoinforme de un título oficial de la UCA, que
comparten criterios, subcriterios, indicadores ISGC y estilo de redacción:

- **Seguimiento**: anual. Entrega un único `.docx` basado en la plantilla oficial, con
  análisis, puntos fuertes/débiles, plan de mejora y anexos.
- **Renovación de la acreditación**: analiza todo el periodo desde la última
  acreditación y se presenta en la plataforma web de ACCUA. Entrega un `.docx` por
  criterio (plantillas del Servicio de Gestión de la Calidad) y un `.docx` con el Anexo I de
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

No hay autoinforme de seguimiento el primer año tras la verificación (solo se envía la
URL del título a ACCUA) ni el año en que el título renueva la acreditación (cada seis
cursos), porque coincidiría con el de renovación. Si el usuario pide un seguimiento en
uno de esos casos, avísale antes de empezar.
## Datos que necesitas

Pregunta (con `AskUserQuestion` si falta) por:

1. **Título y centro**: denominación exacta del Grado/Máster, centro/s, ID Ministerio,
   curso académico de implantación, web, modalidad, si es título doble/conjunto,
   última renovación de acreditación.
2. **Curso y convocatoria** del autoinforme (p. ej. curso 2025/26, convocatoria 2027).
   Determina los años de las columnas de las tablas de indicadores.
3. **Campus** del centro (Puerto Real, Cádiz, Jerez o Algeciras): decide qué bloque de
   bibliotecas del 5.1 se conserva (campo `campus` del JSON).
4. **Origen de los indicadores**: LinceBI (recomendado) y/o archivos aportados por el
   usuario (Excel/PDF descargados de data.uca.es o UCADRIVE).
5. **¿Va a Seguimiento ACCUA o solo seguimiento interno?** (solo en seguimiento).
   Cada título va a ACCUA a los tres años de renovar la acreditación; los demás años, el
   seguimiento es interno. La plantilla es la misma en todos los casos (también en la
   prueba piloto) y el borrador cumple siempre todo lo que pide ACCUA: la coordinación
   decide después cuánto profundiza, sobre todo en los subcriterios 6.1 y 6.2. Solo
   cambia esto si no va a ACCUA: se elimina la tabla «Aplicaciones para la gestión
   documental y sistemas de información» y no se cita la auditoría de la información
   pública, que el Servicio de Gestión de la Calidad hace solo a los títulos que van a
   ACCUA. En la renovación todo aplica siempre.

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
reconocidos del curso (LinceBI no los publica); resultados de primer curso si no aparecen
en LinceBI; y las rutas de
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

- **Desde LinceBI**: usa las herramientas `lincebi_*`. Empieza por el **informe agregado
  del Anexo I** (`/public/Datos Académicos/Calidad/Autoinforme/Autoinforme.prpt`), que
  reúne todos los indicadores; si falla o le falta alguno, recurre a los informes
  disgregados (ver el mapa). Para cada informe: resuelve parámetros con
  `lincebi_get_report_parameters` (normalmente título/plan, centro y curso) y extrae datos
  con `lincebi_get_report_data`; si no conoces la ruta, búscala con
  `lincebi_search_resources` (filtra `types=["REPORT_PRD"]`). LinceBI requiere VPN/sesión
  UCA: si no responde, avisa al usuario y continúa con los archivos que aporte o deja
  `[PENDIENTE]`.
- **Desde archivos**: si el usuario aporta Excel/CSV/PDF, extrae los valores por
  indicador y año. Para Excel usa la skill `xlsx`; para PDF, la skill `pdf`.

Reúne los valores en un JSON de datos (ver esquema en
`references/mapa-indicadores-lincebi.md`).

**Entorno de producción obligatorio.** Antes de extraer, comprueba el host de LinceBI
(por ejemplo, en el `viewerUrl` que devuelve `lincebi_get_report_data`): debe ser
`data.uca.es`. Si es `datapru.uca.es` (pruebas), **detente** y avisa al usuario: sus
valores no son los definitivos (en las evaluaciones, la tasa de graduación llegó a
duplicarse). Registra el entorno, la fecha y la fuente (`agregado`, `disgregados` o
`mixta`) en el bloque `extraccion` del JSON.

**Serie en vivo.** Extrae de LinceBI todos los cursos de cada tabla, no solo el último;
usa el autoinforme anterior únicamente para las columnas que LinceBI ya no muestra y
para valores vivos incoherentes, según la "Regla de la serie histórica" del mapa. Eso
incluye el sexto curso de los resultados globales del 6.3: tómalo del autoinforme anterior
en vez de dejarlo pendiente. Las
cohortes de egresados son las cinco últimas con datos (convocatoria 2027: previsiblemente
`2020-21 … 2024-25`; compruébalo en LinceBI).

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

El script rellena la portada (con las fechas de elaboración y aprobación, o
`[PENDIENTE]`), la tabla de identificación, las tablas de indicadores
(ISGC P01–P07, con las cabeceras de años del JSON) y, si se aportan, la tabla de
recomendaciones de ACCUA, las tablas de puntos fuertes y débiles y el plan de mejora
(pasos 4b y 5); además conserva solo el bloque de bibliotecas del
campus indicado. Localiza las tablas por su contenido, no por su posición. Revisa los
`AVISO` que imprime: falta de entorno o fecha de extracción, entorno de pruebas, valores
de satisfacción fuera de la escala 0-5, tablas cuyo número de columnas no coincide con
los años del JSON, `campus` ausente, tablas de la plantilla que no encuentra,
recomendaciones o puntos débiles sin acción y fechas que no son MM/AAAA.

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
anexo), la numeración de puntos fuertes y débiles y de acciones (con códigos
`PF/PD/AM-<CENTRO>-crit.n` solo en los centros que los usan, como la ESI y la ETSIA:
campo `codigo_centro` del JSON), el manejo de "No procede", la comparación con los
objetivos de la memoria y el aviso de cohortes/participación en egresados. Al redactar
cada criterio, repasa en `references/recomendaciones-accua.md` los temas que ACCUA pide
de forma recurrente y analiza los que apliquen al título con los datos de la entrada.

**Indicaciones del Servicio de Gestión de la Calidad** (aplícalas al redactar; las de
formato, enlaces y entrega de su guía rápida están en `references/guia-redaccion.md`):

- Escribe «ACCUA», nunca «DEVA» (nombre antiguo), y «Servicio de Gestión de la Calidad»;
  los datos se comprueban en el Sistema de Información, no «con la Unidad de Calidad».
- No afirmes que el centro o el título carecen de un elemento del SGC (cuadro de mando,
  informes de gestión, actas, planes de mejora) sin consultar su web: es la fuente. Si no
  lo localizas, escribe `[PENDIENTE: no localizado en la web del centro]`, no su ausencia.
- Cada vez que analices indicadores, indica que están en el Anexo 1. No incluyas en el
  6.3 la tabla de calificaciones (es el Anexo IV): solo su análisis. En el criterio 4, no
  enlaces la relación del profesorado: indica que está en el Anexo 2 del autoinforme y
  analízala; en el propio Anexo II basta el enlace a la tabla, sin copiarla.
- La Política de Calidad vigente es la de las directrices aprobadas el 29-9-2026
  (BOUCA; https://ucalidad.uca.es/wp-content/uploads/2026/10/BOUCA-DIRECTRICES-POLITICA-DE-CALIDAD-29-9-26.pdf).
  `rellenar_autoinforme.py` ya cambia el enlace antiguo de la plantilla; no cites la de
  2022 en el texto.
- En el 5.4, analiza ISGC-P01-03 e ISGC-P07-04 y enlaza el censo del PTGAS
  (`[PENDIENTE: enlace al censo del PTGAS]` si no se aporta).
- Cada evidencia va en su subcriterio, no en una lista al final del criterio. Tras cada
  enlace de UCADrive, ACCUA exige usuario, contraseña y ruta completa a un solo clic:
  escribe la ruta que aporte el centro y deja
  `[PENDIENTE: usuario y contraseña de UCADrive]`, que completa la coordinación (no pidas
  ni escribas credenciales).
- En el 7.4 (empleadores), cita como evidencias el informe de resultados de la encuesta,
  el acta que lo aprueba con conclusiones y acciones, los indicadores publicados y las
  actas de reuniones con empleadores. Desde 2026 el Servicio de Gestión de la Calidad hace
  la encuesta a los centros que la piden.
- No enlaces LinceBI, GADES, ICARO ni el Campus Virtual: los evaluadores no tienen acceso.
  Cítalos como fuente y enlaza la evidencia publicada o en UCADrive, a dos clics como
  máximo. Un indicador no es una evidencia.

Para los apartados institucionales comunes a la UCA (SGC, servicios de orientación,
CAU/BAU/SIRE, Campus Virtual, DOCENTIA, ORI…), parte de `assets/bloques_reutilizables_uca.md`
y adapta solo lo específico del título/centro, verificando versiones y fechas.

Sobre el `.docx` generado, sustituye los textos entre corchetes (instrucciones de
cumplimentación) por el análisis real de cada subcriterio, apoyándote en los indicadores
obtenidos y comentando su **evolución**. Usa la skill `docx` para editar el documento con
fidelidad. En el seguimiento, el objetivo es **un único documento**: integra el análisis
dentro de cada criterio (no en un anexo aparte). En la renovación, redacta cada criterio
en su `.docx`, analizando el periodo completo de acreditación.

**Marcas en rojo dentro del texto modelo.** Antes de depurar, sustituye en los párrafos
en negro las marcas que la depuración borraría: «Facultad/Escuela», «Grado/Máster» y
«grado/máster» por el nombre real del centro y del título; los paréntesis vacíos «()»
por la URL correspondiente, y las marcas `XXXX` (p. ej. `http://xxxxxx.uca.es` o
«Facultad/Escuela de XXXXXXXX» en el 5.1) por su valor. Un párrafo que conserve `XXXX`
se elimina entero.

**Directrices azules dentro del texto modelo** (sobre todo en el criterio 1). Cuando un
párrafo en negro intercala una lista en azul (p. ej. los elementos que publica la web
del título), la depuración conserva el azul en negro. Comprueba en la web del título cada
elemento de la lista: deja solo los publicados y añade su enlace; los que no lo estén
pásalos a un punto débil o márcalos `[PENDIENTE: verificar en la web …]`.

**Recordatorio de información pública** (en rojo en la plantilla, al final del criterio 1:
«Se recuerda que deben estar publicados…»). La depuración lo conserva en negro porque el
Servicio de Gestión de la Calidad quiere que la coordinación lo tenga presente. Añade a
cada elemento su enlace en la web del título o del centro, o
`[PENDIENTE: no localizado en la web]`, y llévalo a un punto débil si falta algo que ACCUA
exige publicar.

**Satisfacción con cada asignatura (6.4).** Los informes de satisfacción por asignatura
están en UCADrive (carpeta del Servicio de Gestión de la Calidad, «Compartidos/ Criterio 6.4
<título>») y no deben publicarse ni copiarse a la carpeta del centro. Analízalos si el
usuario los aporta e incluye siempre el enlace de UCADrive con acceso interno para los
evaluadores de ACCUA (`[PENDIENTE: enlace UCADrive con acceso interno]`); a veces no se
pueden obtener, porque proceden de las encuestas docentes.

### 4b. Depurar instrucciones (documento único y limpio)
Cuando el análisis esté redactado, elimina el texto de instrucciones/directrices de la
plantilla ejecutando:

```bash
python scripts/depurar_instrucciones.py --entrada <borrador.docx> --salida <final.docx>
```

Borra los párrafos en rojo (instrucciones) y azul (directrices ACCUA), los que van entre
corchetes `[ … ]` y los marcadores `XXXX`, también dentro de las tablas. En los párrafos
mixtos quita solo los fragmentos en rojo y pasa a negro los azules. También pasan a negro
las etiquetas cortas en azul de las tablas (encabezados como «Suspensos» o «%»). Conserva
el texto en negro (análisis), las tablas y los `[PENDIENTE: …]`. Si tras quitar el rojo
un párrafo mixto queda solo con puntuación, lo borra; si conserva texto, lo lista en la
salida de error con el prefijo `REVISAR`. Resuelve cada aviso: borra lo que sea resto de una instrucción o una
opción que no procede para el título (p. ej. el texto para títulos con varias
modalidades, «Punto débil nº» sin número) y completa lo que sea contenido. Revisa además
el resultado para asegurarte de que no se ha eliminado contenido útil.
En la renovación, ejecútalo sobre cada `Criterio_n.docx`.

Al final aplica el formato que pide el Servicio de Gestión de la Calidad: los
`[PENDIENTE …]` en rojo para que la coordinación los localice, sin resaltados de color, las
URL sueltas convertidas en enlaces activos en azul y la prosa de los criterios justificada
a 10 pt en la fuente de la plantilla. Avisa con `REVISAR` de cada mención a «DEVA» y de
los enlaces a rutas locales (`file:///…`): sustitúyelos por «ACCUA» y por la URL pública.
Es idempotente: puedes ejecutarlo de nuevo tras corregir.

El script `rellenar_autoinforme.py` también vuelca la **tabla de recomendaciones de
ACCUA** (criterio 2) si aportas en el JSON el bloque `accua` (esquema en
`references/mapa-indicadores-lincebi.md`): `informe` («Informe de seguimiento de ACCUA,
<DD/MM/AAAA>») e `items` con `num`, `tipo`, `rec` y `acciones`. Copia cada recomendación
**literal** del último informe de ACCUA, una por fila y con su **número original**; no
añadas columnas ni estados como «en curso». Cada recomendación lleva al menos una acción,
que el script vuelca también en el plan de mejora con el mismo texto.

### 5. Puntos fuertes/débiles y plan de mejora
En el **seguimiento**, cada criterio cierra con puntos fuertes y débiles **de este
autoinforme** (no de años anteriores). Cada punto débil debe enlazar con una acción de
mejora, y todas las acciones se consolidan en el Plan de Mejora final, que además debe
incluir todas las recomendaciones vivas del último informe ACCUA. El script los vuelca
desde el bloque `puntos` del JSON: antepone «Curso <curso>.» y un ordinal a cada punto
fuerte dentro de su criterio, y numera los puntos débiles de forma correlativa en todo
el autoinforme. No escribas tú esa numeración en el texto.

**Puntos débiles: todos los que tengan evidencia.** No hay tope: es punto débil todo
indicador o hecho con evidencia de que requiere mejora, en particular una satisfacción
por debajo de 2,5 o una tendencia negativa durante dos cursos seguidos. No lo es una
variación puntual sin tendencia. Todos pasan al plan de mejora. Las recomendaciones de
ACCUA **no** van en las tablas de puntos débiles: solo en la tabla del criterio 2 y en el
plan, donde el script las vuelca idénticas.

**Acciones del plan de mejora.** Redacta cada acción como algo concreto, con un único
responsable (si es externo al centro, `[PENDIENTE: autorización del responsable
externo]`), sus evidencias, fechas de inicio y fin en formato MM/AAAA, concretas o
estimadas (nunca «Permanente», «Continua» ni «Finalizada»: el cierre lo decide ACCUA), e
indicador de seguimiento con su valor actual en la última columna. Si la recomendación pide
«analizar las causas», la acción explica cómo se analizarán y qué se hará con las
conclusiones. Si el punto débil es la falta de datos de satisfacción de empleadores, la
acción son las actividades para conocerla (encuesta del Servicio de Gestión de la
Calidad, reuniones con empleadores) y la evidencia, su informe o acta.

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
que ninguna acción propuesta o texto modelo figura como realizado sin evidencia (relee el
texto modelo conservado en negro) ni actividad del curso conocida solo por el autoinforme
anterior, y que las causas sin fuente figuran como hipótesis; que no quedan celdas con «-»
o vacías sin explicación, guiones convertidos en 0 o narrados como ausencia, ni
`[PENDIENTE]` de datos que estén en la entrada (memoria y autoinforme anterior incluidos)
o en LinceBI; que los signos de evolución, los extremos y los cuantificadores («mayoría»,
«suficiente») coinciden con el cálculo; que no quedan restos de plantilla en negro (notas
de cumplimentación, opciones alternativas, filas de ejemplo, enlaces pegados al texto) ni
avisos `REVISAR` sin resolver; que en el texto modelo no quedan «Facultad/Escuela»,
«Grado/Máster» genéricos ni paréntesis vacíos «()» sin su URL, y que cada elemento de las
listas que eran azules está comprobado en la web; que el 5.1 conserva solo el bloque de
bibliotecas del campus del centro; que el 6.4 enlaza los informes por asignatura sin
reproducir sus datos; y que la síntesis de sostenibilidad (7.6) cubre todos sus
elementos y cierra con una valoración explícita. Comprueba también las indicaciones del
Servicio de Gestión de la Calidad: ni «DEVA» ni «Unidad de Calidad»; cada análisis de
indicadores remite al Anexo 1; el 6.3 sin tabla; el 5.4 con ISGC-P01-03, ISGC-P07-04 y el
enlace al censo del PTGAS; cada evidencia de UCADrive en su subcriterio con su ruta y el
`[PENDIENTE]` de credenciales; el recordatorio de información pública con un enlace por
elemento; la tabla de aplicaciones eliminada si el título no va a ACCUA; y en el plan,
recomendaciones literales y numeradas, todos los puntos débiles con acción y fechas
MM/AAAA.
Relee `references/guia-redaccion.md` (checklist final, que incluye la guía rápida),
repasa `references/recomendaciones-accua.md` criterio a criterio y, en la renovación,
relee el checklist de `references/estructura-renovacion.md`.

## Entrega

Guarda el autoinforme cumplimentado en `.docx` (en la renovación, los siete criterios y
el Anexo I) y preséntalo al usuario. Recuerda que es un borrador para revisión de la
coordinación y la CGC, y que antes de enviarlo hay que resolver todos los `[PENDIENTE]`,
dejar todo el texto en negro sin comentarios ni resaltados, probar los enlaces (si hay
que acortarlos, con https://url.uca.es/redir/crear) y generar el PDF **sin firma
digital**, con la aprobación firmada del centro como anexo en la última página.
