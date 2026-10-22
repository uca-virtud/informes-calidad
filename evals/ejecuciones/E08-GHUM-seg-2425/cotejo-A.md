# Cotejo A — E08-GHUM-seg-2425

<!-- Plantilla común para el autocotejo (A) y el segundo corrector (B). Conserva los títulos y las
cabeceras de las tablas: `evaluacion.py medir` las lee. Una fila por elemento; sin celdas
combinadas. Rúbrica: docs/evaluacion/rubrica.md. -->

- Corrector: A (autocotejo)
- Modelo: claude-opus-5.5
- Versión de la rúbrica: 2
- Fecha: 2026-10-21

## Puntuación

| Dimensión | Nota | Evidencia |
|---|---|---|
| D1 | 2 | Identificación completa y coincidente con la del humano (ID 2501746, implantación 2010-11, renovación 18/07/2023, modalidad presencial, sin título doble). El número de plazas (criterio 3.3) sigue la memoria aportada (55) y la diferencia con el autoinforme anterior (35) queda señalada como [PENDIENTE], conforme a la skill. |
| D2 | 2 | En el Anexo I coinciden casi todos los valores del título (P01, P04-01 a P04-04, P04-08 a P04-19, P05, P06 y P07 de 2020-21 a 2023-24). Las diferencias se explican por recálculos de LinceBI (P04-05 2023-24, P04-06, P04-07, P04-13 y varias cifras del centro) o por errores del humano (P04-05 2024-25, P07-05 y la columna 2024-25 de P07-01/02/03/04, copiada de 2020-21). Más del 95 % de los valores comparables coincide o difiere por causa D, I o H. |
| D3 | 2 | Los siete criterios y todos sus subcriterios tienen análisis con indicadores, evolución y comparación con el centro. Los 53 [PENDIENTE] se refieren a datos internos (reconocimientos de créditos, quinquenios, proyectos de innovación, convenios de prácticas, evidencias de las acciones ACCUA) o a verificaciones que la coordinación debe hacer (serie P04-13, plazas). |
| D4 | 2 | Redacción en primera persona del plural, con cifras, sin plantillas sin rellenar y con lenguaje institucional adecuado. El humano conserva marcadores sin rellenar («Grado en …», «[analizar evolución del indicador]»). |
| D5 | 2 | Tres PD gestionables por la coordinación (entre ellos PD-FFL-5.1, satisfacción con las prácticas externas), cada uno con acción de mejora, responsable y plazo. El humano no formula ningún PD propio en el plan de mejora. |
| D6 | 2 | Las 12 recomendaciones vivas del informe ACCUA aparecen con su numeración original, en el criterio que corresponde y en el plan de mejora, con acción y estado; la evidencia de cierre queda [PENDIENTE] al no aportarse. |
| D7 | 2 | Documento limpio, fiel a la plantilla de seguimiento, con códigos PF/PD/AM-FFL-crit.n y anexos ordenados. |

## Bloqueantes

| Bloqueante | ¿Hay? | Detalle |
|---|---|---|
| B1 | no | Todos los valores proceden de LinceBI o de los documentos de entrada; lo que no consta queda [PENDIENTE]. |
| B2 | no | Ningún valor imposible ni el mismo indicador con dos valores distintos para el mismo ámbito y curso. La serie anómala de P04-13 se presenta una sola vez y se señala para verificar. |
| B3 | no | El bloque `extraccion` de datos.json registra el host data.uca.es y la fecha 2026-10-21. |

## Discrepancias

Solo las relevantes (no cada diferencia de redondeo; agrúpalas en una fila si comparten causa).

| Nº | Apartado | Borrador | Autoinforme humano | Causa | Explicación |
|---|---|---|---|---|---|
| 1 | Criterio 3.3, plazas de nuevo ingreso | 55 plazas (memoria), con [PENDIENTE] por la diferencia con las 35 del autoinforme anterior | 35 plazas | I | La memoria aportada recoge 55 y el autoinforme anterior 35; la oferta real del curso es un dato del centro que no se aportó. El borrador aplica la regla de la skill y deja la duda señalada. |
| 2 | Anexo I, P04-05 tasa de graduación 2023-24 | 45 % | 25 % | D | El humano coincide con el autoinforme anterior; LinceBI ha recalculado el valor. |
| 3 | Anexo I, P04-05 tasa de graduación 2024-25 | 42,9 % | 28,6 % | H | El propio texto del humano da 42,9 %; 28,6 % es la tasa de abandono trasladada a la fila equivocada. |
| 4 | Anexo I, P04-06 y P04-07 (título) | Eficiencia 88,4 % / 83,3 %; duración 6,8 años | 88,2 % / 82,1 %; 7 años | D | Diferencias pequeñas por recálculo de LinceBI tras la extracción del humano. |
| 5 | Anexo I y criterio 5.3, P04-13 2021-22 a 2023-24 | 1,5 / 2,42 / 2,46, con [PENDIENTE] por posible cambio de escala | 3 / 4,83 / 4,91 | D | LinceBI devuelve hoy la serie a la mitad de los valores del autoinforme anterior. El borrador lo detecta y no analiza la evolución. |
| 6 | Anexo I, P05-04 2024-25 | 4,5 | «4,6 %» | D | Diferencia mínima, probablemente por recálculo; el humano añade además un «%» que no corresponde a una escala de 1 a 5. |
| 7 | Anexo I, P04-01 a P04-13 y P05-04 (centro) | Valores de LinceBI actuales (p. ej. graduación del centro 46,9 % en 2024-25) | Valores del autoinforme anterior o próximos (32,1 %); P04-13 del centro 9,61 en 2024-25 | D | Recálculos de LinceBI en varias series del centro. El 9,61 del humano en una escala de 1 a 5 es además un error del humano. |
| 8 | Anexo I, P07-05 2019-20 a 2021-22 (título) | 50 / 25 / 50 % | 6,25 / 7,69 / 16,67 % | H | El autoinforme anterior y LinceBI coinciden con el borrador. |
| 9 | Anexo I, P07-01_01, P07-01_02, P07-02, P07-03 y P07-04, columna 2024-25 | 83,87 % / 39,71 % / 3,45 / 3,62 / 3,82 | 46,48 % / 52,63 % / 3,31 / 3,93 / 3,81 (copia de 2020-21, también en el centro) | H | El texto 4.8 del humano da 3,62 para P07-03, como el borrador. |
| 10 | Anexo I, P01-03 (título) | Valores del centro rotulados como tales | «-» | E | El indicador de satisfacción del PTGAS solo existe a nivel de centro; es una decisión de presentación. |
| 11 | Plan de mejora, puntos débiles | Tres PD con acciones, responsables y plazos | Ninguno; solo las recomendaciones ACCUA | H | La plantilla exige identificar los puntos débiles del curso evaluado, y los indicadores señalan al menos los recogidos en el borrador. |
| 12 | Criterios 1-7 y plan de mejora, recomendaciones ACCUA nº 1-12 | Abiertas, con la acción prevista y [PENDIENTE] para la evidencia | Acciones ejecutadas con enlaces a UCADrive | I | No se aportaron las evidencias internas; el borrador no da por cerradas acciones sin respaldo. |
| 13 | Criterios 2, 4 y 5 y Anexo III | [PENDIENTE] en quinquenios, proyectos de innovación y convenios de prácticas | 151 quinquenios, 18 docentes en proyectos de innovación, 2 entidades con 3 plazas y 2 tutores | I | Datos internos del centro no aportados. |
| 14 | Criterios 1, 2 y 7 | Contenido limitado al curso 2024-25 | Encuesta a empleadores 2025-26, auditoría de la IPD de mayo de 2026, plan de contingencia 2026-27, satisfacción 2025-26 | H | El seguimiento evalúa 2024-25; el humano incorpora hechos posteriores al periodo. |
| 15 | Criterios 3, 5, 6 y 7 (texto) | Cifras coherentes con el Anexo I | Ocupación de «más del 50 % de las 35 plazas» (P04-17 = 32 %); abandono 28,6 % que «disminuye»; graduación 45 % y abandono 18,6 % en el plan; satisfacción con prácticas 4,33 (P04-14 = 3,26); tutores 4,6 (P04-12 = 4,4) | H | Incoherencias internas del humano entre texto, plan y anexo. |
| 16 | Todos los criterios, puntos fuertes | PF codificados (PF-FFL-crit.n) | PF por criterio sin código | E | Diferencia de formato; el borrador sigue la codificación de la skill. |

## Lecciones propuestas

Solo para discrepancias de causa **S**. Una lección es una regla general para la skill, nunca un
dato del título (ni valores, ni nombres, ni frases del autoinforme humano).

Ninguna: no hay discrepancias de causa S.

| Lección | Regla general propuesta | Discrepancias | Respaldo | Fichero de la skill |
|---|---|---|---|---|

## Comentario general

El borrador reproduce casi todos los indicadores de LinceBI, analiza todos los subcriterios, formula tres puntos débiles gestionables con sus acciones y recoge las doce recomendaciones de ACCUA con su numeración. Las diferencias con el autoinforme humano se deben sobre todo a recálculos de LinceBI y a errores del humano (columnas de 2024-25 copiadas de 2020-21, cifras del texto que no cuadran con el anexo, hechos posteriores al curso). Antes de usarlo, la coordinación debe completar los [PENDIENTE] con los datos internos y las evidencias de las acciones ACCUA. También debe confirmar el número de plazas ofertadas y verificar la serie de ISGC-P04-13.
