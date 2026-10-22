import sys, docx
from docx.oxml.ns import qn
d=docx.Document(sys.argv[1])
pi=0
for el in d.element.body.iterchildren():
    if el.tag==qn('w:p'):
        for h in el.iter(qn('w:hyperlink')):
            rid=h.get(qn('r:id')); t=''.join(x.text or '' for x in h.iter(qn('w:t')))
            tgt=d.part.rels[rid].target_ref if rid else h.get(qn('w:anchor'))
            print(f"P{pi}: {t!r} -> {tgt}")
        pi+=1
