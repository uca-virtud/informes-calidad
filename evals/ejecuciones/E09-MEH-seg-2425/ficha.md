# Ficha de ejecución — E09-MEH-seg-2425

<!-- La crea `evaluacion.py nueva`. Los campos entre <…> los completa quien se indica. -->

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | E09 |
| Caso | MEH-seg-2425 |
| Título | Máster Universitario en Estudios Hispánicos |
| Tipo y curso | seguimiento, 2024-25 (convocatoria 2026) |
| Seguimiento ACCUA | no consta: se asume sí |
| Conjunto | aprendizaje |
| Fecha | 2026-10-22 |
| Versión de la skill | f759c6e |
| Versión de la rúbrica | 2 |
| Modelo A (generador y autocotejo) | claude-opus-5.5 |
| Modelo B (segundo corrector) | gpt-6.1-sol |

## Generación (completa el subagente A)

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (herramientas `lincebi_*`) |
| Fecha de extracción | 2026-10-22 (extracción principal y consultas complementarias de P05-01, PorcentajeCalificaciones y prácticas) |
| Documentos de entrada usados | `entrada/memoria.pdf`, `entrada/autoinforme-anterior.pdf`, `entrada/informe-accua.pdf`, `entrada/plan-mejora.pdf` |
| Supuestos tomados sin poder preguntar | Tipo: seguimiento. Seguimiento ACCUA: no consta; se asume sí. Indicadores: LinceBI. Datos internos del centro no aportados: quedan `[PENDIENTE]` (créditos reconocidos, plazas y convenios de prácticas, tutores académicos y profesionales, actas de coordinación y detalle del profesorado por persona). En total, 57 marcas `[PENDIENTE]` en el borrador. |
| Decisiones relevantes | Columna «No presentados» añadida a la tabla de calificaciones del 6.3. Valores de 2019-20 de la tabla de objetivos tomados del autoinforme anterior. Anexo II en forma agregada (P05-01), porque no hay datos por profesor. Prácticas a partir de LinceBI (9 estudiantes: 5 en FUNDUCA y 4 en la UCA). P01-03 a nivel de centro. Cuatro puntos débiles (criterios 4 a 7), cada uno con su acción en el plan de mejora; en los criterios 1 a 3, «No se identifican puntos débiles». Se descartaron como puntos débiles P04-11 (2,75), P01-02 (3,43) y la falta de movilidad saliente, por tener causa externa o estar ya cubiertos. Subapartados de dobles títulos, títulos conjuntos e intercentro eliminados; el enunciado de estructuras específicas se mantiene con «No procede». Eliminada la opción de varias modalidades (el título es presencial). |
| Incidencias | La generación se hizo en dos sesiones: la primera se canceló por tiempo tras la extracción, y la segunda retomó desde `datos.json` (con varias compactaciones de contexto). Corrección del orquestador: los cinco valores de 2020-21 del centro de P07 (P07-01_01 = 34,46; P07-01_02 = 41,15; P07-02 = 3,14; P07-03 = 3,91; P07-04 = 3,81), de `P07_IndicadoresTotal.prpt` (MÁSTER, `pcentro=5`), figuraban como no disponibles; se actualizaron en `datos.json`, se corrigió la nota de `extraccion` y se regeneró el documento antes de redactar. La tasa de graduación difiere del autoinforme anterior por ser dinámica (37,5 → 50; 23,1 → 42,3). El informe «Personal docente disponible» no existe en LinceBI. ACCUA citó como del título cifras de P06-03 del centro. LinceBI no ofrece P04-16 a 19 de 2020-21. El depurador emitió 5 avisos `REVISAR`, resueltos a mano: se borró la opción de varias modalidades, se conservaron las referencias a los anexos y se sustituyeron las filas «Punto débil nº» vacías. |

## Resultado (completa `evaluacion.py medir`)

<!-- medir:inicio -->
| Métrica | Borrador | Humano |
|---|---|---|
| Palabras | 13029 | 22917 |
| PF distintos | 7 | 0 |
| PD distintos | 4 | 0 |
| AM distintas | 14 | 0 |
| `[PENDIENTE]` | 57 | 0 |

Extensión borrador / humano: 13.029 / 22.917 (57 %).
Valores del Anexo I presentes en algún lugar de la referencia (cota superior, no mide la celda): 503/515 (97.7 %).

| Dim. | A | B | Final |
|---|---|---|---|
| D1 | 2 | 2 | 2 |
| D2 | 2 | 2 | 2 |
| D3 | 2 | 1 | 1 |
| D4 | 1 | 1 | 1 |
| D5 | 1 | 1 | 1 |
| D6 | 2 | 2 | 2 |
| D7 | 2 | 1 | 1 |

Media final: 1.43. Bloqueantes: B1. Discrepancias por causa (B): S=7, D=5, I=2, H=3, E=1.

**Aviso de huellas de casos en la skill** (revisar que no sean datos de títulos):
- `skills/uca-informes-calidad/assets/bloques_reutilizables_uca.md`: 5 frases de MEH-seg-2425 (p. ej. «de innovación y mejora docente actuaciones avaladas para»)
- `skills/uca-informes-calidad/references/estilo-y-ejemplos.md`: 2 frases de MEH-seg-2425 (p. ej. «accua o punto débil acciones de mejora a»)
- `skills/uca-informes-calidad/references/estructura-autoinforme.md`: 3 frases de MEH-seg-2425 (p. ej. «3 4 criterios de admisión perfil de ingreso»)
- `skills/uca-informes-calidad/references/mapa-indicadores-lincebi.md`: 4 frases de GH-seg-2425, MEH-seg-2425 (p. ej. «del alumnado con las prácticas externas isgc p04»)
<!-- medir:fin -->

## Valoración de la coordinación (completa `evaluacion.py valoracion`)

<!-- valoracion:inicio -->
Pendiente de recibir la hoja de valoración (paso 8).
<!-- valoracion:fin -->

## Pendiente de revisión experta

- Bloqueante B1
- Discrepancia 6 (H): Anexo I, erratas del humano
- Discrepancia 8 (H): Portada y datos fuera del curso
- Discrepancia 9 (H): Criterio 5, puntos fuertes y débiles
- Discrepancia 10 (H): Criterios 1 y 7, satisfacción de los empleadores
- Discrepancia 11 (H): 6.1 y 7.3, P07-03 y asimetrías
- Discrepancia 12 (H): 7.6, sostenibilidad
- Discrepancia 13 (H): 5.1, P05-04 de 2023-24
- Discrepancia 14 (I): Anexo III, prácticas externas
- Discrepancia 8 (H): Identificación y Anexo III, naturaleza de las prácticas
- Discrepancia 9 (I): 3.3-3.4, 4.5, 5.4, 6.1 y Anexo III, datos internos
- Discrepancia 10 (I): 4.1 y Anexo II, detalle individual del profesorado
- Discrepancia 15 (H): Anexo I, cinco errores del humano
- Discrepancia 18 (H): 3.4, alcance temporal del máximo de preferencia

## Decisión del responsable

| Lección | Decisión | Motivo |
|---|---|---|
| <Lxx> | <incorporada / candidata / descartada> | <filtro de admisión: norma, ≥2 títulos o Unidad de Calidad> |

## Retro del proceso

<Qué ajustar de la rúbrica, las plantillas, el procedimiento o el script antes de la siguiente
ejecución.>
