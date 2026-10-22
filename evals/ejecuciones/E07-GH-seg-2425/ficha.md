# Ficha de ejecución — E07-GH-seg-2425

<!-- La crea `evaluacion.py nueva`. Los campos entre <…> los completa quien se indica. -->

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | E07 |
| Caso | GH-seg-2425 |
| Título | Grado en Historia |
| Tipo y curso | seguimiento, 2024-25 (convocatoria 2026) |
| Seguimiento ACCUA | no consta: se asume sí |
| Conjunto | aprendizaje |
| Fecha | 2026-10-04 |
| Versión de la skill | 4e6da0d |
| Versión de la rúbrica | 2 |
| Modelo A (generador y autocotejo) | claude-opus-5.5 |
| Modelo B (segundo corrector) | gpt-6.1-sol |

## Generación (completa el subagente A)

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (comprobado en las URL del visor que devuelven las herramientas lincebi_*) |
| Fecha de extracción | 2026-10-04 |
| Documentos de entrada usados | `entrada/autoinforme-anterior.pdf` (autoinforme 2023-24), `entrada/memoria.pdf` (memoria verificada/modificada), `entrada/informe-accua.pdf` (informe final de renovación de la acreditación). Informes de LinceBI: P01, P04 (rendimiento, satisfacción y acceso), P05 resto de indicadores, P05_01_evolucion_Total, P06, P07_Indicadores_satisfaccion, P07_Indicadores_bau, P07_IndicadoresTotal (solo columna 2020-21), encue_RSGC_P07_3 (egresados), P04_Perfil_Ing_Tit_Grado y PorcentajeCalificaciones (centro 5, plan 0519, curso 2024). |
| Supuestos tomados sin poder preguntar | Tipo seguimiento; seguimiento ACCUA no consta y se asume sí (se mantienen tabla UCADrive y líneas de evidencias por criterio). Indicadores de LinceBI. Sin datos internos del centro: fechas de elaboración/aprobación, usuario y clave UCADrive, rutas de evidencias, actas de coordinación, Anexo III (prácticas), relación nominal del Anexo II, reconocimiento de créditos y resultados de primer curso quedan `[PENDIENTE]`. Acrónimo de centro FFL en los códigos PF/PD/AM. Columna 2020-21 de P01, P04-16…19 y P06 tomada del autoinforme anterior (LinceBI solo muestra cuatro cursos). «-» de LinceBI en BAU y en movilidad saliente internacional 2020-21 consignado como 0%, con nota. |
| Decisiones relevantes | Cuatro puntos débiles con su acción: PD-FFL-3.1 (coordinación, ISGC-P04-10 2,88), PD-FFL-4.1 (participación en formación del PDI), PD-FFL-5.1 (movilidad saliente) y PD-FFL-7.1 (sin datos de empleadores); criterios 1, 2 y 6 sin puntos débiles. Plan de mejora de 13 filas: recomendaciones ACCUA citadas por criterio y tipo (el informe no las numera) y recomendaciones DEVA 8 y 9 que siguen abiertas. 4.6 y 5.5 «No procede» (solo presencial); 3.6 «No procede». Tabla de objetivos de la memoria en 6.3 (éxito 87,3% < 90%; eficiencia 91,7% < 92%). Anexo IV con todas las asignaturas y columna añadida de no presentados; en 6.3, selección de 12 asignaturas. Anexo II con totales del P05-01 (49 profesores, 97,96% doctores) y relación nominal `[PENDIENTE]`. 80 marcas `[PENDIENTE]` en total. Frases modelo de la plantilla no acreditadas por las fuentes (p. ej. «intensa actividad de coordinación», «reuniones periódicas») sustituidas o dejadas en `[PENDIENTE]`. |
| Incidencias | El informe nominal «P05 - Personal docente disponible para impartir el título» no está accesible en LinceBI (solo P05_01_evolucion_Total y P05_RestoIndicadores_Total). No hay informe de créditos reconocidos ni de resultados de primer curso. Serie ISGC-P04-13 2021-22…2023-24 ≈ mitad de la del autoinforme anterior. Fecha del informe de renovación discrepante (05/07/2023 en un documento, 26/10/2022 en otro). Nuevo ingreso 2024-25: 70 en LinceBI frente a 75 en el autoinforme anterior, con ocupación 100%. Tasas dinámicas (P04-05) distintas de las publicadas antes (43 y 32). P05-06 + P05-07 del centro suman más de 100%. ISGC-P07-07 cohorte 2022-23 «No disponible». Scripts: `narrativa.py` falló al principio por desplazamiento de índices de tabla tras insertar la tabla de objetivos (corregido fijando referencias); `depurar_instrucciones.py` dejó restos de enlaces genéricos a data.uca.es y un espacio antes de punto, corregidos con `trabajo/retoques.py`. |

## Resultado (completa `evaluacion.py medir`)

<!-- medir:inicio -->
| Métrica | Borrador | Humano |
|---|---|---|
| Palabras | 14229 | 40914 |
| PF distintos | 9 | 0 |
| PD distintos | 4 | 0 |
| AM distintas | 4 | 0 |
| `[PENDIENTE]` | 77 | 0 |

Extensión borrador / humano: 14.229 / 40.914 (35 %).
Valores del Anexo I presentes en algún lugar de la referencia (cota superior, no mide la celda): 571/587 (97.3 %).

| Dim. | A | B | Final |
|---|---|---|---|
| D1 | 2 | 2 | 2 |
| D2 | 2 | 2 | 2 |
| D3 | 2 | 1 | 1 |
| D4 | 2 | 1 | 1 |
| D5 | 2 | 2 | 2 |
| D6 | 1 | 2 | 2 |
| D7 | 2 | 1 | 1 |

Media final: 1.57. Bloqueantes: B1. Discrepancias por causa (B): S=6, D=3, I=2, H=4, E=1.

**Aviso de huellas de casos en la skill** (revisar que no sean datos de títulos):
- `skills/uca-informes-calidad/references/estilo-y-ejemplos.md`: 1 frases de GIDIDP-seg-2425 (p. ej. «de eficiencia esta tasa con un valor de»)
- `skills/uca-informes-calidad/references/estructura-autoinforme.md`: 1 frases de GH-seg-2425 (p. ej. «2 sistema de garantía interno de la calidad»)
- `skills/uca-informes-calidad/references/mapa-indicadores-lincebi.md`: 1 frases de GH-seg-2425 (p. ej. «participación en proyectos de innovación y mejora docente»)
<!-- medir:fin -->

## Pendiente de revisión experta

- Bloqueante B1
- Discrepancia 4 (H): Anexo I, ISGC-P04-13 de centro en 2024-25
- Discrepancia 6 (H): Anexo I, egresados de centro: P07-09, P07-10 y P07-01_03
- Discrepancia 9 (H): 6.3, tasa de graduación de 2024-25
- Discrepancia 11 (I): Criterios 1, 2 y 7 y plan de mejora: empleadores
- Discrepancia 12 (I): 3.3, 2.x, 1.x, Anexos II y III, portada
- Discrepancia 3 (H): Anexo I, P04-13 del centro, 2024-25
- Discrepancia 5 (H): Anexo I, P07-01_03 del centro, cohorte 2023-24
- Discrepancia 6 (H): 7.5, cohorte de egresados
- Discrepancia 7 (H): 6.3, objetivos de la memoria
- Discrepancia 13 (I): Anexo II; 3.3 y 6.3; evidencias de criterios
- Discrepancia 14 (I): Anexo III y 7.4, datos internos

## Decisión del responsable

| Lección | Decisión | Motivo |
|---|---|---|
| <Lxx> | <incorporada / candidata / descartada> | <filtro de admisión: norma, ≥2 títulos o Unidad de Calidad> |

## Retro del proceso

<Qué ajustar de la rúbrica, las plantillas, el procedimiento o el script antes de la siguiente
ejecución.>
