# Procedimiento de evaluación de la skill

Cómo evaluar `skills/uca-informes-calidad` de forma sistemática. Cada **ejecución** evalúa
**un título** y se orquesta entera desde GitHub Copilot CLI: el agente principal
(orquestador) lanza dos subagentes y ejecuta el script `tools/evaluacion/evaluacion.py`.

El responsable del proyecto valida el caso, decide qué lecciones se aplican a la skill y si
se envía material a la coordinación; todo lo demás lo hacen el orquestador y los subagentes.

## Piezas

| Pieza | Qué es |
|---|---|
| `tools/evaluacion/evaluacion.py` | Script con los subcomandos `enlaces`, `caso`, `nueva`, `medir` y `valoracion`. |
| `evals/casos.csv` | Catálogo de casos (`id`, `titulo`, `nivel`, `centro`, `tipo`, `curso`, `convocatoria`, `seguimiento_accua` y `conjunto`: `aprendizaje`, `reserva` o `excluido`). |
| `docs/evaluacion/rubrica.md` | Rúbrica cerrada: D1–D7 (0-1-2), bloqueantes B1–B3, causas S/D/I/H/E. |
| `docs/evaluacion/plantilla-cotejo.md` | Formato obligatorio de `cotejo-A.md` y `cotejo-B.md`. |
| `docs/evaluacion/plantilla-ficha.md` | Ficha de cada ejecución (la crea el script). |
| `evals/casos/<id>/entrada/` | Lo que recibiría la skill: autoinforme anterior, memoria, informe ACCUA… |
| `evals/casos/<id>/referencia/autoinforme-humano.*` | Autoinforme presentado por la coordinación. **Nunca** lo ve A al generar. |
| `evals/casos/<id>/fuentes.md` | Procedencia de los documentos del caso (URL, fecha, SHA-256), si se preparó con `caso`. |
| `evals/ejecuciones/Enn-<id>/` | Ficha, borrador, cotejos y métricas de la ejecución. |
| `evals/historial.md` | Tabla con todas las ejecuciones (la regenera `medir`). |
| `docs/EVALUACIONES.md` | Registro versionado: resumen de cada ejecución y estado de las lecciones. |
| `web/evaluacion.html` | Página pública con las cifras globales. |
| `web/procedimiento.html` | Página pública con el proceso de evaluación y la rúbrica. |

`evals/` contiene datos personales y no se versiona: al repositorio y a la web solo llegan
cifras agregadas, lecciones generalizadas y, si el responsable lo aprueba, el material del
paso 7.

## Requisitos previos (una vez)

1. MCP de LinceBI configurado en Copilot CLI contra `data.uca.es` (lo configura el
   responsable; el agente no ve las credenciales).
2. Entorno Python con `pip install -r tools/evaluacion/requirements.txt`.
3. Modelos fijos: **A** = `claude-opus-5.5` (genera y se autocoteja); **B** = `gpt-6.1-sol`
   (segundo corrector, de otra familia). Si cambian, se anota en la ficha (campos «Modelo A» y
   «Modelo B») y en la sección de la ejecución en `docs/EVALUACIONES.md`.
4. Que Copilot use la skill del repositorio (`skills/uca-informes-calidad/SKILL.md`), no una
   copia global antigua.

## Antes de la ejecución: el caso

Elige el título **por variedad** (otro centro, máster, renovación…) frente a los ya
evaluados. Hay dos formas de preparar el caso:

- **Automática** (recomendada): pide al agente «Prepara un caso con el `<título>`». El agente
  sigue la skill de proyecto
  [`.github/skills/preparar-caso/`](../.github/skills/preparar-caso/SKILL.md):
  1. Localiza en la web del centro el último autoinforme publicado (la referencia) y los
     documentos de entrada anteriores a él.
  2. Te pregunta ante cualquier duda y por el `conjunto`.
  3. Ejecuta `python tools/evaluacion/evaluacion.py caso <fuentes.json>`, que añade la fila
     a `casos.csv`, descarga los documentos y deja su procedencia en
     `evals/casos/<id>/fuentes.md`.
- **Manual**: añade una fila a `casos.csv` y copia:
  - en `evals/casos/<id>/entrada/`: `autoinforme-anterior.*`, `memoria.*` y, si existen,
    `informe-accua.*` y `plan-mejora.*`;
  - en `evals/casos/<id>/referencia/`: `autoinforme-humano.*`.

  Para registrar también la procedencia en `fuentes.md`, ejecuta `caso` con `--sin-descarga`.

## Pasos de una ejecución

Pídeselo al orquestador con: «Evalúa la skill con el caso `<id>` siguiendo
docs/PROCEDIMIENTO.md». Los pasos forman dos ciclos; las tablas los resumen y cada paso se
detalla después, con su prompt cuando lo lleva.

**Ciclo de IA (pasos 1-6).** Se completa en una sesión y no espera a la coordinación: la
consolidación del paso 5 es provisional, solo con los dos correctores de IA, y con ella el
responsable decide y la skill puede pasar a la siguiente versión.

| Paso | Quién | Acción | Produce |
|---|---|---|---|
| [1](#paso-1-abrir-la-ejecución) | Orquestador | `evaluacion.py nueva <id>` | `Enn-<id>/ficha.md` |
| [2](#paso-2-generación-a) | Subagente A | Genera el borrador | `borrador.docx`, `datos.json`, sección «Generación» de la ficha |
| [3](#paso-3-autocotejo-a) | Mismo subagente A | Coteja su borrador | `cotejo-A.md` |
| [4](#paso-4-segundo-corrector-b) | Subagente B | Coteja el borrador | `cotejo-B.md` |
| [5](#paso-5-consolidación-provisional) | Orquestador | `evaluacion.py medir Enn` | `metricas.json`, ficha completada, `evals/historial.md` |
| [6](#paso-6-registro-y-decisión-del-responsable) | Orquestador → responsable | Registra la ejecución y la resume al responsable, que decide | `docs/EVALUACIONES.md`, `web/evaluacion.html`, decisión en la ficha |

Los pasos 3 y 4 se lanzan a la vez en cuanto existe `borrador.docx`.

**Ciclo de la coordinación (pasos 7-8), asíncrono.** Empieza tras el paso 6 y puede tardar
semanas; mientras tanto se siguen evaluando otros títulos y aplicando lecciones. Cuando llega
la valoración, completa la consolidación de esa ejecución y sus propuestas se deciden junto
con las de la siguiente ejecución que esté en curso. Si no llega, la ejecución queda
consolidada solo con la IA.

| Paso | Quién | Acción | Produce |
|---|---|---|---|
| [7](#paso-7-material-para-la-coordinación) | Orquestador, **solo si el responsable lo aprueba** | Prepara el material para la coordinación | `docs/evaluacion/material-coordinaciones/<id>/` |
| [8](#paso-8-valoración-de-la-coordinación-y-consolidación-final) | Orquestador, cuando la coordinación devuelve la hoja | `evaluacion.py valoracion Enn` y propuesta de lecciones | `valoracion.json`, sección de la ficha, columnas del historial |

Reglas del orquestador durante toda la ejecución:

- A no recibe la ruta de `referencia/` hasta el paso 3 (por eso el prompt del paso 2 solo le
  permite leer `entrada/`). B no recibe `cotejo-A.md`.
- Si A detecta `datapru.uca.es`, se detiene la ejecución (bloqueante B3) y se avisa al
  responsable; nunca se continúa con datos de pruebas. Si LinceBI deja de responder, se
  reintenta; si no se recupera, se detiene y se avisa igualmente.
- El orquestador **no modifica la skill**. Las lecciones se aplican después (ver
  [Después de la ejecución](#después-de-la-ejecución-aplicar-lecciones)).
- En los prompts, sustituye `<…>` con los datos de la ficha y de `casos.csv`.

### Paso 1: abrir la ejecución

El orquestador ejecuta `python tools/evaluacion/evaluacion.py nueva <id>`, que asigna el
número `Enn` y crea `evals/ejecuciones/Enn-<id>/ficha.md`.

### Paso 2: generación (A)

El orquestador lanza el subagente A (`general-purpose`, `claude-opus-5.5`, en segundo
plano) con este prompt:

```text
Eres el subagente generador de una evaluación de la skill. Trabaja en la raíz del
repositorio uca-informes-calidad. Lee y sigue skills/uca-informes-calidad/SKILL.md (no uses
ninguna otra skill de autoinformes instalada) para redactar el autoinforme de <tipo> del
<titulo>, curso <curso>, convocatoria <convocatoria>.

No puedes preguntar al usuario. Estas son sus respuestas a lo que la skill pregunta:
- Tipo: <tipo>. ¿Seguimiento ACCUA?: <sí/no/no consta: asume sí y anótalo>.
- Indicadores: LinceBI (data.uca.es) mediante las herramientas lincebi_*.
- Documentos aportados: los de evals/casos/<id>/entrada/ (lístalos).
- Datos internos del centro: no se aportan; déjalos [PENDIENTE] como indica la skill.
Si la skill pidiera algo más, toma el supuesto más razonable y anótalo.

Prohibido: leer de evals/casos/<id>/ nada que no esté en entrada/; leer las carpetas de
otras ejecuciones en evals/ejecuciones/; modificar ficheros de skills/. Si el host de
LinceBI no es data.uca.es, detente y explícalo.

Escribe en evals/ejecuciones/Enn-<id>/: borrador.docx (entregable de la skill) y
datos.json (el JSON de datos con el bloque extraccion). Completa la sección
«Generación» de ficha.md (host, fecha de extracción, documentos usados, supuestos,
decisiones, incidencias). Termina con un resumen breve; no hagas todavía ningún cotejo.
```

### Paso 3: autocotejo (A)

Cuando existe `borrador.docx`, el orquestador envía al mismo subagente A (con
`write_agent`) este prompt:

```text
Ahora coteja tu borrador con el autoinforme presentado por la coordinación:
evals/casos/<id>/referencia/autoinforme-humano.*. No modifiques el borrador.

Puntúa con docs/evaluacion/rubrica.md y escribe evals/ejecuciones/Enn-<id>/cotejo-A.md
con el formato exacto de docs/evaluacion/plantilla-cotejo.md (no cambies los títulos de
sección ni las columnas de las tablas). Para cada discrepancia relevante asigna una causa
S/D/I/H/E; el autoinforme humano no es la verdad: si el borrador es correcto, la causa es
H. Propón lecciones solo para causas S: reglas generales sin datos del título, indicando
su respaldo (norma, otros títulos o «ninguno aún»). No edites la skill.
```

### Paso 4: segundo corrector (B)

A la vez que el paso 3, el orquestador lanza el subagente B (`general-purpose`,
`gpt-6.1-sol`) con este prompt:

```text
Eres un corrector independiente. Evalúa un borrador de autoinforme de calidad de la
Universidad de Cádiz generado por IA, comparándolo con el que presentó la coordinación.

- Borrador: evals/ejecuciones/Enn-<id>/borrador.docx (y datos.json si existe).
- Autoinforme humano: evals/casos/<id>/referencia/autoinforme-humano.*.
- Documentos de entrada que tuvo la IA: evals/casos/<id>/entrada/.
- Contexto de la generación: sección «Generación» de evals/ejecuciones/Enn-<id>/ficha.md.
- Reglas que debía seguir: skills/uca-informes-calidad/ (para decidir si una
  discrepancia es de causa S).

No leas cotejo-A.md ni otras ejecuciones. No modifiques nada salvo el fichero de salida.
Puntúa con docs/evaluacion/rubrica.md y escribe evals/ejecuciones/Enn-<id>/cotejo-B.md con
el formato exacto de docs/evaluacion/plantilla-cotejo.md. Justifica cada nota con una
evidencia concreta (apartado y texto o valor). El autoinforme humano no es la verdad: si
el borrador es correcto y el humano no, la causa es H.
```

### Paso 5: consolidación provisional

Con los dos cotejos escritos, el orquestador ejecuta
`python tools/evaluacion/evaluacion.py medir Enn`, que consolida así (la valoración de la
coordinación se añade en el paso 8, si llega):

- La nota final es la de B (o la de A si no hay B).
- Pasan a «Pendiente de revisión experta» de la ficha: las dimensiones en las que A y B
  difieren 2 puntos, los bloqueantes y las discrepancias de causa H o I de ambos cotejos.
- Las métricas automáticas (extensión, PF/PD/AM, `[PENDIENTE]`, Anexo I) son aproximadas.
  La del Anexo I cuenta los valores del borrador que aparecen en cualquier parte del texto
  humano, así que es solo una cota superior: en la línea base dio 97 % donde B comprobó
  menos del 80 % celda a celda. La nota de D2 la pone B comparando por celda.
- Avisa de **huellas**: frases de 8 palabras que solo aparecen en la referencia de un
  título y también en la skill. Indican que la skill contiene texto de un caso de
  evaluación, lo que infla sus notas en ese caso.

### Paso 6: registro y decisión del responsable

`medir` solo actualiza `evals/`, que no se versiona; el registro público lo hace el
orquestador tras cada ejecución, sin esperar a la decisión del responsable. En
`docs/EVALUACIONES.md`, sin datos del título más allá de su sigla:

- «Resumen de la serie»: una fila con la ejecución, las lecciones a validar, la media y los
  bloqueantes; revisa la frase de conclusión bajo la tabla.
- «Ejecuciones»: una sección «### Enn: <sigla> con <lecciones a validar>» al final, con la
  media, las dimensiones con 2, los bloqueantes y su causa, las lecciones validadas o
  insuficientes, las nuevas candidatas y la línea «Decisión del responsable: pendiente.».
- «Lecciones incorporadas»: en la columna «Estado», sustituye cada «validar en Enn» por
  «validada en Enn» o «insuficiente en Enn (<motivo>)».
- «Lecciones candidatas»: una fila por candidata nueva, con el siguiente número C libre;
  actualiza «Observada en» de las que se repitan.

Actualiza también `web/evaluacion.html`, sin datos personales ni detalles que identifiquen
documentos internos:

- cifras globales tomadas de `evals/historial.md`, en las tarjetas de «En resumen» (versiones
  iniciales frente a asistente actual, con sus barras y porcentaje de cambio) y en la línea de
  contexto;
- en «Resultados», la barra de la ejecución en «Evolución de la nota» y, si repite un título, su
  par en «Mismo título, antes y después»;
- en «Por ejecución», la fila de la ejecución (versión de la skill con su tooltip, nota de cada
  aspecto D1-D7, media y un chip con el número de errores graves cuyo tooltip nombra cada uno
  —dato inventado, valor contradictorio u origen no garantizado— con su motivo generalizado; no
  se publican los códigos B1-B3) y su fila desplegable (valoración breve, métricas de `medir`
  con las mismas etiquetas que las demás fichas, que el script de la página usa para mostrar
  su ayuda, errores graves y material);
- la lista «Qué dicen los resultados», si la ejecución la cambia;
- en «Qué aprende el asistente en cada versión», el estado de las lecciones contrastadas
  (Funciona, Reforzada, A reforzar, Por comprobar), sus recuentos y «Próximos pasos»;
- la fecha de «Última actualización».

Cuando se aplican lecciones a la skill (ver [después de la
ejecución](#después-de-la-ejecución-aplicar-lecciones)), añade la nueva versión a la línea
temporal con su número, commit, fecha y lecciones en «Por comprobar».

Después presenta al responsable un resumen con las notas, los bloqueantes, lo pendiente de
revisión experta y las lecciones candidatas. El responsable anota en la ficha qué lecciones
aprueba, rechaza o deja como candidatas, y el orquestador copia la decisión a la sección de
la ejecución en `docs/EVALUACIONES.md`.

### Paso 7: material para la coordinación

Este paso copia a la parte versionada documentos de `evals/` que verán terceros. Por eso el
orquestador pregunta antes al responsable e indica si la ejecución tiene bloqueantes (puede
preferir no enviar un borrador con B1 o B2). Si lo aprueba, crea
`docs/evaluacion/material-coordinaciones/<id>/` con:

| Fichero | Origen |
|---|---|
| `borrador-ia.docx` | `evals/ejecuciones/Enn-<id>/borrador.docx`, sin cambios |
| `autoinforme-coordinacion.pdf` | `evals/casos/<id>/referencia/autoinforme-humano.*` (convertido a PDF si no lo es) |
| `rubrica-valoracion.xlsx` | Copia de la de otro título cambiando solo las celdas C3 (nombre del título) y C4 («<Tipo>, curso <aaaa/aa> (convocatoria <aaaa>)») |

Si el título ya tenía material de una ejecución anterior, se sustituye por el de la más
reciente. Después, en la fila desplegable de la ejecución de `web/evaluacion.html`, cambia
«—» del apartado «Material» por los tres enlaces, con el mismo formato que las demás filas.

### Paso 8: valoración de la coordinación y consolidación final

Llega semanas después del paso 7, cuando la coordinación devuelve la hoja rellenada, y no
detiene el ciclo de IA: la skill puede haber cambiado de versión entretanto. El
responsable la guarda en `evals/ejecuciones/Enn-<id>/valoracion-coordinacion.xlsx` (con
sufijo `-1`, `-2`… si valoran varias personas); va en `evals/` porque contiene comentarios
y el rol de quien valora. El orquestador ejecuta
`python tools/evaluacion/evaluacion.py valoracion Enn`, que:

- lee las notas 1-5, los comentarios, la respuesta a «Errores graves» y los textos libres
  (las celdas vacías son NA; con varias hojas, media por aspecto y errores graves si alguien
  responde «Sí»);
- convierte las notas a la escala de la rúbrica con (nota − 1) / 2: 1→0, 3→1, 5→2;
  «Esfuerzo» y «Global» se quedan en 1-5 porque no tienen equivalente en la rúbrica;
- escribe `valoracion.json` y la sección «Valoración de la coordinación» de la ficha, y
  añade al historial la media de la coordinación, su diferencia con la de la IA, «Esfuerzo»
  y «Global»;
- añade a «Pendiente de revisión experta» las dimensiones en las que coordinación e IA
  difieren 1 punto o más, y los desacuerdos entre «Errores graves» y los bloqueantes B1/B2.
  `medir` los conserva si se vuelve a ejecutar.

Una hoja anterior a la separación de D1 y D2 se acepta con aviso: «Datos» puntúa ambas y no
hay D6 ni errores graves.

Después el orquestador presenta al responsable:

- **Lecciones candidatas** a partir de los comentarios y los textos libres, generalizadas
  sin frases ni nombres del título (regla 3 contra el sobreajuste). Lo que pidan dos
  coordinaciones distintas cumple el filtro de admisión.
- **Hallazgos**: errores del autoinforme humano (causa H) o datos internos (causa I) que la
  coordinación confirme o desmienta.
- **Calibración de la rúbrica**: si en 3 o más títulos la coordinación y la IA difieren
  1 punto o más en la misma dimensión y en el mismo sentido, se propone revisarla (ver
  [cambios de rúbrica](#casos-especiales-línea-base-y-cambios-de-rúbrica)).

La valoración se refiere a la versión de la skill con la que se generó el borrador: una
lección que salga de ella se valida, como las demás, con una ejecución posterior de otro
título. El responsable decide en la ficha como en el paso 6 (en la siguiente decisión que
tenga pendiente, sin abrir un ciclo aparte) y el orquestador lo registra en
`docs/EVALUACIONES.md` (apartado «Valoración de las coordinaciones», con medias y diferencias
por dimensión) y en `web/evaluacion.html` (nota de la coordinación junto a la de la IA,
«Esfuerzo» y «Global»), siempre con cifras agregadas y sin comentarios literales.

### Casos especiales: línea base y cambios de rúbrica

Para ejecuciones anteriores al protocolo (E01–E03) o cuando cambia la versión de la
rúbrica, solo se lanza B (paso 4) sobre el borrador existente y después `medir` (paso 5).
Si la ficha no tiene sección «Generación», se quita esa línea del prompt de B. Un cambio de
rúbrica se refleja también en «La rúbrica de evaluación» de `web/procedimiento.html`.

## Tiempos orientativos

Medidos en E04-E07 (grados de seguimiento) con las fechas de los ficheros de cada ejecución.
No incluyen caídas de LinceBI ni la revisión del responsable.

| Paso | Duración | Observaciones |
|---|---|---|
| 1. `nueva` | Segundos | |
| 2. Generación (A) | 15-21 min | Unos 11-12 min hasta tener `datos.json` (lectura de entrada y LinceBI); el resto, redacción y depuración del `.docx` |
| 3 y 4. Autocotejo (A) y corrector (B) | 6-9 min | En paralelo; cada uno tarda 5-9 min |
| 5. `medir` | Menos de 1 min | |
| **Total por título (ciclo de IA)** | **25-30 min** | Más el registro y la decisión del responsable (paso 6); la valoración de la coordinación llega aparte |

Para medir, usa las fechas de creación de `datos.json`, `borrador.docx` y los cotejos: el
tiempo que informa `read_agent` incluye la espera entre turnos del subagente.

## Después de la ejecución: aplicar lecciones

Las lecciones que apruebe el responsable se aplican a la skill en un cambio pequeño y con su
propia versión, fuera de la ejecución. Después, el orquestador las añade a «Lecciones
incorporadas» de `docs/EVALUACIONES.md` con su origen, dónde están en la skill y el estado
«Incorporada el <fecha>; validar en Enn», donde Enn es la siguiente ejecución de otro
título. Si procede de una candidata, su fila en «Lecciones candidatas» pasa a «Incorporada
como Lnn».

Ciclo de vida de una lección:

1. **Candidata**: observada, aún fuera de la skill (tabla «Lecciones candidatas»).
2. **Incorporada**, con «validar en Enn» mientras espera contraste.
3. **Validada en Enn** o **insuficiente en Enn (<motivo>)**. Una lección insuficiente se
   refuerza con una nueva (p. ej. L16 → L16b) que vuelve a empezar en el estado 2.

## Reglas contra el sobreajuste

1. Cada título nuevo contrasta las lecciones anteriores: una lección solo pasa a
   **validada** cuando mejora (o no empeora) un título distinto evaluado después.
2. Filtro de admisión: la lección procede de la normativa o la guía, se observó en 2 o más
   títulos de 2 o más coordinaciones, o la aprueba la Unidad de Calidad. Si no, queda como
   **candidata**.
3. La skill no contiene datos, frases ni nombres de los casos de evaluación. Sus ejemplos
   literales proceden solo de títulos marcados como `conjunto = excluido` en `casos.csv`
   (hoy, GIM, cuyos autoinformes están en `samples/`), que nunca se evalúan. El aviso de
   huellas de `medir` lo comprueba; una frase suelta compartida con un título excluido del
   mismo centro es redacción común y puede quedarse.
4. El autoinforme humano es una referencia, no la verdad.
5. Elige el siguiente título por variedad; reserva algunos (`conjunto = reserva`) que no
   se usan para aprender y se evalúan en los hitos para detectar regresiones.
6. Cambios en la skill pequeños, versionados y aprobados por el responsable.
