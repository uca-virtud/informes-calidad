# Guía de redacción del análisis

El autoinforme no es un volcado de datos: es un **análisis reflexivo** del título por
parte de la coordinación y la CGC. Los indicadores son el apoyo; el valor está en la
interpretación y en las decisiones de mejora que se derivan.

> Para el estilo concreto (micro-formato de indicadores, codificación de puntos y
> acciones, ejemplos reales) usa `estilo-y-ejemplos.md`, y para el texto institucional
> común `../assets/bloques_reutilizables_uca.md`. Los principios y el convenio de colores
> valen para seguimiento y renovación; para lo específico de la renovación (periodo
> completo, puntos por curso, impacto, subcriterio 2.4, checklist) usa
> `estructura-renovacion.md`.

## Principios

- **Analiza la evolución**, no solo el último dato. Comenta tendencias en los años
  disponibles, comparaciones título vs. centro y, si procede, con la media de la
  UCA/rama. Recuerda que las tasas son dinámicas.
- **Contrasta la serie con la del autoinforme anterior**. En los cursos que aparecen en las
  dos fuentes, compara los valores de LinceBI con los publicados el año anterior. Si un
  indicador difiere de forma sistemática (p. ej. a la mitad o en otra escala), no analices
  su evolución entre esos cursos: explica la diferencia en una nota de fuente y deja
  `[PENDIENTE: verificar serie de …]`.
- **Relaciona indicador y decisión**. Todo indicador se comenta: si es favorable, puede
  dar lugar a un punto fuerte; si es desfavorable, explica su causa y si requiere acción.
  Solo se convierte en punto débil si la coordinación puede abordarlo con una acción
  propia (ver "Puntos fuertes y débiles"). No dejes indicadores "huérfanos" sin comentar.
- **Cita el indicador** por su código (p. ej. "la tasa de rendimiento —ISGC-P04-01—
  ha pasado del … al …") e indica que está en el Anexo 1.
- **No inventes**. Si falta un dato, escribe `[PENDIENTE: dato de …]`. Si un apartado no
  aplica (p. ej. prácticas externas, enseñanza virtual, título conjunto), indícalo o
  elimínalo según la plantilla.
- **Propuesta no es hecho**. Una acción del plan de mejora anterior, una recomendación de
  ACCUA o el texto modelo de la plantilla (reuniones con acta, coordinadores, periodicidades,
  procedimientos) no se describen como realizados en el curso salvo que la entrada lo
  acredite. Si no consta su ejecución, escribe que está prevista o en curso, o deja
  `[PENDIENTE: confirmar si se ha implantado …]`, y no des por resuelta la recomendación.
  Quitar el color no basta: relee cada frase del texto modelo que conserves en negro y
  borra o adapta las que no se correspondan con el título (modalidades, estructuras,
  supuestos condicionales). Del mismo modo, el estado de una estructura o acción que solo
  conoces por el autoinforme anterior no se da como vigente («según el autoinforme
  anterior…» y `[PENDIENTE: confirmar estado actual]`). Tampoco se juzga si una acción ha
  sido eficaz sin evidencia de que se implantó: separa implantación, evolución del
  indicador y efecto atribuible.
  Lo que dicen el autoinforme o el plan del curso anterior es un antecedente, no actividad
  del curso: reuniones, tutorías, «sin incidencias» o «no hubo …» se afirman solo con una
  evidencia fechada del curso. Si no la hay, el `[PENDIENTE]` cubre la ejecución misma,
  no solo su enlace. Una causa explicativa sin fuente (cambio de escala, de procedimiento
  o de plan) se redacta como hipótesis («podría deberse a…») y se descarta si la propia
  serie, del título o del centro, la contradice.
- **Datos de identidad, de la memoria**. La habilitación para una profesión regulada, la
  modalidad, las plazas y los centros se toman de la memoria verificada, sin deducirlos de
  las competencias, del perfil profesional o de sellos de calidad.
- **Cero no es «sin dato»**. No dejes guiones ni celdas vacías ambiguas. Si el valor
  no está en LinceBI, búscalo antes en toda la entrada (autoinforme anterior, informes,
  anexos), con el mismo indicador, ámbito y curso. Si no aparece, escribe
  `[PENDIENTE: dato de …]` o «No disponible», indicando el motivo.
  Mantén distintos «cero», «no calculado», «sin respuestas» y «no disponible» en el JSON,
  en las tablas y en el texto. Un guion de la fuente no se convierte en 0 ni se narra como
  ausencia («no hubo …», «ninguna persona …») salvo que la fuente lo defina así o lo
  respalde un recuento; una nota tuya no basta. Tampoco quedan pendientes los datos
  normativos que da la memoria (p. ej. créditos de prácticas obligatorias) ni las columnas
  históricas que aporta el autoinforme anterior.
- **Antes de dejar algo pendiente, búscalo**. Un anexo o tabla con fuente en LinceBI se
  extrae del informe previsto en el mapa de indicadores. Un total, un agregado o un enlace
  genérico a la plataforma no sustituyen la tabla exigida. El anexo se entrega completo, o
  con un enlace específico al informe íntegro del mismo curso; nunca condicionado a «si se
  requiere». Antes de declarar interna o no disponible una tabla de un anexo, consulta el
  informe exacto que indica el mapa para ese anexo, con el curso del autoinforme.
- **Concluye solo lo que mide el indicador**. No deduzcas un indicador a partir de otro
  (p. ej. la nota de corte a partir de la preferencia). Evita «garantiza», «todas cumplen»
  o «en todos los casos» salvo que lo hayas comprobado indicador a indicador. Los adjetivos
  de evolución («continuado», «por cuarto curso consecutivo») se comprueban con toda la
  serie, y la comparación con un objetivo de la memoria solo se hace con la tasa que lo
  tiene, en todas sus apariciones (análisis, puntos fuertes y síntesis).
  Comprueba el signo de cada evolución, en el título y en el centro, y que «el más bajo» o
  «el más alto» lo sea en todo el conjunto citado. «Mayoría», «suficiente», «estable» o
  «representativo» exigen comprobar el universo, las categorías y el cálculo (menos de la
  mitad no es mayoría). Un rasgo no sustituye a otro afín: la cualificación del profesorado
  no acredita su estabilidad.
- **Plantilla depurada por su sentido, no solo por su color**. Tras el paso 4b, resuelve
  los avisos `REVISAR` del script y relee el texto en negro que queda: elimina las órdenes
  al redactor («especificar…», «rellenar solo en su caso», notas de cumplimentación de
  tablas) y las alternativas que no proceden para el título (Grado/Máster, modalidades,
  opciones de un apartado), y conserva las definiciones de campo. Las tablas que la
  plantilla exige (p. ej. objetivos de la memoria antes del análisis de las tasas) se
  incluyen con sus notas.
- **La síntesis de sostenibilidad (7.6) cierra el autoinforme**. Recorre demanda,
  profesorado, recursos, resultados e inserción laboral, responde a las debilidades que
  señaló ACCUA y termina con una valoración explícita proporcionada a los datos (ver
  `estilo-y-ejemplos.md`, «Sostenibilidad»).
- **Tono**: institucional, claro y concreto. Evita generalidades vacías; aporta cifras,
  fechas, enlaces y responsables.

## Convenio de colores de la plantilla

- **Negro** = recomendaciones de redacción. Puedes reescribirlas con el contenido real
  del título.
- **Rojo** = instrucciones de cumplimentación. **Eliminar** antes de presentar.
  `depurar_instrucciones.py` borra todo el rojo salvo las excepciones que declara en su
  cabecera (p. ej. el recordatorio de lo que debe estar publicado). Si el Servicio de Gestión
  de la Calidad pide conservar otro texto en rojo, añádelo como excepción en el script; no lo
  restaures a mano en el documento.
- **Azul** = directrices de ACCUA. **Eliminar** antes de presentar.
- Sustituye todos los marcadores `XXXX`, `xxxx`, `http://xxxxxx.uca.es` por los datos
  reales del título/centro.

## Puntos fuertes y débiles (seguimiento)

- Solo los **del presente autoinforme** (no arrastres los de años anteriores a estas
  tablas; los débiles no resueltos sí van al plan de mejora).
- **Todos los puntos débiles con evidencia**, sin tope: satisfacción por debajo de 2,5,
  tendencia negativa durante dos cursos seguidos u otro hecho documentado que requiera
  mejora. Una variación puntual sin tendencia se analiza en el texto, pero no es punto
  débil. Todos pasan al plan de mejora.
- **Las recomendaciones de ACCUA no son puntos débiles**: van solo en la tabla del
  criterio 2 y en el plan de mejora. Un punto débil propio puede tratar el mismo asunto si
  el análisis de este curso lo evidencia, pero sin copiar la recomendación.
- Cada **punto débil** enlaza con una o varias **acciones de mejora**. La numeración la
  pone el script: ordinales con el curso delante en los fuertes y números correlativos en
  todo el autoinforme en los débiles.
- Redacta puntos concretos y verificables, apoyados en indicadores o hechos. Los puntos
  fuertes pueden ser también de proceso (p. ej. agilidad en el reconocimiento de créditos,
  convocatorias de TFG frecuentes), no solo de indicadores.

## Plan de mejora (seguimiento)

- Un solo **responsable** por acción. Si es externo al centro (un servicio central, otra
  facultad), añade `[PENDIENTE: autorización del responsable externo]`.
- Las columnas conservan la denominación exacta de la plantilla.
- Incluye: todas las recomendaciones vivas del último informe ACCUA (hasta que la
  agencia las cierre) + todos los puntos débiles de este autoinforme + los puntos
  débiles no resueltos del plan anterior.
- Lee entero el informe de ACCUA. Las recomendaciones de informes anteriores que declare
  no resueltas o resueltas en parte siguen vivas: inclúyelas con su número y fecha
  originales.
- Cada acción con prioridad (Alta/Media/Baja), fechas de inicio y fin en formato MM/AAAA,
  concretas o estimadas (nunca «Permanente», «Continua» ni «Finalizada»: el cierre lo
  decide ACCUA), e indicador de seguimiento con su valor actual en la última columna (en
  la renovación, la serie de los cinco últimos cursos; sin dato, «-» o «No procede»).
- Cada acción lleva sus evidencias, con enlace directo, en una línea separada. Un
  indicador no es una evidencia: es el resultado que la evidencia sustenta.
- Si la recomendación pide «analizar las causas», la acción dice cómo se analizarán y qué
  se hará con las conclusiones. Si falta la satisfacción de empleadores, la acción son las
  actividades para conocerla y la evidencia, su informe o acta.
- Las recomendaciones de ACCUA se copian literales, una por fila, con su número original
  y sin estados («en curso»). La tabla del criterio 2 y el plan coinciden exactamente: su
  segunda columna (recomendación) es la primera del plan y su tercera (acciones y
  evidencias, con los enlaces) es la segunda. El script las genera de la misma fuente; no
  las edites por separado.
- Para anticipar lo que ACCUA suele pedir y no repetir sus recomendaciones, revisa
  `recomendaciones-accua.md`.

## Formato, enlaces y entrega (guía rápida del Servicio de Gestión de la Calidad)

- **Estructura de la plantilla intacta**: no reorganices ni renumeres apartados. Un
  apartado sin contenido se elimina o lleva «No procede». Conserva las subdivisiones de
  cada subcriterio (sus apartados y los aspectos que ACCUA pide valorar): analiza cada una
  o márcala «No procede» con el motivo; no las fundas en un texto único. No repitas en
  varios apartados la misma información, enlace o indicador: analízalo donde corresponda y
  remite a él.
  Separa bien los párrafos.
- **Indicadores**: cada mención lleva nombre, código y curso analizado (el de la
  convocatoria, recogido en el Anexo I). En el criterio 7, los datos de egresados se
  refieren a **cohortes**, no a cursos académicos.
- **Anexos**: con el formato del modelo. El Anexo I reproduce literalmente las tablas de
  LinceBI. En los Anexos II, III y IV ninguna celda queda en blanco: «-» o «No procede».
- **Enlaces**:
  - No enlaces herramientas a las que no acceden los evaluadores: LinceBI, GADES, ICARO,
    Campus Virtual y similares. Cítalas como fuente sin enlace y enlaza la evidencia
    publicada o en UCADrive. La depuración avisa de ellos con `REVISAR`.
  - Cada evidencia, a un máximo de dos clics: enlaza el documento concreto, no la portada
    de la web ni una carpeta genérica.
  - Los enlaces van activos, en azul y subrayados. Si hay que acortar una URL, se usa el
    acortador de la UCA (https://url.uca.es/redir/crear): otros fallan o añaden un paso
    intermedio que suma clics. La skill no acorta URL; lo hace la coordinación si lo
    necesita.
  - UCADrive: acceso interno, nunca un enlace público. Lleva la ruta para localizar la
    evidencia y el enlace directo al fichero (ver «Indicaciones del Servicio de Gestión de
    la Calidad» en `SKILL.md`).
- **Versión que se envía** (la prepara la coordinación; recuérdalo en la entrega): todos
  los `[PENDIENTE]` resueltos, todo el texto en negro, sin comentarios ni resaltados, todos
  los enlaces probados. El PDF definitivo **no lleva firma digital**, porque rompe los
  enlaces: la aprobación del centro, firmada, se añade como anexo en la última página.

## Apartados que solo aplican a Seguimiento ACCUA

El borrador cumple siempre todo lo que pide ACCUA, vaya o no el título a ACCUA ese año;
la coordinación decide cuánto profundiza. Si el título no va a ACCUA, elimina solo la
tabla de aplicaciones de la identificación y no cites la auditoría de la información
pública, que el Servicio de Gestión de la Calidad hace solo a los títulos que van. Si va,
cita esa auditoría como evidencia y prepara además: guías docentes, información de cinco
asignaturas obligatorias representativas (incl. TFG/TFM y prácticas), pruebas de
evaluación que cubran todo el espectro de calificaciones y, en su caso, memorias de
prácticas.

## Checklist final del seguimiento (verificación antes de entregar)

1. Encabezado con curso y convocatoria correctos; tabla de identificación completa.
2. Columnas de años de las tablas de indicadores acordes a la convocatoria, y las de
   egresados con las cinco últimas cohortes con datos; los resultados globales del 6.3
   cubren seis cursos (el más antiguo, del autoinforme anterior).
3. Indicadores extraídos de producción (`data.uca.es`), con entorno y fecha indicados;
   ningún indicador de satisfacción por encima de 5; misma alineación de cohortes en las
   tablas de egresados del título y del centro.
4. No queda texto en rojo/azul (instrucciones/directrices) ni marcadores `XXXX`, tampoco
   en celdas de tablas ni dentro de párrafos con análisis; sí queda, en negro y con un
   enlace por elemento, el recordatorio de información pública del criterio 1.
5. Cada criterio tiene análisis real en todos sus subcriterios aplicables.
6. Todos los puntos débiles con evidencia, cada uno con su acción de mejora; el plan de
   mejora consolida ACCUA + débiles, con fechas MM/AAAA y sin acciones «Permanente» ni
   «Finalizada».
7. Recomendaciones de ACCUA literales, una por fila y con su numeración original.
8. Los indicadores citados en el texto coinciden con los del Anexo 1, y los objetivos de
   la memoria se comparan con la tasa a la que corresponden.
9. Enlaces reales (web del título, página de la CGC, normativas, actas, rutas UCADrive)
   en lugar de placeholders; cada evidencia de UCADrive en su subcriterio, con su ruta
   completa y `[PENDIENTE: usuario y contraseña de UCADrive]`.
10. Apartados no aplicables eliminados o marcados como «No procede».
11. Ninguna acción propuesta, recomendación o texto modelo aparece como ya ejecutado sin
    evidencia en la entrada; la habilitación profesional coincide con la memoria; el texto
    modelo conservado en negro se ha releído y se corresponde con el título; la actividad
    del curso no se apoya solo en el autoinforme anterior y las causas sin fuente figuran
    como hipótesis.
12. Ninguna celda con «-» o vacía sin explicación; ningún guion convertido en 0 o narrado
    como ausencia sin definición de la fuente o recuento; cada `[PENDIENTE]` corresponde a
    un dato que no está en la entrada (memoria y autoinforme anterior incluidos) ni en el
    informe de LinceBI previsto en el mapa.
13. Están todas las recomendaciones vivas de ACCUA, también las de informes anteriores que
    el último declara abiertas.
14. Ninguna conclusión va más allá de lo que mide su indicador ni generaliza sin
    comprobarlo; los adjetivos de evolución y las comparaciones con objetivos coinciden
    con toda la serie y con la memoria en todas sus apariciones; los signos de evolución
    (título y centro), los extremos y los cuantificadores («mayoría», «suficiente») están
    comprobados con el cálculo.
15. Los cursos comunes con el autoinforme anterior están contrastados y las diferencias
    sistemáticas explicadas.
16. No quedan restos de plantilla en negro: notas de cumplimentación, opciones alternativas
    («Grado/Máster»), filas de ejemplo ni enlaces pegados al texto siguiente; los avisos
    `REVISAR` de la depuración están resueltos y están las tablas que exige la plantilla.
17. La síntesis de sostenibilidad (7.6) cubre demanda, profesorado, recursos, resultados e
    inserción, responde a las debilidades de ACCUA y cierra con una valoración explícita.
18. Guía rápida: ninguna recomendación de ACCUA en las tablas de puntos débiles; tabla del
    criterio 2 y plan coincidentes; cada acción con su evidencia (ningún indicador como
    evidencia) y sin fechas «Finalizada»; responsables externos con su autorización
    pendiente; ningún enlace a LinceBI, GADES, ICARO o Campus Virtual; ninguna información,
    enlace o indicador repetido entre apartados; indicadores con nombre, código y curso;
    datos de egresados por cohortes; ninguna celda en blanco en los Anexos II–IV; todas las
    subdivisiones de cada subcriterio conservadas.
19. Repasados los temas que ACCUA pide de forma recurrente en cada criterio
    (`recomendaciones-accua.md`): los que aplican al título están analizados o tienen
    acción en el plan.