# Cotejo A — E06-GIDIDP-seg-2425

- Corrector: A (autocotejo)
- Modelo: Claude (GitHub Copilot CLI; identificador exacto no expuesto en la sesión)
- Versión de la rúbrica: 2
- Fecha: 2026-10-03

## Puntuación

| Dimensión | Nota | Evidencia |
|---|---|---|
| D1 | 2 | Tabla de identificación: ID 2502561, implantación 2011-12, web, doble título (SÍ, con Mecánica), modalidad presencial, renovación de la acreditación 17/07/2023, 0 créditos obligatorios y estructuras curriculares «No». Todo coincide con el humano y con la entrada. |
| D2 | 2 | Anexo I: más del 95 % de los valores comparables coinciden. Las diferencias son de causa D (graduación de 2024-25, ajustes de una décima del centro, P04-13 de 2021-22 a 2023-24, valores de 2020-21 fuera de la ventana de LinceBI) o H (graduación de 2023-24 y egresados desplazados en el humano, P04-13 = 9,3 > 5). Cursos y cohortes bien alineados en todas las tablas. |
| D3 | 2 | Todos los criterios y subcriterios tienen análisis. Los `[PENDIENTE]` afectan a datos internos no aportados: créditos reconocidos de 2024-25 (no hay informe en LinceBI; comprobado con `lincebi_search_resources`), Anexo III de prácticas y fechas de aprobación de la CGC y la Junta. |
| D4 | 1 | Buena interpretación de la evolución y comparación con el objetivo correcto de la memoria (rendimiento 50±5 %). Dos fallos: (1) el criterio 2 afirma como vigente que la ESI no tiene SGC propio ni cuadro de mandos, cuando ese estado procede del autoinforme anterior y hoy ya no se cumple; (2) en 5.3 se valora una fuerte subida de P04-13 (2,40 → 4,66) con una serie de LinceBI que contradice los valores del autoinforme anterior (4,79 en 2023-24), sin señalar la diferencia. |
| D5 | 2 | Puntos fuertes concretos y del curso. Puntos débiles PD-ESI-4.1 (TFG) y PD-ESI-6.1 (asignaturas básicas) asumibles, con acción, responsable y plazo. Salvedad: se mantiene la acción heredada PD-ESI-2.1 (desarrollar el cuadro de mandos), que puede estar ya cumplida. |
| D6 | 2 | Están las 14 recomendaciones y subsanaciones del autoinforme anterior, con su numeración y con estado y acción. |
| D7 | 2 | Documento limpio: sin texto de instrucciones en rojo o azul, sin `XXXX`, con códigos PF/PD/AM-ESI-n.n y registro formal. |

## Bloqueantes

| Bloqueante | ¿Hay? | Detalle |
|---|---|---|
| B1 | no | Todos los valores proceden de LinceBI o de la entrada. La afirmación sobre el SGC y el cuadro de mandos sale del autoinforme anterior (está desactualizada, no inventada; se penaliza en D4). |
| B2 | no | No hay valores fuera de rango ni el mismo indicador, ámbito y curso con dos valores distintos dentro del borrador. |
| B3 | no | Extracción desde data.uca.es el 2026-10-03, registrada en datos.json y en ficha.md. |

## Discrepancias

Solo las relevantes (no cada diferencia de redondeo; agrúpalas en una fila si comparten causa).

| Nº | Apartado | Borrador | Autoinforme humano | Causa | Explicación |
|---|---|---|---|---|---|
| 1 | Anexo I, P04-05 título 2024-25 | 21,3 | 10,60 en el anexo y 12,8 en el plan | D | La tasa de graduación de la cohorte se recalcula según avanza la extracción. El humano también se contradice entre su anexo y su plan. |
| 2 | Anexo I, P04-05 título 2023-24 | 34,6 | 32,70 en el anexo y 34,6 en el plan | H | El propio plan del humano da el valor del borrador; su anexo es incoherente. |
| 3 | Anexo I, centro: P04-01, P04-03, P04-05, P04-07; título: P04-06 2024-25 | 62,3; 82,5; 17,8/17,5; 6,34; 74,3 | 62,20; 82,40; 17,40/7,30; 6,35; 75,10 | D | Diferencias de una décima o recálculo de cohortes entre las dos extracciones. El 7,30 del centro parece además una errata del humano. |
| 4 | Anexo I, P04-13 de 2021-22 a 2023-24 (título y centro) | Título 1,75/2,25/2,40; centro 1,91/2,32/2,25 | Título 3,5/4,5/4,79; centro 1,7/4,64/4,5 | D | Los valores del borrador son la mitad de los del humano y de los del autoinforme anterior aportado en la entrada. La serie actual de LinceBI difiere de la publicada; requiere revisión experta. El borrador no detectó la diferencia (ver nº 13). |
| 5 | Anexo I, P04-13 centro 2024-25 | 4,65 | 9,3 | H | Valor imposible en una escala de 1 a 5. |
| 6 | Anexo I, valores de 2020-21 (P01-01/02, P04-16 a 19, P06, P07 del centro; P07-01_01/02 del título) | «No disponible» | Con valores | D | La ventana de cursos de LinceBI ya no incluye 2020-21 para esos informes, y el autoinforme anterior no los trae. |
| 7 | Anexo I, egresados del título (P07-09/10) | Columna 2023-24: 29,55 % (13/44) | Columna 2023-24: 7,14 % (2/28) | H | La tabla del humano está desplazada una cohorte; su propio texto da 29,55 % (13/44). |
| 8 | Criterio 3, créditos reconocidos 2024-25 | `[PENDIENTE]` | 29 estudiantes y 436,5 créditos | I | LinceBI no tiene informe de créditos reconocidos (búsquedas «créditos reconocidos» y «reconocimiento» sin resultado pertinente). El dato es interno de la secretaría y quedó `[PENDIENTE]`. |
| 9 | Criterio 5.3, Anexo III; fechas de la CGC y la Junta | `[PENDIENTE]` | 19 plazas, 7 entidades; 24/03/2026 y 27/03/2026 | I | Datos internos no aportados; correctamente pendientes. |
| 10 | Criterio 2, SGC del centro | «La ESI no dispone todavía de un SGC propio ni de un cuadro de mandos» y se mantiene PD-ESI-2.1 | Hay cuadro de mandos de la ESI y Política de Calidad prorrogada el 18/07/2025 | S | El borrador trasladó como vigente un estado descrito en el autoinforme anterior, en lugar de marcarlo como pendiente de confirmar. |
| 11 | Criterio 1, objetivo de la memoria | Rendimiento 50±5 % | Atribuye el 50±5 % a la tasa de éxito | H | La memoria fija el objetivo para la tasa de rendimiento. |
| 12 | Criterio 5, profesorado (P05-01) y otros datos del texto humano | 64 profesores; nota de corte, P05-04 y P04-08 coherentes con el anexo | 128 profesores; nota de corte 9,841/9,851; P05-04 4,5/4,4; P04-08 «No hay valores», pero el anexo da 2,14 | H | Incoherencias internas del humano. Los 64 del borrador cuadran con los denominadores de P05 (28/64 = 43,75 %) y con los 18 TU. |
| 13 | Criterio 5.3, análisis de P04-13 | «alcanza 4,66 (2,40 en 2023-24)», es decir, presenta una fuerte mejora | 4,66 frente a 4,79, es decir, estabilidad | S | La entrada traía la serie publicada y el borrador no la contrastó con la de LinceBI, por lo que el análisis interpreta una subida que puede ser un artefacto. |
| 14 | Puntos débiles | PD-ESI-4.1 (satisfacción con el TFG y su asignación) y PD-ESI-6.1 (asignaturas básicas con >50 % de no presentados y suspensos) | Solo PD-ESI-3.1 (baja asignación de TFG) | E | Mismo problema del TFG con distinto criterio de ubicación. PD-ESI-6.1 es una debilidad adicional apoyada en datos de LinceBI. |
| 15 | Plan de mejora, responsables y fechas | Subdirección de Calidad / Coordinación; fechas de 2026 | Responsable de Calidad del Centro / Subdirección de Estudiantes; fechas de 2025-09 a 2027-12 | E | Decisión organizativa de la coordinación; el borrador propone valores razonables. |
| 16 | Criterio 2 y plan, numeración de ACCUA | Rec. 3.1, 4.1 (incluye sexenios), 6.1 y 6.2; 14 filas | Rec. 3.2, 4.2, 6.2 y 6.3; 15 filas (separa la 4.2) | H | El borrador usa la numeración del autoinforme anterior, única fuente aportada. Si el informe de ACCUA original numera como el humano, la causa sería I; requiere revisión experta. |

## Lecciones propuestas

Solo para discrepancias de causa **S**. Una lección es una regla general para la skill, nunca un
dato del título (ni valores, ni nombres, ni frases del autoinforme humano).

| Lección | Regla general propuesta | Discrepancias | Respaldo | Fichero de la skill |
|---|---|---|---|---|
| L01 | Cuando el estado de una estructura o acción (SGC del centro, cuadro de mandos, procedimientos, acciones del plan anterior) solo se conoce por el autoinforme anterior, no afirmarlo como vigente: redactarlo como «según el autoinforme anterior…» y añadir `[PENDIENTE: confirmar estado actual]`. Mantener la acción heredada en el plan solo con esa misma marca. | 10 | ninguno aún | references/guia-redaccion.md |
| L02 | Contrastar los cursos que se solapan entre la serie de LinceBI y la tabla de indicadores del autoinforme anterior. Si un valor difiere de forma sistemática (p. ej. una proporción constante o una escala distinta), no basar el análisis en la evolución entre esos cursos: señalar la diferencia en una nota de fuente y marcarla `[PENDIENTE: verificar serie]`. | 4, 13 | ninguno aún | SKILL.md (paso de verificación de datos) |

## Comentario general

El borrador acierta en la identificación, en casi todo el Anexo I (con alineación de cohortes mejor que la del humano, que tiene varias incoherencias internas) y en la cobertura de ACCUA, y su análisis compara con los objetivos correctos de la memoria. Falla en dos puntos de análisis: da por vigente la ausencia de SGC propio y de cuadro de mandos de la ESI, tomada del autoinforme anterior, y construye una «subida» de P04-13 sobre una serie de LinceBI que contradice la publicada. Antes de usarlo, la coordinación debe corregir el criterio 2 y la acción PD-ESI-2.1, revisar la serie P04-13 y completar los `[PENDIENTE]` internos (créditos reconocidos, Anexo III y fechas de aprobación).
