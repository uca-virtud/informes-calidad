import json,sys,shutil
src=sys.argv[1]; name=sys.argv[2]
s=open(src).read(); d,_=json.JSONDecoder().raw_decode(s)
json.dump(d,open('lince_'+name+'.json','w'),ensure_ascii=False)
print(d['columns'], d.get('totalRows'), d.get('hasMore'))
cur=None
keys=[k.lower() for k in sys.argv[3:]] or ['historia','facultad','uca']
for r in d['rows']:
    if r[1]: cur=r[1]
    if cur and any(k in cur.lower() for k in keys):
        print(cur[:25],'|',' | '.join(x for x in r[2:] if x is not None))
