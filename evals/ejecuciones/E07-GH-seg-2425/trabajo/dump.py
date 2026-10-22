import sys, docx
from docx.oxml.ns import qn
d=docx.Document(sys.argv[1])
body=d.element.body
pi=ti=0
for el in body.iterchildren():
    if el.tag==qn('w:p'):
        p=docx.text.paragraph.Paragraph(el,d)
        cols=set()
        for r in p.runs:
            c=r.font.color.rgb if r.font.color and r.font.color.type else None
            if r.text.strip(): cols.add(str(c))
        t=p.text.strip()
        if t: print(f"P{pi} [{','.join(sorted(cols))}] {p.style.name}: {t[:110]}")
        pi+=1
    elif el.tag==qn('w:tbl'):
        print(f"--- T{ti}"); ti+=1
