# Estilo y ejemplos reales de redacción

Patrones extraídos de un autoinforme de seguimiento real de la UCA ya presentado
(Grado de la ESI, curso 24/25). Reprodúcelos para que el borrador "suene" como los que
elabora la coordinación. Adapta siempre los datos concretos al título en cuestión.

## Estructura de cada subcriterio

1. **Reproduce el enunciado de la directriz** (el texto del subcriterio, p. ej. "3.1 El
   diseño del título está actualizado y se revisa periódicamente…") como encabezado o
   frase inicial.
2. **Narrativa**: explica cómo el título cumple la directriz, citando normativa (con su
   código UCA), la web del título/centro, aplicaciones (GADES, ICARO, GOA, SIRE, CAU,
   BAU, tfgm.uca.es), rutas del repositorio Colabora, comisiones y actas.
3. **Análisis de indicadores** del subcriterio, uno por párrafo (ver micro-formato).
4. **Remisión a anexos**: "Los valores se recogen en el Anexo I"; tablas en Anexos II-IV.

## Micro-formato de análisis de un indicador

`ISGC-Pxx-yy: <nombre del indicador>. <valor actual con unidad> + <evolución> +
<comparación con objetivo de memoria o con centro/UCA, si procede> + <interpretación o
causa> + <acción de mejora si el dato lo justifica>.`

Ejemplos reales (adáptalos, no los copies literalmente):

- «ISGC-P01-01: Grado de satisfacción del alumnado con la información publicada del
  Título. El indicador ha disminuido levemente (valor de 3,23 sobre 5 este curso). En
  general, este valor se mantiene estable, por encima de 3 durante los últimos cursos.
  Esto puede deberse a que ha habido pocos cambios en la web del título durante este
  curso.»
- «ISGC-P04-05: Tasa de graduación. Este valor tan bajo (10,60%), inferior al objetivo de
  la memoria (20±5%), se relaciona con la alta empleabilidad que tienen los estudiantes
  de este grado incluso antes de finalizar los estudios. Esto provoca que, en muchas
  ocasiones, el estudiante comience a trabajar antes de realizar su TFG.»
- «ISGC-P05-06: Porcentaje de calificaciones "EXCELENTES"… se sitúa en promedio al
  72,44%. El valor del curso 2023-24 es de 83,33%, mientras que ha bajado al 54,55% en
  el 2024-25, situación que consideramos puntual, como demuestra el conjunto de
  indicadores en los últimos cinco años (68,75% | 77,78% | 77,78% | 83,33% | 54,55%).»

Notas de estilo: valores con coma decimal y "sobre 5" en satisfacciones; vocabulario de
evolución ("se mantiene estable", "ha disminuido/aumentado levemente", "tras un descenso
…"); primera persona del plural institucional ("contamos con", "consideramos").

## Comparación con objetivos de la memoria (Criterio 6)

Antes de analizar P04-01 a 07, incluye una **tabla** con los objetivos de la memoria
verificada (columna "Valor esperado (Memoria)") y compara cada tasa con su objetivo.
Ejemplo real (Ingeniería Informática): tasa de graduación 20%, abandono 25%, eficiencia
60%, éxito 50%. Estos valores están en el apartado "Resultados previstos" (§8.1) de la
memoria: pídela al usuario si no se conocen. Asocia cada valor a la **tasa que indica la
memoria** (en algún título el 50 % corresponde al rendimiento, no al éxito); no lo copies
del autoinforme anterior sin comprobarlo. Es habitual agrupar P04-01/02/03 en un mismo
comentario y detallar por separado abandono, graduación (relacionándola con la
empleabilidad y la tasa de no presentados del TFG), eficiencia y duración media.

## Análisis de calificaciones por asignatura (Criterio 6.3 y Anexo IV)

El Criterio 6.3 no se limita a las tasas globales: incluye un **análisis de las
calificaciones por asignatura** a partir del informe `PorcentajeCalificaciones` de LinceBI
(Anexo IV). Es una parte sustancial del criterio en los autoinformes reales. Redáctalo así:

- Identifica y nombra las **asignaturas con tasa de suspensos alta** (p. ej. por encima
  del 25-30%), como puntos de vigilancia, e indica el porcentaje.
- Señala las asignaturas con **alto porcentaje de No Presentados** (p. ej. > 35%),
  interpretando posibles causas (complejidad, sobrecarga, TFG).
- Destaca en contraste las **asignaturas de excelencia** (alto % de Notable/Sobresaliente).
- Cierra relacionando este perfil con el cumplimiento de los objetivos de la memoria.

Ejemplo real (extracto): «…se identifica un grupo de asignaturas donde la tasa de
suspensos supera el 25%… Destacan Sistemas Distribuidos (41%), Estructuras de Datos no
Lineales (35%)… En contraste, Ingeniería de Sistemas de Información, donde el 95% del
alumnado se sitúa en el rango de excelencia (77% Sobresaliente)…».

## Nota sobre P01-03 (PTGAS)

El indicador ISGC-P01-03 (satisfacción del PTGAS) se analiza **a nivel de centro** (no de
título), siguiendo la recomendación de ACCUA. Indícalo al comentarlo.

## Datos de LinceBI: entorno de producción

Extrae los indicadores del entorno de **producción** (`data.uca.es`). Los datos del
entorno de pruebas (`datapru.uca.es`) pueden diferir mucho de los definitivos (en las
evaluaciones, una tasa de graduación del 7,5 % apareció como 16,4 %). Si detectas que
estás en pruebas, detente y avisa. Cuando cites la tasa de graduación, recuerda que es un
valor dinámico y que depende de la fecha de extracción.

## Egresados (P07-05 a 10): cohortes y participación

Analiza en el 7.5 **la cohorte más reciente encuestada** (convocatoria 2026: 2023-24).
Advierte siempre que los valores son **por cohorte de egreso** (no por curso académico) y
señala la **tasa de participación** con el número de encuestas y de egresados: p. ej.
«son los de la cohorte 2023-24 y se han conseguido con una tasa de participación del
29,55% (13 encuestas de 44 egresados)». Si la participación es muy baja (p. ej. 2 de 28),
indica que el porcentaje no permite obtener conclusiones.

## "No procede"

Para subcriterios no aplicables al título (p. ej. 4.6 y 5.5 enseñanza híbrida/virtual si
es presencial), escribe simplemente «No procede.» tras el enunciado, o elimina el
apartado según indique la plantilla.

## Codificación de puntos fuertes/débiles y acciones

Sigue el esquema del ejemplo real, usando el acrónimo del centro:

- Punto fuerte: `PF-<CENTRO>-<criterio>.<n>.- <texto>` (p. ej. `PF-ESI-6.1.- La tasa de
  éxito y de eficiencia se mantienen, por encima de los valores objetivo.`)
- Punto débil: `PD-<CENTRO>-<criterio>.<n>.- <texto>`
- Acción de mejora: `AM-<CENTRO>-<criterio>.<n>.- <texto>`

Cada punto débil enlaza con su acción (mismo número). Redacta puntos concretos y
apoyados en indicadores o hechos del curso analizado. Limita los puntos débiles a los que
la coordinación asumirá con acción propia (entre 1 y 5 en todo el autoinforme; ver
`guia-redaccion.md`).

## Tabla de recomendaciones ACCUA (Criterio 2)

Reproduce, tal cual, del último informe ACCUA: la **fecha del informe**, cada
recomendación con su tipo y **numeración original** (`Subsanación 1.1.- …`,
`Recomendación 2.1.- …`), sin renumerarlas aunque el autoinforme anterior lo haya hecho,
y, en la tercera columna, la **acción de mejora** que le da respuesta (con evidencia).
Mantén TODAS las recomendaciones hasta que ACCUA las dé por cerradas.

Para la composición de la CGC, remite a su página en la web del título o del centro en
lugar de enumerar a sus miembros.

## Plan de Mejora (columnas reales)

`Recomendación ACCUA o punto débil | Acciones de mejora a desarrollar | Prioridad |
Responsable (uno) | Fecha de inicio | Fecha de finalización | Indicador de seguimiento`.
Consolida: recomendaciones ACCUA vivas + puntos débiles de este autoinforme + débiles no
resueltos del plan anterior.

## Sostenibilidad (7.6)

Redáctala como **síntesis transversal** que recoge conclusiones de los Criterios 3
(demanda: preferencia/ocupación), 4 (profesorado), 5 (recursos) y 6 (tasas), cerrando con
una valoración explícita ("consideramos que el título es sostenible").

## Contenido institucional reutilizable

Gran parte de los Criterios 1, 2, 5 y 7 es texto institucional común a la UCA (SGC,
servicios de orientación, CAU/BAU/SIRE, Campus Virtual, DOCENTIA, ORI…), casi idéntico
entre títulos. Está recopilado en `assets/bloques_reutilizables_uca.md`: reutilízalo
cambiando solo lo específico del título/centro, y verifica versiones y fechas (el SGC y
las normativas se actualizan).
