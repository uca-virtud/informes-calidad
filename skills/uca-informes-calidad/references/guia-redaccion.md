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
- **Azul** = directrices de ACCUA. **Eliminar** antes de presentar.
- Sustituye todos los marcadores `XXXX`, `xxxx`, `http://xxxxxx.uca.es` por los datos
  reales del título/centro.

## Puntos fuertes y débiles (seguimiento)

- Solo los **del presente autoinforme** (no arrastres los de años anteriores a estas
  tablas; los débiles no resueltos sí van al plan de mejora).
- **Pocos puntos débiles**: entre 1 y 5 en todo el autoinforme, como hacen las
  coordinaciones. Solo los que la coordinación asumirá con una acción propia; no conviertas
  cada indicador a la baja en un punto débil. Las demás debilidades se analizan en el
  texto y se proponen al usuario como candidatas.
- Cada **punto débil** enlaza con una o varias **acciones de mejora** numeradas.
- Redacta puntos concretos y verificables, apoyados en indicadores o hechos. Los puntos
  fuertes pueden ser también de proceso (p. ej. agilidad en el reconocimiento de créditos,
  convocatorias de TFG frecuentes), no solo de indicadores.

## Plan de mejora (seguimiento)

- Un solo **responsable** por acción.
- Incluye: todas las recomendaciones vivas del último informe ACCUA (hasta que la
  agencia las cierre) + todos los puntos débiles de este autoinforme + los puntos
  débiles no resueltos del plan anterior.
- Lee entero el informe de ACCUA. Las recomendaciones de informes anteriores que declare
  no resueltas o resueltas en parte siguen vivas: inclúyelas con su número y fecha
  originales.
- Cada acción con prioridad (Alta/Media/Baja), fechas de inicio y fin, y, si procede,
  indicador de seguimiento.

## Apartados que solo aplican a Seguimiento ACCUA

Si el título se presenta a ACCUA, prepara además: guías docentes, información de cinco
asignaturas obligatorias representativas (incl. TFG/TFM y prácticas), pruebas de
evaluación que cubran todo el espectro de calificaciones, y (en su caso) memorias de
prácticas. Si es solo seguimiento interno, puedes omitir estas evidencias y la tabla de
aplicaciones [T3].

## Checklist final del seguimiento (verificación antes de entregar)

1. Encabezado con curso y convocatoria correctos; tabla de identificación completa.
2. Columnas de años de las tablas de indicadores acordes a la convocatoria, y las de
   egresados con las cinco últimas cohortes con datos; los resultados globales del 6.3
   cubren seis cursos (el más antiguo, del autoinforme anterior).
3. Indicadores extraídos de producción (`data.uca.es`), con entorno y fecha indicados;
   ningún indicador de satisfacción por encima de 5; misma alineación de cohortes en las
   tablas de egresados del título y del centro.
4. No queda texto en rojo/azul (instrucciones/directrices) ni marcadores `XXXX`, tampoco
   en celdas de tablas ni dentro de párrafos con análisis.
5. Cada criterio tiene análisis real en todos sus subcriterios aplicables.
6. Entre 1 y 5 puntos débiles en total; cada uno con su acción de mejora; el plan de
   mejora consolida ACCUA + débiles.
7. Recomendaciones de ACCUA con su numeración original.
8. Los indicadores citados en el texto coinciden con los del Anexo 1, y los objetivos de
   la memoria se comparan con la tasa a la que corresponden.
9. Enlaces reales (web del título, página de la CGC, normativas, actas, rutas UCADrive)
   en lugar de placeholders.
10. Apartados no aplicables eliminados o marcados como "No aplica".
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
