# Ficha de ejecución — E07-GH-seg-2425

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

## Generación

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (comprobado en las URL del visor que devuelven las herramientas lincebi_*) |
| Fecha de extracción | 2026-10-04 |
| Documentos de entrada usados | `entrada/autoinforme-anterior.pdf` (autoinforme 2023-24), `entrada/memoria.pdf` (memoria verificada/modificada), `entrada/informe-accua.pdf` (informe final de renovación de la acreditación). Informes de LinceBI: P01, P04 (rendimiento, satisfacción y acceso), P05 resto de indicadores, P05_01_evolucion_Total, P06, P07_Indicadores_satisfaccion, P07_Indicadores_bau, P07_IndicadoresTotal (solo columna 2020-21), encue_RSGC_P07_3 (egresados), P04_Perfil_Ing_Tit_Grado y PorcentajeCalificaciones (centro 5, plan 0519, curso 2024). |
| Supuestos tomados sin poder preguntar | Tipo seguimiento; seguimiento ACCUA no consta y se asume sí (se mantienen tabla UCADrive y líneas de evidencias por criterio). Indicadores de LinceBI. Sin datos internos del centro: fechas de elaboración/aprobación, usuario y clave UCADrive, rutas de evidencias, actas de coordinación, Anexo III (prácticas), relación nominal del Anexo II, reconocimiento de créditos y resultados de primer curso quedan `[PENDIENTE]`. Acrónimo de centro FFL en los códigos PF/PD/AM. Columna 2020-21 de P01, P04-16…19 y P06 tomada del autoinforme anterior (LinceBI solo muestra cuatro cursos). «-» de LinceBI en BAU y en movilidad saliente internacional 2020-21 consignado como 0%, con nota. |
| Decisiones relevantes | Cuatro puntos débiles con su acción: PD-FFL-3.1 (coordinación, ISGC-P04-10 2,88), PD-FFL-4.1 (participación en formación del PDI), PD-FFL-5.1 (movilidad saliente) y PD-FFL-7.1 (sin datos de empleadores); criterios 1, 2 y 6 sin puntos débiles. Plan de mejora de 13 filas: recomendaciones ACCUA citadas por criterio y tipo (el informe no las numera) y recomendaciones DEVA 8 y 9 que siguen abiertas. 4.6 y 5.5 «No procede» (solo presencial); 3.6 «No procede». Tabla de objetivos de la memoria en 6.3 (éxito 87,3% < 90%; eficiencia 91,7% < 92%). Anexo IV con todas las asignaturas y columna añadida de no presentados; en 6.3, selección de 12 asignaturas. Anexo II con totales del P05-01 (49 profesores, 97,96% doctores) y relación nominal `[PENDIENTE]`. 80 marcas `[PENDIENTE]` en total. Frases modelo de la plantilla no acreditadas por las fuentes (p. ej. «intensa actividad de coordinación», «reuniones periódicas») sustituidas o dejadas en `[PENDIENTE]`. |
| Incidencias | El informe nominal «P05 - Personal docente disponible para impartir el título» no está accesible en LinceBI (solo P05_01_evolucion_Total y P05_RestoIndicadores_Total). No hay informe de créditos reconocidos ni de resultados de primer curso. Serie ISGC-P04-13 2021-22…2023-24 ≈ mitad de la del autoinforme anterior. Fecha del informe de renovación discrepante (05/07/2023 en un documento, 26/10/2022 en otro). Nuevo ingreso 2024-25: 70 en LinceBI frente a 75 en el autoinforme anterior, con ocupación 100%. Tasas dinámicas (P04-05) distintas de las publicadas antes (43 y 32). P05-06 + P05-07 del centro suman más de 100%. ISGC-P07-07 cohorte 2022-23 «No disponible». Scripts: `narrativa.py` falló al principio por desplazamiento de índices de tabla tras insertar la tabla de objetivos (corregido fijando referencias); `depurar_instrucciones.py` dejó restos de enlaces genéricos a data.uca.es y un espacio antes de punto, corregidos con `trabajo/retoques.py`. |
