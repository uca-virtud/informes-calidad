# Ficha de ejecución — E10-GH-seg-2526

<!-- La crea `evaluacion.py nueva`. Los campos entre <…> los completa quien se indica. -->

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | E10 |
| Caso | GH-seg-2526 |
| Título | Grado en Historia |
| Tipo y curso | seguimiento, 2025-26 (convocatoria 2027) |
| Seguimiento ACCUA | no consta: se asume sí |
| Conjunto | aprendizaje |
| Referencia | ninguna: evaluación solo de la coordinación (pasos 1, 2, 6, 7 y 8) |
| Fecha | 2026-11-09 |
| Versión de la skill | 8907496 |
| Versión de la rúbrica | 3 |
| Modelo A (generador y autocotejo) | claude-opus-5.5 |
| Modelo B (segundo corrector) | no aplica (sin referencia) |

## Generación (completa el subagente A)

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (comprobado antes de extraer) |
| Fecha de extracción | 2026-11-09 (informes disgregados de indicadores; el informe agregado devolvía un error de caché) |
| Documentos de entrada usados | `entrada/memoria.pdf` (memoria MOD-NS 2024), `entrada/autoinforme-anterior.pdf` (seguimiento 2024-25, convocatoria 2026) y `entrada/informe-accua.pdf` (informe final de renovación de la acreditación, 05/07/2023). Además, la web pública del centro y del título (filosofia.uca.es) para los enlaces |
| Supuestos tomados sin poder preguntar | Tipo seguimiento, con seguimiento ACCUA asumido (no consta). Indicadores de LinceBI. Los aspectos del 1 al 13 del informe de renovación de 2023 son las recomendaciones que hay que atender. Datos internos del centro no aportados: `[PENDIENTE]`. Estado de las acciones del plan de mejora anterior: `[PENDIENTE]` (no hay documento de cierre). Cohortes de egresados de 2019-20 a 2023-24. Oferta de 75 plazas (memoria) |
| Decisiones relevantes | Indicadores sin valor como «Sin dato» o «No disponible». Subcriterios 4.6 y 5.5 «No procede». Tasa de graduación de 2025-26 marcada como provisional. Personal remitido al Anexo 2 y a la web. Enlaces tomados de la web del centro, incluido un enlace por elemento del recordatorio de información pública (Real Decreto 534/2024 frente al 412/2014 marcado para comprobar). Eliminados los bloques de títulos conjuntos, intercentro y dobles, las bibliotecas de otros centros y los ejemplos de otros títulos. Extinción, plan de contingencia, cuadro de mando, UCADrive (listados, rúbricas e informes por asignatura) y fecha de aprobación de la Política de Calidad: `[PENDIENTE]`. Criterios 1 y 2 sin puntos débiles, con la fila «No se han identificado…». ICARO citado sin enlace. Subcriterios 6.2 a 6.4 numerados. Subtítulos de TFG de la plantilla convertidos en `[PENDIENTE]`. Punto fuerte de eficiencia corregido: 91 %, muy cerca del 92 % de la memoria |
| Incidencias | El venv de python-docx y pypdf se creó dentro del repositorio porque /tmp y `mktemp` están prohibidos en el entorno; se borró al terminar. El P07 total de LinceBI devolvía cursos antiguos, así que se usó el informe de satisfacción. BAU y calificaciones por asignatura sin datos de 2025-26. Aviso del script por la fila de implantación 2010/11. Denominadores de P07-01_03 del centro, corregidos a mano. El rellenado no quitó las bibliotecas de otros centros (se quitaron a mano). Hipervínculo de ICARO heredado de la plantilla (se quitó). La web del título usa secciones desplegables sin URL propia: para algunos elementos se cita la sección |

## Resultado (completa `evaluacion.py medir`)

<!-- medir:inicio -->
No se mide: caso sin referencia (sin autocotejo, B ni `medir`).
<!-- medir:fin -->

## Valoración de la coordinación (completa `evaluacion.py valoracion`)

<!-- valoracion:inicio -->
Pendiente de recibir la hoja de valoración (paso 8).
<!-- valoracion:fin -->

## Pendiente de revisión experta

Sin notas de la IA con las que comparar. Al recibir la hoja de la coordinación, revisar:

- Los 93 `[PENDIENTE]` del borrador: datos internos del centro, estado de las acciones del plan
  de mejora anterior, fecha de aprobación de la Política de Calidad, extinción, plan de
  contingencia, cuadro de mando y documentos de UCADrive.
- El seguimiento ACCUA asumido y la cita del Real Decreto 534/2024 frente al 412/2014 en el
  recordatorio de información pública.
- Los indicadores corregidos a mano (P07 total, denominadores de P07-01_03 del centro) y los que
  LinceBI no tenía para 2025-26 (BAU y calificaciones por asignatura).

## Decisión del responsable

Pendiente de la valoración de la coordinación (paso 8). Las lecciones L30-L38 de la versión 8
siguen «por comprobar»: un caso sin referencia no las valida por sí solo.

## Retro del proceso

- La generación tardó unos 53 minutos, muy por encima de la estimación (15-21 min), por el
  informe agregado de LinceBI caído y las correcciones manuales de indicadores.
- El subagente A no pudo usar /tmp ni `mktemp` y creó el venv dentro del repositorio (lo borró
  al terminar): conviene indicarle una ruta temporal permitida en el prompt.
