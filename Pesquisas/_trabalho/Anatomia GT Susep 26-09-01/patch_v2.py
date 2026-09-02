# -*- coding: utf-8 -*-
"""v2: integra as abas Linear e Reuniões, fonte 27, masthead, Check e Destaque."""
import io, os
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
def rep(s, a, b):
    assert a in s, a[:80]; return s.replace(a, b, 1)

# build.py: abas, fragmentos, 27 fontes
b = load("build.py")
b = rep(b, '("blue", "Blueprint"), ("5w2h", "5W2H")', '("blue", "Blueprint"), ("linear", "Da estratégia à entrega"), ("reun", "Reuniões e fluxo"), ("5w2h", "5W2H")')
b = rep(b, 'for x in "ABCD")', 'for x in "ABCDE")')
b = rep(b, "26 fontes internas com data", "27 fontes internas com data")
b = rep(b, "n < 1 or n > 26)", "n < 1 or n > 27)")
b = rep(b, "set(range(1, 27))", "set(range(1, 28))")
b = rep(b, 'sem alçada, sem braço reservado e sem porta única para os desafios. Ramos Elementares cresce apesar disso. Vida trava por causa disso. O remédio já está escrito pelo próprio grupo; falta o desenho que o sustente.',
        'sem alçada, sem braço reservado e sem porta única para os desafios. Ramos Elementares cresce apesar disso. Vida trava por causa disso. O remédio já está escrito pelo próprio grupo; falta o desenho que o sustente. Este documento reúne o diagnóstico, o blueprint da estratégia à entrega e o rascunho das reuniões e do fluxo de informação.')
b = rep(b, "grid-template-columns:repeat(10,max-content)", "grid-template-columns:repeat(11,max-content)")
save("build.py", b)

# frag_D: fonte 27
d = load("frag_D.html")
d = rep(d, '<h3>Documento derivado (25)</h3>',
'''<h3>Reunião de 1º de setembro de 2026, modelo de squads (27)</h3>
<ol start="27">
<li>Transcrição automática da reunião "Modelo de Squads", com Camila Fernanda Silva Gomes, Fabíola Brandão, Ingrid Guaiato Campos Alves e Kelly Cristina Alonso Adolpho, 61 minutos. 1º de setembro de 2026. Fornecida pelo autor; guardada na pasta de trabalho deste documento. Usada apenas na aba Reuniões e fluxo. Grafias da transcrição mantidas entre aspas.</li>
</ol>
<h3>Documento derivado (25)</h3>''')
d = rep(d, "mais a transcrição de uma reunião de 1º de setembro, guardados no notebook",
        "mais as transcrições de duas reuniões de 1º de setembro, guardados no notebook")
d = rep(d, '<div class="card"><strong>Fórum de Negócio SUSEP.</strong> Rito proposto em setembro de 2026 como lugar de entrega das squads, reunindo o que hoje é Frente, S&amp;OP e Diagnóstico.</div>',
        '<div class="card"><strong>Fórum de Negócio SUSEP.</strong> Rito proposto em setembro de 2026 como lugar de entrega das squads, reunindo o que hoje é Frente, S&amp;OP e Diagnóstico; na descrição da Ingrid, em três camadas (diretores, superintendentes, squads).</div>\n<div class="card"><strong>Acelerador.</strong> Esteira de TI que recebe demandas já diagnosticadas; sem critério de despriorização definido.</div>\n<div class="card"><strong>Planning, review, daily e retrô.</strong> Os quatro ritos de uma squad: combinar o ciclo, mostrar o entregue, destravar o dia, aprender com o ciclo.</div>')
save("frag_D.html", d)

# frag_A: mapa dos orgaos
a = load("frag_A.html")
a = rep(a, '<div class="card"><strong>Modelo, Blueprint, 5W2H.</strong> O desenho proposto: tipos de demanda, pipeline da estratégia à entrega, governança, times, ritos e o plano para construir com o time.</div>',
        '<div class="card"><strong>Modelo, Blueprint, Da estratégia à entrega, Reuniões e fluxo, 5W2H.</strong> O desenho proposto: tipos de demanda, governança, times e ritos; o blueprint linear em oito etapas; o rascunho das reuniões e do fluxo mínimo de informação no formato do blueprint da Previdência; e o plano para construir com o time.</div>')
save("frag_A.html", a)

# frag_check: versao 2
c = load("frag_check.html")
c = rep(c, '<h3>Limitações honestas</h3>',
'''<h3>Versão 2: o que entrou depois do veredito</h3>
<p>Duas abas foram acrescentadas a pedido: "Da estratégia à entrega" (blueprint linear, todo marcado como proposta) e "Reuniões e fluxo" (rascunho no formato do blueprint da Previdência, com base na transcrição da reunião "Modelo de Squads", fonte 27). O ataque foi repetido sobre a versão inteira: abas casadas, travessão zero, sobrescritos dentro de 1 a 27, nenhuma fonte órfã, citações da fonte 27 conferidas contra o extrato literal. A aba Reuniões e fluxo carrega uma faixa de RASCUNHO porque nada nela foi validado com Ingrid, Caio, Dani ou Flávio; os cifrões de custo são impressão, não conta.</p>

<h3>Limitações honestas</h3>''')
save("frag_check.html", c)
print("patch v2 ok")
