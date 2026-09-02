# -*- coding: utf-8 -*-
"""v27: aviso de que prazos, dias e cadências são especulativos e propostas para discutir, nas abas de desenho."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'
AV = '<div class="alerta"><strong>PRAZOS, DIAS E CADÊNCIAS SÃO ESPECULATIVOS.</strong> Todo tempo citado nesta aba (dias úteis, semanas, ciclos, durações de reunião, leituras em 30 e 90 dias) é ponto de partida para discutir com o grupo e com os mentores, não compromisso. O que valer é o que sair dos encontros. ' + SP + '</div>\n'
targets = {"G": ["exec", "linear"], "H": ["proposta", "ritos"], "I": ["omodelo"], "J": ["alcadas"], "K": ["problema"], "E": ["reun"]}
done = []
for k, pids in targets.items():
    s = load(f"frag_{k}.html")
    for pid in pids:
        m = re.search(r'(<section id="p-%s" class="pane">.*?<p class="gancho">.*?</p>\n)' % pid, s, re.S)
        if m and "PRAZOS, DIAS E CADÊNCIAS" not in m.group(1):
            s = s.replace(m.group(1), m.group(1) + AV, 1); done.append(pid)
    save(f"frag_{k}.html", s)
d = load("frag_D.html")
if "Prazos, dias e cadências" not in d:
    d = d.replace("Desenho proposto para validação nos encontros com o time; não é afirmação sobre a realidade.", "Desenho proposto para validação nos encontros com o time; não é afirmação sobre a realidade. Prazos, dias e cadências citados nas abas de desenho são especulativos: propostas para discutir, não compromissos.", 1)
    save("frag_D.html", d)
print("patch v27 ok; abas:", done)
