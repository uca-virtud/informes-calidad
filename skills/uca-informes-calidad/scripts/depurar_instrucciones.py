#!/usr/bin/env python3
"""Depura el texto de instrucciones de la plantilla del autoinforme.

Elimina las instrucciones de cumplimentación y las directrices, para dejar un único
documento limpio tras redactar el análisis. Recorre el cuerpo y las celdas de las tablas
(también las anidadas). Criterios de borrado:
  - Párrafos cuyo texto va entero en ROJO (instrucciones) o AZUL (directrices ACCUA),
    según el convenio de colores de la plantilla.
  - Párrafos entre corchetes "[ ... ]" (instrucciones) o con marcadores "XXXX"/"xxxx".
  - En párrafos mixtos, solo los fragmentos (runs) en rojo o azul. Excepción: si el
    párrafo tiene texto propio en negro, el azul intercalado lo completa (p. ej. la lista
    de lo que publica la web en el criterio 1): se conserva en negro y solo se borra el
    rojo. Quien redacta debe comprobar en la web cada elemento conservado.
Excepción previa: el recordatorio en rojo «Se recuerda que deben estar publicados…» y su
lista se conservan en negro, porque el Servicio de Gestión de la Calidad quiere que la
coordinación los tenga presentes (quien redacta añade a cada elemento su enlace).
En las celdas, las etiquetas cortas solo en azul (encabezados de ejemplo como
«Suspensos» o «%») se conservan y pasan a negro: son parte de la estructura de la tabla.
Conserva el texto en negro (análisis), las tablas y los marcadores "[PENDIENTE: …]".
En una celda que se quedaría sin párrafos se vacía el texto en lugar de borrar el último.
Tras quitar los fragmentos de color de un párrafo mixto, borra el párrafo si solo queda
puntuación, recorta el guion final que queda colgando y los espacios sobrantes, y lista el
resto para revisarlo: el texto en negro de un párrafo mixto puede ser parte de una
instrucción o una opción que no procede para el título, y eso solo puede decidirlo quien
redacta.

Al final aplica el formato que pide el Servicio de Gestión de la Calidad (idempotente):
marcas [PENDIENTE…] en rojo, sin resaltados de color, URL sueltas convertidas en enlaces
activos, enlaces en azul y subrayados, y la prosa del cuerpo (criterios 1 a 6) justificada,
a 10 pt y en la fuente del tema. Avisa de las menciones a «DEVA», de los enlaces que
apuntan a rutas locales y de los que llevan a herramientas a las que no acceden los
evaluadores (LinceBI, GADES, ICARO, Campus Virtual).

Uso:
  python depurar_instrucciones.py --entrada relleno.docx --salida final.docx
"""
import argparse
import re
import sys
from copy import deepcopy

try:
    import docx
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor
    from docx.text.run import Run
except ImportError:
    sys.exit("Falta python-docx: pip install python-docx --break-system-packages")

XXXX = re.compile(r"[Xx]{3,}")
PENDIENTE = "[PENDIENTE"
MAX_PALABRAS_ETIQUETA = 6
SOLO_PUNTUACION = re.compile(r"^[\s\-–—.:;,()]*$")
GUION_COLGANTE = re.compile(r"(?<=\s)[-–—]\s*\.?\s*$")
LETRAS = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2}")
ESPACIO_SOBRANTE = re.compile(r" (?=[ ,;:.)])|(?<=\() ")
MAX_AVISOS = 40
# Marcas [PENDIENTE…] (con las URL que contengan) o URL sueltas, en texto de un run.
MARCA_O_URL = re.compile(r"(?P<pend>\[PENDIENTE[^\]]*\]?)|(?P<url>https?://[^\s<>\[\]\"«»]+)")
ROJO = RGBColor(0xFF, 0x00, 0x00)
AZUL = RGBColor(0x00, 0x00, 0xFF)
TAMANO_PROSA = Pt(10)
MIN_CAR_PROSA = 60
FIN_CUERPO = "PLAN DE MEJORA"
DEVA = re.compile(r"\bDEVA\b")
INICIO_INFO_PUBLICA = "Se recuerda que deben estar publicados"
# Herramientas con acceso UCA (LinceBI, GADES, ICARO, Campus Virtual) que los evaluadores
# de ACCUA no pueden abrir.
HERRAMIENTAS_RESTRINGIDAS = re.compile(r"lincebi|gades\.uca\.es|icaro|campusvirtual|/moodle",
                                       re.IGNORECASE)


def _rgb(run):
    try:
        c = run.font.color
        if c is not None and c.rgb is not None:
            return (c.rgb[0], c.rgb[1], c.rgb[2])
    except Exception:
        pass
    return None


def _is_reddish(rgb):
    r, g, b = rgb
    return r >= 120 and g < 90 and b < 90


def _is_bluish(rgb):
    r, g, b = rgb
    # Cubre el azul oscuro (0070C0) y el azul claro (00B0F0) de las directrices ACCUA.
    return b >= 120 and r < 90 and g < b


def _is_colored(run):
    rgb = _rgb(run)
    return bool(rgb) and (_is_reddish(rgb) or _is_bluish(rgb))


def is_instruction(p):
    t = p.text.strip()
    if not t or PENDIENTE in t:
        return False
    if t.startswith("[") or XXXX.search(t):
        return True
    runs = [r for r in p.runs if r.text.strip()]
    return bool(runs) and all(_is_colored(r) for r in runs)


def is_etiqueta_tabla(p):
    t = p.text.strip()
    if not t or t.startswith("[") or XXXX.search(t) or len(t.split()) > MAX_PALABRAS_ETIQUETA:
        return False
    colores = [_rgb(r) for r in p.runs if r.text.strip() and _is_colored(r)]
    return bool(colores) and all(_is_bluish(c) for c in colores)


def _borrar(p, en_celda):
    if en_celda and len(p._element.getparent().findall(p._element.tag)) == 1:
        for r in p.runs:
            r.text = ""
    else:
        p._element.getparent().remove(p._element)


def _recortar_final(p, patron):
    texto = "".join(r.text for r in p.runs)
    m = patron.search(texto)
    if not m:
        return
    sobran = len(texto) - m.start()
    for r in reversed(p.runs):
        if sobran <= 0:
            break
        n = min(len(r.text), sobran)
        r.text = r.text[:len(r.text) - n]
        sobran -= n


def _texto_propio(p):
    """¿Tiene el párrafo texto con letras fuera del rojo y del azul?"""
    return any(LETRAS.search(r.text) for r in p.runs if r.text.strip() and not _is_colored(r))


def _normalizar_espacios(p):
    """Quita los espacios dobles y los previos a un signo de puntuación que quedan tras
    borrar fragmentos, sin tocar el formato de cada run."""
    texto = "".join(r.text for r in p.runs)
    sobran = {m.start() for m in ESPACIO_SOBRANTE.finditer(texto)}
    if not sobran:
        return
    pos = 0
    for r in p.runs:
        n = len(r.text)
        if any(pos <= i < pos + n for i in sobran):
            r.text = "".join(ch for k, ch in enumerate(r.text) if pos + k not in sobran)
        pos += n


def depurar_parrafos(parrafos, en_celda=False, revisar=None):
    """Devuelve (párrafos borrados, fragmentos borrados).

    Añade a `revisar` el texto que queda en los párrafos mixtos depurados."""
    borrados = fragmentos = 0
    for p in list(parrafos):
        if en_celda and is_etiqueta_tabla(p):
            for r in p.runs:
                r.font.color.rgb = None
        elif is_instruction(p):
            _borrar(p, en_celda)
            borrados += 1
        elif PENDIENTE not in p.text:
            color = [r for r in p.runs if r.text.strip() and _is_colored(r)]
            if not color:
                continue
            if _texto_propio(p):
                # El azul intercalado en una frase en negro la completa (lista de lo que
                # publica la web): se conserva en negro y se borra solo el rojo.
                rojos = [r for r in color if _is_reddish(_rgb(r))]
                for r in color:
                    if r not in rojos:
                        r.font.color.rgb = None
                color = rojos
            for r in color:
                r.text = ""
            fragmentos += len(color)
            if SOLO_PUNTUACION.match("".join(r.text for r in p.runs)):
                _borrar(p, en_celda)
                borrados += 1
                continue
            _recortar_final(p, GUION_COLGANTE)
            _normalizar_espacios(p)
            if revisar is not None:
                revisar.append(p.text.strip())
    return borrados, fragmentos


def depurar_tablas(tablas, revisar=None):
    borrados = fragmentos = 0
    for tabla in tablas:
        celdas = set()
        for fila in tabla.rows:
            for celda in fila.cells:
                if celda._tc in celdas:
                    continue
                celdas.add(celda._tc)
                b, f = depurar_parrafos(celda.paragraphs, en_celda=True, revisar=revisar)
                bt, ft = depurar_tablas(celda.tables, revisar)
                borrados, fragmentos = borrados + b + bt, fragmentos + f + ft
    return borrados, fragmentos


# --- Pasada final de formato (idempotente) --------------------------------------------

def _todos_los_parrafos(doc):
    """Párrafos del cuerpo y de todas las celdas, también de tablas anidadas."""
    yield from doc.paragraphs
    pendientes, vistas = list(doc.tables), set()
    while pendientes:
        tabla = pendientes.pop()
        for fila in tabla.rows:
            for celda in fila.cells:
                if celda._tc in vistas:
                    continue
                vistas.add(celda._tc)
                yield from celda.paragraphs
                pendientes.extend(celda.tables)


def _run_simple(r):
    """Run con un único w:t y sin tabuladores, saltos, campos ni dibujos: se puede partir."""
    hijos = [h.tag for h in r if h.tag != qn("w:rPr")]
    return hijos == [qn("w:t")]


def _texto_run(r):
    return "".join(t.text or "" for t in r.iter(qn("w:t")))


def _partir(r, i):
    """Parte un run simple en la posición i; devuelve el run de la derecha."""
    derecho = deepcopy(r)
    t_izq, t_der = r.find(qn("w:t")), derecho.find(qn("w:t"))
    texto = t_izq.text
    t_izq.text, t_der.text = texto[:i], texto[i:]
    for t in (t_izq, t_der):
        t.set(qn("xml:space"), "preserve")
    r.addnext(derecho)
    return derecho


def _tramos(p):
    """[(run, inicio, fin)] de los runs directos del párrafo (no los de hipervínculos)."""
    out, pos = [], 0
    for r in p._p.findall(qn("w:r")):
        n = len(_texto_run(r))
        out.append((r, pos, pos + n))
        pos += n
    return out


def _recortar_url(url):
    while url and (url[-1] in ".,;:" or (url[-1] == ")" and url.count(")") > url.count("("))):
        url = url[:-1]
    return url


def _coincidencias(texto):
    for m in MARCA_O_URL.finditer(texto):
        if m.group("pend"):
            yield "pend", m.start(), m.end()
        else:
            url = _recortar_url(m.group("url"))
            if len(url) > len("https://"):
                yield "url", m.start(), m.start() + len(url)


def _aislar(p, ini, fin):
    """Parte los runs para que [ini, fin) quede en runs propios; devuelve esos runs, o
    None si algún run afectado no se puede partir."""
    for corte in (ini, fin):
        for r, a, b in _tramos(p):
            if a < corte < b:
                if not _run_simple(r):
                    return None
                _partir(r, corte - a)
                break
    return [r for r, a, b in _tramos(p) if a >= ini and b <= fin and b > a]


def _color(r, rgb, subrayado=False):
    run = Run(r, None)
    run.font.color.rgb = rgb
    if subrayado:
        run.font.underline = True


def _enlazar(p, runs, url):
    enlace = OxmlElement("w:hyperlink")
    enlace.set(qn("r:id"), p.part.relate_to(url, RT.HYPERLINK, is_external=True))
    enlace.set(qn("w:history"), "1")
    runs[0].addprevious(enlace)
    for r in runs:
        enlace.append(r)


def _marcar_pendientes_y_enlaces(p):
    """Pone en rojo las marcas [PENDIENTE…] y convierte en hipervínculo las URL sueltas.

    Las URL de un párrafo con campos (HYPERLINK como código de campo) no se tocan."""
    con_campos = p._p.find(".//" + qn("w:fldChar")) is not None or \
        p._p.find(".//" + qn("w:fldSimple")) is not None
    texto = "".join(_texto_run(r) for r, _, _ in _tramos(p))
    for tipo, ini, fin in reversed(list(_coincidencias(texto))):
        if tipo == "url" and con_campos:
            continue
        runs = _aislar(p, ini, fin)
        if runs is None:
            if tipo == "pend":  # no se puede partir: el run entero en rojo
                for r, a, b in _tramos(p):
                    if a < fin and b > ini:
                        _color(r, ROJO)
            continue
        if tipo == "pend":
            for r in runs:
                _color(r, ROJO)
        else:
            _enlazar(p, runs, texto[ini:fin])


def _quitar_resaltado(p):
    for h in list(p._p.iter(qn("w:highlight"))):
        h.getparent().remove(h)


def _enlaces_en_azul(p):
    for enlace in p._p.findall(qn("w:hyperlink")):
        for r in enlace.iter(qn("w:r")):
            if PENDIENTE not in _texto_run(r):
                _color(r, AZUL, subrayado=True)


def _es_prosa(p):
    estilo = (p.style.name if p.style is not None else "").lower()
    if any(k in estilo for k in ("heading", "título", "title", "toc")):
        return False
    alineacion = p.alignment
    if alineacion not in (None, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.JUSTIFY):
        return False
    return len(p.text.strip()) >= MIN_CAR_PROSA


def _fuente_tema(rpr):
    """Sustituye las fuentes explícitas ajenas por la fuente del tema (minorHAnsi)."""
    f = rpr.find(qn("w:rFonts"))
    if f is not None and (f.get(qn("w:ascii")) or f.get(qn("w:hAnsi"))):
        rpr.remove(f)
        f = None
    if f is None:
        f = OxmlElement("w:rFonts")
        rpr.insert(0, f)
    for atr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme"):
        f.set(qn(atr), "minorHAnsi")


def _formato_prosa(p):
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for r in p._p.iter(qn("w:r")):
        run = Run(r, None)
        run.font.size = TAMANO_PROSA
        _fuente_tema(r.get_or_add_rPr())


def formato_final(doc):
    """Pasada de formato que pide el Servicio de Gestión de la Calidad. Devuelve los
    párrafos que mencionan «DEVA» (hay que escribir «ACCUA»)."""
    en_cuerpo = {id(p._p) for p in doc.paragraphs}
    fuera_de_prosa = False
    deva = []
    for p in _todos_los_parrafos(doc):
        _marcar_pendientes_y_enlaces(p)
        _quitar_resaltado(p)
        _enlaces_en_azul(p)
        if DEVA.search(p.text):
            deva.append(p.text.strip())
        if id(p._p) in en_cuerpo:
            t = p.text.strip().upper()
            if t.startswith(FIN_CUERPO) or t.startswith("ANEXO"):
                fuera_de_prosa = True
            if not fuera_de_prosa and _es_prosa(p):
                _formato_prosa(p)
    return deva


def _enlaces(doc):
    """(texto, destino) de cada hipervínculo externo del cuerpo."""
    rels = doc.part.rels
    for h in doc.element.body.iter(qn("w:hyperlink")):
        rid = h.get(qn("r:id"))
        if rid:
            destino = rels[rid].target_ref if rid in rels else ""
            yield "".join(t.text or "" for t in h.iter(qn("w:t"))).strip(), destino


def enlaces_no_web(doc):
    """Textos de los hipervínculos que apuntan a rutas locales u otros destinos no web."""
    return [texto for texto, destino in _enlaces(doc)
            if not destino.lower().startswith(("http://", "https://", "mailto:"))]


def enlaces_restringidos(doc):
    """Destinos de los hipervínculos a herramientas a las que no acceden los evaluadores."""
    return list(dict.fromkeys(destino for _, destino in _enlaces(doc)
                              if HERRAMIENTAS_RESTRINGIDAS.search(destino)))


def conservar_info_publica(doc):
    """Pasa a negro el recordatorio en rojo de lo que debe publicarse en la web y su lista,
    para que la depuración no lo borre: el Servicio de Gestión de la Calidad lo mantiene
    en el autoinforme para que la coordinación no lo olvide. Devuelve los párrafos."""
    parrafos = doc.paragraphs
    for i, p in enumerate(parrafos):
        if p.text.strip().startswith(INICIO_INFO_PUBLICA):
            bloque = [p]
            for q in parrafos[i + 1:]:
                rojos = [r for r in q.runs if r.text.strip() and _is_reddish(_rgb(r) or (0, 0, 0))]
                if not rojos or q.text.strip().startswith("["):
                    break
                bloque.append(q)
            for q in bloque:
                for r in q.runs:
                    if _rgb(r) and _is_reddish(_rgb(r)):
                        r.font.color.rgb = None
            return len(bloque)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--salida", required=True)
    args = ap.parse_args()
    d = docx.Document(args.entrada)
    conservar_info_publica(d)
    revisar = []
    borrados, fragmentos = depurar_parrafos(d.paragraphs, revisar=revisar)
    bt, ft = depurar_tablas(d.tables, revisar)
    deva = formato_final(d)
    d.save(args.salida)
    print(f"OK: {args.salida} | párrafos de instrucciones eliminados: {borrados + bt} "
          f"(en tablas: {bt}) | fragmentos en rojo/azul eliminados: {fragmentos + ft}")
    avisar_revision(revisar)
    _avisar("párrafos mencionan «DEVA»; la agencia es ACCUA", deva)
    _avisar("enlaces apuntan a una ruta local u otro destino no web; sustitúyelos por la "
            "URL pública", enlaces_no_web(d))
    _avisar("enlaces llevan a herramientas a las que no acceden los evaluadores (LinceBI, "
            "GADES, ICARO, Campus Virtual); cita la herramienta sin enlace o enlaza la "
            "evidencia publicada o en UCADrive", enlaces_restringidos(d))


def avisar_revision(revisar):
    """Lista, sin repetir, los párrafos mixtos cuyo resto en negro hay que revisar."""
    _avisar("párrafos mezclaban instrucciones y texto en negro. Comprueba que lo que queda "
            "no sea parte de una instrucción ni una opción que no procede para el título",
            list(dict.fromkeys(t for t in revisar if t)))


def _avisar(titulo, textos):
    if not textos:
        return
    print(f"REVISAR: {len(textos)} {titulo}:", file=sys.stderr)
    for t in textos[:MAX_AVISOS]:
        print(f"  - {t[:110]}{'…' if len(t) > 110 else ''}", file=sys.stderr)
    if len(textos) > MAX_AVISOS:
        print(f"  … y {len(textos) - MAX_AVISOS} más.", file=sys.stderr)


if __name__ == "__main__":
    main()
