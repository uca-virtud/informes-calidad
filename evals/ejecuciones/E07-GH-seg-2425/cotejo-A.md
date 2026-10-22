# Cotejo A — E07-GH-seg-2425

<!-- Plantilla común para el autocotejo (A) y el segundo corrector (B). Conserva los títulos y las
cabeceras de las tablas: `evaluacion.py medir` las lee. Una fila por elemento; sin celdas
combinadas. Rúbrica: docs/evaluacion/rubrica.md. -->

- Corrector: A (autocotejo)
- Modelo: claude-opus-5.5
- Versión de la rúbrica: 2
- Fecha: 2026-10-04

## Puntuación

| Dimensión | Nota | Evidencia |
|---|---|---|
| D1 | 2 | Tabla de identificación con ID 2501745, implantación 2010/2011, web, modalidad presencial, sin doble título y renovación 05/07/2023, igual que el humano. El `[PENDIENTE: confirmar fecha]` está justificado porque el autoinforme anterior da otra fecha (26/10/2022). «Estructuras curriculares» recoge los dos itinerarios de la memoria; el humano deja el campo vacío. |
| D2 | 2 | Unos 510 valores en las 14 tablas del Anexo I. Coinciden con el humano alrededor del 92 %, y el resto difiere por causas D, H o E (P04-05, P04-06, P04-13 y egresados P07-05 a 07 por volatilidad y cambio de fórmula; P07-09/10 de centro desplazados en el humano). No hay causas S. Cursos 2020-21 a 2024-25 y cohortes 2019-20 a 2023-24 bien alineados en todas las tablas. |
| D3 | 2 | Todos los subcriterios del 1.1 al 7.6 tienen análisis; 3.6, 4.6 y 5.5 se cierran con un «No procede» justificado. Los `[PENDIENTE]` afectan a datos internos no aportados (reconocimiento de créditos, sesiones de la CGC, Anexos II nominal y III, evidencias UCADrive) o no disponibles en LinceBI (resultados de primer curso). |
| D4 | 2 | Interpreta la evolución de cada tasa y la compara con el centro y con los objetivos de la memoria (tabla en 6.3: graduación y abandono cumplen; éxito 87,3 < 90). Explica la volatilidad de las tasas dinámicas y las cohortes de egresados. Como retoques: una causa sin fuente en 7.2 (véase B1) y un análisis de calificaciones por asignatura solo del curso 2024-25, sin evolución. |
| D5 | 2 | Puntos fuertes concretos y del curso. Cuatro puntos débiles (coordinación, formación del PDI, movilidad saliente, empleadores) con su acción, responsable y plazo en el plan de mejora; tres de ellos coinciden con los del humano. Códigos PF/PD/AM-FFL correctos. |
| D6 | 1 | Están las 12 recomendaciones del informe de 05/07/2023, con su texto literal, su tipo (subsanar/mejora) y acción y estado. Pero en la tabla del criterio 2 se agrupan por criterio (7 filas): varias recomendaciones comparten una sola celda de acción. La skill pide cada recomendación con su tipo, y el humano usa una fila por recomendación. |
| D7 | 2 | Documento fiel a la plantilla, sin texto rojo o azul, sin `XXXX` ni restos de instrucciones, en registro formal. El Anexo I lleva notas de fuente y de tratamiento de «-». |

## Bloqueantes

| Bloqueante | ¿Hay? | Detalle |
|---|---|---|
| B1 | sí | En 7.2 se afirma como hecho que «buena parte de los egresados continúa con estudios de máster (profesorado de Secundaria, patrimonio, archivística)». No procede de la entrada ni de LinceBI: solo el dato que lo respaldaría está en `[PENDIENTE]`. Es leve, pero es una afirmación no documentada. |
| B2 | no | Ninguna satisfacción supera 5 ni ninguna tasa acotada supera el 100 %. Cada indicador, ámbito y curso tiene un único valor en todo el borrador. |
| B3 | no | Extracción de data.uca.es con fecha 2026-10-04, registrada en `datos.json` y en la ficha. |

## Discrepancias

Solo las relevantes (no cada diferencia de redondeo; agrúpalas en una fila si comparten causa).

| Nº | Apartado | Borrador | Autoinforme humano | Causa | Explicación |
|---|---|---|---|---|---|
| 1 | Anexo I y 6.3, ISGC-P04-05 (título y centro) | Título 45,6 / 44 / 62,3 % (2022-23 a 2024-25); centro 39,1 / 46,9 % (2023-24, 2024-25) | Título 43 / 32 / 49,4 %; centro 37,9 / 29,6 % | D | Tasa dinámica que LinceBI recalcula. El humano repite para 2022-23 y 2023-24 los valores del autoinforme anterior. El borrador avisa de la volatilidad en 6.3 y en la nota del Anexo I. |
| 2 | Anexo I y 6.3, ISGC-P04-06 de 2024-25 | 91,7 %, «por debajo (−0,3 puntos)» del objetivo del 92 % | 92 %, «en la línea establecida en la memoria» | D | Valor de extracción distinto; cambia la valoración frente al objetivo por tres décimas. |
| 3 | Anexo I y 4.5, ISGC-P04-13 de 2021-22 a 2023-24 | Título 2,02 / 2,34 / 2,33; centro 1,52 / 2,35 / 2,35, con `[PENDIENTE: verificar la serie]` | Título 4,03 / 4,67 / 4,66; centro 2,67 / 4,7 / 4,71 | D | El borrador reproduce LinceBI en vivo y señala que la serie es la mitad de la publicada antes. El valor correcto requiere la Unidad de Calidad. |
| 4 | Anexo I, ISGC-P04-13 de centro en 2024-25 | 4,81 | 9,61 | H | Valor imposible en una escala de 1 a 5. |
| 5 | Anexo I, egresados: P07-05 de título (cohortes 2019-20 a 2021-22) y P07-05/06/07 de centro | Título 20,00 / 9,09 / 10,00; centro P07-05 34,38 / 25,53 / 33,33 | Título 3,70 / 3,92 / 5,77; centro P07-05 6,79 / 5,64 / 8,56 | D | El borrador copia LinceBI en vivo (`encue_RSGC_P07_3`). El humano parece aplicar la nueva fórmula (sobre egresados) a las cohortes antiguas. El borrador explica que la serie no es homogénea desde 2022-23. |
| 6 | Anexo I, egresados de centro: P07-09, P07-10 y P07-01_03 | P07-09 2,87 / 3,51 / 3,09 / 3,41 / 3,43; P07-01_03 2023-24 24,23 % | P07-09 2,92 / 2,87 / 3,51 / 3,09 / 3,43; P07-01_03 2023-24 4,23 % | H | El humano desplaza una cohorte las series de 2019-20 a 2022-23 (el título sí coincide) y comete una errata en la tasa de respuesta. |
| 7 | Anexo I, redondeos (centro P04-01 y P04-04 de 2024-25) y Anexo IV (Prehistoria de la Península Ibérica) | 78,6 %; 25,3 %; 18 % de aprobados | 78,5 %; 25,4 %; 17 % de aprobados | D | Diferencias de una décima o de un punto entre extracciones. |
| 8 | Anexo I, celdas sin dato (BAU, movilidad saliente internacional 2020-21, P07-07 2022-23) | 0 % con nota; «No disponible*» con nota | «-» o celda vacía | E | Misma información; el borrador explica el tratamiento en notas. |
| 9 | 6.3, tasa de graduación de 2024-25 | 62,3 % en el texto y en el Anexo I | 49,2 % en el texto y 49,4 % en el Anexo I | H | Incoherencia interna del humano, además de la diferencia de extracción de la fila 1. |
| 10 | Criterio 2 (tabla ACCUA) y plan de mejora | Una fila por criterio (7 filas) que agrupa las 12 recomendaciones; los criterios 2, 4, 5 y 7 tienen varias recomendaciones en la misma celda | Una fila por recomendación, cada una con su acción y evidencia | S | La skill pide cada recomendación con su tipo. Al no estar numeradas en el informe de ACCUA, el borrador las agrupó por criterio y diluyó la acción de cada una. |
| 11 | Criterios 1, 2 y 7 y plan de mejora: empleadores | «Sin datos de satisfacción de empleadores» en 2024-25 (PD-FFL-7.1), estado de la encuesta `[PENDIENTE]` | Encuesta del centro administrada en 2026 (28 respuestas), publicada en la web; puntos débiles 5 a 8 derivados de ella | I | Dato interno, posterior al curso evaluado y no aportado. El borrador es correcto con la entrada y lo dejó `[PENDIENTE]`. |
| 12 | 3.3, 2.x, 1.x, Anexos II y III, portada | `[PENDIENTE]` en reconocimiento de créditos, sesiones de la CGC, auditorías de la IPD, relación nominal del PDI, prácticas y convenios, fechas de aprobación y rutas UCADrive | Datos del centro (24 solicitudes y 158 créditos reconocidos, auditoría de mayo de 2026, tablas nominales, convenios…) | I | Datos internos no aportados, que quedaron `[PENDIENTE]` como indica la skill. |
| 13 | 6.3, calificaciones por asignatura | Asignaturas extremas de 2024-25 (suspensos, no presentados, excelencia) sin evolución temporal | Cinco asignaturas obligatorias de referencia comparadas con 2020-21, más la evolución global (3 % → 7 % de suspensos) | S | La skill solo pide los extremos del curso. El análisis queda estático y no conecta con las cinco asignaturas de las evidencias de seguimiento ACCUA. |
| 14 | 7.2, causa de la baja inserción | Continuación en másteres (con ejemplos), afirmada como hecho | No lo afirma | S | La IA no aplicó «propuesta no es hecho» a las causas: una hipótesis sin fuente se redactó como dato (B1). |
| 15 | Criterio 1, puntos débiles | Sin puntos débiles; analiza la valoración del alumnado (3,43) | Punto débil por el descenso de 3,68 a 3,43 en ISGC-P01-01 | E | Ambos analizan el mismo dato. Calificarlo como débil es criterio de la coordinación y la rúbrica no puntúa el número de puntos. |
| 16 | Identificación, estructuras curriculares específicas | Itinerarios de Historia de las Relaciones Internacionales y de Historia Cultural (memoria) | Vacío | E | Información de la memoria; el humano no la consigna. |

## Lecciones propuestas

Solo para discrepancias de causa **S**. Una lección es una regla general para la skill, nunca un
dato del título (ni valores, ni nombres, ni frases del autoinforme humano).

| Lección | Regla general propuesta | Discrepancias | Respaldo | Fichero de la skill |
|---|---|---|---|---|
| L01 | En la tabla de recomendaciones del criterio 2 y en el plan de mejora, una fila por recomendación, nunca agrupadas por criterio. Si el informe de ACCUA no las numera, identifícalas por criterio, tipo y orden dentro del criterio (p. ej. «Criterio 5 – subsanación 2») y da a cada una su propia acción, evidencia y estado. | 10 | Norma: plantilla de autoinforme (tabla de recomendaciones con una recomendación por fila) y la regla de la skill «cada recomendación con su tipo»; en otros títulos, ninguno aún | references/estilo-y-ejemplos.md |
| L02 | En el análisis de calificaciones por asignatura de 6.3, añade a los extremos del curso una comparación con un curso anterior de referencia (el primero de la serie del Anexo I o el de la última renovación), extraída de `PorcentajeCalificaciones`. En seguimiento ACCUA, analiza expresamente las cinco asignaturas obligatorias elegidas como evidencia (incluidos TFG y prácticas). | 13 | Ninguno aún | references/estilo-y-ejemplos.md |
| L03 | Redacta como hipótesis («podría deberse a…») y con `[PENDIENTE: confirmar]` las causas explicativas que no procedan de la entrada, de LinceBI o de la norma. No enumeres ejemplos concretos sin documento que los respalde. | 14 | Norma: rúbrica B1 y la regla «propuesta no es hecho» de la guía de redacción; en otros títulos, ninguno aún | references/guia-redaccion.md |

## Comentario general

El borrador es sólido en datos y análisis. Reproduce LinceBI en vivo con su fecha, explica las series volátiles o heterogéneas, compara con los objetivos de la memoria y del centro, y sus puntos débiles coinciden casi por completo con los de la coordinación. Fallan tres cosas: las recomendaciones de ACCUA están agrupadas por criterio en vez de una por fila, el análisis de calificaciones se queda en el curso 2024-25 y hay una causa en 7.2 afirmada sin fuente. Antes de usarlo, la coordinación debe:
- desdoblar la tabla de recomendaciones;
- eliminar o confirmar la frase sobre los másteres;
- revisar con la Unidad de Calidad la serie ISGC-P04-13 y los valores dinámicos de graduación y eficiencia;
- completar los `[PENDIENTE]` internos (empleadores 2026, reconocimiento de créditos, Anexos II y III, evidencias UCADrive).
