# -*- coding: utf-8 -*-
"""v14: restos do v13 (card do KR na Executiva, 'única folha', tese da Estrutura), últimos 'sessão', O modelo como visão atual."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
F = {k: load(f"frag_{k}.html") for k in "ABCDEFGHIJK"}
MISS = []
def R(k, old, new, rx=False, count=0):
    s = F[k]
    if rx: s2, n = re.subn(old, new, s, count=count, flags=re.S)
    else: n = s.count(old); s2 = s.replace(old, new) if n else s
    if n == 0: MISS.append((k, old[:70]))
    F[k] = s2
SV = '<span class="sel sel-v">Verificado</span>'; SP = '<span class="sel sel-p">Proposta</span>'

# Executiva: card do número do KR e "Na prática" sem explicar o artefato
R("G", r'(<li><strong>Vida perde na porta, não no preço\.</strong>.*?</li>)', r'\1\n<li><strong>O número não tem dono.</strong> A meta de 20% é mantida como acordo com mentores, o grupo trabalha com o número da Controladoria, ninguém sabe o fechamento de 2024, e nenhuma ata diz de onde vem o número do KR nem se o OKR foi construído com o grupo ou comunicado a ele.<sup>3, 6, 20, 24</sup> ' + SV + '</li>', rx=True, count=1)
R("G", "Se a Estratégia levar uma única folha para a diretoria, é esta. A frase de abertura: a frente SUSEP entrega mais do que consegue decidir.", "O diagnóstico cabe em uma frase: a frente SUSEP entrega mais do que consegue decidir.")
R("G", "O pedido: três decisões que só a diretoria pode tomar", "O que ele envolve: três decisões que só a diretoria pode tomar")

# Estrutura: síntese + gancho na primeira parte (normas)
R("B", '<p class="tese">Não é um grupo sem regras. É um grupo com regras de convivência muito boas e regras de decisão quase inexistentes.</p>', '<p class="tese">O grupo tem regras de convivência muito boas e regras de decisão quase inexistentes; papéis e sistemas seguem o mesmo padrão.</p>\n<p class="gancho">O que a frente é obrigada a cumprir e o que ninguém definiu?</p>')

# últimos "sessão"
R("C", "Cerca de 12 horas de sessão para o núcleo, mais 2 horas de mentores", "Horas de sala negociadas com os participantes, mais a presença dos mentores")
R("C", "As sessões um e três podem ser curtas; a dois não", "Os encontros de problemas e de reuniões podem ser curtos; o de fluxo, não")
R("H", "pedido formal de cota de TI na sessão 5", "pedido formal de cota de TI no encontro de papéis")
R("H", "Urgência que atropela as sessões", "Urgência que atropela os encontros")

# O modelo: visão atual, não final
R("I", r'(<p class="gancho">Quantas reuniões isso exige e o que a execução tem de entregar a cada ciclo\?</p>)', r'\1\n<div class="alerta"><strong>VISÃO ATUAL, NÃO FINAL.</strong> O que está nesta aba é a leitura de hoje, montada a partir das atas e das reuniões de 1º de setembro. O modelo ainda será desenhado com o time nos encontros da aba Proposta; o que sair de lá substitui o que está aqui.</div>', rx=True, count=1)
R("I", "O modelo separa quem dirige de quem entrega, define o que cada camada deve à outra e mede o sucesso do sistema, nunca da adoção do modelo.", "O modelo, na visão de hoje, separa quem dirige de quem entrega, define o que cada camada deve à outra e mede o sucesso do sistema, nunca da adoção do modelo.")
for k, s in F.items(): save(f"frag_{k}.html", s)

p = load("pratica.py")
for a, b in [("A primeira sessão útil com o grupo não é sobre nomes", "O primeiro encontro útil com o grupo não é sobre nomes"), ("Na primeira sessão, coloque na fila", "No primeiro encontro, coloque na fila"),
             ("As sessões um e três podem ser curtas; a dois não", "Os encontros de problemas e de reuniões podem ser curtos; o de fluxo, não")]:
    if a not in p: MISS.append(("pratica", a[:50]))
    p = p.replace(a, b)
save("pratica.py", p)
print("patch v14 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
