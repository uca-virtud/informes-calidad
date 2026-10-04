# Ficha de ejecución — E04-GII-seg-2425

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | E04 |
| Caso | GII-seg-2425 |
| Título | Grado en Ingeniería Informática |
| Tipo y curso | seguimiento, 2024-25 (convocatoria 2026) |
| Seguimiento ACCUA | no consta: se asume sí |
| Conjunto | aprendizaje |
| Fecha | 2026-10-03 |
| Versión de la skill | d5ed099 + cambios sin commit |
| Versión de la rúbrica | 2 |
| Modelo A (generador y autocotejo) | claude-opus-5.5 |
| Modelo B (segundo corrector) | gpt-6.1-sol |

## Generación

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (producción; verificado en `viewerUrl`) |
| Fecha de extracción | 2026-10-03 |
| Documentos de entrada usados | `entrada/autoinforme-anterior.pdf` (autoinforme de seguimiento 2023-24: recomendaciones ACCUA del informe de 5/7/2023, plan de mejora previo, valores 2020-21 fuera de la ventana de LinceBI, créditos reconocidos 2023-24, datos descriptivos del centro); `entrada/memoria.pdf` (estructura de 240 ECTS, 150 plazas, objetivos del §8.1, prácticas optativas de 12 ECTS); plantilla y scripts de la skill; indicadores de LinceBI vía `lincebi_*` |
| Supuestos tomados sin poder preguntar | Tipo seguimiento; seguimiento ACCUA asumido (se conserva la tabla T3 de aplicaciones y se citan evidencias de asignaturas representativas); estado de las acciones ACCUA desconocido: se mantienen todas vivas y se amplían sus fechas de fin a 2026; un único responsable por acción elegido por afinidad (Coordinador de Grado, Subdirector de Estudiantes, Secretario Académico, Director); 4 puntos débiles (PD-ESI-6.1 TFG no presentados, 6.2 programación 1.º-2.º, 7.1 orientación, 7.2 empleadores) y arrastre de PD-ESI-4.1 solo al plan de mejora; web del título y espacio Colabora tomados del autoinforme anterior |
| Decisiones relevantes | Serie viva de LinceBI (se avisa de que difiere de lo publicado: graduación 2023-24 6,1→18,3; P04-13 2023-24 4,45→2,22); 2020-21 de P01, P06 y P04-16..19 del título del autoinforme anterior y centro 2020-21 «n.d.»; egresados por cohorte 2019-20..2023-24 con n/N y aviso del cambio de cálculo de P07-05..08 desde 2022-23; tabla objetivos memoria vs. tasas en 6.3; Anexo IV con las 77 asignaturas (NP entre paréntesis, aprobados con compensación). Quedan `[PENDIENTE]` (35): fechas de elaboración/aprobación, usuario/clave UCADrive, fecha de la Política de Calidad, enlaces a la página y al reglamento de la CGC, ruta UCADrive/evidencias, créditos reconocidos 2024-25, plazas/matrícula de nuevo ingreso y del doble título, enlace del itinerario del doble grado, técnicos de laboratorio, participantes en orientación, reunión con empleadores, relación nominal del profesorado, convenios/plazas/tutores de prácticas y fila GLOBAL de calificaciones (datos internos del centro no aportados o no disponibles en LinceBI) |
| Incidencias | El entorno rechaza escribir en /tmp: los temporales se crearon en la carpeta de sesión del agente; LinceBI devolvió `nextOffset` nulo y no se pudieron leer las filas finales de algunos informes (GLOBAL de calificaciones, total de P05-01, calculado a mano); no existe informe de créditos reconocidos del título en LinceBI; un 401 puntual de LinceBI resuelto al reintentar; `depurar_instrucciones.py` no limpia celdas de tabla ni párrafos mixtos (negro + rojo/XXXX): se reescribieron a mano y se recolorearon a negro 7 cabeceras azules de las tablas de calificaciones; las tablas de puntos débiles sin PD quedaban con «Punto débil nº XX» y se sustituyeron por «No se han identificado puntos débiles» |
