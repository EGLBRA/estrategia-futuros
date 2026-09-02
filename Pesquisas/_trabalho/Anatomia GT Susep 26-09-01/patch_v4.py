# -*- coding: utf-8 -*-
"""v4: aba Perguntas de design."""
import io, os
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
def rep(s, a, b):
    assert a in s, a[:80]; return s.replace(a, b, 1)
b = load("build.py")
b = rep(b, '("modelo", "Modelo"),', '("modelo", "Modelo"), ("design", "Perguntas de design"),')
b = rep(b, 'for x in "ABCDE")', 'for x in "ABCDEF")')
b = rep(b, "grid-template-columns:repeat(11,max-content)", "grid-template-columns:repeat(12,max-content)")
save("build.py", b)
a = load("frag_A.html")
a = rep(a, '<div class="card"><strong>Modelo, Blueprint, Fluxo funcional, 5W2H.</strong>', '<div class="card"><strong>Modelo, Perguntas de design, Blueprint, Fluxo funcional, 5W2H.</strong>')
save("frag_A.html", a)
c = load("frag_check.html")
c = rep(c, 'Duas abas foram acrescentadas a pedido:', 'Três abas foram acrescentadas a pedido: "Perguntas de design" (a lente de design organizacional em perguntas e respostas, cada resposta com o sintoma ou a fala que a sustenta),')
save("frag_check.html", c)
print("patch v4 ok")
