import sys, docx
d=docx.Document(sys.argv[1])
for i in [int(x) for x in sys.argv[2:]]:
    t=d.tables[i]; print(f"=== T{i} {len(t.rows)}x{len(t.columns)}")
    for r in t.rows:
        seen=[];
        for c in r.cells:
            if not seen or c._tc is not seen[-1][0]: seen.append((c._tc,c.text.strip().replace('\n',' / ')[:40]))
        print(" | ".join(x[1] for x in seen))
