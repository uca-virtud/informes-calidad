import sys, docx
from docx.oxml.ns import qn
d=docx.Document(sys.argv[1]); idx=[int(x) for x in sys.argv[2:]]
ps=[docx.text.paragraph.Paragraph(el,d) for el in d.element.body.iterchildren() if el.tag==qn('w:p')]
for i in idx:
    print(f"== P{i}")
    for r in ps[i].runs:
        c=r.font.color.rgb if r.font.color and r.font.color.type else None
        if r.text: print(f"  <{c}> {r.text!r}")
