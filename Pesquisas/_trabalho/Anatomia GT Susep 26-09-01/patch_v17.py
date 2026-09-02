# -*- coding: utf-8 -*-
"""v17: papel do agilista de melhoria contínua (dono do fluxo), em O modelo, Executiva, Problema e entregas e Alçadas."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SV = '<span class="sel sel-v">Verificado</span>'
MISS = []
def rep(fn, old, new, rx=False):
    s = load(fn)
    if rx: s2, n = re.subn(old, new, s, count=1, flags=re.S)
    else: n = s.count(old); s2 = s.replace(old, new, 1)
    if n == 0: MISS.append((fn, old[:60]))
    save(fn, s2)

SEC = '''
<h3>Um papel para cuidar do fluxo: o agilista de melhoria contínua</h3>
<p>Facilitar reunião não basta. O fluxo precisa de um dono que meça, aponte, corrija e articule a correção, de forma ativa, todo mês.</p>
<table>
<thead><tr><th>Dimensão</th><th>O papel</th></tr></thead>
<tbody>
<tr><td><strong>Missão</strong></td><td>Fazer o caminho da estratégia à entrega ficar mais curto e mais previsível a cada ciclo; responde pelo tempo entre entrada e decisão e pelo tempo de ciclo da ficha ao pronto.</td></tr>
<tr><td><strong>O que faz</strong></td><td>Lê o painel dos oito indicadores e as fricções registradas nas fichas de reunião; identifica onde o fluxo trava (porta, triagem, alçada, capacidade, retorno); propõe a correção com dado; executa o que cabe nos ritos; articula com TI, Processos e líderes de esteira o que exige mudança fora deles; registra o que mudou e o efeito medido.</td></tr>
<tr><td><strong>O que não é</strong></td><td>Não é o facilitador das reuniões nem o dono da carteira de demandas; não decide prioridade nem alçada; não substitui o líder da esteira.</td></tr>
<tr><td><strong>Entradas</strong></td><td>Painel mensal; fichas de reunião com fricções; retrospectivas do time; recusas e itens estacionados; tempo de fila da TI.</td></tr>
<tr><td><strong>Saídas</strong></td><td>Uma melhoria implementada por mês, com antes e depois medidos; lista pública de travas do fluxo com dono e data; proposta de mudança de rito ou regra ao Fórum de Negócio quando a correção exceder sua alçada.</td></tr>
<tr><td><strong>Alçada</strong></td><td>Muda pauta, cadência e formato dos ritos da execução sem pedir; mudanças de alçada, cota ou estrutura sobem ao Fórum de Negócio com recomendação única.</td></tr>
<tr><td><strong>Ritmo e dedicação</strong></td><td>Participa da triagem, das revisões do time e do comitê; conduz uma retrospectiva mensal do fluxo; dedicação a negociar no encontro de papéis, com o mínimo protegido em agenda.</td></tr>
<tr><td><strong>A quem responde</strong></td><td>Ao líder da esteira pelo resultado; à Estratégia pelo método; ao Fórum de Negócio pela lista de travas.</td></tr>
<tr><td><strong>Como se mede</strong></td><td>Melhorias implementadas por trimestre com efeito medido; queda do tempo entre entrada e decisão e do tempo de ciclo; reuniões com saída válida; fricções repetidas de um mês para o outro (quanto menos, melhor).</td></tr>
</tbody>
</table>
<p>''' + SP + '''</p>
'''
rep("frag_I.html", r"(<h3>[^<]*Quantas reuniões[^<]*</h3>)", SEC + r"\1", rx=True)
rep("frag_G.html", r"(<tr><td>Porta única com triagem quinzenal e tipologia de demanda</td>.*?</tr>)", r"\1\n<tr><td>Um dono da melhoria do fluxo: agilista de melhoria contínua, com tempo protegido</td><td>Estratégia com o líder da esteira</td><td>Sem dono, as travas do fluxo viram tema de reunião e não de correção (aba O modelo).</td></tr>", rx=True)
rep("frag_K.html", r'(<div class="card"><strong>Ponta comercial\.</strong>.*?</div>)', r'\1\n<div class="card"><strong>Agilista de melhoria contínua.</strong> Papel novo: mede o fluxo, aponta a trava, corrige o que cabe nos ritos e articula o resto; entrega uma melhoria medida por mês (aba O modelo).</div>', rx=True)
rep("frag_K.html", "Horas por pessoa, o que sai da rotina, suplente por frente, pedido de reposição e de cota de TI", "Horas por pessoa, o que sai da rotina, suplente por frente, dono da melhoria do fluxo, pedido de reposição e de cota de TI")
rep("frag_J.html", "<td>Fórum de Negócio, com o grupo</td><td>Estratégia, Agilidade</td>", "<td>Fórum de Negócio, com o grupo; ritos da execução, o agilista de melhoria contínua</td><td>Estratégia, Agilidade</td>")
print("patch v17 ok; faltas:", MISS)
