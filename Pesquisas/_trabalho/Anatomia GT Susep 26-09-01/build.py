# -*- coding: utf-8 -*-
"""Monta a Anatomia Profunda do GT Susep Vida e RE clonando a casca do exemplar de 26-08-30."""
import io, re, os, sys

WORK = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
OUTDIR = r"A:\_01 Projetos\Estrategia\Pesquisas\Anatomia Profunda - GT Susep Vida e RE - 26-09-01"
NAME = "Anatomia Profunda - GT Susep Vida e RE - 26-09-01"
EXEMPLAR = r"A:\_01 Projetos\Estrategia\Pesquisas\Anatomia Profunda - Clinicas de Terapia Infantil e Psicologia - Extrema MG - 26-08-30\Anatomia Profunda - Clinicas de Terapia Infantil e Psicologia - Extrema MG - 26-08-30.html"
os.makedirs(OUTDIR, exist_ok=True)

TABS = [("dest", "Destaque"), ("exec", "Executiva"), ("problema", "Problema"), ("proposta", "Proposta"), ("omodelo", "Modelo"),
        ("alcadas", "Alçadas"), ("ritos", "Reuniões"), ("linear", "Caminho"), ("reun", "Fluxo"), ("design", "Desenho"),
        ("entenda", "Entenda"), ("eco", "Ecossistema"), ("proc", "Processos"), ("sint", "Sintomas"), ("estrutura", "Estrutura"),
        ("loops", "Laços"), ("analise", "Análise"), ("riscos", "Riscos"), ("cem", "Perguntas"), ("gloss", "Referências")]
MERGE = {"estrutura": ["normas", "papeis", "sist"], "analise": ["analise", "sut"], "gloss": ["gloss", "fontes"]}

ex = io.open(EXEMPLAR, encoding="utf-8").read()
head = ex.split("<body>")[0]
# titulo
head = re.sub(r"<title>.*?</title>", "<title>A frente que entrega mais do que consegue decidir</title>", head, flags=re.S)
# seletores CSS das abas: substituir os dois blocos
ids = [t[0] for t in TABS]
sel1 = ",".join(f"#r-{i}:checked~#p-{i}" for i in ids) + "{display:block}"
sel2 = ",".join(f"#r-{i}:checked~.tabs [for=r-{i}]" for i in ids) + "{color:#1a1a1a;border-bottom-color:#b71c1c;font-weight:700}"
head = re.sub(r"#r-dest:checked~#p-dest[^\n]*\{display:block\}", sel1, head)
head = re.sub(r"#r-dest:checked~\.tabs \[for=r-dest\][^\n]*\{color:#1a1a1a;border-bottom-color:#b71c1c;font-weight:700\}", sel2, head)
# grid de abas: 10 colunas (20 abas em 2 linhas)
head = head.replace("grid-template-columns:repeat(12,max-content)", "grid-template-columns:repeat(11,max-content)")
head = head.replace("</style>", ".sel-p{background:#e8f0fe;color:#1a4a8a} .news{border:1px solid #e3e3e3;border-radius:8px;padding:12px 18px;margin:10px 0;background:#fff} .news .nt{margin:0 0 6px;font-size:15.5px} .news p{margin:6px 0} .badge{display:inline-block;color:#fff;font-family:system-ui,sans-serif;font-size:11px;font-weight:700;padding:2px 8px;border-radius:10px;margin-left:8px;vertical-align:2px} .meta{float:right;font-family:system-ui,sans-serif;font-size:11.5px;color:#777} .news .q{border-left:3px solid #ddd;padding-left:12px;font-style:italic;color:#555;font-size:13.5px} .gancho{font-family:Georgia,serif;font-style:italic;font-size:14px;color:#666;margin:-10px 0 20px} .gancho::before{content:'► ';color:#b71c1c;font-style:normal;font-size:10px;vertical-align:1px} .tabs{grid-template-columns:repeat(10,1fr);column-gap:8px;row-gap:6px;justify-content:stretch} .tab{font-size:13.5px;text-align:center;padding:3px 0} @media (max-width:1000px){.tabs{grid-template-columns:repeat(5,1fr)}} table{font-size:12.5px}th,td{padding:6px 8px} .g2 .card{font-size:13.5px} ol li,ul li{margin-bottom:5px} </style>", 1)
assert sel1 in head and sel2 in head, "seletores nao substituidos"

radios = "\n".join(f'<input class="tabr" type="radio" name="tab" id="r-{i}"{" checked" if k == 0 else ""}>' for k, i in enumerate(ids))
labels = "\n".join(f'  <label class="tab" for="r-{i}">{n}</label>' for i, n in TABS)

masthead = f'''<body>
<div class="W">

{radios}

<p class="lbl">Diagnóstico Rápido &middot; Seguros Unimed &middot; GT Evoluir Modelo de Negócio SUSEP Vida e RE &middot; 2026-09-01 &middot; Uso interno &middot; Material sensível</p>
<h1>A frente que entrega mais do que consegue decidir</h1>
<p class="tese">A frente que carrega a meta de crescer 20% na SUSEP opera há um ano e meio sem alçada própria, sem braço reservado e sem um único lugar por onde os desafios entram e saem. Ramos Elementares cresce apesar do desenho; Vida espera por causa dele.</p>
<p class="gancho">O que faz Ramos Elementares avançar, e o que falta para Vida avançar do mesmo jeito?</p>
<p class="note" style="margin:6px 0 14px">Diagnóstico rápido, feito a partir das atas e das reuniões de 1º de setembro de 2026. Precisa ser validado pelas partes envolvidas antes de orientar qualquer decisão.</p>

<nav class="tabs">
{labels}
</nav>

'''

frags = "".join(io.open(os.path.join(WORK, f"frag_{x}.html"), encoding="utf-8").read() + "\n" for x in "ABCDEFGHIJKL")
check_path = os.path.join(WORK, "frag_check.html")
check = io.open(check_path, encoding="utf-8").read() if os.path.exists(check_path) else '''<!-- ============================== CHECK ============================== -->
<section id="p-check" class="pane">
<h2>O veredito do advogado à vista</h2>
<p class="note">Em elaboração: esta aba recebe o resultado do ataque adversarial antes da entrega.</p>
</section>
'''
# ordem dos paineis segue a ordem das abas
panels = {}
for m in re.finditer(r'<!-- =+ [A-Z0-9 ]+ =+ -->\s*<section id="p-([a-z0-9]+)" class="pane">.*?</section>', frags + check, re.S):
    panels[m.group(1)] = m.group(0)
for tgt, parts in MERGE.items():
    inner = []
    for j, p in enumerate(parts):
        body = re.sub(r'^<!-- =+ [A-Z0-9 ]+ =+ -->\s*<section id="p-[a-z0-9]+" class="pane">', '', panels[p].strip())
        body = re.sub(r'</section>\s*$', '', body)
        if j < len(parts) - 1:
            body = re.sub(r'<div class="pratica">.*?</div>\s*(?=$)', '', body, flags=re.S)
        if j > 0:
            body = body.replace('<h2>', '<h3>').replace('</h2>', '</h3>').replace('<p class="tese">', '<p>')
        elif tgt == 'estrutura':
            body = re.sub(r'<h2>(.*?)</h2>\s*(<p class="tese">.*?</p>)(\s*<p class="gancho">.*?</p>)?', r'<h2>Estrutura: boas regras de convivência, quase nenhuma regra de decisão</h2>' + chr(10) + r'\2\3' + chr(10) + r'<h3>\1</h3>', body, count=1, flags=re.S)
        inner.append(body)
    panels[tgt] = '<!-- ============================== %s ============================== -->\n<section id="p-%s" class="pane">\n' % (tgt.upper(), tgt) + "\n<hr style=\"border:0;border-top:1px solid #e0e0e0;margin:28px 0\">\n".join(inner) + '\n</section>'
missing = [i for i in ids if i not in panels]
assert not missing, f"paineis faltando: {missing}"
body = "\n\n".join(panels[i] for i in ids)

footer = '''

</div>
<div class="W"><p class="lbl" style="margin:40px 0 24px;border-top:1px solid #e5e5e5;padding-top:12px;font-size:11px;font-weight:400;color:#9a9a9a;letter-spacing:.3px;line-height:1.7">GT Evoluir Modelo de Negócio SUSEP Vida e RE, Seguros Unimed &middot; Diagnóstico de 1º de setembro de 2026 &middot; Uso interno<br>Material sensível: não circular fora da área de Estratégia &middot; Diagnóstico rápido, a validar pelas partes envolvidas</p></div>
</body>
</html>
'''
html = head + masthead + body + footer
out_html = os.path.join(OUTDIR, NAME + ".html")
io.open(out_html, "w", encoding="utf-8", newline="\n").write(html)

# ---------------- QA de forma
def qa(html):
    rep = {}
    rep["radios"] = len(re.findall(r'<input class="tabr" type="radio"', html))
    rep["labels"] = len(re.findall(r'<label class="tab" for="r-', html))
    rep["panes"] = len(re.findall(r'<section id="p-[a-z0-9]+" class="pane">', html))
    rep["travessao"] = html.count("\u2014"); rep["en_dash"] = html.count("\u2013")
    rep["setas"] = len(re.findall(r"→|⇒|=>", html)) + len(re.findall(r"(?<!-)->", html.replace("-->", "")))
    body_txt = html.split("<body>")[1]
    sups = re.findall(r"<sup>([^<]*)</sup>", body_txt)
    nums = set()
    bad = []
    for s in sups:
        for tok in s.split(","):
            tok = tok.strip()
            if not tok.isdigit(): bad.append(s); continue
            nums.add(int(tok))
    rep["sup_invalidos"] = bad
    rep["sup_fora_1_25"] = sorted(n for n in nums if n < 1 or n > 27)
    rep["fontes_orfas"] = sorted(set(range(1, 28)) - nums)
    forb = re.findall(r"HackMarket|Hack ?News|Panorama Mercado|\bFATO\b|HIPÓTESE|\[E\]|\[I\]|\[S\]", body_txt)
    rep["marcas_proibidas"] = forb
    proc = re.findall(r"\bagente\b|\bmodelo de linguagem\b|\bprompt\b", body_txt, re.I)
    rep["mencoes_processo"] = proc
    rep["bytes"] = len(html.encode("utf-8"))
    return rep
r = qa(html)
for k, v in r.items(): print(f"{k}: {v}")
ok = r["radios"] == r["labels"] == r["panes"] == len(TABS) and r["travessao"] == 0 and r["en_dash"] == 0 and r["setas"] == 0 and not r["sup_invalidos"] and not r["sup_fora_1_25"] and not r["fontes_orfas"] and not r["marcas_proibidas"] and not r["mencoes_processo"]
print("QA FORMA:", "OK" if ok else "FALHOU")

# ---------------- espelho .md (conversor adaptado a esta casca)
from html.parser import HTMLParser
nav = re.search(r'<nav class="tabs">(.*?)</nav>', html, re.S).group(1)
order = re.findall(r'<label class="tab" for="r-([a-z0-9]+)">', nav)
pan = {m.group(1): m.group(2) for m in re.finditer(r'<section id="p-([a-z0-9]+)" class="pane">(.*?)</section>', html, re.S)}
SEL = {'sel-v': '[Verificado]', 'sel-i': '[Inferência]', 'sel-e': '[Especulativo]', 'sel-p': '[Proposta]'}
class Conv(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.md=[]; self.cur=[]; self.cell=None; self.rows=None; self.row=None
        self.list_stack=[]; self.ol=[]; self.divkind=[]; self.item_active=0; self.spanstack=[]; self.skip=0
    def w(self,s): (self.cell if self.cell is not None else self.cur).append(s)
    def flush(self):
        t=''.join(self.cur).strip(); t=re.sub(r'[ \t]+',' ',t).replace('\xa0',' ').strip()
        if t: self.md.append(t)
        self.cur=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); cls=a.get('class','')
        if tag in ('h2','h3','h4'): self.flush()
        elif tag=='p':
            if self.item_active: self.w(' ')
            else: self.flush()
        elif tag in ('ul','ol'):
            self.flush(); self.list_stack.append(tag)
            if tag=='ol': self.ol.append(int(a.get('start','1'))-1)
        elif tag=='li': self.flush()
        elif tag=='table': self.flush(); self.rows=[]
        elif tag=='tr': self.row=[]
        elif tag in ('td','th'): self.cell=[]
        elif tag=='div':
            if cls in ('kpi','card','accent'): self.flush(); self.divkind.append('item'); self.item_active+=1
            elif cls in ('apex','tl-item'): self.flush(); self.divkind.append('block'); self.item_active+=1
            else: self.divkind.append('container')
        elif tag=='span':
            if cls.startswith('sel'):
                k=cls.split()[-1]; self.w(' '+SEL.get(k,'')+' '); self.spanstack.append(True); self.skip+=1
            elif cls=='num': self.w('**'); self.spanstack.append('num')
            else: self.spanstack.append(False)
        elif tag in ('strong','b'): self.w('**')
        elif tag=='small': self.w(' ')
        elif tag=='br': self.w(' ')
        elif tag=='sup': self.w(' [')
        elif tag=='svg': self.skip+=1
    def handle_endtag(self,tag):
        if tag=='svg': self.skip-=1; return
        if tag in ('h2','h3','h4'):
            t=re.sub(r'[ \t]+',' ',''.join(self.cur)).replace('\xa0',' ').strip()
            pre={'h2':'## ','h3':'### ','h4':'#### '}[tag]
            if t: self.md.append('\n'+pre+t)
            self.cur=[]
        elif tag=='p':
            if self.item_active: self.w(' ')
            else: self.flush()
        elif tag=='li':
            t=re.sub(r'[ \t]+',' ',''.join(self.cur)).replace('\xa0',' ').strip()
            if t:
                if self.list_stack and self.list_stack[-1]=='ol':
                    self.ol[-1]+=1; self.md.append('%d. %s'%(self.ol[-1],t))
                else: self.md.append('- '+t)
            self.cur=[]
        elif tag in ('ul','ol'):
            if self.list_stack: self.list_stack.pop()
            if tag=='ol' and self.ol: self.ol.pop()
        elif tag in ('td','th'):
            c=re.sub(r'[ \t]+',' ',''.join(self.cell)).replace('\xa0',' ').replace('|','/').strip(); self.row.append(c); self.cell=None
        elif tag=='tr':
            if self.row is not None: self.rows.append(self.row); self.row=None
        elif tag=='table': self.emit_table(); self.rows=None
        elif tag=='div':
            if self.divkind:
                kind=self.divkind.pop()
                if kind in ('item','block'):
                    t=re.sub(r'[ \t]+',' ',''.join(self.cur)).replace('\xa0',' ').strip()
                    if t: self.md.append(('- ' if kind=='item' else '> ')+t)
                    self.cur=[]; self.item_active-=1
        elif tag=='span':
            if self.spanstack:
                v=self.spanstack.pop()
                if v is True: self.skip-=1
                elif v=='num': self.w('**')
        elif tag in ('strong','b'): self.w('**')
        elif tag=='sup': self.w(']')
    def handle_data(self,data):
        if self.skip>0: return
        self.w(data)
    def emit_table(self):
        rows=self.rows
        if not rows: return
        self.md.append(''); self.md.append('| '+' | '.join(rows[0])+' |'); self.md.append('|'+'|'.join(['---']*len(rows[0]))+'|')
        for r in rows[1:]:
            while len(r)<len(rows[0]): r.append('')
            self.md.append('| '+' | '.join(r)+' |')
        self.md.append('')
title = re.search(r'<h1>(.*?)</h1>', html, re.S).group(1).strip()
tese = re.sub(r'<.*?>','', re.search(r'<p class="tese">(.*?)</p>', html, re.S).group(1)).strip()
doc=['# '+title, '### '+tese, '', 'Documento espelho do HTML (A Anatomia Profunda). Selos [Verificado] / [Inferência] / [Especulativo] em cada afirmação. Citações entre colchetes apontam para a lista única de Fontes. Sem travessão.', '']
for tid in order:
    if tid not in pan: continue
    c=Conv(); c.feed(pan[tid]); doc.append(''); doc.append('---'); doc.extend(c.md)
text='\n'.join(doc); text=re.sub(r'\n{3,}','\n\n',text)
out_md=os.path.join(OUTDIR, NAME + ".md")
io.open(out_md,'w',encoding='utf-8',newline='').write(text)
print("MD bytes:", len(text.encode('utf-8')), "| travessao md:", text.count('\u2014'), "| [Verificado] Verificado dup:", text.count('[Verificado] Verificado'))
print("OK", out_html)
