# -*- coding: utf-8 -*-
"""v23: menu com uma palavra por aba e remissões no texto ajustadas."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
b = load("build.py")
old = re.search(r"TABS = \[.*?\]\n", b, re.S)
new = '''TABS = [("dest", "Destaque"), ("exec", "Executiva"), ("problema", "Problema"), ("proposta", "Proposta"), ("omodelo", "Modelo"),
        ("alcadas", "Alçadas"), ("ritos", "Reuniões"), ("linear", "Caminho"), ("reun", "Fluxo"), ("design", "Desenho"),
        ("entenda", "Entenda"), ("eco", "Ecossistema"), ("proc", "Processos"), ("sint", "Sintomas"), ("estrutura", "Estrutura"),
        ("loops", "Loops"), ("analise", "Análise"), ("riscos", "Riscos"), ("cem", "Perguntas"), ("gloss", "Referências")]
'''
b = b.replace(old.group(0), new, 1)
b = b.replace(".tab{font-size:12.5px;text-align:center;padding:3px 0}", ".tab{font-size:13.5px;text-align:center;padding:3px 0}")
b = re.sub(r"\.gancho\{[^}]*\}", ".gancho{font-family:Georgia,serif;font-style:italic;font-size:14px;color:#666;margin:-10px 0 20px} .gancho::before{content:'► ';color:#b71c1c;font-style:normal;font-size:10px;vertical-align:1px}", b, count=1)
save("build.py", b)
REF = [("abas Estratégia a entrega e Fluxo funcional", "abas Caminho e Fluxo"), ("aba Estratégia a entrega", "aba Caminho"), ("aba Reuniões e custo", "aba Reuniões"), ("aba Fluxo funcional", "aba Fluxo"),
       ("aba Desenho e regras", "aba Desenho"), ("aba Problema e entregas", "aba Problema"), ("abas O modelo e Problema e entregas", "abas Modelo e Problema"), ("abas O modelo e Estratégia a entrega", "abas Modelo e Caminho"),
       ("aba O modelo", "aba Modelo"), ("abas O modelo", "abas Modelo"), ("aba Cem perguntas", "aba Perguntas"), ("aba Riscos e tensões", "aba Riscos"), ("aba Glossário e fontes", "aba Referências"), ("aba Fontes", "aba Referências"), ("aba Glossário", "aba Referências"),
       ("abas Alçadas e O modelo", "abas Alçadas e Modelo"), ("abas Estrutura e Proposta", "abas Estrutura e Proposta"), ("(aba Reuniões e custo)", "(aba Reuniões)")]
for fn in [f"frag_{k}.html" for k in "ABCDEFGHIJKL"] + ["pratica.py", "build.py"]:
    try: s = load(fn)
    except FileNotFoundError: continue
    for a, c in REF: s = s.replace(a, c)
    s = s.replace("<h2>Riscos e tensões:", "<h2>Riscos:")
    save(fn, s)
print("patch v23 ok")
