#!/usr/bin/env python3
"""Rellena la parte determinista del Autoinforme de Seguimiento (UCA/ACCUA).

Vuelca sobre la plantilla oficial .docx, sin alterar su formato:
  - Encabezado (curso, convocatoria, título, centro)
  - Tabla de datos de identificación del título
  - Bloque de bibliotecas del criterio 5.1: conserva el del `campus` y borra los demás
  - Enlaces de la plantilla dados por obsoletos (ENLACES_VIGENTES), como la Política de
    Calidad
  - Tablas de indicadores del Anexo 1 (ISGC P01-P07), por TÍTULO y por CENTRO, con las
    cabeceras de años tomadas de `anios` y `anios_egresados` (admite 2024-25 y 2024/25)
  - (Opcional) Recomendaciones de ACCUA del Criterio 2, puntos fuertes/débiles por
    criterio y Plan de Mejora, localizados por el contenido de sus tablas. El plan se
    genera a partir de las recomendaciones y de los puntos débiles, para que coincida
    literalmente con ellos; `plan_mejora` solo añade filas extra.

Uso:
  python rellenar_autoinforme.py --plantilla plantilla.docx --datos datos.json \
         --salida autoinforme.docx

El esquema de datos.json está en references/mapa-indicadores-lincebi.md.
El análisis narrativo NO lo rellena este script: se redacta después sobre el .docx.
"""
import argparse
import json
import re
import sys
from copy import deepcopy

try:
    import docx
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
except ImportError:
    sys.exit("Falta python-docx. Instala con: pip install python-docx --break-system-packages")

YEAR_RE = re.compile(r"^\s*\d{4}[-/]\d{2}\s*$")
CODE_RE = re.compile(r"ISGC-P\d{2}[-_]\d{2}(?:_\d{2})?")
FECHA_RE = re.compile(r"^(\d{1,2}/)?\d{1,2}/\d{4}$")
N_CRITERIOS = 7
PENDIENTE = "[PENDIENTE]"
CAMPOS_PLAN = ("prioridad", "responsable", "inicio", "fin", "indicador")

# Color de fuente de cada bloque de bibliotecas del criterio 5.1 de la plantilla.
CAMPUS_COLORES = {
    "puerto-real": "F79646",
    "cadiz": "808080",
    "jerez": "FB2DCF",
    "algeciras": "7030A0",
}

# Enlaces de la plantilla que el Servicio de Gestión de la Calidad ha dado por obsoletos.
ENLACES_VIGENTES = {
    # Política de Calidad: directrices aprobadas el 29-9-2026.
    "BOUCA356-16-19.pdf":
        "https://ucalidad.uca.es/wp-content/uploads/2026/10/"
        "BOUCA-DIRECTRICES-POLITICA-DE-CALIDAD-29-9-26.pdf",
}


def norm_year(text):
    """Clave común para un curso escrito como 2024-25 o como 2024/25."""
    return str(text).strip().replace("/", "-")


def set_cell_text(cell, text):
    """Reemplaza el contenido de una celda conservando el estilo del 1er párrafo.

    Soporta varias líneas (\n -> salto de línea) y elimina párrafos/placeholders
    sobrantes que trae la plantilla en la celda.
    """
    text = "" if text is None else str(text)
    lines = text.split("\n")
    # elimina párrafos adicionales de la celda (placeholders de la plantilla)
    for p in cell.paragraphs[1:]:
        p._element.getparent().remove(p._element)
    p = cell.paragraphs[0]
    if p.runs:
        run = p.runs[0]
        run.text = lines[0]
        for r in p.runs[1:]:
            r._element.getparent().remove(r._element)
    else:
        run = p.add_run(lines[0])
    for line in lines[1:]:
        run.add_break()
        run.add_text(line)


def _base_rpr(cell, row=None):
    """Formato de carácter de referencia para escribir en una celda.

    Toma el del primer run de la celda; si está vacía, el de la marca de párrafo o el
    de otra celda de la fila. Quita color y resaltado (los placeholders van en rojo)."""
    fuentes = [cell] + (list(row.cells) if row is not None else [])
    rpr = None
    for c in fuentes:
        for p in c.paragraphs:
            if p.runs and p.runs[0]._r.rPr is not None:
                rpr = p.runs[0]._r.rPr
                break
            ppr = p._p.pPr
            if ppr is not None and ppr.find(qn("w:rPr")) is not None:
                rpr = ppr.find(qn("w:rPr"))
                break
        if rpr is not None:
            break
    if rpr is None:
        return None
    rpr = deepcopy(rpr)
    for tag in ("w:color", "w:highlight", "w:shd", "w:b", "w:bCs", "w:ins", "w:del"):
        for el in rpr.findall(qn(tag)):
            rpr.remove(el)
    return rpr


def set_cell_rich(cell, lines, row=None):
    """Escribe en una celda un párrafo por línea; cada línea es una lista de
    segmentos (texto, negrita). Conserva el formato de párrafo y de carácter de la
    plantilla y elimina el contenido previo (placeholders)."""
    rpr = _base_rpr(cell, row)
    for p in cell.paragraphs[1:]:
        p._element.getparent().remove(p._element)
    p0 = cell.paragraphs[0]._p
    for child in list(p0):
        if child.tag != qn("w:pPr"):
            p0.remove(child)
    molde = deepcopy(p0)
    parrafos = [p0]
    for _ in lines[1:]:
        nuevo = deepcopy(molde)
        parrafos[-1].addnext(nuevo)
        parrafos.append(nuevo)
    for p_el, segmentos in zip(parrafos, lines or [[]]):
        par = Paragraph(p_el, cell)
        for texto, negrita in segmentos:
            if not texto:
                continue
            run = par.add_run(texto)
            if rpr is not None:
                run._r.insert(0, deepcopy(rpr))
            if negrita:
                run.bold = True


def distinct_leading(cells, first_year_col):
    """Textos distintos y no vacíos de las celdas anteriores a la 1ª columna-año."""
    out = []
    for c in cells[:first_year_col]:
        t = c.text.strip()
        if t and (not out or out[-1] != t):
            out.append(t)
    return out


def fill_header(doc, enc):
    if not enc:
        return
    for p in doc.paragraphs:
        t = p.text.strip()
        low = t.lower()
        if low.startswith("autoinforme de seguimiento curso") and enc.get("curso"):
            set_para(p, f"Autoinforme de seguimiento Curso {enc['curso']}")
        elif low.startswith("(convocatoria") and enc.get("convocatoria"):
            set_para(p, f"(Convocatoria {enc['convocatoria']})")
        elif t.upper().startswith("GRADO/MÁSTER EN") and enc.get("titulo"):
            set_para(p, f"{t} {enc['titulo']}")
        elif t.upper().startswith("CENTRO/S") and enc.get("centro"):
            set_para(p, f"{t} {enc['centro']}")
    fill_fechas_portada(doc, enc)


def fill_fechas_portada(doc, enc):
    """Rellena «Fecha: xxx» (elaborado / aprobado) conservando la letra blanca del diseño;
    sin fecha deja una marca [PENDIENTE] para que la depuración no vacíe la celda."""
    tabla = _tabla_por_cabecera(doc, "elaborado:")
    if tabla is None:
        return
    claves = (("fecha_elaboracion", "elaboración"), ("fecha_aprobacion", "aprobación"))
    for fila in tabla.rows:
        for col, celda in enumerate(fila.cells[:2]):
            for p in celda.paragraphs:
                if not p.text.strip().startswith("Fecha:"):
                    continue
                clave, que = claves[col]
                valor = enc.get(clave) or f"{PENDIENTE[:-1]}: fecha de {que}]"
                for r in p.runs:
                    if "xxx" in r.text.lower():
                        r.text = re.sub(r"[Xx]{3,}", valor, r.text)


def set_para(p, text):
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(text)


def fill_identity(doc, ident):
    if not ident:
        return
    # Busca la tabla de identificación (contiene "ID Ministerio")
    for tb in doc.tables:
        labels = [tb.cell(r, 0).text.strip() for r in range(len(tb.rows))]
        if any("ID Ministerio" in l for l in labels):
            for r, row in enumerate(tb.rows):
                key = row.cells[0].text.strip()
                if key == "Oferta de título doble":
                    # fila con SÍ / NO en la celda intermedia
                    mid = row.cells[1].text.strip().upper() if len(row.cells) > 2 else ""
                    val = str(ident.get("Oferta de título doble", "")).strip().upper()
                    if mid in ("SÍ", "SI", "NO") and mid.replace("Í", "I") == val.replace("Í", "I"):
                        set_cell_text(row.cells[-1], "X")
                    continue
                if key in ident:
                    set_cell_text(row.cells[-1], ident[key])
            break


def _year_cells(row):
    """Celdas-año distintas de una fila (las celdas combinadas se repiten en row.cells)."""
    out = []
    for c in row.cells:
        if YEAR_RE.match(c.text) and not any(o._tc is c._tc for o in out):
            out.append(c)
    return out


def relabel_year_headers(doc, data):
    """Sustituye los años de las cabeceras de la plantilla por `anios`/`anios_egresados`.

    Las tablas de egresados se reconocen por la cabecera "AÑO DE EGRESO".
    """
    general = data.get("anios") or []
    egresados = data.get("anios_egresados") or []
    for tb in doc.tables:
        is_egr = any("AÑO DE EGRESO" in c.text.upper() for row in tb.rows[:2] for c in row.cells)
        nuevos = egresados if is_egr else general
        if not nuevos:
            continue
        for row in tb.rows:
            cells = _year_cells(row)
            if not cells:
                continue
            if len(cells) != len(nuevos):
                print(f"AVISO: una tabla tiene {len(cells)} columnas de años y el JSON aporta "
                      f"{len(nuevos)}; no se han cambiado sus cabeceras.", file=sys.stderr)
                continue
            for c, year in zip(cells, nuevos):
                # Conserva el separador de la plantilla (2021/22 en general, 2019-20 en egreso).
                sep = "/" if "/" in c.text else "-"
                nuevo = norm_year(year).replace("-", sep)
                if c.text.strip() != nuevo:
                    set_cell_text(c, nuevo)


def check_scale(label, scope, year, value):
    """Avisa si un indicador de satisfacción (escala 0-5) supera el máximo.

    Las tasas de respuesta de las encuestas (P07-01) citan la satisfacción en su nombre,
    pero son porcentajes: no se comprueban."""
    low = label.lower()
    if "satisfacci" not in low or "tasa de respuesta" in low or "(%)" in low:
        return
    try:
        num = float(str(value).replace(",", ".").split()[0])
    except (ValueError, IndexError):
        return
    if num > 5:
        print(f"AVISO: {label[:40]}… ({scope}, {year}) = {value} supera la escala 0-5; "
              "revisa el dato.", file=sys.stderr)


def check_extraction(data):
    """Avisa si falta la procedencia de los datos o si vienen del entorno de pruebas."""
    ext = data.get("extraccion") or {}
    entorno = str(ext.get("entorno", "")).lower()
    if not entorno or not ext.get("fecha"):
        print("AVISO: falta 'extraccion' (entorno y fecha) en el JSON; documenta de dónde y "
              "cuándo se extrajeron los indicadores.", file=sys.stderr)
    if "datapru" in entorno:
        print("AVISO: los indicadores proceden del entorno de PRUEBAS (datapru.uca.es); "
              "repite la extracción en producción (data.uca.es).", file=sys.stderr)


def fill_indicators(doc, data):
    relabel_year_headers(doc, data)
    check_extraction(data)
    inds = data.get("indicadores", {})
    if not inds:
        return 0
    written = 0
    for tb in doc.tables:
        scope = None
        colyears = {}  # col_index -> year
        first_year_col = None
        for row in tb.rows:
            cells = row.cells
            texts = [c.text.strip() for c in cells]
            rowtext = " ".join(texts)
            # ¿fila de cabecera con años?
            year_cols = {i: norm_year(t) for i, t in enumerate(texts) if YEAR_RE.match(t)}
            if year_cols:
                colyears = year_cols
                first_year_col = min(year_cols)
            # ¿indica ámbito? Solo en cabeceras: las etiquetas de datos dicen "Título-Centro".
            up = rowtext.upper()
            if not CODE_RE.search(up):
                if "CENTRO" in up and "TÍTULO" not in up and "TITULO" not in up:
                    scope = "centro"
                elif "TÍTULO" in up or "TITULO" in up:
                    scope = "titulo"
            # ¿fila de datos? El código ISGC debe ser el PREFIJO de la etiqueta,
            # para no confundir con filas "NOTA: ISGC-P07-05 al ISGC-P07-10 ...".
            if not (colyears and first_year_col is not None and scope):
                continue
            leading = distinct_leading(cells, first_year_col)
            label = leading[0] if leading else ""
            if label.upper().startswith("NOTA"):
                continue
            m = CODE_RE.match(label.strip())
            if not m:
                continue
            code = m.group(0)
            key = code
            if code == "ISGC-P04-09" and len(leading) >= 2:
                key = f"{code}|{leading[-1]}"
            values = inds.get(key)
            if not values:
                continue
            byyear = {norm_year(y): v for y, v in (values.get(scope) or {}).items()}
            for ci, year in colyears.items():
                if year in byyear and byyear[year] not in (None, ""):
                    check_scale(label, scope, year, byyear[year])
                    set_cell_text(tb.cell(row._index if hasattr(row, "_index") else _row_index(tb, row), ci), byyear[year])
                    written += 1
    return written


def _row_index(tb, row):
    for i, r in enumerate(tb.rows):
        if r._tr is row._tr:
            return i
    return 0


def _first_cell(tb):
    return tb.cell(0, 0).text.strip().lower() if tb.rows else ""


def puntos_tables(doc):
    """Pares (tabla de puntos fuertes, tabla de puntos débiles) en orden de criterio.

    Se localizan por la celda (0,0) para no depender de la posición de las tablas,
    que cambia entre versiones de la plantilla."""
    fuertes = [tb for tb in doc.tables if _first_cell(tb).startswith("puntos fuertes")]
    debiles = [tb for tb in doc.tables if _first_cell(tb).startswith(("puntos débiles", "puntos debiles"))]
    if len(fuertes) != N_CRITERIOS or len(debiles) != N_CRITERIOS:
        print(f"AVISO: la plantilla tiene {len(fuertes)} tablas de puntos fuertes y {len(debiles)} "
              f"de puntos débiles (se esperaban {N_CRITERIOS}); revisa los criterios rellenados.",
              file=sys.stderr)
    return dict(enumerate(zip(fuertes, debiles), start=1))


def _accion(a):
    """Normaliza una acción de mejora: cadena o dict con accion, evidencia, prioridad,
    responsable, inicio, fin e indicador."""
    return dict(a) if isinstance(a, dict) else {"accion": str(a)}


def _codigo(data, tipo, ref):
    """Código PF/PD/AM-<centro>-<ref>, solo si el JSON trae `codigo_centro` (centros con
    varios títulos que lo usan, como la ESI o la ETSIA)."""
    centro = str(data.get("codigo_centro") or "").strip()
    return f"{tipo}-{centro}-{ref}" if centro else ""


def _rotulo(base, codigo=""):
    return f"{base} ({codigo}): " if codigo else f"{base}: "


def modelo_puntos(data):
    """Numera los puntos del bloque `puntos`.

    Los fuertes se numeran dentro de cada criterio y llevan delante el curso analizado
    (se copian luego en la renovación). Los débiles y sus acciones se numeran de forma
    correlativa en todo el autoinforme, porque todos pasan al plan de mejora."""
    puntos = data.get("puntos") or {}
    curso = str((data.get("encabezado") or {}).get("curso", "")).strip()
    modelo, n_pd, n_am = {}, 0, 0
    for crit in range(1, N_CRITERIOS + 1):
        info = puntos.get(str(crit)) or puntos.get(crit) or {}
        fuertes = []
        for i, texto in enumerate(info.get("fuertes") or [], 1):
            base = f"Curso {curso}. Punto fuerte {i}º" if curso else f"Punto fuerte {i}º"
            fuertes.append((_rotulo(base, _codigo(data, "PF", f"{crit}.{i}")), texto))
        debiles = []
        for i, deb in enumerate(info.get("debiles") or [], 1):
            n_pd += 1
            brutas = deb.get("acciones") or []
            acciones = []
            for k, a in enumerate(brutas, 1):
                n_am += 1
                a = _accion(a)
                ref = f"{crit}.{i}" + (f".{k}" if len(brutas) > 1 else "")
                a["rotulo"] = _rotulo(f"Acción de mejora {n_am}ª", _codigo(data, "AM", ref))
                acciones.append(a)
            debiles.append({
                "rotulo": _rotulo(f"Punto débil {n_pd}º", _codigo(data, "PD", f"{crit}.{i}")),
                "texto": deb.get("punto", ""),
                "acciones": acciones,
            })
        modelo[crit] = {"fuertes": fuertes, "debiles": debiles}
    return modelo


def items_accua(data):
    """Normaliza el bloque `accua`: una entrada por recomendación, con su numeración
    original y sus acciones. Admite el formato anterior (`fecha`, `accion` en texto)."""
    accua = data.get("accua") or {}
    informe = accua.get("informe") or accua.get("fecha", "")
    out = []
    for it in accua.get("items") or []:
        brutas = it.get("acciones")
        if brutas is None:
            brutas = [it["accion"]] if it.get("accion") else []
        acciones = [_accion(a) for a in brutas]
        if it.get("evidencia") and acciones and "evidencia" not in acciones[0]:
            acciones[0]["evidencia"] = it["evidencia"]
        tipo = str(it.get("tipo") or "Recomendación").strip()
        num = str(it.get("num") or "").strip()
        out.append({
            "informe": it.get("informe") or informe,
            "rotulo": _rotulo(f"{tipo} nº {num}" if num else tipo),
            "texto": it.get("rec", ""),
            "acciones": acciones,
        })
    return out


def _lineas_acciones(acciones):
    """«Acción de mejora» y «Evidencia» en párrafos distintos, con la etiqueta en negrita."""
    lineas = []
    for a in acciones or [{}]:
        lineas.append([(a.get("rotulo") or "Acción de mejora: ", True),
                       (a.get("accion") or PENDIENTE, False)])
        lineas.append([("Evidencia: ", True), (a.get("evidencia") or PENDIENTE, False)])
    return lineas


def _fila_datos(tb, j):
    """Índice de la fila de datos j (0 = primera tras la cabecera). Si la plantilla no
    tiene bastantes, clona la primera para conservar su formato."""
    while len(tb.rows) <= j + 1:
        tb._tbl.append(deepcopy(tb.rows[1]._tr))
    return j + 1


def _quitar_filas(tb, desde):
    """Elimina las filas de placeholder que no se han usado."""
    for row in list(tb.rows)[desde:]:
        tb._tbl.remove(row._tr)


def _tabla_por_cabecera(doc, texto):
    return next((t for t in doc.tables if t.rows
                 and texto in " ".join(c.text.lower() for c in t.rows[0].cells)), None)


def fill_puntos(doc, modelo):
    if not any(m["fuertes"] or m["debiles"] for m in modelo.values()):
        return
    for crit, (tbf, tbd) in puntos_tables(doc).items():
        m = modelo.get(crit) or {}
        if m.get("fuertes") and len(tbf.rows) > 1:
            set_cell_rich(tbf.cell(1, 0), [[(rot, True), (txt, False)] for rot, txt in m["fuertes"]],
                          tbf.rows[1])
        debiles = m.get("debiles") or []
        if not debiles:
            continue
        for j, deb in enumerate(debiles):
            r = _fila_datos(tbd, j)
            set_cell_rich(tbd.cell(r, 0), [[(deb["rotulo"], True), (deb["texto"], False)]], tbd.rows[r])
            if len(tbd.columns) > 1:
                lineas = [[(a["rotulo"], True), (a.get("accion") or PENDIENTE, False)]
                          for a in deb["acciones"]]
                set_cell_rich(tbd.cell(r, 1), lineas or [[("Acción de mejora: ", True), (PENDIENTE, False)]],
                              tbd.rows[r])
        _quitar_filas(tbd, len(debiles) + 1)


def fill_accua(doc, items):
    """Rellena la tabla de recomendaciones de ACCUA (Criterio 2): una recomendación por
    fila, con el informe (fecha y tipo) solo cuando cambia respecto a la fila anterior."""
    if not items:
        return
    tb = _tabla_por_cabecera(doc, "recomendaciones recibidas")
    if tb is None or len(tb.columns) < 3:
        print("AVISO: no se ha encontrado la tabla de recomendaciones de ACCUA del Criterio 2.",
              file=sys.stderr)
        return
    previo = None
    for j, it in enumerate(items):
        r = _fila_datos(tb, j)
        row = tb.rows[r]
        informe = it["informe"] if it["informe"] != previo else ""
        previo = it["informe"]
        set_cell_rich(tb.cell(r, 0), [[(informe, False)]], row)
        set_cell_rich(tb.cell(r, 1), [[(it["rotulo"], True), (it["texto"], False)]], row)
        set_cell_rich(tb.cell(r, 2), _lineas_acciones(it["acciones"]), row)
    _quitar_filas(tb, len(items) + 1)


def filas_plan(data, accua, modelo):
    """Filas del plan de mejora, generadas de una sola fuente para que coincidan con las
    tablas del autoinforme: recomendaciones de ACCUA (mismo orden y texto que en el
    Criterio 2), puntos débiles de este autoinforme y filas extra de `plan_mejora`
    (p. ej. puntos débiles no resueltos del plan anterior)."""
    filas = [{"origen": [[(it["rotulo"], True), (it["texto"], False)]], "acciones": it["acciones"],
              "ref": it["rotulo"]} for it in accua]
    for crit in sorted(modelo):
        for deb in modelo[crit]["debiles"]:
            filas.append({"origen": [[(deb["rotulo"], True), (deb["texto"], False)]],
                          "acciones": deb["acciones"], "ref": deb["rotulo"]})
    for f in data.get("plan_mejora") or []:
        if any(str(f.get(k, "")).strip() for k in ("origen", "accion", "evidencia")):
            filas.append({"origen": [[(f.get("origen", ""), False)]], "acciones": [_accion(f)],
                          "ref": f.get("origen", "")[:40]})
    return filas


def avisar_plan(filas):
    """Avisa de acciones sin texto o sin evidencia y de fechas que no son MM/AAAA (p. ej.
    «Permanente» o «Finalizada»)."""
    for f in filas:
        ref = f["ref"].strip().rstrip(":")
        if not f["acciones"] or not all(a.get("accion") for a in f["acciones"]):
            print(f"AVISO: «{ref}» no tiene acción de mejora; toda recomendación y todo punto "
                  "débil la necesitan.", file=sys.stderr)
        elif not all(a.get("evidencia") for a in f["acciones"]):
            print(f"AVISO: «{ref}» tiene acciones sin evidencia; cada acción lleva la suya "
                  "(un indicador no es una evidencia).", file=sys.stderr)
        for a in f["acciones"]:
            for campo in ("inicio", "fin"):
                v = str(a.get(campo, "")).strip()
                if v and not FECHA_RE.match(v):
                    print(f"AVISO: «{ref}», fecha de {campo} «{v}» no válida: usa MM/AAAA (ninguna "
                          "acción es «Permanente» ni «Finalizada»; el cierre lo decide ACCUA).",
                          file=sys.stderr)


def fill_plan_mejora(doc, filas):
    if not filas:
        return
    tb = _tabla_por_cabecera(doc, "prioridad")
    if tb is None:
        print("AVISO: no se ha encontrado la tabla del plan de mejora (cabecera con "
              "«Prioridad»).", file=sys.stderr)
        return
    for j, f in enumerate(filas):
        r = _fila_datos(tb, j)
        row = tb.rows[r]
        columnas = [f["origen"], _lineas_acciones(f["acciones"])]
        for campo in CAMPOS_PLAN:
            vacio = "" if campo == "indicador" else PENDIENTE
            columnas.append([[(str(a.get(campo) or vacio), False)] for a in f["acciones"] or [{}]])
        for ci, lineas in enumerate(columnas[:len(tb.columns)]):
            set_cell_rich(tb.cell(r, ci), lineas, row)
    _quitar_filas(tb, len(filas) + 1)
    avisar_plan(filas)


def _para_color(p):
    """Color común de los runs con texto del párrafo, o None si no hay uno solo."""
    colores = {str(r.font.color.rgb) if r.font.color and r.font.color.type is not None
               and r.font.color.rgb is not None else None
               for r in p.runs if r.text.strip()}
    return colores.pop() if len(colores) == 1 else None


def fill_campus(doc, data):
    """Deja en el criterio 5.1 solo el bloque de bibliotecas del campus del título.

    La plantilla trae un bloque por campus, cada uno con su color de fuente
    (CAMPUS_COLORES). Se conserva en negro el del campus indicado y se borran los demás.
    """
    campus = str(data.get("campus", "")).strip().lower()
    color_campus = CAMPUS_COLORES.get(campus)
    if not color_campus:
        print(f"AVISO: 'campus' ausente o no válido ({campus or 'vacío'}); usa uno de "
              f"{', '.join(CAMPUS_COLORES)}. Los bloques de bibliotecas del 5.1 quedan sin "
              "recortar.", file=sys.stderr)
        return
    otros = set(CAMPUS_COLORES.values()) - {color_campus}
    for p in list(doc.paragraphs):
        color = _para_color(p)
        if color == color_campus:
            for r in p.runs:
                r.font.color.rgb = None
        elif color in otros:
            p._element.getparent().remove(p._element)


def actualizar_enlaces(doc):
    """Sustituye los hipervínculos obsoletos de la plantilla (ENLACES_VIGENTES)."""
    for rel in doc.part.rels.values():
        if not rel.is_external:
            continue
        for antiguo, nuevo in ENLACES_VIGENTES.items():
            if antiguo in rel.target_ref:
                rel._target = nuevo


def main():
    ap = argparse.ArgumentParser(description="Rellena la plantilla del Autoinforme de Seguimiento (UCA).")
    ap.add_argument("--plantilla", required=True)
    ap.add_argument("--datos", required=True)
    ap.add_argument("--salida", required=True)
    args = ap.parse_args()

    with open(args.datos, encoding="utf-8") as f:
        data = json.load(f)

    doc = docx.Document(args.plantilla)
    fill_header(doc, data.get("encabezado"))
    fill_identity(doc, data.get("identificacion"))
    fill_campus(doc, data)
    actualizar_enlaces(doc)
    n = fill_indicators(doc, data)
    modelo = modelo_puntos(data)
    accua = items_accua(data)
    fill_accua(doc, accua)
    fill_puntos(doc, modelo)
    fill_plan_mejora(doc, filas_plan(data, accua, modelo))
    doc.save(args.salida)
    print(f"OK: {args.salida} | valores de indicadores escritos: {n}")


if __name__ == "__main__":
    main()
