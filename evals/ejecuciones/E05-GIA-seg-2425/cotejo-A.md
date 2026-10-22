# Cotejo A — E05-GIA-seg-2425

- Corrector: A (autocotejo)
- Modelo: claude-opus-5.5
- Versión de la rúbrica: 2
- Fecha: 2026-10-03

## Puntuación

| Dimensión | Nota | Evidencia |
|---|---|---|
| D1 | 2 | Identificación correcta: ID 2502553, denominación, implantación 2011-2012, centro, web, modalidad presencial, renovación de la acreditación 05/07/2023 y prácticas no obligatorias, todo igual que en el humano. Las fechas de aprobación de la CGC y de la Junta quedan `[PENDIENTE]` porque son datos internos (I). |
| D2 | 2 | Coinciden con el humano P01, P04-01 a P04-19 del título, P05-02 a P05-07, P06, BAU y el perfil de ingreso 2024-25 (plazas 70, nuevo ingreso 71, nota de corte 12,274). Las diferencias tienen causa D (graduación y otras tasas de 2024-25, ventana de egresados) o H (tabla del centro y anexo P07 del humano). La única de causa S son las 16 celdas del centro en 2020-21 que quedan «-» (nº 10), por debajo del 5 % de las celdas comparables. |
| D3 | 1 | Todos los subcriterios tienen análisis, pero hay `[PENDIENTE]` evitables. Créditos reconocidos: el autoinforme anterior aportado da la ruta del informe en el Sistema de Información (nº 8). Relación nominal del profesorado: el borrador remite a un informe de LinceBI que no extrajo (nº 9). El resto de marcas son datos internos. |
| D4 | 2 | Cada tasa se compara con el objetivo de la memoria y con el centro y la UCA, con causas plausibles. La graduación 2024-25 se interpreta de forma coherente con el dato vivo, y se explica el cambio de fórmula de P07-05 a P07-08. No hay comparaciones erróneas. El humano, en cambio, afirma que rendimiento, eficiencia y éxito suben cuando bajan (nº 14). |
| D5 | 2 | Cuatro PD (1.1, 3.1, 5.1 y 6.1) dentro del rango de 1 a 5. Cada uno tiene su AM con código regular, responsable, fechas e indicador de seguimiento, y el plan de mejora final recoge además las recomendaciones vivas de ACCUA. La selección difiere de la del humano (nº 11), pero los PD del borrador están respaldados por datos y por recomendaciones de ACCUA. |
| D6 | 2 | Están las 15 recomendaciones del informe ACCUA, con su numeración, tipo, criterio, texto literal y estado. El humano parafrasea alguna (nº 12). |
| D7 | 1 | Sin `XXXX` ni instrucciones de color, pero quedan restos de la plantilla: una frase alternativa de 3.2 («el título se imparte en varias modalidades…») que contradice «solo presencial», «Grado/Máster» en 6.4 y en la portada, y la fila de cabecera de la tabla de calificaciones por asignatura del anexo IV sin etiquetas (nº 13). |

## Bloqueantes

| Bloqueante | ¿Hay? | Detalle |
|---|---|---|
| B1 | no | No se detectan datos inventados. Los valores salen de LinceBI (`datos.json`) o de los documentos de entrada, y los datos internos que faltan van como `[PENDIENTE]`. |
| B2 | no | No hay valores fuera de rango: las satisfacciones están entre 0 y 5 y las tasas entre 0 y 100. Ningún indicador aparece con dos valores dentro del borrador; P07-05 2022-23 vale 20,93 en el anexo y en el texto, de acuerdo con la nueva fórmula. |
| B3 | no | Host data.uca.es. La fecha y los dos tramos de la extracción constan en `datos.json` → `extraccion` y en la ficha. |

## Discrepancias

Solo las relevantes (no cada diferencia de redondeo; agrúpalas en una fila si comparten causa).

| Nº | Apartado | Borrador | Autoinforme humano | Causa | Explicación |
|---|---|---|---|---|---|
| 1 | Anexo I y criterio 6, tasa de graduación 2024-25 | 29,9 % (2023-24: 33,3) | 7,5 % (2023-24: 33,3); lo convierte en el PD-6.1 y lo atribuye a la «alta empleabilidad» | D | Tasa viva que crece a medida que se gradúa la cohorte. El humano la extrajo unos seis meses antes. Su PD y su interpretación dependen de ese valor provisional. |
| 2 | Anexo I, tasas de 2024-25 | Eficiencia 73,4; rendimiento 67,4; éxito 79,8; evaluación 84,5 | 73,0; 67,3; 79,7; 84,4 | D | Diferencias de una o pocas décimas, propias de datos vivos extraídos en fechas distintas. |
| 3 | Anexo I, P04 del centro | Valores propios del centro; P04-13 del centro `[PENDIENTE]` en 2020-21 a 2022-23 (dato normalizado dos veces) y 4,65 en 2024-25 | Copia los valores del título en la columna del centro, incluido P04-13 del centro 2,11 / 2,32 / 2,38, que son valores del título partidos por dos | H | La tabla del centro del humano no es del centro. El borrador usa los valores del centro de LinceBI y marca para revisión los que vienen normalizados dos veces. |
| 4 | Anexo I, P04-08 2024-25 | Título 1,15; centro 1,93 | Título «–»; centro 1,15 | H | El valor del título aparece en la columna del centro. |
| 5 | Anexo I, P07 (satisfacción del alumnado) | 2024-25: participación 17,58; P07-02 3,68; P07-03 3,89; P07-04 3,79 | El anexo pone en 2024-25 31,21; 3,42; 4,08; 3,86, que son los valores de 2020-21. El texto del propio humano da 3,68; 3,89; 3,79. | H | Las columnas del anexo humano están desplazadas o invertidas. El borrador coincide con el texto humano. |
| 6 | Criterio 7 y anexo, egresados | Cohortes 2019-20 a 2023-24; última cohorte con participación 36,36 % (24/66), P07-10 3,13 y P07-06 95,24 | Cohortes 2018-19 a 2022-23; el texto da 20,93 % (9/43) y el anexo 21,05 % para la misma cohorte | D | Cuando el humano extrajo, la cohorte 2023-24 no estaba disponible. Los valores del texto humano para 2022-23 coinciden con el borrador; los de su anexo no (H secundario). LinceBI advierte del cambio de fórmula de P07-05 a P07-08 desde 2022-23, por lo que ningún lado es comparable con las cohortes anteriores. Conviene que un experto lo revise. |
| 7 | Criterio 4, P05-01 | Sexenios de 38 a 71 (2020-21 a 2024-25); doctores del 66,67 % al 77,03 %; 74 profesores, 29 TU, 149 quinquenios | Texto: sexenios «de 89 a 149»; en la recomendación nº 9 de ACCUA: de 25 a 46. Profesorado, TU y quinquenios iguales. | H | El humano se contradice: 149 son los quinquenios. El borrador toma la serie de LinceBI. Conviene que un experto lo revise, porque las bases de cálculo pueden variar entre informes. |
| 8 | Criterio 3, créditos reconocidos 2024-25 | `[PENDIENTE: el informe no existe en LinceBI]` | 101 estudiantes y 787 créditos, del Sistema de Información de la UCA | S | El autoinforme anterior aportado indica la ruta exacta del informe de créditos reconocidos, dentro de P04. El generador lo buscó por nombre, no lo encontró y dejó un `[PENDIENTE]` evitable. |
| 9 | Criterio 4 y anexo II, profesorado | Relación nominal `[PENDIENTE: completar con LinceBI]` | Enlace al documento del profesorado | S | El borrador nombra el informe de LinceBI que contiene la relación del profesorado y no lo extrae. Es un dato disponible en la fuente autorizada. |
| 10 | Anexo I, columna del centro 2020-21 (P01, P04-16 a P04-19, P06 y P07) | «-» en 16 celdas | Valores (p. ej. P01-01 centro 3,27) | S | El curso 2020-21, ausente en LinceBI, se completó desde el autoinforme anterior para el título, pero no para el centro, que figura en el mismo documento. |
| 11 | Puntos débiles y plan de mejora | PD 1.1 encuestas; 3.1 coordinación (P04-10 baja a 2,75; ACCUA nº 7); 5.1 movilidad (ACCUA nº 10); 6.1 TFG no presentados y duración. P05-02 se analiza en el texto y queda como candidato. | PD 1.1 encuestas; 3.1 asignación de TFG; 4.1 formación del profesorado (P05-02); 6.1 graduación | E | Las dos selecciones están dentro del rango de 1 a 5 y la del borrador sigue la regla de la skill. El TFG aparece en ambos, en criterios distintos. El PD de graduación del humano depende del dato provisional (nº 1). Su omisión de coordinación y movilidad, ambas ligadas a aspectos que ACCUA pide subsanar, es una elección de la coordinación. |
| 12 | Tabla de recomendaciones de ACCUA | Las 15 con tipo y criterio. La nº 6 recoge el texto literal de ACCUA («…el número de encuestas y el tamaño de la población encuestada…»). | «Recomendación 1-15» sin tipo; la nº 6 parafraseada | H | El texto del borrador coincide con el informe de ACCUA aportado. La paráfrasis humana pierde el contenido concreto de la recomendación. |
| 13 | Restos de plantilla (3.2, 6.4, portada, anexo IV) | Frase alternativa «varias modalidades…»; «Grado/Máster en Ingeniería Aeroespacial»; cabecera de la tabla de asignaturas sin etiquetas | Sin restos | S | La depuración no elimina las opciones alternativas de la plantilla que no aplican, ni los marcadores partidos entre runs, y borra las etiquetas de cabecera escritas en color de instrucción. |
| 14 | Texto de los criterios 4, 5 y 6 del humano | Cifras iguales a las del anexo. PF-6.1 basado en tasas comparadas con la memoria. | P04-12 «4,44» frente a 4,40 en su anexo; P04-19 «27,18 %» frente a 16,28; PF de prácticas con valores del curso anterior (2,89 → 4,20); PF-6.1 «rendimiento, eficiencia y éxito han subido» cuando bajan | H | Errores e incoherencias internas del humano. El borrador es correcto en estos puntos. |
| 15 | Fechas y documentos internos (política de calidad, CGC, Junta, repositorio, prácticas: 15 estudiantes, convenios y tutores) | `[PENDIENTE]`; repositorio Colabora, tomado del autoinforme anterior | Política 26/07/2022, ampliada el 18/07/2025; CGC 24/03/2026; Junta 27/03/2026; UCADrive; datos de prácticas | I | Datos internos del centro que no se aportaron. El autoinforme anterior no contiene la fecha de la política, así que la marca no era evitable. |
| 16 | Identificación, estructuras curriculares específicas | «Menciones en Aeronaves y en Equipos y Materiales Aeroespaciales» | «Sí. 12 ECTS optativos» | E | Redacción distinta. El humano además se contradice en el anexo III («12 ECTS obligatorios» frente a «No» en la identificación). |

## Lecciones propuestas

Solo para discrepancias de causa **S**. Una lección es una regla general para la skill, nunca un
dato del título (ni valores, ni nombres, ni frases del autoinforme humano).

| Lección | Regla general propuesta | Discrepancias | Respaldo | Fichero de la skill |
|---|---|---|---|---|
| L01 | Antes de marcar un dato como «no disponible en LinceBI», busca en los documentos aportados (sobre todo el autoinforme anterior) la ruta o el nombre del informe del Sistema de Información que se usó, y localízalo en LinceBI por esa ruta o carpeta, no solo por palabras clave. Si sigue sin aparecer, indica en el `[PENDIENTE]` la ruta citada para que la coordinación lo obtenga. | 8 | ninguno aún | references/mapa-indicadores-lincebi.md |
| L02 | Si el borrador remite a un informe de LinceBI para un dato del autoinforme (p. ej. la relación del profesorado), extráelo e incorpóralo; no dejes un `[PENDIENTE]` que apunte a la propia fuente autorizada. | 9 | ninguno aún | SKILL.md |
| L03 | Cuando un curso de la serie de cinco no está en LinceBI y se completa desde el autoinforme anterior, aplica la misma regla a todas las columnas que ese documento ofrezca (título, centro y UCA), no solo al título. | 10 | ninguno aún | SKILL.md |
| L04 | En la verificación final, comprueba que no quedan opciones alternativas de la plantilla que contradigan los datos de identificación (p. ej. la modalidad), ni marcadores genéricos «Grado/Máster», y que las filas de cabecera de las tablas conservan sus etiquetas tras eliminar las instrucciones en color. | 13 | ninguno aún | SKILL.md |

## Comentario general

El borrador reproduce con fidelidad los indicadores de LinceBI y analiza cada criterio frente a la memoria, el centro y la UCA. En varios puntos es más fiable que el autoinforme humano, cuya tabla del centro, anexo de satisfacción del alumnado y cifras de sexenios contienen errores. Sus fallos son de completitud y limpieza: `[PENDIENTE]` evitables (créditos reconocidos, profesorado y centro 2020-21) y restos de la plantilla en 3.2, 6.4, la portada y el anexo IV. Antes de usarlo, la coordinación debe:
- completar los datos internos;
- borrar la frase de «varias modalidades»;
- revisar la tasa de graduación y la ventana de egresados a la fecha de presentación;
- confirmar la selección de puntos débiles, en particular si incluye la formación del profesorado.
