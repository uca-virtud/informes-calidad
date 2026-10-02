
# Objetivo del proyecto
Automatizar/acelerar la generación de informes de calidad de los títulos de la Universidad de Cádiz. Esos informes se hacen con periodicidad y son muy tediosos de rellenar. 


# Situación actual
La unidad de calidad proporciona una plantilla que entrega a los coordinadores de títulos para que la rellenen. Los 
coordinadores rellenan esa plantilla a partir de la información interna (que almacenan en una carpeta de Nextcloud), 
su propio conocimiento y los datos que se obtienen del sistema de información estratégica de la universidad (LinceBI). 

Los coordinadores devuelven las plantillas rellenas a la unidad de calidad, que revisa los informes y los devuelve a 
los coordinadores con una serie de anotaciones para que hagan las modificaciones pertinentes. Una vez que la unidad de 
calidad tiene los informes revisados y los valida, se los envía a las agencias de calidad externas para su evaluación 
o directamente para su archivado si es de seguimiento interno.

# Situación deseada
El objetivo futuro es que la unidad de calidad no mande a los coordinadores las plantillas, sino los borradores de los
informes generados con ayuda de IA. 

# Fases del proyecto
1. Desarrollo de un nuevo modelo de datos en LinceBI y un informe agregado para exponer rápidamente los indicadores 
   de calidad (P01–P08) necesarios para rellenar el anexo 1, descargables en su formato. Solicitado al Sistema de 
   Información con puesta en marcha deseada en noviembre de 2026, para usarse en los autoinformes del curso 2025-26; 
   el cuadro de mando se solicitará más adelante. Detalle en 
   [solicitud-SI-fase1.md](peticiones-cartera/solicitud-SI-fase1.md).
2. Desarrollar un MCP de conexión con LinceBI (ya desarrollado como un proyecto de Spring Boot con Maven).
3. Desarrollar skill para rellenar la plantilla de informes de calidad (disponible en carpeta 
   skills/uca-informes-calidad; cubre seguimiento y renovación de la acreditación). La versión anterior, solo de 
   seguimiento, se ha evaluado con tres grados de la ESI frente a sus autoinformes reales: ver 
   [EVALUACIONES.md](EVALUACIONES.md).
4. Establecer el entorno procedimental y operativo para la unidad técnica informática, la unidad de calidad y para 
   los coordinadores de títulos.
5. Pilotaje en Escuela Superior de Ingeniería y Facultad de Filosofía y Letras, para evaluación y mejora continua de 
   las skills y de todo el proceso.
6. Despliegue en el resto de facultades y escuelas.


