#!/usr/bin/env python3
"""Organiza y mide las ejecuciones de evaluación de la skill de autoinformes.

Uso (desde la raíz del repositorio):
  python tools/evaluacion/evaluacion.py nueva <id> [--modelo-a M] [--modelo-b M]
  python tools/evaluacion/evaluacion.py medir <Enn>

Ver docs/evaluacion/procedimiento.md.
"""
import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DOC_EVAL = RAIZ / "docs" / "evaluacion"
EVALS = RAIZ / "evals"
CASOS_DIR = EVALS / "casos"
EJEC_DIR = EVALS / "ejecuciones"
SKILL_DIR = RAIZ / "skills" / "uca-informes-calidad"
PLANTILLA_DOCX = SKILL_DIR / "assets" / "plantilla_autoinforme_seguimiento.docx"

MODELO_A = "claude-opus-5.5"
MODELO_B = "gpt-6.1-sol"
DIMENSIONES = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"]
CAUSAS = ["S", "D", "I", "H", "E"]
ENTRADA_OBLIGATORIA = {"seguimiento": ["autoinforme-anterior.pdf", "memoria.pdf"]}

RE_CODIGO = re.compile(r"\b(PF|PD|AM)[\s\-–]*[A-Z]{2,6}[\s\-–]*\d+(?:\.\d+)*\b")
RE_INDICADOR = re.compile(r"\bP0\d[\-_ ]?\d{2}")
RE_NUMERO = re.compile(r"(?<![\w.,])-?\d{1,3}(?:\.\d{3})*(?:,\d+)?(?:\.\d+)?(?![\w])")
MARCA_INI, MARCA_FIN = "<!-- medir:inicio -->", "<!-- medir:fin -->"


def error(msg):
    sys.exit("ERROR: " + msg)


def leer_casos():
    with open(DOC_EVAL / "casos.csv", encoding="utf-8") as f:
        return {fila["id"]: fila for fila in csv.DictReader(f)}


def version_rubrica():
    m = re.search(r"^Versión:\s*(\S+)", (DOC_EVAL / "rubrica.md").read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else "?"


def version_skill():
    try:
        commit = subprocess.run(["git", "log", "-1", "--format=%h", "--", str(SKILL_DIR)],
                                cwd=RAIZ, capture_output=True, text=True).stdout.strip()
        cambios = subprocess.run(["git", "status", "--porcelain", "--", str(SKILL_DIR)],
                                 cwd=RAIZ, capture_output=True, text=True).stdout.strip()
    except OSError:
        return "desconocida"
    return (commit or "sin commit") + (" + cambios sin commit" if cambios else "")


# --- nueva -------------------------------------------------------------------

def comprobar_caso(caso):
    base = CASOS_DIR / caso["id"]
    entrada, referencia = base / "entrada", base / "referencia"
    faltan = [n for n in ENTRADA_OBLIGATORIA.get(caso["tipo"], []) if not (entrada / n).exists()]
    if not entrada.is_dir() or not any(entrada.iterdir()):
        faltan.append("entrada/ (vacía)")
    if not list(referencia.glob("autoinforme-humano.*")):
        faltan.append("referencia/autoinforme-humano.*")
    if faltan:
        error(f"al caso {caso['id']} le faltan: {', '.join(faltan)} (en {base})")


def siguiente_numero():
    nums = [int(m.group(1)) for m in (re.match(r"E(\d+)-", p.name) for p in EJEC_DIR.glob("E*-*")) if m]
    return max(nums, default=0) + 1


def cmd_nueva(args):
    casos = leer_casos()
    caso = casos.get(args.id) or error(f"el caso {args.id} no está en docs/evaluacion/casos.csv")
    if caso["conjunto"] == "excluido":
        error(f"{args.id} está excluido: la skill usa textos suyos como ejemplos")
    comprobar_caso(caso)
    nombre = f"E{siguiente_numero():02d}-{caso['id']}"
    carpeta = EJEC_DIR / nombre
    carpeta.mkdir(parents=True)
    accua = caso.get("seguimiento_accua") or "no consta: se asume sí"
    valores = {
        "<Enn-id>": nombre, "<Enn>": nombre.split("-")[0], "<id>": caso["id"],
        "<titulo>": caso["titulo"], "<tipo>": caso["tipo"], "<curso>": caso["curso"],
        "<convocatoria>": caso["convocatoria"], "<sí / no / no consta: se asume sí>": accua,
        "<aprendizaje / reserva>": caso["conjunto"], "<AAAA-MM-DD>": date.today().isoformat(),
        "<commit de skills/ y si hay cambios sin commit>": version_skill(),
        "<n>": version_rubrica(), "<modelo>": None,
    }
    texto = (DOC_EVAL / "plantilla-ficha.md").read_text(encoding="utf-8")
    for clave, valor in valores.items():
        if valor is not None:
            texto = texto.replace(clave, valor, 1 if clave == "<AAAA-MM-DD>" else -1)
    texto = texto.replace("<modelo>", args.modelo_a, 1).replace("<modelo>", args.modelo_b, 1)
    (carpeta / "ficha.md").write_text(texto, encoding="utf-8")
    print(f"Creada {carpeta.relative_to(RAIZ)}")
    print(f"  entrada:    {(CASOS_DIR / caso['id'] / 'entrada').relative_to(RAIZ)}")
    print(f"  referencia: {(CASOS_DIR / caso['id'] / 'referencia').relative_to(RAIZ)} (no se da a A al generar)")


# --- extracción de texto ------------------------------------------------------

def texto_docx(ruta):
    import docx
    doc = docx.Document(str(ruta))
    partes = [p.text for p in doc.paragraphs]
    vistas = set()
    for tabla in doc.tables:
        for fila in tabla.rows:
            for celda in fila.cells:
                if celda._tc not in vistas:
                    vistas.add(celda._tc)
                    partes.append(celda.text)
    return "\n".join(partes)


def texto_pdf(ruta):
    import pypdf
    return "\n".join((p.extract_text() or "") for p in pypdf.PdfReader(str(ruta)).pages)


def texto(ruta):
    return texto_docx(ruta) if ruta.suffix.lower() == ".docx" else texto_pdf(ruta)


def a_numero(token):
    t = token.replace(".", "") if "," in token else token
    try:
        return float(t.replace(",", "."))
    except ValueError:
        return None


def es_anio(x):
    return x.is_integer() and 1990 <= x <= 2035


def valores_anexo(ruta_docx):
    """Valores numéricos de las filas de indicadores ISGC (P0x-yy) del borrador."""
    import docx
    valores = []
    for tabla in docx.Document(str(ruta_docx)).tables:
        for fila in tabla.rows:
            celdas = [c.text.strip() for c in fila.cells]
            if not celdas or not RE_INDICADOR.search(celdas[0]):
                continue
            vistas = set()
            for c in fila.cells[1:]:
                if c._tc in vistas:
                    continue
                vistas.add(c._tc)
                for tok in RE_NUMERO.findall(c.text):
                    x = a_numero(tok)
                    if x is not None and not es_anio(x):
                        valores.append(x)
    return valores


def metricas_documento(txt):
    return {
        "palabras": len(txt.split()),
        "pf": len({m.group(0) for m in RE_CODIGO.finditer(txt) if m.group(1) == "PF"}),
        "pd": len({m.group(0) for m in RE_CODIGO.finditer(txt) if m.group(1) == "PD"}),
        "am": len({m.group(0) for m in RE_CODIGO.finditer(txt) if m.group(1) == "AM"}),
        "pendientes": len(re.findall(r"\[PENDIENTE", txt, re.I)),
    }


def coincidencia_anexo(valores, txt_ref):
    ref = [a_numero(t) for t in RE_NUMERO.findall(txt_ref)]
    ref1 = {round(x, 1) for x in ref if x is not None}
    ref2 = {round(x, 2) for x in ref if x is not None}
    if not valores:
        return None
    hits = sum(1 for x in valores if round(x, 2) in ref2 or round(x, 1) in ref1)
    return {"valores": len(valores), "encontrados": hits, "porcentaje": round(100 * hits / len(valores), 1)}


# --- huellas de casos en la skill -------------------------------------------

def tejas(txt, n=8):
    palabras = re.findall(r"\w+", txt.lower())
    return {" ".join(palabras[i:i + n]) for i in range(len(palabras) - n + 1)}


def huellas_en_skill(casos):
    """Frases de 8 palabras que solo aparecen en la referencia de un título y también en la skill.

    Las frases presentes en la plantilla oficial o en las referencias de varios títulos se
    consideran institucionales y no se avisan."""
    genericas = tejas(texto_docx(PLANTILLA_DOCX)) if PLANTILLA_DOCX.exists() else set()
    por_caso = {}
    for caso in casos.values():
        for ref in (CASOS_DIR / caso["id"] / "referencia").glob("autoinforme-humano.*"):
            por_caso[caso["id"]] = tejas(texto(ref)) - genericas
    especificas = {}
    for caso_id, frases in por_caso.items():
        otras = set().union(*(f for c, f in por_caso.items() if c != caso_id))
        for frase in frases - otras:
            if sum(not w.isdigit() for w in frase.split()) >= 5:
                especificas[frase] = caso_id
    nombres = [c["titulo"] for c in casos.values()]
    hallazgos = []
    for f in sorted(SKILL_DIR.rglob("*")):
        if f.suffix not in {".md", ".json", ".py"} or "__pycache__" in f.parts:
            continue
        contenido = f.read_text(encoding="utf-8", errors="ignore")
        comunes = sorted(tejas(contenido) & especificas.keys())
        titulos = [n for n in nombres if n.lower() in contenido.lower()]
        if comunes or titulos:
            hallazgos.append({"fichero": str(f.relative_to(RAIZ)), "frases": len(comunes),
                              "casos": sorted({especificas[c] for c in comunes}),
                              "ejemplo": comunes[0] if comunes else "", "titulos": titulos})
    return hallazgos


# --- cotejos ------------------------------------------------------------------

def filas_tabla(md, seccion):
    m = re.search(rf"^## {seccion}\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    if not m:
        return []
    filas = []
    for linea in m.group(1).splitlines():
        if linea.startswith("|") and not re.match(r"^\|\s*-", linea):
            filas.append([c.strip() for c in linea.strip().strip("|").split("|")])
    return filas[1:]


def version_cotejo(ruta):
    if ruta.exists():
        m = re.search(r"^- Versión de la rúbrica:\s*(\S+)", ruta.read_text(encoding="utf-8"), re.M)
        if m:
            return m.group(1)
    return "—"


def leer_cotejo(ruta):
    if not ruta.exists():
        return None
    md = ruta.read_text(encoding="utf-8")
    notas = {}
    for f in filas_tabla(md, "Puntuación"):
        if f and f[0] in DIMENSIONES and len(f) > 1:
            notas[f[0]] = int(f[1]) if f[1] in {"0", "1", "2"} else None
    bloqueantes = [f[0] for f in filas_tabla(md, "Bloqueantes") if len(f) > 1 and f[1].lower().startswith("s")]
    causas = {c: 0 for c in CAUSAS}
    pendientes = []
    for f in filas_tabla(md, "Discrepancias"):
        if len(f) > 4 and f[4].upper() in causas:
            causas[f[4].upper()] += 1
            if f[4].upper() in {"H", "I"}:
                pendientes.append(f"Discrepancia {f[0]} ({f[4].upper()}): {f[1]}")
    lecciones = [f[0] for f in filas_tabla(md, "Lecciones propuestas") if f and f[0] and not f[0].startswith("<")]
    return {"notas": notas, "bloqueantes": bloqueantes, "causas": causas,
            "pendientes": pendientes, "lecciones": lecciones}


def consolidar(a, b):
    final, pendientes = {}, []
    for d in DIMENSIONES:
        na = a["notas"].get(d) if a else None
        nb = b["notas"].get(d) if b else None
        final[d] = nb if nb is not None else na
        if na is not None and nb is not None and abs(na - nb) >= 2:
            pendientes.append(f"{d}: A={na}, B={nb}")
    validas = [v for v in final.values() if v is not None]
    media = round(sum(validas) / len(validas), 2) if validas else None
    return final, media, pendientes


# --- medir --------------------------------------------------------------------

def buscar_ejecucion(clave):
    candidatas = [p for p in EJEC_DIR.glob(f"{clave}*") if p.is_dir()]
    if len(candidatas) != 1:
        error(f"no hay una única ejecución que empiece por {clave}")
    return candidatas[0]


def nota(valor):
    return "—" if valor is None else valor


def tabla_md(cabecera, filas):
    lineas = ["| " + " | ".join(cabecera) + " |", "|" + "---|" * len(cabecera)]
    lineas += ["| " + " | ".join(str(c) for c in f) + " |" for f in filas]
    return "\n".join(lineas)


def bloque_resultado(r):
    m, h = r["borrador"], r["referencia"]
    ratio = f"{m['palabras']:,} / {h['palabras']:,} ({round(100 * m['palabras'] / h['palabras'])} %)".replace(",", ".")
    anexo = r["anexo"]
    partes = [
        tabla_md(["Métrica", "Borrador", "Humano"], [
            ["Palabras", m["palabras"], h["palabras"]], ["PF distintos", m["pf"], h["pf"]],
            ["PD distintos", m["pd"], h["pd"]], ["AM distintas", m["am"], h["am"]],
            ["`[PENDIENTE]`", m["pendientes"], h["pendientes"]]]),
        f"\nExtensión borrador / humano: {ratio}.",
        f"Valores del Anexo I presentes en algún lugar de la referencia (cota superior, no mide la celda): "
        + (f"{anexo['encontrados']}/{anexo['valores']} ({anexo['porcentaje']} %)." if anexo else "sin tablas de indicadores."),
        "",
        tabla_md(["Dim.", "A", "B", "Final"],
                 [[d, nota(r["notas_a"].get(d)), nota(r["notas_b"].get(d)), nota(r["final"][d])] for d in DIMENSIONES]),
        f"\nMedia final: {nota(r['media'])}. Bloqueantes: {', '.join(r['bloqueantes']) or 'ninguno'}. "
        f"Discrepancias por causa (B): " + ", ".join(f"{k}={v}" for k, v in r["causas_b"].items()) + ".",
    ]
    if r["huellas"]:
        partes.append("\n**Aviso de huellas de casos en la skill** (revisar que no sean datos de títulos):")
        partes += [f"- `{x['fichero']}`: {x['frases']} frases de {', '.join(x['casos']) or '—'}"
                   + (f", títulos {x['titulos']}" if x["titulos"] else "")
                   + (f" (p. ej. «{x['ejemplo']}»)" if x["ejemplo"] else "") for x in r["huellas"]]
    return "\n".join(str(p) for p in partes)


def actualizar_ficha(carpeta, r):
    ficha = carpeta / "ficha.md"
    if not ficha.exists():
        return
    txt = ficha.read_text(encoding="utf-8")
    txt = re.sub(re.escape(MARCA_INI) + ".*?" + re.escape(MARCA_FIN),
                 lambda _: f"{MARCA_INI}\n{bloque_resultado(r)}\n{MARCA_FIN}", txt, flags=re.S)
    pend = r["pendientes"] or ["Nada pendiente."]
    txt = re.sub(r"(## Pendiente de revisión experta\n\n).*?(?=\n## )",
                 lambda m: m.group(1) + "\n".join(f"- {p}" for p in pend) + "\n", txt, flags=re.S)
    ficha.write_text(txt, encoding="utf-8")


def campo_ficha(carpeta, campo):
    ficha = carpeta / "ficha.md"
    if ficha.exists():
        m = re.search(rf"^\| {re.escape(campo)} \| (.*?) \|", ficha.read_text(encoding="utf-8"), re.M)
        if m and not m.group(1).startswith("<"):
            return m.group(1)
    return "—"


def actualizar_historial():
    filas = []
    for carpeta in sorted(EJEC_DIR.glob("E*-*")):
        f = carpeta / "metricas.json"
        if not f.exists():
            continue
        r = json.loads(f.read_text(encoding="utf-8"))
        b, h = r["borrador"], r["referencia"]
        filas.append([carpeta.name, campo_ficha(carpeta, "Fecha"), campo_ficha(carpeta, "Versión de la skill"),
                      r["rubrica"]] + [nota(r["final"][d]) for d in DIMENSIONES]
                     + [nota(r["media"]), ", ".join(r["bloqueantes"]) or "—",
                        f"{round(100 * b['palabras'] / h['palabras'])} %", f"{b['pd']} / {h['pd']}",
                        b["pendientes"], f"{r['anexo']['porcentaje']} %" if r["anexo"] else "—",
                        r["causas_b"]["S"], len(r["pendientes"])])
    cab = ["Ejecución", "Fecha", "Skill", "Rúbrica"] + DIMENSIONES + [
        "Media", "Bloq.", "Extensión", "PD IA/hum.", "[PEND.]", "Anexo I (cota sup.)", "Causas S", "Pend. revisión"]
    (EVALS / "historial.md").write_text(
        "# Historial de ejecuciones\n\nGenerado por `evaluacion.py medir`; no editar a mano.\n\n"
        + tabla_md(cab, filas) + "\n", encoding="utf-8")


def cmd_medir(args):
    carpeta = buscar_ejecucion(args.ejecucion)
    caso_id = carpeta.name.split("-", 1)[1]
    casos = leer_casos()
    if caso_id not in casos:
        error(f"el caso {caso_id} no está en casos.csv")
    borrador = carpeta / "borrador.docx"
    refs = list((CASOS_DIR / caso_id / "referencia").glob("autoinforme-humano.*"))
    if not borrador.exists() or not refs:
        error("faltan borrador.docx o la referencia del caso")
    txt_b, txt_h = texto_docx(borrador), texto(refs[0])
    a, b = leer_cotejo(carpeta / "cotejo-A.md"), leer_cotejo(carpeta / "cotejo-B.md")
    if b is None:
        print("AVISO: no hay cotejo-B.md; la nota final será la de A.")
    final, media, pend_dim = consolidar(a, b)
    rubrica = version_cotejo(carpeta / ("cotejo-B.md" if b else "cotejo-A.md"))
    if rubrica not in ("—", version_rubrica()):
        print(f"AVISO: el cotejo usa la rúbrica {rubrica} y la vigente es la {version_rubrica()}; "
              "vuelve a puntuar con B.")
    bloqueantes = sorted(set((a or {}).get("bloqueantes", [])) | set((b or {}).get("bloqueantes", [])))
    pendientes = pend_dim + [f"Bloqueante {x}" for x in bloqueantes]
    for c in (a, b):
        for p in (c or {}).get("pendientes", []):
            if p not in pendientes:
                pendientes.append(p)
    r = {
        "rubrica": rubrica,
        "borrador": metricas_documento(txt_b), "referencia": metricas_documento(txt_h),
        "anexo": coincidencia_anexo(valores_anexo(borrador), txt_h),
        "notas_a": (a or {}).get("notas", {}), "notas_b": (b or {}).get("notas", {}),
        "final": final, "media": media, "bloqueantes": bloqueantes,
        "causas_b": (b or a or {}).get("causas", {c: 0 for c in CAUSAS}),
        "lecciones": sorted(set((a or {}).get("lecciones", [])) | set((b or {}).get("lecciones", []))),
        "pendientes": pendientes, "huellas": huellas_en_skill(casos),
    }
    (carpeta / "metricas.json").write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
    actualizar_ficha(carpeta, r)
    actualizar_historial()
    print(bloque_resultado(r))
    print(f"\nActualizados {carpeta.name}/metricas.json, ficha.md y evals/historial.md")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="orden", required=True)
    n = sub.add_parser("nueva", help="crea la carpeta y la ficha de una ejecución")
    n.add_argument("id")
    n.add_argument("--modelo-a", default=MODELO_A)
    n.add_argument("--modelo-b", default=MODELO_B)
    n.set_defaults(func=cmd_nueva)
    m = sub.add_parser("medir", help="calcula métricas, consolida cotejos y actualiza el historial")
    m.add_argument("ejecucion", help="prefijo de la ejecución, p. ej. E04")
    m.set_defaults(func=cmd_medir)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
