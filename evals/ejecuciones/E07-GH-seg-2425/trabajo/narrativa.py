"""Redacta el análisis del autoinforme sobre trabajo/paso1.docx y guarda trabajo/paso2.docx."""
import copy
import json
from pathlib import Path

import docx
from docx.enum.text import WD_COLOR_INDEX
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

BASE = Path(__file__).resolve().parent
d = docx.Document(BASE / "paso1.docx")
NEGRO = RGBColor(0, 0, 0)
T = list(d.tables)


def pars():
    return [docx.text.paragraph.Paragraph(el, d) for el in d.element.body.iterchildren() if el.tag == qn("w:p")]


def find(prefix, n=1, after=None):
    """n-ésimo párrafo cuyo texto empieza por prefix (opcionalmente tras el párrafo after)."""
    started = after is None
    count = 0
    for p in pars():
        if not started:
            started = p._p is after._p
            continue
        if p.text.strip().startswith(prefix):
            count += 1
            if count == n:
                return p
    raise SystemExit(f"Ancla no encontrada: {prefix!r} (n={n})")


def color(run):
    return run.font.color.rgb if run.font.color and run.font.color.type else None


def blacken(p, mapping):
    """Sustituye el texto de runs rojos/azules según mapping y los pasa a negro."""
    for r in p.runs:
        if r.text in mapping and color(r) in (RGBColor(0xFF, 0, 0), RGBColor(0, 0xB0, 0xF0)):
            r.text = mapping[r.text]
            r.font.color.rgb = NEGRO


def replace_run(p, old, new):
    for r in p.runs:
        if r.text == old:
            r.text = new
            r.font.color.rgb = NEGRO
            return
    raise SystemExit(f"Run no encontrado: {old!r}")


def set_links(p, items):
    """Sustituye, en orden, los hipervínculos 'xxxxxx' del párrafo por (texto, url)."""
    links = [h for h in p._p.iter(qn("w:hyperlink")) if "xxxxxx" in "".join(t.text or "" for t in h.iter(qn("w:t")))]
    assert len(links) == len(items), (p.text[:60], len(links), len(items))
    for h, (texto, url) in zip(links, items):
        ts = list(h.iter(qn("w:t")))
        ts[0].text = texto
        for t in ts[1:]:
            t.text = ""
        h.set(qn("r:id"), d.part.relate_to(url, RT.HYPERLINK, is_external=True))


def set_text(p, text):
    runs = p.runs
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    for h in list(p._p.iter(qn("w:hyperlink"))):
        h.getparent().remove(h)
    if runs:
        runs[0].text = text
        runs[0].font.color.rgb = NEGRO
    else:
        p.add_run(text)


def delete(p):
    p._p.getparent().remove(p._p)


def add_runs(par, text):
    """Añade texto; los fragmentos **así** van en negrita."""
    partes = text.split("**")
    for i, frag in enumerate(partes):
        if frag:
            r = par.add_run(frag)
            r.bold = i % 2 == 1
            r.font.color.rgb = NEGRO


def before(anchor, items):
    """Inserta antes de anchor párrafos (str), viñetas ('-', str) o tablas ('tabla', filas)."""
    for it in items:
        if isinstance(it, tuple) and it[0] == "tabla":
            filas = it[1]
            t = d.add_table(rows=len(filas), cols=len(filas[0]))
            t.style = "Table Grid"
            for i, fila in enumerate(filas):
                for j, val in enumerate(fila):
                    c = t.cell(i, j)
                    c.text = ""
                    run = c.paragraphs[0].add_run(str(val))
                    run.font.size = Pt(9)
                    run.bold = i == 0
            anchor._p.addprevious(t._tbl)
            sep = anchor.insert_paragraph_before("", style="Normal")
        elif isinstance(it, tuple) and it[0] == "-":
            np_ = anchor.insert_paragraph_before("", style="List Paragraph")
            add_runs(np_, "• " + it[1])
        else:
            np_ = anchor.insert_paragraph_before("", style="Normal")
            np_.paragraph_format.space_after = Pt(6)
            add_runs(np_, it)


# ---------------------------------------------------------------- Portada
p = find("GRADO/MÁSTER EN:")
set_text(p, "GRADO EN: HISTORIA")
p = find("CENTRO/S:")
set_text(p, "CENTRO: FACULTAD DE FILOSOFÍA Y LETRAS")

t0 = T[0]
for c in t0.rows[2].cells:
    for par in c.paragraphs:
        if "xxx" in par.text:
            set_text(par, par.text.replace("xxx", "[PENDIENTE: fecha de aprobación]"))

t3 = T[3]
for j in (2, 3):
    c = t3.rows[1].cells[j]
    for par in c.paragraphs:
        set_text(par, "[PENDIENTE: facilitar por el centro]" if j == 2 else "[PENDIENTE: facilitar por el centro por canal seguro]")

# ---------------------------------------------------------------- Criterio 1
blacken(find("La información pública del "), {"grado/máster ": "Grado en Historia ", "XXXXXX ": ""})
set_text(
    find("En dicha web el título publica"),
    "En dicha web (https://filosofia.uca.es/grado-en-historia/) el título publica información sobre las características del "
    "programa y su desarrollo operativo, los resultados alcanzados, el Sistema de Garantía de Calidad (responsables, procesos "
    "y procedimientos) y los documentos oficiales del título (memoria, autoinformes e informes de ACCUA), así como el acceso a "
    "las normativas académicas y a los sistemas de apoyo al alumnado matriculado. La publicación de los resultados de "
    "satisfacción de todos los grupos de interés y del plan de mejora vigente fue señalada por ACCUA en su informe de "
    "05/07/2023 y se sigue en el Plan de Mejora [PENDIENTE: confirmar que los informes de satisfacción y el plan de mejora "
    "2024-25 están enlazados en la web del título].",
)

c1 = find("[Solo se incluirán los puntos fuertes", 1)
before(c1, [
    "**Análisis de la información pública disponible (curso 2024-25).** La web del título ofrece la memoria modificada "
    "(https://filosofia.uca.es/memoria-modificada-historia/), los informes de seguimiento y de renovación "
    "(https://filosofia.uca.es/informes-de-seguimiento-ghist/), el SGC del centro y las actas de la CGC "
    "(https://filosofia.uca.es/sistema-de-garantia-de-calidad/), las guías docentes (https://asignaturas.uca.es/asig/), la "
    "información de acceso y perfil de ingreso, prácticas externas y TFG. [PENDIENTE: resultado de la revisión anual de la "
    "información pública del título por la CGC en 2024-25 y fecha del acta.]",
    "Los indicadores del proceso P01 (Anexo 1, tabla 1) muestran una valoración estable y aceptable de la información "
    "publicada. La satisfacción del alumnado con la información publicada (ISGC-P01-01) baja de 3,68 en 2023-24 a 3,43 en "
    "2024-25, en línea con el centro (3,45), y se mantiene dentro de la franja 3,37-3,68 de toda la serie. La satisfacción "
    "del PDI (ISGC-P01-02) sube de 3,82 a 3,97, ligeramente por debajo del centro (4,08), y se ha mantenido por encima de 3,8 "
    "en los cinco cursos. La satisfacción del PTGAS con la información publicada (ISGC-P01-03) se mide para el centro, no "
    "para el título: 3,66 en 2024-25, frente a 3,73 del curso anterior.",
    "La valoración del alumnado debe leerse con cautela, porque la tasa de respuesta de su encuesta (ISGC-P07-01_01) es del "
    "21,6% en 2024-25, muy inferior a la del centro (40,53%). El descenso de ISGC-P01-01 no se considera punto débil: es "
    "moderado, iguala la media del centro y la publicación de resultados en la web ya se sigue como recomendación de ACCUA en "
    "el Plan de Mejora.",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 1].",
])

# ---------------------------------------------------------------- Criterio 2
blacken(find("En base al P02-"), {"XXXXXXXXXXXXXX ": "", "XXXXXXXXXXXXXXXXXXXXX ": "Facultad ", "XX/XX/XX": "28/07/2021"})
replace_run(find("En base al P02-"), "Proceso para la revisión de la gestión de la calidad la Facultad/Escuela ",
            "Proceso para la revisión de la gestión de la calidad la Facultad de Filosofía y Letras ")
p = find("La Comisión de Garantía de Calidad de la Facultad/Escuela")
blacken(p, {"XXXXXX ": ""})
replace_run(p, "La Comisión de Garantía de Calidad de la Facultad/Escuela ",
            "La Comisión de Garantía de Calidad de la Facultad de Filosofía y Letras ")
guiones = [q for q in pars() if q.text.strip() == "--"]
set_text(guiones[0], "Representantes del equipo decanal, de la administración del campus y de los diferentes grados del centro; la "
         "composición nominal vigente se publica en https://filosofia.uca.es/comision-de-garantia-de-calidad-de-la-facultad-de-filosofia-y-letras/ "
         "[PENDIENTE: confirmar composición vigente en 2024-25].")
for g in guiones[1:]:
    delete(g)
blacken(find("Esta "), {"XXXXXXXXXXXXXX": "https://filosofia.uca.es/wp-content/uploads/2022/07/REGLAMENTO_DE_LA_COMISION_DE_GARANTIA_DE_CALIDAD-JF_06-07-2022.pdf"})
set_text(
    find("El título cuenta con un Plan de Mejora actualizado"),
    "El título cuenta con un Plan de Mejora que se actualiza con este autoinforme a partir del análisis de la información "
    "recogida por los procesos del SGC y de los informes de evaluación externa (ACCUA). Para cada acción se identifican el "
    "indicador de seguimiento, el responsable, la prioridad y la temporalización (ver Plan de Mejora al final del documento).",
)

c2 = find("[Solo se incluirán los puntos fuertes", 2)
before(c2, [
    "**Análisis del funcionamiento del SGC en el título (curso 2024-25).** La CGC del centro es el órgano responsable del "
    "seguimiento del título y aprueba, junto con la Junta de Facultad, el autoinforme anual y su plan de mejora. El Plan "
    "Director del centro se aprobó en Junta de Facultad el 07/06/2022 (https://peuca3.uca.es/wp-content/uploads/2022/10/FACULTAD-DE-FILOSOFIA-Y-LETRAS.pdf). "
    "[PENDIENTE: sesiones de la CGC celebradas en 2024-25 en las que se trató el título y enlace a sus actas.]",
    "El último informe de ACCUA es el informe final de renovación de la acreditación de 05/07/2023 [PENDIENTE: confirmar la "
    "fecha; el autoinforme 2023-24 cita el 26 de octubre de 2022 como fecha de la última renovación]. Sus recomendaciones se "
    "recogen en la tabla siguiente con la acción que les da respuesta, y todas siguen abiertas en el Plan de Mejora. El "
    "informe de ACCUA no numera sus recomendaciones, por lo que se identifican por criterio y por su tipo (de obligado "
    "cumplimiento o de mejora). En el Plan de Mejora se mantienen además las recomendaciones 8 y 9 del Plan de Mejora de la "
    "DEVA de 08/11/2019 que el autoinforme anterior conservaba abiertas.",
    "Sobre la eficacia del SGC, el autoinforme anterior describía la gestión documental en tres plataformas (web, Sistema de "
    "Información y espacio colaborativo del centro); este curso se remite al UCADrive del centro [PENDIENTE: confirmar que "
    "las evidencias del título se han trasladado al UCADrive]. La satisfacción global con el título del alumnado "
    "(ISGC-P07-02: 3,80), del PDI (ISGC-P07-03: 3,81) y del PTGAS con el centro (ISGC-P07-04: 3,82) se analiza en los "
    "criterios 4, 5 y 6; sus tablas están en el Anexo 1 (tabla 5).",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 2].",
])

# ---------------------------------------------------------------- Criterio 3
p = find("El desarrollo del plan de estudios, conforme a la memoria verificada")
set_links(p, [("https://filosofia.uca.es/memoria-modificada-historia/", "https://filosofia.uca.es/memoria-modificada-historia/"),
              ("https://filosofia.uca.es/informes-de-seguimiento-ghist/", "https://filosofia.uca.es/informes-de-seguimiento-ghist/")])
before(find("La modalidad de enseñanza (presencial"), [
    "El plan de estudios (240 ECTS: 60 de formación básica, 114 obligatorios, 6 de TFG y 60 optativos, entre ellos las "
    "prácticas externas optativas de 6 ECTS) se ha impartido en 2024-25 conforme a la memoria. El autoinforme anterior "
    "señalaba que la memoria data de 2010 y que se había constituido una comisión de trabajo para su reforma [PENDIENTE: "
    "confirmar el estado actual de la propuesta de modificación del título]. En 2024-25 se han ofertado los dos itinerarios "
    "optativos previstos (Historia de las Relaciones Internacionales e Historia Cultural) [PENDIENTE: confirmar oferta].",
])
p = find("Las modalidades de impartición del título se corresponden")
blacken(p, {".": "."})
before(find("3.3."), ["El Grado en Historia se imparte solo en modalidad presencial, tal como establece la memoria verificada."])
delete(find("Rellenar solo en su caso"))
p = find("Respecto a la gestión de los TFG/TFM")
blacken(p, {"centro XXXXXXXX": "centro, la Facultad de Filosofía y Letras"})
set_links(p, [("https://filosofia.uca.es/trabajo-de-fin-de-grado/", "https://filosofia.uca.es/trabajo-de-fin-de-grado/")])
set_text(
    find("Así mismo, los estudiantes tienen que superar"),
    "Asimismo, el alumnado debe superar cada curso un número mínimo de créditos para continuar sus estudios, según el "
    "Reglamento por el que se establecen las normas de Progreso y Permanencia para los estudios oficiales de Grado en la "
    "Universidad de Cádiz, descrito en la web de la Oficina del Estudiante (https://oficinadelestudiante.uca.es/permanencia-estudios/).",
)
before(find("Los criterios de admisión, el perfil del estudiante"), [
    "**Reconocimiento de créditos en 2024-25.** No se ha localizado en el Sistema de Información un informe de créditos "
    "reconocidos por plan de estudios accesible para este autoinforme. [PENDIENTE: número de solicitudes de reconocimiento "
    "y de créditos reconocidos en el Grado en Historia en 2024-25, por tipo (estudios universitarios, ciclos formativos, "
    "experiencia profesional), a facilitar por la Secretaría del centro.]",
    "**TFG.** La normativa marco de la UCA y el reglamento interno del centro regulan la oferta de líneas, la asignación de "
    "tutores, el cronograma y la defensa; la información se publica cada curso en la web del centro. La satisfacción del "
    "alumnado con la elección y realización del TFG (ISGC-P04-11) sube de 3,26 en 2023-24 a 3,55 en 2024-25, el valor más "
    "alto de la serie y por encima del centro (3,38). Este dato es coherente con la acción de la Recomendación 8 de la DEVA "
    "(curso específico en el Campus Virtual), aunque no consta evidencia de su implantación en 2024-25 que permita atribuirle "
    "la mejora [PENDIENTE: confirmar si el curso del Campus Virtual de TFG se ha mantenido en 2024-25].",
    "**Complementos formativos.** El título no contempla complementos de formación. Las actividades de refuerzo de lengua "
    "inglesa para el B1 y de lengua latina descritas en el autoinforme anterior son voluntarias [PENDIENTE: confirmar si se "
    "han ofertado en 2024-25].",
])
p = find("El número de estudiantes de nuevo ingreso se corresponde")
blacken(p, {". ": ". "})
set_links(p, [
    ("perfil recomendado", "https://filosofia.uca.es/estudios/grados/grado-en-historia/acceso-grado-en-historia/perfil-recomendado-para-el-alumnado-de-nuevo-ingreso-ghist/"),
    ("acceso al Grado en Historia", "https://filosofia.uca.es/estudios/grados/grado-en-historia/acceso-grado-en-historia/"),
    ("web del título", "https://filosofia.uca.es/grado-en-historia/"),
    ("acceso y nuevo ingreso", "https://filosofia.uca.es/estudios/grados/grado-en-historia/acceso-grado-en-historia/"),
    ("orientación y apoyo al estudiante", "https://filosofia.uca.es/actividades-de-orientacion-y-apoyo-al-estudiante/"),
])
before(find("La coordinación docente permite la adecuada planificación"), [
    "**Demanda, ocupación y perfil de ingreso (Anexo 1, tabla 2).** La memoria fija 75 plazas de nuevo ingreso. En 2024-25 "
    "la tasa de ocupación (ISGC-P04-17) es del 100%, tras situarse entre el 102,67% y el 109,33% en los cursos anteriores, "
    "por lo que se ajusta a la oferta. La tasa de preferencia (ISGC-P04-18) es del 129,33% (130,67% en 2023-24), muy por "
    "encima del centro (87,45%): las solicitudes en primera opción superan las plazas en toda la serie. La tasa de "
    "adecuación (ISGC-P04-16) se mantiene alta, en el 92% (91,46% en 2023-24; centro, 81,56%), y la tasa de renovación o "
    "nuevo ingreso (ISGC-P04-19) baja del 24,54% al 21,5%, por debajo del centro (24,69%).",
    "Según el informe de perfil de ingreso del Sistema de Información, en 2024-25 ingresaron 70 estudiantes (78, 75 y 80 en "
    "los tres cursos anteriores y 69 en 2025-26): 66 por la PEvAU, 2 desde ciclos formativos de grado superior, 1 por el "
    "acceso para mayores y 1 por otras vías. La nota media de acceso fue de 9,157 y la nota de corte publicada, 5. "
    "[PENDIENTE: verificar la cifra de nuevo ingreso de 2024-25, ya que el autoinforme anterior indica 75 estudiantes y la "
    "tasa de ocupación es del 100%.]",
    "No hay pruebas de admisión específicas distintas de la PEvAU. El perfil de ingreso recomendado es público y coherente "
    "con la titulación. Los grupos de prácticas de laboratorio de Prehistoria y Arqueología se desdoblan en grupos reducidos "
    "[PENDIENTE: tabla de tamaños de grupo de 2024-25, a facilitar por el centro].",
])
blacken(find("En relación con el programa formativo del título de"), {"Grado / Máster": "Grado", " en": " en", " ": " ", "xxxxx": "Historia"})
p = find("El desarrollo de la coordinación se asegura")
set_links(p, [("[PENDIENTE: enlace a las actas de coordinación de 2024-25]", "https://filosofia.uca.es/grado-en-historia/")])
before(find("Implantación de los títulos con estructuras"), [
    "La coordinación horizontal y vertical se articula, según la memoria y el autoinforme anterior, a través de la "
    "Coordinación del Grado, la coordinación de cada asignatura, las comisiones de ordenación académica de los "
    "departamentos, la Comisión de TFG del centro, la reunión de coordinadores de grado y la CGC. En prácticas externas, la "
    "Coordinación de prácticas del centro y la Coordinación del Grado organizan sesiones informativas para el alumnado de 3º "
    "y 4º. [PENDIENTE: reuniones de coordinación celebradas en 2024-25 (fechas, asistentes y acuerdos) y enlace a las actas; "
    "cuadro del personal implicado en la coordinación.]",
    "La satisfacción del alumnado con la coordinación docente (ISGC-P04-10) baja a 2,88 sobre 5 en 2024-25, el valor más "
    "bajo de la serie (3,01 en 2023-24 y 2020-21) y por debajo del centro (3,14), que en cambio mejora. ACCUA ya señaló en "
    "2023 la baja satisfacción con la coordinación como aspecto que subsanar, y la acción del plan anterior (análisis de las "
    "asignaturas peor valoradas) no ha logrado elevar el indicador. Se recoge como punto débil PD-FFL-3.1, con la acción "
    "AM-FFL-3.1 (análisis de causas por curso y plan de coordinación de asignaturas compartidas). Las asignaturas con "
    "porcentajes altos de suspensos o no presentados que se analizan en el criterio 6 son un punto de partida para ese "
    "análisis.",
])
# 3.6: eliminar el modelo de estructuras que no aplican
p_ini = find("[Completar solo en caso de que el plan de estudios las contemple")
p_fin = find("[Solo se incluirán los puntos fuertes", 3)
borrar, dentro = [], False
for q in pars():
    if q._p is p_ini._p:
        dentro = True
    if q._p is p_fin._p:
        break
    if dentro:
        borrar.append(q)
for q in borrar:
    delete(q)
before(p_fin, [
    "No procede. El Grado en Historia se imparte en un único centro (Facultad de Filosofía y Letras), no es un título "
    "conjunto, no se oferta como doble titulación y no tiene mención dual ni itinerario académico abierto. Sus itinerarios "
    "optativos forman parte del plan de estudios ordinario.",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 3].",
])

# ---------------------------------------------------------------- Criterio 4
before(find("El personal académico implicado en el título es suficiente"), [
    "**Perfil del profesorado (ISGC-P05-01, Anexo II).** En 2024-25 imparten docencia en el título 49 profesores y "
    "profesoras (44, 46, 47 y 45 en los cursos anteriores), de los que el 97,96% son doctores (100% en 2023-24). Acumulan "
    "158 quinquenios docentes y 104 sexenios de investigación, frente a 149 y 96 en 2023-24, lo que refleja una plantilla "
    "con amplia experiencia docente e investigadora y en crecimiento. Por categorías, hay 13 catedráticos de universidad "
    "(26,53%), 15 titulares de universidad (30,61%), 5 profesores contratados doctores y 9 ayudantes doctores (18,37%, "
    "frente a 2 en 2023-24); el profesorado sustituto u otras figuras se reduce de 14 a 7. El aumento de ayudantes doctores "
    "y la reducción de figuras temporales favorecen la estabilidad del profesorado y su relevo.",
])
before(find("4.3 La actividad docente"), [
    "La dedicación total al título es de 332 créditos en 2024-25 (entre 331,5 y 338 en toda la serie), estable para unos "
    "70-80 estudiantes de nuevo ingreso por curso. Con 49 docentes y una ocupación del 100%, el profesorado se considera "
    "suficiente para el programa formativo. [PENDIENTE: relación nominal del profesorado de 2024-25 (Anexo II) para "
    "detallar la dedicación por asignatura.]",
])
before(find("Disponibilidad de criterios de selección y asignación de TFM o TFG"), [
    "**Formación, innovación y evaluación docente (Anexo 1, tabla 3).** La participación del profesorado del título en "
    "acciones formativas (ISGC-P05-02) desciende al 26,53% en 2024-25 (40% en 2023-24), el valor más bajo de la serie y por "
    "debajo del centro (32,95%). Se recoge como punto débil PD-FFL-4.1, con la acción AM-FFL-4.1, vinculada a la "
    "recomendación de mejora de ACCUA sobre innovación docente y DOCENTIA. En cambio, la participación en proyectos de "
    "innovación y mejora docente (ISGC-P05-03) se duplica, del 15,56% al 30,61%, al nivel del centro (31,21%).",
    "La participación en DOCENTIA (ISGC-P05-05) crece de forma continuada desde 2022-23 (8,7%) hasta el 20,41% en 2024-25, "
    "por encima del centro (16,18%). De las evaluaciones del título, el 50% obtienen la calificación de «excelente» "
    "(ISGC-P05-06) y el 50% la de «favorable» (ISGC-P05-07). En el centro, los porcentajes publicados (53,57% y 60,71%) "
    "suman más del 100%, por lo que no son comparables [PENDIENTE: verificar con la Unidad de Calidad la serie de ISGC-P05-06 "
    "y P05-07 del centro].",
])
blacken(find("En el entendimiento de que los trabajos de fin"), {"grado/máster ": "grado ", "grado/máster": "grado"})
before(find("4.5 En su caso, adecuación del perfil"), [
    "En el Grado en Historia, la oferta de líneas y tutores, la asignación provisional y definitiva, la composición de las "
    "comisiones evaluadoras y los impresos se publican cada curso en https://filosofia.uca.es/trabajo-de-fin-de-grado/. En "
    "2024-25 el TFG presenta un 28% de no presentados y un 6% de incompatibles, mientras que entre los presentados no hay "
    "suspensos (Anexo IV), lo que apunta a dificultades para completar el trabajo en el curso más que a problemas de "
    "evaluación. La satisfacción del alumnado con el TFG (ISGC-P04-11) es de 3,55, la más alta de la serie.",
])
before(find("4.6. En su caso"), [
    "Las prácticas externas del título son optativas (20519046, 6 ECTS, 4º curso). Las supervisan profesores del título "
    "como tutores académicos y personal de las entidades colaboradoras como tutores externos, bajo la Coordinación de "
    "prácticas del centro. La satisfacción de los tutores académicos (ISGC-P04-12) sube a 4,33 (4,17 en 2023-24), igual al "
    "centro, y la de los tutores de las entidades (ISGC-P04-13) es de 4,61. [PENDIENTE: verificar la serie de ISGC-P04-13: "
    "los valores de 2021-22 a 2023-24 del Sistema de Información (2,02-2,34) son aproximadamente la mitad de los publicados "
    "en el autoinforme anterior (4,66-4,67), lo que sugiere un cambio de escala o de cálculo.] [PENDIENTE: tabla de tutores "
    "académicos y externos de 2024-25 (Anexo III), a facilitar por el centro.]",
])
before(find("4.7 El alumnado está satisfecho"), ["No procede. El título se imparte solo en modalidad presencial."])
before(find("El profesorado está satisfecho con el desarrollo del programa formativo"), [
    "La satisfacción global del alumnado con la docencia (ISGC-P05-04) se mantiene en 4,5 sobre 5 por tercer curso "
    "consecutivo, por encima del centro (4,4), y en 4,4-4,5 en toda la serie. La satisfacción global del alumnado con el "
    "título (ISGC-P07-02) sube a 3,80 en 2024-25, su valor más alto de la serie, por encima del centro (3,57) y de la UCA "
    "(3,63). La tasa de respuesta del alumnado (21,6%) obliga a interpretar este último dato con cautela.",
])
before(find("[Solo se incluirán los puntos fuertes", 4), [
    "La satisfacción global del PDI con el título (ISGC-P07-03) es de 3,81 en 2024-25, estable desde 2022-23 (3,88 y 3,82) "
    "y ligeramente por debajo del centro (3,84) y de la UCA (3,96). Con una tasa de respuesta del PDI del 64,71% (51,06% en "
    "2023-24), el dato es representativo. No se considera punto débil, pero se seguirá en el próximo curso junto con la "
    "satisfacción con la coordinación.",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 4].",
])

# ---------------------------------------------------------------- Criterio 5
before(find("5.2. En su caso"), [
    "Las aulas de la Facultad de Filosofía y Letras disponen de equipamiento multimedia, y el título usa el laboratorio de "
    "docencia de Prehistoria y Arqueología para las prácticas en grupos reducidos; las actividades de campo se realizan en "
    "yacimientos y archivos. El autoinforme anterior destacaba también el uso de las infraestructuras científicas del LABAP "
    "[PENDIENTE: confirmar su uso docente en 2024-25]. Como recursos generales se dispone de la Biblioteca, el Campus "
    "Virtual, el CAU, el BAU y el SIRE.",
    "La satisfacción del alumnado con los recursos materiales e infraestructuras (ISGC-P06-03) baja de 3,70 a 3,37 en "
    "2024-25, su valor más bajo de la serie y por debajo del centro (3,44); la del profesorado (ISGC-P06-04) baja de 3,99 a "
    "3,77, también por debajo del centro (3,84). Ambos descensos acompañan al del centro, lo que apunta a una causa común de "
    "infraestructuras del edificio más que a un problema propio del título. [PENDIENTE: confirmar con el centro si hubo "
    "incidencias de infraestructura en 2024-25.] Se analizará la evolución el próximo curso antes de plantear una acción.",
])
before(find("5.3. En el caso de que el programa formativo incluya"), [
    "**Movilidad (Anexo 1, tabla 2, ISGC-P04-09).** La movilidad entrante internacional sube al 18,38% en 2024-25 (15,95% "
    "en 2023-24), aunque por debajo del centro (42,16%); la entrante nacional es del 0,62%. La movilidad saliente sigue "
    "siendo muy baja: internacional del 1,56% (0,31% en 2023-24; 0% en 2020-21, curso en que no hubo estudiantes salientes "
    "internacionales) frente al 5,87% del centro, y nacional del 0,31%. ACCUA señaló la baja movilidad saliente como "
    "aspecto que subsanar y la acción anterior (sesiones generales del centro) no ha tenido efecto apreciable, por lo que se "
    "mantiene como punto débil PD-FFL-5.1 con la acción AM-FFL-5.1. La satisfacción del alumnado con la movilidad "
    "(ISGC-P04-15) es de 3,83 (3,48 en 2023-24), similar al centro (3,87), con muy pocos participantes salientes.",
])
before(find("5.4. El personal de apoyo"), [
    "Las prácticas externas son optativas (6 ECTS) y se gestionan mediante convenios en la plataforma GADES de la UCA. La "
    "relación entre plazas ofertadas y alumnado que las solicita (ISGC-P04-08) mejora de forma continuada desde 1,00 en "
    "2021-22 hasta 1,67 en 2024-25, por encima del centro (1,65): hay plazas suficientes para la demanda. La satisfacción "
    "del alumnado con las prácticas (ISGC-P04-14) crece en toda la serie, de 3,26 en 2020-21 a 3,94 en 2024-25, por encima "
    "del centro (3,70), y la de los tutores académicos y externos se analiza en el subcriterio 4.5. En la asignatura, el 89% "
    "obtiene sobresaliente y el 11%, notable (Anexo IV).",
    "[PENDIENTE: Anexo III, tablas 1 y 2: créditos y plazas de prácticas, número de estudiantes, convenios con plazas y "
    "tutores, y tutores académicos con su dedicación en 2024-25, a facilitar por el centro.]",
])
before(find("5.5. En caso de enseñanza"), [
    "El PTGAS no se adscribe a títulos concretos: la Secretaría del campus, la Conserjería, la Biblioteca y los servicios "
    "centrales atienden a todas las titulaciones del centro. La satisfacción del PTGAS con el centro (ISGC-P07-04) es de "
    "3,82, estable en toda la serie (3,78-3,82). ACCUA pidió analizar la suficiencia del personal administrativo de apoyo y "
    "el autoinforme anterior indicaba una carga burocrática que recae en el profesorado; se mantiene en el Plan de Mejora la "
    "solicitud al centro de un análisis de la suficiencia del PTGAS [PENDIENTE: tabla general del personal de apoyo del "
    "centro, disponible en el Campus Virtual].",
])
before(find("[Solo se incluirán los puntos fuertes", 5), [
    "No procede. El título se imparte solo en modalidad presencial.",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 5].",
])

# ---------------------------------------------------------------- Criterio 6
before(find("Las actividades formativas, la metodología y los sistemas de evaluación son pertinentes"), [
    "Los resultados de aprendizaje de las guías docentes (https://asignaturas.uca.es/asig/) se corresponden con el nivel 2 "
    "del MECES (Grado) y con el perfil de egreso de la memoria. Las calificaciones de 2024-25 (Anexo IV) muestran que, en "
    "conjunto, el alumnado presentado supera las asignaturas: 7% de suspensos, 36% de aprobados, 31% de notables, 7% de "
    "sobresalientes y 1% de matrículas de honor, con un 14% de no presentados.",
    "[PENDIENTE: subir al UCADrive las evidencias de seguimiento ACCUA: guías docentes y profesorado de cinco asignaturas "
    "obligatorias representativas y del TFG, una selección de pruebas de evaluación que cubra el espectro de calificaciones, "
    "la tabla de evaluación continua y cinco memorias de prácticas externas.]",
])
before(find("Los resultados de los indicadores académicos y su evolución"), [
    "Las actividades formativas (clases teóricas, prácticas de aula, de laboratorio y de campo, seminarios y tutorías) y los "
    "sistemas de evaluación de las guías docentes se ajustan a la memoria. El TFG se elabora y defiende según el reglamento "
    "del centro, con criterios de asignación y rúbricas públicos; las prácticas externas, según el reglamento interno de "
    "prácticas curriculares del centro. [PENDIENTE: listado de TFG defendidos en 2024-25 con sus calificaciones, rúbrica de "
    "evaluación del TFG y listado de prácticas realizadas, con centros y tutores, para el UCADrive.]",
])
anexo_iv = find("ANEXO IV:", 1)
before(anexo_iv, [
    "**Indicadores académicos (Anexo 1, tabla 2) y objetivos de la memoria.** La tasa de rendimiento (ISGC-P04-01) es del "
    "77% en 2024-25 (79,4% en 2023-24; centro, 78,6%), dentro de la franja 74-79% desde 2021-22. La tasa de éxito "
    "(ISGC-P04-02) baja ligeramente al 87,3% (89,3%; centro, 87,6%) y la de evaluación o presentados (ISGC-P04-03) se "
    "mantiene en el 88,2% (88,9%; centro, 89,7%). La tasa de abandono (ISGC-P04-04) vuelve al 18,2% tras el pico del 33,3% "
    "de 2023-24 y queda por debajo del centro (25,3%); la de graduación (ISGC-P04-05) sube al 62,3%, la más alta de la serie "
    "(centro, 46,9%). La tasa de eficiencia (ISGC-P04-06) es del 91,7% (centro, 88%) y la duración media de los estudios "
    "(ISGC-P04-07) baja a 4,6 años, la menor de la serie (centro, 5,38). Las tasas son valores dinámicos y pueden cambiar en "
    "el Sistema de Información; por ejemplo, el autoinforme anterior publicó tasas de graduación del 43% y del 32% para "
    "2022-23 y 2023-24, distintas de las actuales (45,6% y 44%).",
    "La comparación con los objetivos de la memoria verificada es la siguiente:",
    ("tabla", [
        ["Indicador", "Objetivo de la memoria", "2022-23", "2023-24", "2024-25", "Valoración 2024-25"],
        ["Tasa de graduación (ISGC-P04-05)", "35,6%", "45,6%", "44%", "62,3%", "Cumple"],
        ["Tasa de abandono (ISGC-P04-04)", "37,38%", "17,7%", "33,3%", "18,2%", "Cumple"],
        ["Tasa de eficiencia (ISGC-P04-06)", "92%", "88,4%", "89%", "91,7%", "Por debajo (−0,3 puntos)"],
        ["Tasa de éxito (ISGC-P04-02)", "90%", "89,4%", "89,3%", "87,3%", "Por debajo (−2,7 puntos)"],
    ]),
    "Las tasas de graduación y abandono cumplen holgadamente los objetivos y la eficiencia queda a tres décimas del suyo. La "
    "tasa de éxito se mantiene por debajo del 90% previsto desde 2021-22. Su origen está en unas pocas asignaturas con "
    "porcentajes altos de suspensos, que se detallan a continuación. Las acciones de la recomendación de mejora de ACCUA "
    "sobre graduación y abandono y de la Recomendación 9 de la DEVA siguen en el Plan de Mejora; dados los resultados de "
    "2024-25, se propone valorar su cierre en el próximo autoinforme si la tendencia se consolida.",
    "**Calificaciones por asignatura (2024-25).** En la tabla siguiente se muestran las asignaturas con mayor porcentaje de "
    "suspensos o de no presentados y las de mejores resultados; la relación completa está en el Anexo IV.",
])
before(find("El título dispone de indicadores para analizar grado de satisfacción"), [
    "Concentran los suspensos Historia Moderna Universal I (35%, con un 19% de no presentados), Epigrafía y Numismática "
    "(31%), Geografía Regional de España y del Mundo (30%, con un 27% de no presentados) e Historia Medieval Universal II "
    "(22%), todas de los primeros cursos. Los no presentados superan el 25% en Prehistoria de la Península Ibérica (32%), "
    "Arte II: Moderno y Contemporáneo (30%), Historia Contemporánea de España (29%), Trabajo Fin de Grado (28%), Geografía "
    "Regional de España y del Mundo (27%), Historia de la Filosofía II (27%) e Introducción a la Arqueología (25%). En el "
    "extremo opuesto destacan Prácticas externas (89% de sobresalientes), Historia Cultural de la Edad Media (58% de "
    "notables y 37% de sobresalientes), El Mediterráneo Medieval (64% y 23%), Historia Contemporánea Universal II (39% de "
    "sobresalientes) y Métodos, técnicas y recursos para la investigación histórica (75% de notables).",
    "Estas asignaturas se trasladarán a la Coordinación del Grado y a los departamentos dentro del análisis de la acción "
    "AM-FFL-3.1, porque coinciden en buena parte con las que el autoinforme anterior vinculaba a conocimientos previos de "
    "latín (Epigrafía y Numismática) y a la coordinación de asignaturas compartidas.",
    "**Resultados globales de la titulación.** Rendimiento, eficiencia, graduación y abandono se han analizado en el "
    "apartado anterior con la serie de cinco cursos del Anexo 1 [PENDIENTE: valores de 2019-20 para completar los seis "
    "cursos que pide ACCUA]. La tasa de no presentados del curso es del 14% (Anexo IV).",
    "**Resultados globales del primer curso.** [PENDIENTE: tasas de abandono, presentados, éxito y rendimiento del primer "
    "curso en los seis últimos cursos; no se han localizado en el Sistema de Información y debe facilitarlas el centro.]",
])
blacken(find("Según el artículo 2.4 del Reglamento UCA/CG09/2022"), {"XXXXXXXX": "de Filosofía y Letras", "XXXXXXXXX": "Historia"})
p = find("Según el artículo 2.4 del Reglamento UCA/CG09/2022")
replace_run(p, "Según el artículo 2.4 del Reglamento UCA/CG09/2022, de 26 de septiembre, sobre la evaluación de la satisfacción del estudiantado con la docencia recibida, el/la Decano/a-Director/a de la Facultad/Escuela",
            "Según el artículo 2.4 del Reglamento UCA/CG09/2022, de 26 de septiembre, sobre la evaluación de la satisfacción del estudiantado con la docencia recibida, la persona titular del Decanato de la Facultad")
replace_run(p, ", tiene acceso a todos los informes de resultados del grado de satisfacción con la docencia de todo el profesorado que imparte docencia en el Grado/Máster ",
            ", tiene acceso a todos los informes de resultados del grado de satisfacción con la docencia de todo el profesorado que imparte docencia en el Grado ")
before(find("[Solo se incluirán los puntos fuertes", 6), [
    "La satisfacción del alumnado con la docencia del título (ISGC-P05-04: 4,5) y con el título (ISGC-P07-02: 3,80) es "
    "alta y está por encima del centro, como se analiza en el criterio 4.",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 6].",
])

# ---------------------------------------------------------------- Criterio 7
before(find("a) Servicio de Atención Psicológica"), [
    "Según el autoinforme anterior, en el centro se desarrollan el Programa de Orientación y Apoyo al Estudiante (PROA), el "
    "Proyecto Compañero (estudiantes mentores de 2º curso o superiores para el alumnado de nuevo ingreso), el Proyecto "
    "Mentoring para estudiantes internacionales (https://filosofia.uca.es/proyecto-companero-y-proyecto-mentoring/), la "
    "Oficina de Orientación y Apoyo al Estudiante del Decanato, las jornadas de acogida y las Jornadas de Orientación de "
    "Másteres para el alumnado de 4º (https://filosofia.uca.es/actividades-de-orientacion-y-apoyo-al-estudiante/). "
    "[PENDIENTE: confirmar las actividades realizadas en 2024-25 y su participación (informe FSGC P06-02).]",
    "Además, la UCA ofrece los siguientes servicios:",
])
before(find("[Se debe valorar si:", 1, after=find("2. Orientación Profesional.")), [
    "En el título, la Subcomisión para la mejora del Grado en Historia tiene prevista en el Plan de Mejora la organización "
    "de charlas y mesas redondas sobre salidas profesionales con expertos y egresados [PENDIENTE: confirmar las actividades "
    "de orientación profesional realizadas en 2024-25 (informe FSGC P06-04)].",
    "La satisfacción del alumnado con el apoyo y la orientación académica (ISGC-P06-01) es de 3,28 en 2024-25, estable "
    "(3,27 en 2023-24) y por encima del centro (3,21). La satisfacción con la orientación profesional (ISGC-P06-02) es de "
    "2,93, ligeramente inferior a la de 2023-24 (3,02) y a la del centro (3,00); se mantiene en torno a 3 en toda la serie y "
    "es el indicador de satisfacción más bajo del alumnado. Se considera atendida por la acción de orientación profesional "
    "vinculada a la recomendación de ACCUA del criterio 7, por lo que no se abre un punto débil nuevo.",
])
before(find("7.3 Los perfiles de egreso"), [
    "**Empleabilidad (Anexo 1, tabla 6).** Los indicadores de egresados se refieren a cohortes de egreso, no a cursos "
    "académicos, y desde la cohorte 2022-23 se calculan con una fórmula distinta, por lo que la serie no es homogénea. La "
    "participación en la encuesta (ISGC-P07-01_03) es baja: 21,28% (10 de 47 egresados) en la cohorte 2023-24, por lo que "
    "los porcentajes se basan en muy pocas respuestas y pueden variar mucho de una cohorte a otra.",
    "En la cohorte 2023-24, la tasa de inserción profesional en cualquier sector (ISGC-P07-05) es del 10,64% (11,11% en la "
    "cohorte anterior; centro, 12,63%). Entre las personas que trabajan, la inserción en un sector relacionado con los "
    "estudios (ISGC-P07-06) es del 60% (16,67% en 2022-23; centro, 59,46%), la tasa de autoempleo (ISGC-P07-07) del 20% y "
    "la inserción con movilidad geográfica (ISGC-P07-08) del 20%. El valor de autoempleo de la cohorte 2022-23 figura como "
    "«No disponible» porque el Sistema de Información no lo ofrece para el título en esa cohorte. La baja tasa de inserción "
    "es coherente con que buena parte de los egresados continúa con estudios de máster (profesorado de Secundaria, "
    "patrimonio, archivística) [PENDIENTE: dato de continuación de estudios de los egresados, si lo facilita el centro].",
])
before(find("7.4 Los empleadores"), [
    "Los perfiles de egreso de la memoria (docencia, investigación, archivos y documentación, patrimonio y gestión cultural) "
    "siguen vigentes. La satisfacción de los egresados con las competencias adquiridas (ISGC-P07-10) alcanza 3,70 en la "
    "cohorte 2023-24, la más alta de la serie (3,20 en 2022-23; centro, 3,44). La adecuación de los perfiles se revisará "
    "dentro del proceso de modificación de la memoria [PENDIENTE: confirmar estado].",
])
blacken(find("Según el proceso P07"), {"Facultad / Escuela de XXXX ": "Facultad de Filosofía y Letras "})
before(find("7.5 Los egresados están satisfechos"), [
    "El título no dispone todavía de datos de satisfacción de los empleadores con la formación de los egresados. ACCUA lo "
    "señaló como aspecto que subsanar (criterios 2 y 7) y el autoinforme anterior indicaba que el Vicedecanato de Posgrado y "
    "Calidad había lanzado una encuesta a empleadores, sin resultados disponibles [PENDIENTE: confirmar si existen "
    "respuestas y actas de reuniones con empleadores en 2024-25]. Las valoraciones de los tutores de las entidades "
    "colaboradoras de prácticas (ISGC-P04-13: 4,61) son una aproximación indirecta, pero no sustituyen al indicador. Se "
    "mantiene como punto débil PD-FFL-7.1, con la acción AM-FFL-7.1.",
])
before(find("7.6 Se analiza la sostenibilidad"), [
    "La satisfacción de los egresados con los estudios realizados (ISGC-P07-09) es de 3,70 en la cohorte 2023-24 (10 "
    "respuestas de 47 egresados), la más alta de la serie (3,44 en 2022-23) y por encima del centro (3,43). Con tan baja "
    "participación, el dato es orientativo. El Plan de Mejora incluye la difusión de la encuesta entre el alumnado de 4º, en "
    "respuesta a la recomendación de ACCUA sobre la representatividad de estos indicadores.",
])
before(find("[Solo se incluirán los puntos fuertes", 7), [
    "**Síntesis de sostenibilidad.** El título es sostenible a la vista de los cuatro ámbitos analizados:",
    ("-", "**Demanda:** preferencia del 129,33% y adecuación del 92%, ambas muy superiores a las del centro, con ocupación "
          "plena de las 75 plazas pese a la oferta de Historia en universidades cercanas (Sevilla, Málaga)."),
    ("-", "**Profesorado:** 49 docentes, casi todos doctores (97,96%), con 104 sexenios, más ayudantes doctores y menos "
          "figuras temporales que en 2023-24."),
    ("-", "**Recursos:** suficientes en aulas, laboratorio y prácticas (1,67 plazas por solicitante), aunque la satisfacción "
          "con las infraestructuras ha bajado este curso."),
    ("-", "**Resultados:** graduación del 62,3% y abandono del 18,2%, mejores que los objetivos de la memoria; satisfacción "
          "con la docencia de 4,5 y con el título de 3,80."),
    "Los riesgos para la sostenibilidad son la baja satisfacción con la coordinación, la escasa movilidad saliente, la baja "
    "inserción laboral inmediata de los egresados y la falta de datos de empleadores; todos tienen acción en el Plan de "
    "Mejora.",
    "Evidencias en el UCADrive del centro: [PENDIENTE: ruta de la carpeta de evidencias del criterio 7].",
])

# ---------------------------------------------------------------- Puntos débiles vacíos (criterios 1, 2 y 6)
for ti in (6, 9, 23):
    t = T[ti]
    while len(t.rows) > 2:
        t._tbl.remove(t.rows[-1]._tr)
    fila = t.rows[1]
    for j, txt in enumerate(["No se identifican puntos débiles en este criterio.", "No procede."]):
        c = fila.cells[j]
        for par in c.paragraphs[1:]:
            par._p.getparent().remove(par._p)
        set_text(c.paragraphs[0], txt)

# ---------------------------------------------------------------- Calificaciones (T21 selección y T44 completa)
cal = json.loads((BASE / "lince_calificaciones.json").read_text())
cab = ["Asignatura", "Suspensos", "Aprobados", "Notables", "Sobresalientes", "Matrículas de honor", "No presentados"]


def fila_cal(f):
    nombre, np_, ss, ap, apc, nt, sb, mh = f[:8]
    return [nombre.capitalize(), f"{ss}%", f"{ap + apc}%", f"{nt}%", f"{sb}%", f"{mh}%", f"{np_}%"]


def volcar(t, filas):
    """Reescribe la tabla de calificaciones: cabecera + filas + GLOBAL, ajustando a 7 columnas."""
    while len(t.columns) < 7:
        t.add_column(t.columns[-1].width)
    plantilla_fila = copy.deepcopy(t.rows[1]._tr)
    for r in list(t.rows)[1:]:
        t._tbl.remove(r._tr)
    datos = [cab] + filas + [fila_cal(cal["totales"])]
    datos[-1][0] = "GLOBAL (plan)"
    for i, valores in enumerate(datos):
        if i == 0:
            fila = t.rows[0]
        else:
            t._tbl.append(copy.deepcopy(plantilla_fila))
            fila = t.rows[-1]
        celdas = []
        for c in fila.cells:
            if not celdas or c._tc is not celdas[-1]._tc:
                celdas.append(c)
        for c, v in zip(celdas, valores):
            for par in c.paragraphs[1:]:
                par._p.getparent().remove(par._p)
            set_text(c.paragraphs[0], v)
            for r in c.paragraphs[0].runs:
                r.font.size = Pt(8)
                r.bold = i == 0 or i == len(datos) - 1


seleccion = ["HISTORIA MODERNA UNIVERSAL I", "EPIGRAFÍA Y NUMISMÁTICA", "GEOGRAFÍA REGIONAL DE ESPAÑA Y DEL MUNDO",
             "HISTORIA MEDIEVAL UNIVERSAL II", "PREHISTORIA DE LA PENÍNSULA IBÉRICA", "ARTE II: MODERNO Y CONTEMPORÁNEO",
             "HISTORIA CONTEMPORÁNEA DE ESPAÑA", "TRABAJO FIN DE GRADO", "HISTORIA CULTURAL DE LA EDAD MEDIA",
             "EL MEDITERRÁNEO MEDIEVAL: OCCIDENTE, BIZANCIO Y EL ISLAM", "HISTORIA CONTEMPORÁNEA UNIVERSAL II", "PRÁCTICAS EXTERNAS"]
por_nombre = {f[0]: f for f in cal["filas"]}
volcar(T[21], [fila_cal(por_nombre[n]) for n in seleccion])
volcar(T[44], [fila_cal(f) for f in cal["filas"]])

# ---------------------------------------------------------------- Anexo II (T40)
t40 = T[40]
fila_den = t40.rows[1]
celdas = []
for c in fila_den.cells:
    if not celdas or c._tc is not celdas[-1]._tc:
        celdas.append(c)
set_text(celdas[1].paragraphs[0], "Grado en Historia")
fila_tot = t40.rows[7]
celdas = []
for c in fila_tot.cells:
    if not celdas or c._tc is not celdas[-1]._tc:
        celdas.append(c)
for i, c in enumerate(celdas):
    if "Núm. Total prof" in c.text:
        set_text(celdas[i + 1].paragraphs[0], "49")
    if "% de Doctores" in c.text:
        set_text(celdas[i + 1].paragraphs[0], "97,96%")
for r_ in (t40.rows[5], t40.rows[6]):
    celdas = []
    for c in r_.cells:
        if not celdas or c._tc is not celdas[-1]._tc:
            celdas.append(c)
    set_text(celdas[0].paragraphs[0], "[PENDIENTE]")
    set_text(celdas[1].paragraphs[0], "[PENDIENTE: relación nominal del profesorado de 2024-25 (informe «P05 - Personal docente disponible para impartir el título», no accesible en el Sistema de Información para este autoinforme)]")
ancla_t40 = docx.text.paragraph.Paragraph(t40._tbl.getnext(), d) if t40._tbl.getnext().tag == qn("w:p") else None
if ancla_t40 is not None:
    before(ancla_t40, [
        "Resumen del personal académico del título en 2024-25 (ISGC-P05-01, Sistema de Información):",
        ("tabla", [
            ["Indicador", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"],
            ["Total profesorado", "44", "46", "47", "45", "49"],
            ["% doctores", "100%", "100%", "95,74%", "100%", "97,96%"],
            ["Quinquenios (total)", "140", "149", "152", "149", "158"],
            ["Sexenios (total)", "81", "92", "92", "96", "104"],
            ["Créditos de dedicación al título", "332", "338", "331,5", "333", "332"],
        ]),
        "Categorías en 2024-25: catedráticos de universidad, 13 (26,53%); titulares de universidad, 15 (30,61%); "
        "contratados doctores, 5; ayudantes doctores, 9 (18,37%); profesorado sustituto y otras figuras, 7.",
    ])

# ---------------------------------------------------------------- Anexo III (T41-T43)
for ti in (41, 42, 43):
    t = T[ti]
    for r_ in t.rows:
        for c in r_.cells:
            if not c.text.strip():
                set_text(c.paragraphs[0], "[PENDIENTE: dato del centro]")
t41 = T[41]
c = t41.rows[1].cells[1]
set_text(c.paragraphs[0], "6 ECTS (asignatura optativa 20519046, Prácticas externas) [PENDIENTE: confirmar]")

d.save(BASE / "paso2.docx")
print("OK paso2.docx")
