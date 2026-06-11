#!/usr/bin/env python3
import os, sys, json, urllib.parse, urllib.request
def key(n):
    v=os.environ.get(n,"").strip()
    if not v and os.path.exists(".env"):
        for ln in open(".env",encoding="utf-8"):
            if ln.strip().startswith(n+"="): v=ln.split("=",1)[1].strip(); break
    return v
UA="Mozilla/5.0 (juris.py)"
def tce(q,tribunal=None,limit=10):
    p={"q":q,"limit":limit}
    if tribunal: p["tribunal"]=tribunal
    url="https://tce.leinamao.com.br/api/v1/decisions?"+urllib.parse.urlencode(p)
    req=urllib.request.Request(url,headers={"Authorization":f"Bearer {key('TCE_API_KEY')}","Accept":"application/json","User-Agent":UA})
    data=json.load(urllib.request.urlopen(req,timeout=45)).get("data",[])
    print(f"[TCE] {len(data)} resultado(s) para '{q}'")
    for it in data:
        tr=(it.get("tribunals") or {}).get("name","-")
        print(f"\n- {tr} | {it.get('type')} n.{it.get('number')}/{it.get('year')} | {it.get('session_date')} | Rel. {it.get('rapporteur') or '-'}")
        print(f"  Assunto: {it.get('subject')}")
        print(f"  Resumo (provedor, NAO literal): {(it.get('ai_summary') or '')[:500]}")
        if it.get('cited_laws'): print(f"  Leis: {', '.join(it['cited_laws'][:6])}")
        if it.get('source_url'): print(f"  Inteiro teor: {it['source_url']}")
def datajud(alias,assunto,size=10):
    url=f"https://api-publica.datajud.cnj.jus.br/api_publica_{alias}/_search"
    body={"size":int(size),"query":{"match_phrase":{"assuntos.nome":assunto}},"sort":[{"dataAjuizamento":{"order":"desc"}}]}
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Authorization":f"APIKey {key('DATAJUD_APIKEY')}","Content-Type":"application/json"})
    hits=json.load(urllib.request.urlopen(req,timeout=45)).get("hits",{}).get("hits",[])
    print(f"[DataJud/{alias}] {len(hits)} processo(s) - '{assunto}' (metadados; sem ementa)")
    for h in hits:
        s=h["_source"]; ass="; ".join(a.get("nome","") for a in s.get("assuntos",[]))
        print(f"\n- {s.get('numeroProcesso')} | {s.get('classe',{}).get('nome')} | {s.get('orgaoJulgador',{}).get('nome','')}")
        print(f"  assuntos: {ass[:160]} | ajuizado: {str(s.get('dataAjuizamento',''))[:8]}")
def teor(url):
    import re, fitz
    req=urllib.request.Request(url,headers={"User-Agent":UA})
    open("/tmp/_j.pdf","wb").write(urllib.request.urlopen(req,timeout=60).read())
    t="\n".join(p.get_text() for p in fitz.open("/tmp/_j.pdf"))
    m=re.search(r"EMENTA(.*?)(ACORDAO|ACÓRDÃO|RELAT[OÓ]RIO|Vistos)",re.sub(r"\s+"," ",t),re.S|re.I)
    print(m.group(1).strip() if m else t[:3000])
a=sys.argv[1:]
if not a: print("uso: tce '<termo>' [tribunal] [limit] | datajud <alias> '<assunto>' [size] | teor '<url>'")
elif a[0]=="tce": tce(a[1], a[2] if len(a)>2 and a[2] else None, int(a[3]) if len(a)>3 else 10)
elif a[0]=="datajud": datajud(a[1],a[2],a[3] if len(a)>3 else 10)
elif a[0]=="teor": teor(a[1])
