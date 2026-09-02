# -*- coding: utf-8 -*-
"""v13b: manchete do cabeçalho como síntese do contexto (não apresentação do documento), h2 de cada aba como síntese,
'O que muda para cada ator'."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
F = {k: load(f"frag_{k}.html") for k in "ABCDEFGHIJK"}
MISS = []
def RA(old, new, rx=False):
    n = 0
    for k in F:
        if rx: F[k], m = re.subn(old, new, F[k], flags=re.S)
        else: m = F[k].count(old); F[k] = F[k].replace(old, new)
        n += m
    if n == 0: MISS.append(("*", old[:70]))

# manchete do cabeçalho
b = load("build.py")
b2, n = re.subn(r'(<p class="tese">)Setenta e dois sintomas em 24 documentos mostram.*?exemplos de partida\.(</p>)',
    r'\1A frente que carrega a meta de crescer 20% na SUSEP opera há um ano e meio sem alçada própria, sem braço reservado e sem um único lugar por onde os desafios entram e saem. Ramos Elementares cresce apesar do desenho; Vida trava por causa dele.\2\n<p class="gancho">Por que as mesmas pessoas que fazem Ramos Elementares crescer não conseguem destravar Vida?</p>', b, count=1, flags=re.S)
if n == 0: MISS.append(("build", "manchete"))
save("build.py", b2)

# Destaque: síntese própria, sem repetir a manchete
RA('<p class="tese">A frente SUSEP entrega mais do que consegue decidir: um ano e meio de trabalho sem alçada própria, sem braço reservado e sem uma porta única por onde os desafios entram e saem.</p>\n<p class="gancho">Por que as mesmas pessoas que fazem Ramos Elementares crescer não conseguem destravar Vida?</p>',
   '<p class="tese">A mesma frente, as mesmas pessoas, resultados opostos: Ramos Elementares fecha em 115% da meta e Vida em 99%, porque em RE o grupo controla preço e cotador e em Vida a aceitação está fora do seu alcance.</p>\n<p class="gancho">O que muda entre uma esteira e outra, se não são as pessoas?</p>')

# h2 de cada aba como síntese do contexto
H2 = [
 ("<h2>Visão executiva: o diagnóstico e a proposta em uma página</h2>", "<h2>Visão executiva: o que trava vem antes da execução</h2>"),
 ("<h2>Problema e entregas: o que a proposta resolve e o que ela deixa nas mãos do time</h2>", "<h2>Problema e entregas: falta um sistema que leve o problema da ponta à decisão com alçada</h2>"),
 ("<h2>Alçadas: quem decide o quê, quem é consultado, para onde sobe e em quanto tempo</h2>", "<h2>Alçadas: hoje toda decisão relevante sobe</h2>"),
 ("<h2>Da estratégia à entrega: o caminho de um desafio, etapa por etapa", "<h2>Da estratégia à entrega: oito etapas e uma volta ao planejamento"),
 ("<h2>Fluxo funcional: quem alimenta quem, da origem do problema à solução entregue", "<h2>Fluxo funcional: cinco origens, uma porta, cinco destinos"),
 ("<h2>Desenho e regras: as perguntas de desenho organizacional, uma a uma</h2>", "<h2>Desenho e regras: é um problema de desenho, não de pessoas</h2>"),
 ("<h2>Entenda: o que é a frente e como ela deveria funcionar</h2>", "<h2>Entenda: uma frente desenhada com papéis e sem caminho de informação</h2>"),
 ("<h2>Ecossistema: quem está em volta do grupo e o que cada um faz com ele</h2>", "<h2>Ecossistema: um núcleo que depende de treze atores e não comanda nenhum</h2>"),
 ("<h2>Processos: como um desafio entra, cresce e sai</h2>", "<h2>Processos: oito portas de entrada e nenhuma saída registrada</h2>"),
 ("<h2>Estrutura: normas, papéis e sistemas</h2>", "<h2>Estrutura: boas regras de convivência, quase nenhuma regra de decisão</h2>"),
 ("<h2>Análise: riscos, SWOT e três cenários</h2>", "<h2>Análise: o maior risco é o desenho continuar igual</h2>"),
 ("<h3>O que muda para cada leitor</h3>", "<h3>O que muda para cada ator</h3>"),
]
for a, c in H2: RA(a, c)
for k, s in F.items(): save(f"frag_{k}.html", s)
b = load("build.py")
b2 = b.replace("<h2>Estrutura: normas, papéis e sistemas</h2>", "<h2>Estrutura: boas regras de convivência, quase nenhuma regra de decisão</h2>")
if b2 == b: MISS.append(("build", "h2 estrutura"))
save("build.py", b2)
print("patch v13b ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
