import json, os

A = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
E = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]


def s(vals, years=A, suf=""):
    vals = vals.split("|")
    assert len(vals) == len(years), vals
    return {y: (v.strip() + suf if v.strip() not in ("", "0%") and suf and not v.strip().endswith("%") else v.strip())
            for y, v in zip(years, vals)}


def ind(t, c, years=A, suf=""):
    return {"titulo": s(t, years, suf), "centro": s(c, years, suf)}


P = "%"
indicadores = {
    "ISGC-P01-01": ind("3,54|3,37|3,46|3,68|3,43", "3,32|3,42|3,5|3,38|3,45"),
    "ISGC-P01-02": ind("3,89|4,16|4,4|3,82|3,97", "4,2|4,2|4,36|4,31|4,08"),
    "ISGC-P01-03": ind("3,71|3,8|3,45|3,73|3,66", "3,71|3,8|3,45|3,73|3,66"),
    "ISGC-P04-01": ind("85,2|74,1|77,1|79,4|77", "83|76|79,6|80,4|78,6"),
    "ISGC-P04-02": ind("92,8|87,4|89,4|89,3|87,3", "91,3|87,8|89,7|88,9|87,6"),
    "ISGC-P04-03": ind("91,8|84,8|86,3|88,9|88,2", "90,9|86,6|88,7|90,3|89,7"),
    "ISGC-P04-04": ind("16,5|15,9|17,7|33,3|18,2", "25|22,3|26,9|31,5|25,3"),
    "ISGC-P04-05": ind("51,9|53,7|45,6|44|62,3", "39,5|39|38,9|39,1|46,9"),
    "ISGC-P04-06": ind("87,3|93,1|88,4|89|91,7", "86,3|89,9|88,5|89|88"),
    "ISGC-P04-07": ind("5,1|4,8|4,9|4,9|4,6", "5,24|5,27|5,25|5,19|5,38"),
    "ISGC-P04-08": ind("1,09|1|1,55|1,56|1,67", "1,99|1,73|1,93|1,62|1,65"),
    "ISGC-P04-09|Movilidad entrante internacional": ind("12,46|24,72|20,06|15,95|18,38", "11,96|24,86|54,2|47,08|42,16", suf=P),
    "ISGC-P04-09|Movilidad entrante nacional": ind("0,85|0,84|1,18|0,92|0,62", "0,33|1,05|1,08|0,79|0,79", suf=P),
    "ISGC-P04-09|Movilidad saliente internacional": ind("0%|0,84|1,47|0,31|1,56", "2,14|5,04|6,89|4,4|5,87", suf=P),
    "ISGC-P04-09|Movilidad saliente nacional": ind("0,57|0,28|0,59|1,23|0,31", "0,8|0,98|0,93|0,79|0,29", suf=P),
    "ISGC-P04-10": ind("3,01|2,93|3|3,01|2,88", "2,81|3,07|3,05|2,97|3,14"),
    "ISGC-P04-11": ind("3,41|3,25|2,82|3,26|3,55", "3,03|3,22|3,24|3,13|3,38"),
    "ISGC-P04-12": ind("4,45|3,94|4|4,17|4,33", "4,3|4,21|4,33|4,39|4,33"),
    "ISGC-P04-13": ind("4,84|2,02|2,34|2,33|4,61", "4,77|1,52|2,35|2,35|4,81"),
    "ISGC-P04-14": ind("3,26|3,46|3,53|3,82|3,94", "3,22|3,59|3,69|3,38|3,7"),
    "ISGC-P04-15": ind("3,43|2,91|3,83|3,48|3,83", "3,55|3,31|3,76|3,51|3,87"),
    "ISGC-P05-02": ind("70,45|34,78|48,94|40|26,53", "50|32,14|31,64|36|32,95", suf=P),
    "ISGC-P05-03": ind("29,55|21,74|34,04|15,56|30,61", "32,35|20,83|21,47|25,14|31,21", suf=P),
    "ISGC-P05-04": ind("4,4|4,4|4,5|4,5|4,5", "4,3|4,3|4,4|4,4|4,4"),
    "ISGC-P05-05": ind("11,36|8,7|8,7|13,33|20,41", "12,94|11,9|11,9|12|16,18", suf=P),
    "ISGC-P05-06": ind("80|75|75|83,33|50", "86,36|85|85|57,14|53,57", suf=P),
    "ISGC-P05-07": ind("20|25|25|16,67|50", "13,64|15|15|9,52|60,71", suf=P),
    "ISGC-P04-16": ind("93,67|85,19|92,21|91,46|92", "82,63|79,33|79,49|77,65|81,56", suf=P),
    "ISGC-P04-17": ind("105,33|108|102,67|109,33|100", "70,32|63,83|66,38|72,34|73,83", suf=P),
    "ISGC-P04-18": ind("141,33|125,33|136|130,67|129,33", "85,26|74,68|72,34|85,11|87,45", suf=P),
    "ISGC-P04-19": ind("21,91|22,01|22,12|24,54|21,5", "23,44|22,26|23,3|25,04|24,69", suf=P),
    "ISGC-P06-01": ind("3,28|3,07|3,24|3,27|3,28", "2,99|3,17|3,16|3,05|3,21"),
    "ISGC-P06-02": ind("2,98|2,98|2,94|3,02|2,93", "2,66|2,89|2,97|2,94|3"),
    "ISGC-P06-03": ind("3,55|3,48|3,63|3,7|3,37", "3,32|3,58|3,57|3,39|3,44"),
    "ISGC-P06-04": ind("3,75|3,92|4,15|3,99|3,77", "3,95|3,94|4,06|4,08|3,84"),
    "ISGC-P07-01_01": ind("31,46|37,15|18,53|25,15|21,6", "57,41|44,13|42,76|45,52|40,53", suf=P),
    "ISGC-P07-01_02": ind("62,22|72,34|54,17|51,06|64,71", "34,22|33,48|28,19|29,34|26,99", suf=P),
    "ISGC-P07-02": ind("3,52|3,48|3,46|3,62|3,8", "3,34|3,48|3,48|3,45|3,57"),
    "ISGC-P07-03": ind("3,89|3,97|3,88|3,82|3,81", "3,97|3,89|3,93|3,99|3,84"),
    "ISGC-P07-04": ind("3,81|3,82|3,81|3,78|3,82", "3,81|3,82|3,81|3,78|3,82"),
    "ISGC-P07-01_03": ind("18,52% (10/54)|21,57% (11/51)|19,23% (10/52)|18,52% (10/54)|21,28% (10/47)",
                          "14,48% (32/221)|14,73% (47/319)|17,51% (45/257)|16,30% (45/276)|24,23% (71/293)", E),
    "ISGC-P07-05": ind("20,00|9,09|10,00|11,11|10,64", "34,38|25,53|33,33|10,87|12,63", E, P),
    "ISGC-P07-06": ind("50,00|0,00|0,00|16,67|60,00", "90,91|58,33|73,33|50,00|59,46", E, P),
    "ISGC-P07-07": ind("0,00|0,00|0,00|No disponible*|20,00", "0,00|8,33|0,00|3,33|8,11", E, P),
    "ISGC-P07-08": ind("0,00|0,00|100,00|16,67|20,00", "54,55|33,33|53,33|40,00|44,44", E, P),
    "ISGC-P07-09": ind("2,00|3,45|2,50|3,44|3,70", "2,87|3,51|3,09|3,41|3,43", E),
    "ISGC-P07-10": ind("2,30|3,18|2,60|3,20|3,70", "3,13|3,51|3,18|3,27|3,44", E),
    "ISGC-P07-11": ind("0,25|1,24|0,26|0,27|0%", "0,48|0,75|0,99|0,08|0,5", suf=P),
    "ISGC-P07-12": ind("0%|0%|0%|0%|0%", "0,84|0,56|0,68|1,08|0,37", suf=P),
    "ISGC-P07-13": ind("0%|0,25|0,26|0%|0%", "0,06|0,06|0,08|0%|0,06", suf=P),
    "ISGC-P07-14": ind("0%|0%|0%|0%|0%", "0,06|0,06|0%|0%|0,06", suf=P),
}
# "No disponible*" no debe llevar sufijo
indicadores["ISGC-P07-07"]["titulo"]["2022-23"] = "No disponible*"

ACCUA_FECHA = "Informe final para la renovación de la acreditación (ACCUA), 05/07/2023"
accua_items = [
    {"rec": "CRITERIO 1. INFORMACIÓN PÚBLICA DISPONIBLE. Aspecto que debe ser subsanado: Se deben incluir en la página web los resultados de satisfacción de todos los grupos de interés (estudiantes, PDI, personal de apoyo, egresados y empleadores).",
     "accion": "Acción de mejora: publicación en el sistema de información de la UCA y enlace desde la web del título a los informes de satisfacción de todos los grupos de interés (acción recogida en el autoinforme 2023-24). Los resultados de empleadores no pueden publicarse mientras no exista la encuesta (ver Criterio 7). Evidencia: [PENDIENTE: enlace de la web del título donde se publican los resultados de satisfacción y confirmación de que incluye a todos los grupos]. Estado: en curso."},
    {"rec": "CRITERIO 2. SISTEMA DE GARANTÍA DE CALIDAD. Aspectos que deben ser subsanados: Se debe contar con un plan de mejora actualizado y disponible en la página web. Se deben aportar indicadores de satisfacción de los empleadores, en particular en relación con la formación recibida por los egresados. Se debe continuar con el esfuerzo para conocer el grado de satisfacción de los egresados mediante indicadores estadísticamente significativos. En este sentido, particularmente relevante resulta conocer el grado de satisfacción de dicho colectivo con el programa formativo.",
     "accion": "Acción de mejora: el plan de mejora se actualiza en cada autoinforme y se publica en la web del título [PENDIENTE: enlace al plan de mejora vigente publicado]. Encuesta a empleadores diseñada por el Vicedecanato de Posgrado y Calidad (acción del autoinforme 2023-24), sin resultados disponibles en 2024-25 [PENDIENTE: confirmar estado de implantación]. Egresados: la participación de la cohorte 2023-24 es del 21,28% (10 de 47), todavía insuficiente para conclusiones estadísticamente significativas (AM-FFL-7.1). Estado: en curso."},
    {"rec": "CRITERIO 3. DISEÑO, ORGANIZACIÓN Y DESARROLLO DEL PROGRAMA FORMATIVO. Aspecto que debe ser subsanado: Se deben analizar las causas de la baja satisfacción de los estudiantes con la coordinación académica del grado e implementar las acciones oportunas para mejorar esa coordinación.",
     "accion": "Acción de mejora: seguimiento de las asignaturas compartidas por varios profesores y reuniones con el profesorado implicado (autoinforme 2023-24). Ante el descenso de ISGC-P04-10 a 2,88 en 2024-25, se refuerza con AM-FFL-3.1 (análisis de causas por curso y plan de coordinación de asignaturas compartidas). Evidencia: [PENDIENTE: actas de las reuniones de coordinación de 2024-25]. Indicador: ISGC-P04-10. Estado: en curso."},
    {"rec": "CRITERIO 4. PROFESORADO. Aspectos para la mejora del título: Se recomienda fomentar la participación del profesorado en proyectos de innovación educativa y mejora de la calidad docente. Se recomienda fomentar la participación del profesorado de la titulación en los programas de evaluación docente de la universidad.",
     "accion": "Acción de mejora: difusión entre el profesorado del título de las convocatorias de innovación, formación y DOCENTIA (AM-FFL-4.1). Indicadores 2024-25: participación en innovación (ISGC-P05-03) 30,61%, frente al 15,56% de 2023-24; participación en DOCENTIA (ISGC-P05-05) 20,41%, frente al 13,33%. Estado: en curso."},
    {"rec": "CRITERIO 5. RECURSOS Y APOYO A LA DOCENCIA. Aspectos que deben ser subsanados: Se deben analizar las causas que pueden estar detrás de los bajos niveles de participación en los programas de movilidad saliente y establecer acciones de mejora para aumentarla. Se debe mejorar la oferta de prácticas externas, con un número suficiente y adecuado de plazas. Se debe analizar si el personal administrativo que presta apoyo a la titulación resulta suficiente y su organización es la adecuada.",
     "accion": "Acción de mejora: aumentar la información sobre los programas de movilidad, teniendo en cuenta la situación socioeconómica del alumnado (autoinforme 2023-24), reforzada con AM-FFL-5.1. Prácticas: ISGC-P04-08 alcanza 1,67 plazas por solicitud en 2024-25 [PENDIENTE: plazas y convenios del curso]. Personal de apoyo: [PENDIENTE: análisis de suficiencia del PTGAS por parte del centro; no consta acción en el plan anterior]. Estado: en curso."},
    {"rec": "CRITERIO 6. RESULTADOS DEL PROGRAMA FORMATIVO. Aspecto para la mejora del título: Se recomienda continuar con el seguimiento de las tasas de graduación y abandono, con el fin de consolidar la tendencia positiva de los últimos cursos académicos.",
     "accion": "Acción de mejora: seguimiento anual de ISGC-P04-04 e ISGC-P04-05 en el autoinforme; flexibilización de la matrícula de optativas en tercer curso y cursos de apoyo idiomático (autoinforme 2023-24). En 2024-25 el abandono baja al 18,2% (33,3% en 2023-24) y la graduación sube al 62,3%. Estado: en curso (seguimiento permanente)."},
    {"rec": "CRITERIO 7. ORIENTACIÓN ACADÉMICA, ORIENTACIÓN PROFESIONAL Y EMPLEABILIDAD. Aspectos que deben ser subsanados: Se deben obtener datos de satisfacción de empleadores con la formación recibida por los egresados. Se debe realizar un análisis y reflexión sobre la empleabilidad del título en relación con su sostenibilidad.",
     "accion": "Acción de mejora: charlas y mesas redondas sobre salidas profesionales con expertos y egresados, previstas por la Subcomisión para la mejora del Grado, y contactos con la Oficina de Egresados (reunión de 09/06/2023) (autoinforme 2023-24). Se añade AM-FFL-7.1 (consulta a empleadores). El análisis de empleabilidad y sostenibilidad se recoge en los subcriterios 7.2 y 7.6. Evidencia: [PENDIENTE: confirmar actividades realizadas en 2024-25]. Estado: en curso."},
]

puntos = {
    "1": {"fuertes": [
        "PF-FFL-1.1.- La satisfacción del PDI con la información publicada sobre el título (ISGC-P01-02) se mantiene por encima de 3,8 sobre 5 en toda la serie (3,97 en 2024-25)."],
        "debiles": []},
    "2": {"fuertes": [
        "PF-FFL-2.1.- Las recomendaciones del informe de renovación de ACCUA de 05/07/2023 se siguen de forma sistemática en el autoinforme y en el plan de mejora."],
        "debiles": []},
    "3": {"fuertes": [
        "PF-FFL-3.1.- Alta demanda del título: tasa de preferencia (ISGC-P04-18) del 129,33% y tasa de adecuación (ISGC-P04-16) del 92% en 2024-25, muy por encima de las del centro (87,45% y 81,56%)."],
        "debiles": [{"punto": "PD-FFL-3.1.- La satisfacción del alumnado con la coordinación docente (ISGC-P04-10) baja a 2,88 sobre 5 en 2024-25, el valor más bajo de la serie y por debajo del centro (3,14), aspecto ya señalado por ACCUA.",
                     "acciones": ["AM-FFL-3.1.- Analizar por curso las causas de la baja satisfacción con la coordinación (consulta a la delegación de estudiantes) y aprobar un plan de coordinación de las asignaturas compartidas con reuniones semestrales con acta."]}]},
    "4": {"fuertes": [
        "PF-FFL-4.1.- Satisfacción global del alumnado con la docencia (ISGC-P05-04) de 4,5 sobre 5 en los tres últimos cursos, por encima del centro (4,4).",
        "PF-FFL-4.2.- Aumenta la participación en DOCENTIA (ISGC-P05-05), del 8,7% en 2022-23 al 20,41% en 2024-25, por encima del centro (16,18%)."],
        "debiles": [{"punto": "PD-FFL-4.1.- La participación del profesorado en acciones formativas (ISGC-P05-02) desciende al 26,53% en 2024-25, el valor más bajo de la serie y por debajo del centro (32,95%).",
                     "acciones": ["AM-FFL-4.1.- Difundir entre el profesorado del título el catálogo de formación y las convocatorias de innovación de la UCA, priorizando acciones sobre coordinación docente y evaluación."]}]},
    "5": {"fuertes": [
        "PF-FFL-5.1.- La satisfacción del alumnado con las prácticas externas (ISGC-P04-14) crece de forma continuada en toda la serie, hasta 3,94 sobre 5 en 2024-25, por encima del centro (3,7)."],
        "debiles": [{"punto": "PD-FFL-5.1.- La movilidad saliente internacional (ISGC-P04-09) sigue siendo muy baja: 1,56% en 2024-25, frente al 5,87% del centro.",
                     "acciones": ["AM-FFL-5.1.- Realizar una consulta al alumnado de 2º y 3º sobre los motivos que frenan la movilidad saliente y organizar una sesión informativa específica del Grado en Historia sobre convenios, ayudas y reconocimiento."]}]},
    "6": {"fuertes": [
        "PF-FFL-6.1.- Las tasas de graduación (62,3%) y de abandono (18,2%) de 2024-25 mejoran ampliamente los objetivos de la memoria (35,6% y 37,38%).",
        "PF-FFL-6.2.- La duración media de los estudios (ISGC-P04-07) se reduce a 4,6 años, la más baja de la serie y por debajo del centro (5,38)."],
        "debiles": []},
    "7": {"fuertes": [
        "PF-FFL-7.1.- La satisfacción de los egresados con los estudios y con las competencias (ISGC-P07-09 y 10) alcanza 3,70 sobre 5 en la cohorte 2023-24, la más alta de la serie (con baja participación: 10 de 47)."],
        "debiles": [{"punto": "PD-FFL-7.1.- El título sigue sin datos de satisfacción de los empleadores con la formación de los egresados, como exige ACCUA.",
                     "acciones": ["AM-FFL-7.1.- Recoger la opinión de las entidades colaboradoras de prácticas y empleadores sobre la formación de los egresados mediante un cuestionario breve y una reunión anual con acta, en coordinación con la Oficina de Egresados."]}]},
}

plan = [
    {"origen": "ACCUA 05/07/2023 – Criterio 1 (subsanar): publicar en la web los resultados de satisfacción de todos los grupos de interés.",
     "accion": "Revisar la web del título y enlazar los informes de satisfacción de alumnado, PDI, PTGAS, egresados y, cuando existan, empleadores.",
     "evidencia": "Página de la web del título con los resultados [PENDIENTE: enlace]", "prioridad": "Alta",
     "responsable": "Vicedecanato de Posgrado y Calidad", "inicio": "2023-24", "fin": "Septiembre 2026",
     "indicador": "Publicación verificada en la revisión anual de la IPD"},
    {"origen": "ACCUA 05/07/2023 – Criterio 2 (subsanar): plan de mejora actualizado y disponible en la web.",
     "accion": "Publicar en la web del título el plan de mejora aprobado con este autoinforme.",
     "evidencia": "Plan de mejora publicado [PENDIENTE: enlace]", "prioridad": "Alta",
     "responsable": "Coordinación del Grado", "inicio": "2023-24", "fin": "Septiembre 2026",
     "indicador": "Plan de mejora publicado"},
    {"origen": "ACCUA 05/07/2023 – Criterios 2 y 7 (subsanar): indicadores de satisfacción de empleadores. PD-FFL-7.1.",
     "accion": "AM-FFL-7.1.- Cuestionario a entidades colaboradoras de prácticas y empleadores y reunión anual con acta, en coordinación con la Oficina de Egresados.",
     "evidencia": "Informe de resultados del cuestionario y acta de la reunión", "prioridad": "Alta",
     "responsable": "Vicedecanato de Posgrado y Calidad", "inicio": "2023-24", "fin": "Septiembre 2026",
     "indicador": "Nº de respuestas de empleadores; satisfacción media con la formación"},
    {"origen": "ACCUA 05/07/2023 – Criterio 2 (subsanar): satisfacción de egresados con indicadores estadísticamente significativos.",
     "accion": "Difundir la encuesta de egresados entre el alumnado de 4º antes de su egreso y a través de la Oficina de Egresados.",
     "evidencia": "Comunicaciones de difusión", "prioridad": "Media",
     "responsable": "Coordinación del Grado", "inicio": "Marzo 2026", "fin": "Septiembre 2027",
     "indicador": "ISGC-P07-01_03 (21,28% en la cohorte 2023-24)"},
    {"origen": "ACCUA 05/07/2023 – Criterio 3 (subsanar): baja satisfacción con la coordinación. PD-FFL-3.1.",
     "accion": "AM-FFL-3.1.- Análisis de causas por curso con la delegación de estudiantes y plan de coordinación de asignaturas compartidas con reuniones semestrales con acta (continúa la acción del plan anterior).",
     "evidencia": "Informe de causas y actas de coordinación", "prioridad": "Alta",
     "responsable": "Coordinación del Grado", "inicio": "2020-21", "fin": "Septiembre 2026",
     "indicador": "ISGC-P04-10 (2,88 en 2024-25)"},
    {"origen": "ACCUA 05/07/2023 – Criterio 4 (mejora): innovación docente y DOCENTIA. PD-FFL-4.1.",
     "accion": "AM-FFL-4.1.- Difusión entre el profesorado del título del catálogo de formación y de las convocatorias de innovación y DOCENTIA.",
     "evidencia": "Comunicaciones de la coordinación al profesorado", "prioridad": "Media",
     "responsable": "Coordinación del Grado", "inicio": "2020-21", "fin": "Septiembre 2026",
     "indicador": "ISGC-P05-02, ISGC-P05-03 e ISGC-P05-05"},
    {"origen": "ACCUA 05/07/2023 – Criterio 5 (subsanar): baja movilidad saliente. PD-FFL-5.1.",
     "accion": "AM-FFL-5.1.- Consulta al alumnado de 2º y 3º sobre los motivos que frenan la movilidad y sesión informativa específica del Grado.",
     "evidencia": "Informe de la consulta y registro de la sesión", "prioridad": "Alta",
     "responsable": "Vicedecanato de Internacionalización [PENDIENTE: confirmar denominación]", "inicio": "Marzo 2026", "fin": "Septiembre 2026",
     "indicador": "ISGC-P04-09 movilidad saliente internacional (1,56% en 2024-25)"},
    {"origen": "ACCUA 05/07/2023 – Criterio 5 (subsanar): oferta de prácticas externas con plazas suficientes.",
     "accion": "Mantener y ampliar los convenios con entidades del ámbito del patrimonio, archivos y gestión cultural.",
     "evidencia": "Relación de convenios y plazas del curso [PENDIENTE: datos del centro]", "prioridad": "Media",
     "responsable": "Coordinación de prácticas del centro", "inicio": "2023-24", "fin": "Septiembre 2026",
     "indicador": "ISGC-P04-08 (1,67 en 2024-25)"},
    {"origen": "ACCUA 05/07/2023 – Criterio 5 (subsanar): suficiencia y organización del personal administrativo de apoyo.",
     "accion": "Solicitar al centro un análisis de la suficiencia y organización del PTGAS que atiende al título.",
     "evidencia": "Informe del centro [PENDIENTE]", "prioridad": "Media",
     "responsable": "Decanato de la Facultad", "inicio": "Marzo 2026", "fin": "Septiembre 2026",
     "indicador": "ISGC-P01-03 e ISGC-P07-04"},
    {"origen": "ACCUA 05/07/2023 – Criterio 6 (mejora): seguimiento de las tasas de graduación y abandono.",
     "accion": "Seguimiento anual de las tasas en el autoinforme; flexibilización de la matrícula de optativas en tercer curso.",
     "evidencia": "Autoinforme anual", "prioridad": "Alta",
     "responsable": "Coordinación del Grado", "inicio": "2018-19", "fin": "Septiembre 2026",
     "indicador": "ISGC-P04-04 e ISGC-P04-05"},
    {"origen": "ACCUA 05/07/2023 – Criterio 7 (subsanar): análisis de la empleabilidad en relación con la sostenibilidad.",
     "accion": "Charlas y mesas redondas sobre salidas profesionales con expertos y egresados (Subcomisión para la mejora del Grado).",
     "evidencia": "Programa de las actividades [PENDIENTE: confirmar realización]", "prioridad": "Alta",
     "responsable": "Subcomisión para la mejora del Grado en Historia", "inicio": "2020-21", "fin": "Septiembre 2026",
     "indicador": "ISGC-P07-05 a ISGC-P07-08"},
    {"origen": "Recomendación 8: PDIII.2: Mejora de la satisfacción del alumnado con los procedimientos relacionados con la gestión de los TFG (Plan de Mejora de la DEVA, 08/11/2019).",
     "accion": "Curso específico en el Campus Virtual con la información y gestión del TFG y recogida de información cualitativa sobre las causas del descontento (acción no finalizada en el plan anterior).",
     "evidencia": "Curso de coordinación de 4º en el Campus Virtual", "prioridad": "Media",
     "responsable": "Vicedecanato de Grados y Ordenación Académica", "inicio": "2021-22", "fin": "Septiembre 2026",
     "indicador": "ISGC-P04-11 (3,55 en 2024-25)"},
    {"origen": "Recomendación 9: PD.V.2.1: Baja tasa de graduación (Plan de Mejora de la DEVA, 08/11/2019).",
     "accion": "Cursos de apoyo idiomático para el B1 y flexibilización de la matrícula de optativas (acción del plan anterior). Se propone valorar su cierre a la vista de la tasa de 2024-25.",
     "evidencia": "Serie de ISGC-P04-05 en el Anexo 1", "prioridad": "Media",
     "responsable": "Coordinación del Grado", "inicio": "2018-19", "fin": "Septiembre 2026",
     "indicador": "ISGC-P04-05 (62,3% en 2024-25; objetivo 35,6%)"},
]

datos = {
    "encabezado": {"curso": "2024/25", "convocatoria": "2026", "titulo": "HISTORIA",
                   "centro": "FACULTAD DE FILOSOFÍA Y LETRAS"},
    "identificacion": {
        "Universidad": "Universidad de Cádiz",
        "ID Ministerio": "2501745",
        "Denominación del título": "Grado en Historia",
        "Curso académico de implantación": "2010/2011",
        "Web de la titulación": "https://filosofia.uca.es/estudios/grados/grado-en-historia/",
        "Oferta de título doble": "NO",
        "En su caso, especificar la/las titulación/es y el/los centro/s": "No procede",
        "En caso de ser un título conjunto, especificar las universidades donde se imparte": "No procede",
        "Modalidad de enseñanza (presencial, semipresencial-híbrida, virtual, a distancia)": "Presencial",
        "En su caso, fecha de la última renovación de la acreditación": "Informe final favorable de ACCUA de 05/07/2023 [PENDIENTE: confirmar fecha de la resolución; el autoinforme 2023-24 indica 26 de octubre de 2022]",
        "En su caso, créditos prácticos obligatorios": "No tiene (prácticas externas optativas de 6 ECTS)",
        "En su caso, estructuras curriculares específicas": "Itinerarios optativos de Historia de las Relaciones Internacionales y de Historia Cultural",
    },
    "anios": A,
    "anios_egresados": E,
    "extraccion": {"entorno": "data.uca.es", "fecha": "2026-10-04",
                   "notas": "Serie 2021-22 a 2024-25 de LinceBI en vivo; columna 2020-21 de P01, P04 (acceso) y P06 tomada del autoinforme 2023-24 porque LinceBI ya no la muestra; P07 2020-21 del informe histórico P07_IndicadoresTotal de LinceBI."},
    "indicadores": indicadores,
    "accua": {"fecha": ACCUA_FECHA, "items": accua_items},
    "puntos": puntos,
    "plan_mejora": plan,
}

out = os.path.join(os.path.dirname(__file__), "..", "datos.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)
print("OK", out)
