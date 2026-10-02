#!/usr/bin/env python3
"""Depura el texto de instrucciones de la plantilla del autoinforme.

Elimina los párrafos que son instrucciones de cumplimentación o directrices, para dejar
un único documento limpio tras redactar el análisis. Criterios de borrado:
  - Párrafos cuyo texto va en ROJO (instrucciones) o AZUL (directrices ACCUA), según el
    convenio de colores de la plantilla.
  - Párrafos entre corchetes "[ ... ]" (instrucciones) o con marcadores "XXXX"/"xxxx".
Conserva el texto en negro (recomendaciones ya reescritas y análisis) y las tablas.

Uso:
  python depurar_instrucciones.py --entrada relleno.docx --salida final.docx
"""
import argparse
import re
import sys

try:
    import docx
except ImportError:
    sys.exit("Falta python-docx: pip install python-docx --break-system-packages")

XXXX = re.compile(r"[Xx]{3,}")


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


def is_instruction(p):
    t = p.text.strip()
    if not t:
        return False
    if t.startswith("[") or XXXX.search(t):
        return True
    runs = [r for r in p.runs if r.text.strip()]
    if not runs:
        return False
    colored = 0
    for r in runs:
        rgb = _rgb(r)
        if rgb and (_is_reddish(rgb) or _is_bluish(rgb)):
            colored += 1
    # todo el texto del párrafo va en rojo/azul -> es instrucción/directriz
    return colored == len(runs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--salida", required=True)
    args = ap.parse_args()
    d = docx.Document(args.entrada)
    removed = 0
    for p in list(d.paragraphs):
        if is_instruction(p):
            p._element.getparent().remove(p._element)
            removed += 1
    d.save(args.salida)
    print(f"OK: {args.salida} | párrafos de instrucciones eliminados: {removed}")


if __name__ == "__main__":
    main()
