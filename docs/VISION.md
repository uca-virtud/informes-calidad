# Visión del proyecto

## Objetivo

Automatizar y acelerar la elaboración de los autoinformes de calidad de los títulos de la
Universidad de Cádiz, que se hacen periódicamente y son muy tediosos de rellenar.

## Situación actual

La Unidad de Calidad entrega a los coordinadores de títulos una plantilla para que la
rellenen. Los coordinadores la completan con la información interna del título (guardada en
una carpeta de Nextcloud), su propio conocimiento y los datos del sistema de información
estratégica de la universidad (LinceBI).

Los coordinadores devuelven las plantillas rellenas a la Unidad de Calidad, que revisa los
informes y se los devuelve con anotaciones para que hagan los cambios pertinentes. Cuando la
Unidad de Calidad valida los informes revisados, los envía a las agencias de calidad
externas para su evaluación o, si son de seguimiento interno, los archiva.

## Situación deseada

La Unidad de Calidad deja de enviar plantillas vacías a los coordinadores y les envía
borradores de los informes generados con ayuda de IA.

## Fases del proyecto

1. **Modelo de datos e informe agregado en LinceBI** para exponer rápidamente los
   indicadores de calidad (P01–P08) que necesita el Anexo I, descargables en su formato.
   Solicitado al Sistema de Información, con puesta en marcha deseada en noviembre de 2026
   para los autoinformes del curso 2025-26; el cuadro de mando se solicitará más adelante.
   *En desarrollo.* Detalle en
   [solicitud-SI-fase1.md](peticiones-cartera/solicitud-SI-fase1.md) (solo en local).
2. **MCP de conexión con LinceBI** (stdio). *Desarrollado* como proyecto Spring Boot con
   Maven.
3. **Skill para rellenar la plantilla** de los autoinformes, de seguimiento y de renovación
   de la acreditación. *Desarrollada* en `skills/uca-informes-calidad/`.
4. **Pilotaje** en la Escuela Superior de Ingeniería y la Facultad de Filosofía y Letras,
   para evaluar y mejorar la skill y todo el proceso. *En curso:* la skill se evalúa frente
   a los autoinformes reales de los títulos ([procedimiento](PROCEDIMIENTO.md) y
   [lecciones](LECCIONES.md)).
5. **MCP en modo HTTP**, con autenticación SSO/LDAP.
6. **Entorno procedimental y operativo** para la unidad técnica informática, la Unidad de
   Calidad y los coordinadores de títulos.
7. **Despliegue** en el resto de facultades y escuelas.
