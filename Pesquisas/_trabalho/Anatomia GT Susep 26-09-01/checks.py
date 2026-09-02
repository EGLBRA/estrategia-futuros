# -*- coding: utf-8 -*-
"""Checker de qualidade: nota 0 a 10 por aba, um ponto por critério. Uso: python checks.py [--json]"""
import io, re, sys, json, unicodedata
HTML = r"A:\_01 Projetos\Estrategia\Pesquisas\Anatomia Profunda - GT Susep Vida e RE - 26-09-01\Anatomia Profunda - GT Susep Vida e RE - 26-09-01.html"
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
CORPUS = r"C:\Users\Dell\AppData\Local\Temp\claude\A---01-Projetos-Estrategia\b9f658da-eddc-4edb-8510-0f6c05555c40\scratchpad\nb\corpus.md"
def norm(t):
    t = unicodedata.normalize("NFKC", t).casefold(); t = re.sub(r"\s+", " ", t); return t.strip(" .;:,")
corpus = norm(io.open(CORPUS, encoding="utf-8").read() + " " + io.open(W + r"\fonte_26_transcricao_2026-09-01.md", encoding="utf-8").read() + " " + io.open(W + r"\fonte_27_transcricao_modelo_squads_ingrid_2026-09-01.md", encoding="utf-8").read())
html = io.open(HTML, encoding="utf-8").read()
nav = re.findall(r'<label class="tab" for="r-([a-z0-9]+)">', html)
panels = {m.group(1): m.group(2) for m in re.finditer(r'<section id="p-([a-z0-9]+)" class="pane">(.*?)</section>', html, re.S)}
PROPOSAL = {"exec", "problema", "proposta", "omodelo", "alcadas", "ritos", "linear", "reun", "design"}
NOPRAT = {"cem", "gloss"}
JARG = re.compile(r"\b(discovery|squad|squads|BAU|assessment|backlog|checklist|kick-off|churn|cross-sell|front-end|lead time|onboarding|scrum|feedback|roadmap|review|daily|sprint)\b", re.I)
NAMES = re.compile(r"\b(Camila|Ingrid|Flávio|Kelly)\b")
SKIP_Q = ("http", "Sintomas Organizacionais", "Estratégia e Operações", "Sugestão de metodologia", "Modelo de Squads", "não fazer", "muda o ponteiro", "pedir para a TI", "os que mais custam", "por onde isso entrou", "estacionado com data", "115% e 99%", "36% dos corretores", "5 anos de defasagem", "fase de entrega", "resultado de vendas")
PT = [r"\b(\w{3,})\s+\1\b", r"\b[aA] a\b", r"\bde de\b", r"\bum um\b", r"\bque que\b", r"\besse esse\b", r"\bà (os|as)\b", r"\bparaas\b", r"\btá\b", r"\bnum (a|as)\b", r"\.\.", r",,"]
results = {}
for pid in nav:
    body = panels[pid]; txt = re.sub(r"<[^>]+>", " · ", body)
    noq = '"'.join(p for i, p in enumerate(txt.split('"')) if i % 2 == 0)
    crit = {}
    crit["tese"] = ('<p class="tese">' in body) or pid in NOPRAT
    h = re.findall(r"<(h[2-4])", body)
    crit["hierarquia"] = h and h[0] == "h2" and not re.search(r"<(ul|ol)>[^<]*<li>[^<]*<(ul|ol)>", body)
    crit["tabelas"] = all(len(re.findall(r"<th>", t)) <= 7 for t in re.findall(r"<thead>.*?</thead>", body, re.S))
    crit["nomes"] = not NAMES.search(txt) if pid != "fontes" else True
    crit["jargao"] = not JARG.search(noq) if pid != "gloss" else True
    bad = []
    for q in re.findall(r'"([A-Za-zÀ-ú][^"\n]{17,220})"', txt):
        if any(k in q for k in SKIP_Q): continue
        parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", q) if p.strip()]
        if not all(norm(p) in corpus for p in parts): bad.append(q)
    crit["citacoes"] = not bad
    sel_ok = not (pid in PROPOSAL and pid not in ("alcadas", "ritos", "design") and ("sel-i" in body or "sel-e" in body))
    resto = re.search(r'<span class="sel sel-[vipe]">[^<]+</span>\s*[.;]|\bé\s+<span class="sel sel-[vipe]">|Proposta Proposta|Verificado Verificado', body)
    crit["selos"] = sel_ok and not resto
    pt = [p for p in PT if re.search(p, noq)]
    crit["portugues"] = not pt
    n_prat = body.count('class="pratica"')
    crit["pratica"] = (n_prat == 1) if pid not in NOPRAT else (n_prat == 0)
    paras = [len(p.split()) for p in re.findall(r"<p(?:\s[^>]*)?>(.*?)</p>", body, re.S)]
    crit["paragrafos"] = (max(paras) <= 150) if paras else True
    nota = sum(1 for v in crit.values() if v)
    results[pid] = {"nota": nota, "falhas": [k for k, v in crit.items() if not v], "citacoes_ruins": bad[:5], "pt": pt, "max_par": max(paras) if paras else 0}
if "--json" in sys.argv:
    print(json.dumps(results, ensure_ascii=False, indent=1))
else:
    for pid in nav:
        r = results[pid]
        print(f"{pid:10s} {r['nota']:2d}/10  {', '.join(r['falhas']) or 'ok'}" + (f"  | cit: {r['citacoes_ruins']}" if r['citacoes_ruins'] else "") + (f"  | pt: {r['pt']}" if r['pt'] else ""))
    print("abas:", len(nav), "| media:", round(sum(r["nota"] for r in results.values()) / len(results), 2), "| abaixo de 9:", [p for p in nav if results[p]["nota"] < 9])
