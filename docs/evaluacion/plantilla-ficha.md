# Ficha de ejecución — <Enn-id>

<!-- La crea `evaluacion.py nueva`. Los campos entre <…> los completa quien se indica. -->

## Ejecución

| Campo | Valor |
|---|---|
| Ejecución | <Enn> |
| Caso | <id> |
| Título | <titulo> |
| Tipo y curso | <tipo>, <curso> (convocatoria <convocatoria>) |
| Seguimiento ACCUA | <sí / no / no consta: se asume sí> |
| Conjunto | <aprendizaje / reserva> |
| Fecha | <AAAA-MM-DD> |
| Versión de la skill | <commit de skills/ y si hay cambios sin commit> |
| Versión de la rúbrica | <n> |
| Modelo A (generador y autocotejo) | <modelo> |
| Modelo B (segundo corrector) | <modelo> |

## Generación (completa el subagente A)

| Campo | Valor |
|---|---|
| Host de LinceBI | <data.uca.es / otro> |
| Fecha de extracción | <AAAA-MM-DD> |
| Documentos de entrada usados | <lista> |
| Supuestos tomados sin poder preguntar | <respuestas que la skill pide al usuario y cómo se resolvieron> |
| Decisiones relevantes | <reglas aplicadas, datos que quedaron `[PENDIENTE]` y por qué> |
| Incidencias | <errores de LinceBI, de scripts, etc.> |

## Resultado (completa `evaluacion.py medir`)

<!-- medir:inicio -->
<!-- medir:fin -->

## Valoración de la coordinación (completa `evaluacion.py valoracion`)

<!-- valoracion:inicio -->
Pendiente de recibir la hoja de valoración (paso 8).
<!-- valoracion:fin -->

## Pendiente de revisión experta

<Dimensiones con notas A y B que difieren en 2, discrepancias de causa H o I y bloqueantes. Las
lista `medir`; `valoracion` añade las dimensiones en las que la coordinación y la IA difieren
1 punto o más y los desacuerdos sobre errores graves. El responsable puede añadir o quitar.>

## Decisión del responsable

| Lección | Decisión | Motivo |
|---|---|---|
| <Lxx> | <incorporada / candidata / descartada> | <filtro de admisión: norma, ≥2 títulos o Unidad de Calidad> |

## Retro del proceso

<Qué ajustar de la rúbrica, las plantillas, el procedimiento o el script antes de la siguiente
ejecución.>
