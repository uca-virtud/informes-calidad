# Ficha de ejecución — E08-GHUM-seg-2425

<!-- La crea `evaluacion.py nueva`. Los campos entre <…> los completa quien se indica. -->

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | E08 |
| Caso | GHUM-seg-2425 |
| Título | Grado en Humanidades |
| Tipo y curso | seguimiento, 2024-25 (convocatoria 2026) |
| Seguimiento ACCUA | no consta: se asume sí |
| Conjunto | aprendizaje |
| Fecha | 2026-10-21 |
| Versión de la skill | 6f9f6cf |
| Versión de la rúbrica | 2 |
| Modelo A (generador y autocotejo) | claude-opus-5.5 |
| Modelo B (segundo corrector) | gpt-6.1-sol |

## Generación (completa el subagente A)

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (producción) |
| Fecha de extracción | 2026-10-21 |
| Documentos de entrada usados | `entrada/memoria.pdf` (memoria verificada), `entrada/autoinforme-anterior.pdf` (autoinforme anterior, fuente del curso 2020-21 y de la numeración de las recomendaciones), `entrada/informe-accua.pdf` (último informe de ACCUA). No se aportó plan de mejora aparte: el plan se reconstruye con las recomendaciones ACCUA y los puntos débiles nuevos. |
| Supuestos tomados sin poder preguntar | Tipo: seguimiento, 2024-25, convocatoria 2026. Seguimiento ACCUA «no consta»: se asume que sí (se cumplimenta el apartado de recomendaciones ACCUA). Indicadores de LinceBI (data.uca.es). Datos internos del centro (actas, CGC, profesorado nominal, empleadores, tasas de primer curso, ejecución de acciones) no aportados: quedan `[PENDIENTE]` (53 marcas). Acrónimo de centro en los códigos PF/PD/AM: FFL. Las recomendaciones conservan la numeración nº 1-12 del autoinforme anterior y del informe ACCUA. |
| Decisiones relevantes | Las 12 recomendaciones de ACCUA se citan en su subcriterio y en el plan de mejora como abiertas, con `[PENDIENTE]` para la evidencia de su ejecución (no se dan por resueltas sin evidencia). Serie de seis cursos del 6.3: 2019-20 y los valores de 2020-21 que LinceBI no ofrece proceden del autoinforme anterior. Tasas de primer curso en `[PENDIENTE]` (no disponibles en LinceBI). Plazas: se sigue la memoria (55), aunque el autoinforme anterior indicaba 35. Tabla de profesorado (Anexo II) solo con agregados (62 profesores, 87,1 % de doctores) y la relación nominal en `[PENDIENTE]`. Tabla de calificaciones del 6.3 con las seis asignaturas con más no presentados; Anexo IV con las 57 asignaturas del informe PorcentajeCalificaciones (2024-25) más el global. Tres puntos débiles (prácticas externas, no presentados de primer curso e idiomas, duración media de los estudios) con su acción; criterios 1-4 y 7 sin puntos débiles nuevos. Párrafos modelo con «XXX» reescritos con datos del título; restos rojos o azules con instrucciones borrados, y referencias a anexos pasadas a negro. Nota en el Anexo 1 que explica el «-». |
| Incidencias | Un 401 transitorio de LinceBI (resuelto al reintentar). P05-01 exigió `ptipoestudio=GRA`. Los egresados se filtraron por el nombre del centro. pypdf pierde letras de los PDF (se interpretó el texto). P04-13 de 2021-24 aparece a la mitad de escala en LinceBI. Tasa de graduación de 2023-24: 45 % en LinceBI frente al 25 % del autoinforme anterior (se usa el valor de LinceBI). `rellenar_autoinforme.py` dio falsos positivos de escala en P07-01 y avisó de una tabla con una sola columna de años. `depurar_instrucciones.py` dejó párrafos de color mixto (instrucciones de 3.2 y referencias a anexos), que se corrigieron a mano. El informe de calificaciones por asignatura se volvió a consultar para transcribir las cifras exactas. |

## Resultado (completa `evaluacion.py medir`)

<!-- medir:inicio -->
| Métrica | Borrador | Humano |
|---|---|---|
| Palabras | 14419 | 18626 |
| PF distintos | 10 | 0 |
| PD distintos | 3 | 0 |
| AM distintas | 3 | 0 |
| `[PENDIENTE]` | 53 | 0 |

Extensión borrador / humano: 14.419 / 18.626 (77 %).
Valores del Anexo I presentes en algún lugar de la referencia (cota superior, no mide la celda): 520/544 (95.6 %).

| Dim. | A | B | Final |
|---|---|---|---|
| D1 | 2 | 2 | 2 |
| D2 | 2 | 2 | 2 |
| D3 | 2 | 1 | 1 |
| D4 | 2 | 1 | 1 |
| D5 | 2 | 1 | 1 |
| D6 | 2 | 2 | 2 |
| D7 | 2 | 1 | 1 |

Media final: 1.43. Bloqueantes: B1. Discrepancias por causa (B): S=9, D=3, I=3, H=5, E=1.

**Aviso de huellas de casos en la skill** (revisar que no sean datos de títulos):
- `skills/uca-informes-calidad/references/estilo-y-ejemplos.md`: 1 frases de GIDIDP-seg-2425 (p. ej. «de eficiencia esta tasa con un valor de»)
- `skills/uca-informes-calidad/references/mapa-indicadores-lincebi.md`: 1 frases de GH-seg-2425 (p. ej. «participación en proyectos de innovación y mejora docente»)
<!-- medir:fin -->

## Valoración de la coordinación (completa `evaluacion.py valoracion`)

<!-- valoracion:inicio -->
Pendiente de recibir la hoja de valoración (paso 8).
<!-- valoracion:fin -->

## Pendiente de revisión experta

- Bloqueante B1
- Discrepancia 1 (I): Criterio 3.3, plazas de nuevo ingreso
- Discrepancia 3 (H): Anexo I, P04-05 tasa de graduación 2024-25
- Discrepancia 8 (H): Anexo I, P07-05 2019-20 a 2021-22 (título)
- Discrepancia 9 (H): Anexo I, P07-01_01, P07-01_02, P07-02, P07-03 y P07-04, columna 2024-25
- Discrepancia 11 (H): Plan de mejora, puntos débiles
- Discrepancia 12 (I): Criterios 1-7 y plan de mejora, recomendaciones ACCUA nº 1-12
- Discrepancia 13 (I): Criterios 2, 4 y 5 y Anexo III
- Discrepancia 14 (H): Criterios 1, 2 y 7
- Discrepancia 15 (H): Criterios 3, 5, 6 y 7 (texto)
- Discrepancia 13 (H): 5.3 y puntos fuertes del criterio 5
- Discrepancia 14 (H): 6.3, plan y Anexo I: graduación y abandono
- Discrepancia 15 (H): Anexo I: P07 satisfacción, última columna
- Discrepancia 16 (H): 7.6: demanda y BAU
- Discrepancia 17 (H): Anexo III: carácter de las prácticas
- Discrepancia 18 (I): Criterios 1-2, 3.1 y 7.4: novedades internas
- Discrepancia 19 (I): 4.5, 5.3 y Anexo III: gestión de prácticas
- Discrepancia 20 (I): Aprobación, 3.3, 6.1 y 6.3: datos internos restantes

## Decisión del responsable

| Lección | Decisión | Motivo |
|---|---|---|
| L11b, L28 | funcionan | Validadas en esta ejecución |
| L19b | incorporada (v7, 22-10-2026) | Refuerzo de L19: insuficiente en E07 y E08 (≥2 títulos) |
| L23b (con C10) | incorporada (v7, 22-10-2026) | Refuerzo de L23: insuficiente en E07 y E08 (≥2 títulos); C10 es un caso de L23, ya respaldada |
| L25b (con C8) | incorporada (v7, 22-10-2026) | Refuerzo de L25: insuficiente en E07 y E08; C8 repetida en los dos (≥2 títulos) |
| L26b (C11) | incorporada (v7, 22-10-2026) | Refuerzo de L26/L20, ya respaldadas por ≥2 títulos; C11 concreta cómo agotar la fuente |
| L27b | incorporada (v7, 22-10-2026) | Refuerzo de L27: insuficiente en E07 y E08 (≥2 títulos); incluye los avisos `REVISAR` de C16 |
| L29 (C13) | incorporada (v7, 22-10-2026) | Norma/guía: `estilo-y-ejemplos.md` («Sostenibilidad») ya exige la síntesis transversal con valoración; se añade a la verificación |
| C15 | corregida en el script | `rellenar_autoinforme.py` no comprueba la escala 0-5 en tasas de respuesta ni en etiquetas con «(%)» |
| C16 | corregida en el script | `depurar_instrucciones.py` borra los párrafos mixtos que quedan solo con puntuación, recorta guiones colgantes y lista con `REVISAR` los restos en negro |
| C12, C14 | candidatas | Solo en este título |
| Huellas | revisadas, 22-10-2026 | El ejemplo de eficiencia pasa a plantilla con marcadores; «Participación en proyectos de innovación y mejora docente» es el nombre oficial de P05-03 y se conserva |

## Retro del proceso

<Qué ajustar de la rúbrica, las plantillas, el procedimiento o el script antes de la siguiente
ejecución.>
