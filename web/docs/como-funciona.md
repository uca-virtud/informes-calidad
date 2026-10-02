# Cómo funciona

## Proceso actual

| Paso | Quién | Qué hace |
|---|---|---|
| 1 | Unidad de Calidad | Envía la plantilla vacía a cada coordinación |
| 2 | Coordinación del título | Rellena la plantilla con la documentación interna, su conocimiento y los indicadores de LinceBI |
| 3 | Unidad de Calidad | Revisa y devuelve el informe con anotaciones |
| 4 | Coordinación del título | Corrige el informe |
| 5 | Unidad de Calidad | Valida y lo envía a la agencia de calidad (o lo archiva si es seguimiento interno) |

## Proceso deseado

| Paso | Quién | Qué hace |
|---|---|---|
| 1 | Unidad de Calidad, con apoyo de la IA | Genera un **borrador** del autoinforme con los indicadores ya extraídos y el análisis redactado |
| 2 | Coordinación del título | Revisa el borrador, completa lo que la IA no puede saber y lo aprueba con la Comisión de Garantía de Calidad |
| 3 | Unidad de Calidad | Revisa, valida y lo envía a la agencia de calidad |

## Qué hace la IA

La IA trabaja con una *skill*: un procedimiento escrito que le indica cómo elaborar el
autoinforme siguiendo el modelo ACCUA/DEVA y la plantilla oficial de la UCA.

1. **Pregunta el tipo de autoinforme** (seguimiento o renovación de la acreditación) y los
   datos del título.
2. **Pide los documentos clave**: el autoinforme del curso anterior (con las recomendaciones de
   ACCUA y el plan de mejora) y la memoria verificada (con los objetivos de las tasas).
3. **Pide los datos internos del centro** que no están en LinceBI: prácticas, convenios,
   créditos reconocidos, rutas de evidencias, etc.
4. **Extrae los indicadores** de LinceBI (entorno de producción) y registra la fecha de
   extracción.
5. **Rellena las tablas** de forma automática y **redacta el análisis**, los puntos fuertes y
   débiles y el plan de mejora.
6. **Entrega un documento Word** con la plantilla oficial.

!!! warning "Siempre es un borrador"
    La IA no inventa datos: lo que no puede obtener queda marcado como **[PENDIENTE]**. La
    coordinación y la Comisión de Garantía de Calidad revisan siempre el contenido antes de
    presentarlo.

## Piezas técnicas

| Pieza | Función |
|---|---|
| LinceBI | Sistema de información estratégica de la UCA; fuente de los indicadores |
| Modelo de datos e informe agregado (fase 1) | Exponen todos los indicadores del Anexo I en una sola vista |
| Servidor MCP (fase 2) | Conecta la IA con LinceBI |
| Skill de autoinformes (fase 3) | Procedimiento, plantillas y scripts para generar el borrador |
