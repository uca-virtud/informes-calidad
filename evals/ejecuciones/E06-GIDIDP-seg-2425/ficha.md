# Ficha de ejecución — E06-GIDIDP-seg-2425

<!-- La crea `evaluacion.py nueva`. Los campos entre <…> los completa quien se indica. -->

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

## Generación (completa el subagente A)

| Campo | Valor |
|---|---|
| Host de LinceBI | data.uca.es (producción; herramientas lincebi_*) |
| Fecha de extracción | 2026-10-03 |
| Documentos de entrada usados | `evals/casos/GIDIDP-seg-2425/entrada/autoinforme-anterior.pdf` (autoinforme 2023-24: continuidad de contenidos, plan de mejora previo, informe ACCUA de 05/07/2023 y valores de 2020-21) y `memoria.pdf` (memoria verificada: plazas, ECTS, modalidad, objetivos de las tasas del apartado 8.1, prácticas optativas de 12 ECTS) |
| Supuestos tomados sin poder preguntar | Tipo: seguimiento, curso 2024-25, convocatoria 2026. ¿Seguimiento ACCUA?: no consta; se asume que sí (se mantienen la tabla UCADrive y la tabla de recomendaciones ACCUA). Indicadores: LinceBI. Datos internos del centro no aportados: fechas de aprobación por la CGC y la Junta de Centro, usuario y clave de UCADrive, enlace al reglamento de la CGC, nominal de profesorado (Anexo II), plazas, convenios y tutores de prácticas (Anexo III) y créditos reconocidos → `[PENDIENTE]` (28 marcas). Se mantiene el doble título PCEO con Ingeniería Mecánica, según el autoinforme anterior. |
| Decisiones relevantes | Series de LinceBI en vivo (tasas dinámicas): la graduación de 2023-24 es 34,6 %, frente al 7,7 % publicado en el autoinforme anterior, y se explica en el texto. Los valores de 2020-21 del título en P01, P04-16 a 19, P06 y P07-02 a 04 se toman del autoinforme anterior porque LinceBI no los devuelve. El objetivo del 50±5 % se aplica a la tasa de rendimiento, como dice la memoria (el autoinforme anterior lo atribuía al éxito). Notación: «Sin registros» cuando el informe no devuelve casos y «No disponible» cuando el dato no existe. Puntos débiles nuevos: solo PD-ESI-4.1 (TFG, ISGC-P04-11 = 2,50) y PD-ESI-6.1 (8 asignaturas básicas con más del 50 % de NP+suspensos). La coordinación, la orientación, los empleadores y la movilidad ya figuran como recomendaciones ACCUA abiertas, por lo que se analizan en el texto y se siguen en el plan de mejora (14 acciones). En los criterios sin debilidades nuevas, la tabla dice «No se identifican puntos débiles nuevos…». Anexo IV: se añade la columna de no presentados y una nota sobre el aprobado por compensación. |
| Incidencias | `P07_IndicadoresTotal.prpt` falló; se sustituyó por `P07_Indicadores_satisfaccion` y `encue_RSGC_P07_3`. LinceBI no tiene informes de créditos reconocidos ni nominal de profesorado. `rellenar_autoinforme.py` da avisos de escala en P07-01_x (falsos positivos: son % reales) y el aviso «una tabla tiene 1 columnas de años», sin efecto visible. `depurar_instrucciones.py` no limpia los fragmentos coloreados de los párrafos que contienen «[PENDIENTE»; por eso esos párrafos se reescribieron completos. En las tablas de puntos débiles de los criterios sin debilidades quedaban filas modelo («Punto débil nº»); se corrigieron a mano tras la depuración. |

## Resultado (completa `evaluacion.py medir`)

<!-- medir:inicio -->
| Métrica | Borrador | Humano |
|---|---|---|
| Palabras | 12892 | 24533 |
| PF distintos | 12 | 16 |
| PD distintos | 7 | 1 |
| AM distintas | 5 | 1 |
| `[PENDIENTE]` | 28 | 0 |

Extensión borrador / humano: 12.892 / 24.533 (53 %).
Valores del Anexo I presentes en algún lugar de la referencia (cota superior, no mide la celda): 544/553 (98.4 %).

| Dim. | A | B | Final |
|---|---|---|---|
| D1 | 2 | 2 | 2 |
| D2 | 2 | 2 | 2 |
| D3 | 2 | 1 | 1 |
| D4 | 1 | 1 | 1 |
| D5 | 2 | 2 | 2 |
| D6 | 2 | 2 | 2 |
| D7 | 2 | 1 | 1 |

Media final: 1.57. Bloqueantes: ninguno. Discrepancias por causa (B): S=8, D=3, I=1, H=3, E=1.

**Aviso de huellas de casos en la skill** (revisar que no sean datos de títulos):
- `skills/uca-informes-calidad/references/estilo-y-ejemplos.md`: 1 frases de GIDIDP-seg-2425 (p. ej. «de eficiencia esta tasa con un valor de»)
<!-- medir:fin -->

## Pendiente de revisión experta

- Discrepancia 2 (H): Anexo I, P04-05 título 2023-24
- Discrepancia 5 (H): Anexo I, P04-13 centro 2024-25
- Discrepancia 7 (H): Anexo I, egresados del título (P07-09/10)
- Discrepancia 8 (I): Criterio 3, créditos reconocidos 2024-25
- Discrepancia 9 (I): Criterio 5.3, Anexo III; fechas de la CGC y la Junta
- Discrepancia 11 (H): Criterio 1, objetivo de la memoria
- Discrepancia 12 (H): Criterio 5, profesorado (P05-01) y otros datos del texto humano
- Discrepancia 16 (H): Criterio 2 y plan, numeración de ACCUA
- Discrepancia 2 (H): Anexo I, egresados del título; 7.2 y 7.5
- Discrepancia 3 (H): Anexo I, P04-13 del centro, 2024-25
- Discrepancia 5 (H): 6.3, objetivos de la memoria
- Discrepancia 13 (I): 3.3; 4.5; 5.3; Anexos II-III y aprobación

## Decisión del responsable

| Lección | Decisión | Motivo |
|---|---|---|
| Adjetivos de evolución y objetivos en todas las apariciones (B-L03, B-L04) | incorporada (L23) | C2 de la línea base, E05 y E06 |
| Contraste con la serie del autoinforme anterior (A-L02) | incorporada (L24) | E05 y E06 |
| Estado heredado y eficacia de acciones (A-L01, B-L05) | incorporada (L25) | E04 y E06 |
| Anexo IV completo o con enlace específico (B-L01) | incorporada (L26) | C5 de la línea base y E06 |
| Restos de plantilla en negro y enlaces pegados (B-L07) | incorporada (L27) | E05 y E06 |
| Hipervínculos del PDF (B-L02), evidencias por criterio (B-L06) | candidata | Un solo título |

## Retro del proceso

<Qué ajustar de la rúbrica, las plantillas, el procedimiento o el script antes de la siguiente
ejecución.>
