# Ficha de ejecución — E06-GIDIDP-seg-2425

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | E06 |
| Caso | GIDIDP-seg-2425 |
| Título | Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto |
| Tipo y curso | seguimiento, 2024-25 (convocatoria 2026) |
| Seguimiento ACCUA | no consta: se asume sí |
| Conjunto | aprendizaje |
| Fecha | 2026-10-03 |
| Versión de la skill | 2816f9e |
| Versión de la rúbrica | 2 |
| Modelo A (generador y autocotejo) | claude-opus-5.5 |
| Modelo B (segundo corrector) | gpt-6.1-sol |

## Generación

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (producción; herramientas lincebi_*) |
| Fecha de extracción | 2026-10-03 |
| Documentos de entrada usados | `evals/casos/GIDIDP-seg-2425/entrada/autoinforme-anterior.pdf` (autoinforme 2023-24: continuidad de contenidos, plan de mejora previo, informe ACCUA de 05/07/2023 y valores de 2020-21) y `memoria.pdf` (memoria verificada: plazas, ECTS, modalidad, objetivos de las tasas del apartado 8.1, prácticas optativas de 12 ECTS) |
| Supuestos tomados sin poder preguntar | Tipo: seguimiento, curso 2024-25, convocatoria 2026. ¿Seguimiento ACCUA?: no consta; se asume que sí (se mantienen la tabla UCADrive y la tabla de recomendaciones ACCUA). Indicadores: LinceBI. Datos internos del centro no aportados: fechas de aprobación por la CGC y la Junta de Centro, usuario y clave de UCADrive, enlace al reglamento de la CGC, nominal de profesorado (Anexo II), plazas, convenios y tutores de prácticas (Anexo III) y créditos reconocidos → `[PENDIENTE]` (28 marcas). Se mantiene el doble título PCEO con Ingeniería Mecánica, según el autoinforme anterior. |
| Decisiones relevantes | Series de LinceBI en vivo (tasas dinámicas): la graduación de 2023-24 es 34,6 %, frente al 7,7 % publicado en el autoinforme anterior, y se explica en el texto. Los valores de 2020-21 del título en P01, P04-16 a 19, P06 y P07-02 a 04 se toman del autoinforme anterior porque LinceBI no los devuelve. El objetivo del 50±5 % se aplica a la tasa de rendimiento, como dice la memoria (el autoinforme anterior lo atribuía al éxito). Notación: «Sin registros» cuando el informe no devuelve casos y «No disponible» cuando el dato no existe. Puntos débiles nuevos: solo PD-ESI-4.1 (TFG, ISGC-P04-11 = 2,50) y PD-ESI-6.1 (8 asignaturas básicas con más del 50 % de NP+suspensos). La coordinación, la orientación, los empleadores y la movilidad ya figuran como recomendaciones ACCUA abiertas, por lo que se analizan en el texto y se siguen en el plan de mejora (14 acciones). En los criterios sin debilidades nuevas, la tabla dice «No se identifican puntos débiles nuevos…». Anexo IV: se añade la columna de no presentados y una nota sobre el aprobado por compensación. |
| Incidencias | `P07_IndicadoresTotal.prpt` falló; se sustituyó por `P07_Indicadores_satisfaccion` y `encue_RSGC_P07_3`. LinceBI no tiene informes de créditos reconocidos ni nominal de profesorado. `rellenar_autoinforme.py` da avisos de escala en P07-01_x (falsos positivos: son % reales) y el aviso «una tabla tiene 1 columnas de años», sin efecto visible. `depurar_instrucciones.py` no limpia los fragmentos coloreados de los párrafos que contienen «[PENDIENTE»; por eso esos párrafos se reescribieron completos. En las tablas de puntos débiles de los criterios sin debilidades quedaban filas modelo («Punto débil nº»); se corrigieron a mano tras la depuración. |
