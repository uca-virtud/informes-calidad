# Cotejo A — E09-MEH-seg-2425

- Corrector: A (autocotejo)
- Modelo: claude-opus-5.5
- Versión de la rúbrica: 2
- Fecha: 2026-10-23

## Puntuación

| Dimensión | Nota | Evidencia |
|---|---|---|
| D1 | 2 | Tabla de identificación completa y coherente con la memoria y el autoinforme anterior: ID 4314324, implantación 2013-14, presencial, renovación 17/06/2021, sin título doble, itinerarios. El humano coincide en todos los campos que rellena (la URL corta de su tabla y la larga de su texto llevan a la misma web). |
| D2 | 2 | De unos 500 valores comparables, unas 25 diferencias: casi todas por D (tasas dinámicas del curso 2024-25 y de la graduación, P04-16 a 19 de 2020-21 de otra fuente) o H (erratas del humano: 26,9, 3,37, 1,13, 0,61 y 6,16). La única de causa S es P04-13 del título de 2021-22 a 2023-24 (3 valores): >95 %. Cursos y cohortes bien alineados. |
| D3 | 2 | Todos los criterios y subcriterios tienen análisis, incluidos el 6.3 y el 7.6. Los `[PENDIENTE]` afectan a datos internos (plazas, convenios y tutores de prácticas, estado de acciones anteriores, evidencias) y a P04-16 a 19 de 2020-21, que LinceBI no devuelve. |
| D4 | 1 | Análisis evolutivo, con comparación con el centro, la UCA y los objetivos de la memoria con su tasa, y causas plausibles. Pero en P04-13 compara 5 con 2,28 sin advertir que la serie de LinceBI de 2021-22 a 2023-24 es exactamente la mitad de la publicada en el autoinforme anterior (L24 no aplicada), y valora como favorable la orientación profesional (P06-02: 2,92, con una caída de 0,51) por superar al centro. |
| D5 | 1 | Cuatro puntos débiles asumibles, cada uno con acciones, responsable y plazo, consolidados en un plan de mejora de 14 acciones. Pero PF-FFL-7.1 convierte en punto fuerte un indicador por debajo de 3 y en descenso (P06-02), que el humano declara punto débil con acción. |
| D6 | 2 | Las recomendaciones vivas de ACCUA (informe de 28/01/2026) figuran en el criterio 2 y en el plan de mejora con su numeración original, su estado y la acción AM-FFL que las atiende; incluye el aspecto que debe subsanarse sobre la satisfacción de los empleadores. |
| D7 | 2 | Plantilla fiel, sin instrucciones ni `XXXX`, con los códigos PF/PD/AM-FFL-crit.n y registro formal en primera persona del plural. |

## Bloqueantes

| Bloqueante | ¿Hay? | Detalle |
|---|---|---|
| B1 | no | Todos los valores proceden de LinceBI, de la entrada o de la norma; lo no disponible queda `[PENDIENTE]`. |
| B2 | no | Sin valores fuera de rango ni duplicados contradictorios. El humano sí tiene uno (P04-12 del centro de 2021-22 = 6,16 sobre 5). |
| B3 | no | Extracción de `data.uca.es` el 2026-10-22, registrada en `datos.json` y en la ficha. |

## Discrepancias

Solo las relevantes (no cada diferencia de redondeo; agrúpalas en una fila si comparten causa).

| Nº | Apartado | Borrador | Autoinforme humano | Causa | Explicación |
|---|---|---|---|---|---|
| 1 | Anexo I y 6.1, P04-13 del título | 1,12 / 2,46 / 2,28 (2021-22 a 2023-24) y 5 en 2024-25; el texto narra «5 (2,28 en 2023-24)» | 2,25 / 4,93 / 4,56, como en el autoinforme anterior | S | La serie de LinceBI es exactamente la mitad de la publicada el año anterior en los tres cursos comunes. La skill (L24) pide detectarlo, no analizar la evolución entre esos cursos, añadir una nota de fuente y dejar `[PENDIENTE: verificar serie]`. El borrador no lo hizo y presenta un salto de 2,28 a 5 que puede ser un artefacto de la fuente. |
| 2 | Criterio 7, puntos fuertes y débiles (P06-02) | PF-FFL-7.1: la orientación profesional (2,92) supera al centro (2,64) | Punto débil sobre la orientación profesional, con acción | S | Con 2,92 sobre 5 y una caída de 0,51 puntos, el indicador no es un logro aunque supere al centro. Debió analizarse como desfavorable y, como la coordinación puede actuar, proponerse como punto débil o como candidato. |
| 3 | Anexo I, P04-05 del título (graduación) | 58,3 / 57,9 / 50 / 42,3 / 82,6; el texto explica el recálculo frente a 37,5 y 23,1 | 53,3 / 57,9 / 37,5 / 42,3 / 56,5; en el texto, 69,6 y 56,5 | D | Tasa dinámica extraída en fechas distintas. El borrador explica el recálculo; el humano mezcla tres versiones (anexo, 6.1 y 6.3), lo que además es un error interno (H). |
| 4 | Anexo I del centro, P04-01 a 05 de 2023-24 y 2024-25 | P. ej. rendimiento 81,9, evaluación 82,9, abandono 10,5 y graduación 66,9 en 2024-25 | 80,2 / 81,4 / 9,8 / 46,6 en 2024-25; diferencias de 0,1 en 2023-24 | D | Tasas del curso evaluado que LinceBI recalcula; el borrador usa la extracción más reciente. |
| 5 | Anexo I, P04-15 y P05-04 del título de 2021-22; P05-04 y P06-04 del centro de 2024-25 | 4,5 / 5 / 4,5 / 3,85 | 4,4 / 4,5 / 4,6 / 3,87 | D | Diferencias pequeñas entre extracciones; el humano da además dos valores de P06-04 del centro (3,85 y 3,87) en lugares distintos. |
| 6 | Anexo I, erratas del humano | P04-09 entrante 26,09; P01-03 del centro de 2023-24 3,73; P04-08 del centro de 2021-22 1,3; movilidad saliente del centro de 2021-22 1,61; P04-12 del centro de 2021-22 4,16 | 26,9 (26,09 en su texto); 3,37; 1,13; 0,61; 6,16 | H | El borrador coincide con LinceBI; el humano transpone cifras y arrastra un valor imposible (>5) del autoinforme anterior. |
| 7 | Anexo I, P04-16 a 19 de 2020-21 | «No disponible en LinceBI» | 100 / 83,33 / 146,67 / 54,35 | D | LinceBI no devuelve ese curso para estos indicadores (verificado por el orquestador); el humano usa otra fuente. |
| 8 | Portada y datos fuera del curso | Portada con «Máster en Estudios Hispánicos»; datos de 2024-25 | «GRADO/MÁSTER» sin depurar; cita datos de 2025-26 | H | Resto de la plantilla y datos ajenos al curso evaluado. |
| 9 | Criterio 5, puntos fuertes y débiles | PF-FFL-5.1 (movilidad entrante) y PD-FFL-5.1 (recursos, P06-03) | Un punto fuerte que cita otro máster y un punto débil de servicios administrativos basado en P01-03 = 3,66 | H | P01-03 es la satisfacción del PTGAS con la información pública, no con los servicios administrativos, y la mención a otro título es una errata. El punto débil de recursos coincide en ambos (E). |
| 10 | Criterios 1 y 7, satisfacción de los empleadores | Sin datos: PD-FFL-7.1 y AM-FFL-7.1, que responden al aspecto que ACCUA pide subsanar | Afirma una satisfacción alta de los empleadores y habla de «instrumentos estables de empleabilidad» | H | No hay evidencia en la entrada ni en LinceBI, y contradice el informe de ACCUA de 28/01/2026. |
| 11 | 6.1 y 7.3, P07-03 y asimetrías | P07-03 baja a 3,45, mínimo de la serie; detecta un 37 % de no presentados en el TFM | «Se mantiene»; niega asimetrías entre asignaturas | H | El borrador se ajusta a los datos; el humano los contradice. |
| 12 | 7.6, sostenibilidad | Demanda, profesorado, recursos, resultados, inserción, respuesta a ACCUA y valoración final | Sin la respuesta a ACCUA ni los datos de inserción; inserción narrada sin cifras en el 7.2 | H | El borrador cubre los elementos que pide la guía de ACCUA. |
| 13 | 5.1, P05-04 de 2023-24 | 4,9 en el título y 4,7 en el centro | Da 4,9 y 4,7 para el título en lugares distintos | H | El humano mezcla el título con el centro. |
| 14 | Anexo III, prácticas externas | Nueve estudiantes con prácticas (LinceBI); plazas, convenios y tutores `[PENDIENTE]` | 10 plazas en dos entidades y tutores con nombre | I | Datos internos del centro no aportados en la entrada. |
| 15 | Criterios 1 a 3, puntos débiles | Sin puntos débiles; la caída de P01-02 (de 4,18 a 3,43) y P04-10 se analizan en el texto o en el criterio 4 | Puntos débiles sobre la información pública, la inserción y la coordinación | E | El borrador declara 4 puntos débiles, dentro del rango de 1 a 5 que fija la skill, y trata las mismas debilidades en otro criterio o en el texto. |
| 16 | Plan de mejora | 14 acciones con código AM-FFL, origen, prioridad y responsable; evidencias `[PENDIENTE]` | 5 puntos débiles sin código, con fechas de 2026-27 e indicadores; arrastra una acción ACCUA de gestión documental | E | Misma cobertura (recursos, TFM, orientación, empleadores, ACCUA) con otro formato. Las fechas y las evidencias concretas son internas (I). |
| 17 | Anexo I, egresados | Serie de egresados del periodo del Anexo I | Añade una tabla histórica de 2016-17 a 2020-21 | E | Diferencia de alcance; no afecta al análisis del curso. |

## Lecciones propuestas

Solo para discrepancias de causa **S**. Una lección es una regla general para la skill, nunca un
dato del título (ni valores, ni nombres, ni frases del autoinforme humano).

| Lección | Regla general propuesta | Discrepancias | Respaldo | Fichero de la skill |
|---|---|---|---|---|
| L24b | Refuerzo de L24: antes de redactar, comparar por indicador y ámbito los cursos comunes de LinceBI con el Anexo I del autoinforme anterior. Si el cociente es constante en todos ellos (p. ej. 0,5 o 2), marcar la serie como discontinua: sin comparar el curso evaluado con esos cursos, con nota de fuente y `[PENDIENTE: verificar serie de …]`. Conviene que la comprobación sea automática (aviso `REVISAR` del script de relleno), porque la revisión manual falló. | 1 | L24 (validada en E07); este título; ninguno aún en otros como reincidencia | `references/guia-redaccion.md` (checklist 15) y `scripts/rellenar_autoinforme.py` |
| L30 | Un punto fuerte solo se apoya en un indicador favorable en términos absolutos: superar al centro o a la UCA no basta si la satisfacción está por debajo de 3 sobre 5 o cae de forma apreciable (≥0,5 puntos) respecto al curso anterior. Ese indicador se analiza como desfavorable y, si la coordinación puede actuar, se propone como punto débil o como candidato en el resumen. | 2 | Guía de seguimiento de ACCUA (los puntos fuertes son logros derivados del análisis); este título; ninguno aún en otros | `SKILL.md` (§5) y `references/guia-redaccion.md` |

## Comentario general

El borrador es sólido: Anexo I fiel a LinceBI, análisis completo con los objetivos de la memoria y tabla de ACCUA con la numeración original. Supera al humano en la satisfacción de los empleadores, el TFM, P07-03 y el 7.6. Validación de la versión 7:
- **Cumplidas:** L19b (guiones distintos de «sin registros»), L25b (antecedentes con `[PENDIENTE: confirmar]` e hipótesis redactadas como tales), L26b (Anexo II con el agregado de P05-01 y prácticas desde LinceBI), L27b y C16 (cinco avisos `REVISAR`, todos resueltos), L29 (7.6 completo, con valoración final) y C15 (sin falso aviso de escala en P07-01).
- **Cumplida con matiz:** L23b, porque no comenta el salto de P04-13.
- **Regresión:** L24 no se aplicó a P04-13.

Antes de usar el borrador, la coordinación debe:
1. Verificar la serie de P04-13 del título.
2. Reconsiderar PF-FFL-7.1 como punto débil de orientación profesional.
3. Completar los `[PENDIENTE]` internos: prácticas, estado de las acciones anteriores y evidencias.
