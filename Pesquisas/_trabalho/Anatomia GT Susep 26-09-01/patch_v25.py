# -*- coding: utf-8 -*-
"""v25: empoderar pessoas e gerir o sistema; quem faz a gestão do trabalho no grupo."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SV = '<span class="sel sel-v">Verificado</span>'
SEC = '''
<h3>Empoderar pessoas, gerir o sistema: quem faz a gestão do trabalho</h3>
<p>Hoje a gestão do trabalho é feita à mão: planilhas coletivas com lembretes repetidos, cobrança na reunião semanal e a facilitação registrando, cobrando e migrando ferramentas.<sup>13, 14, 15, 20</sup> ''' + SV + ''' O desenho inverte a lógica: gere-se o sistema (fila, capacidade, regras, indicadores), e as pessoas ganham alçada para decidir dentro dele. Ninguém gere a tarefa de ninguém; a ficha e a fila fazem isso.</p>
<table>
<thead><tr><th>O que se gere</th><th>Quem</th><th>Instrumento</th><th>O que a pessoa ganha</th></tr></thead>
<tbody>
<tr><td><strong>A fila e a prioridade</strong></td><td>Líder da esteira, com o comitê</td><td>Carteira carimbada; limite de itens em andamento</td><td>Decide a ordem dentro da alçada, sem pedir.</td></tr>
<tr><td><strong>O fluxo</strong></td><td>Agilista de melhoria contínua</td><td>Painel dos oito indicadores; fichas de reunião com fricções</td><td>Aponta a trava e corrige o que cabe nos ritos.</td></tr>
<tr><td><strong>A capacidade</strong></td><td>Líder da esteira com TI e superintendentes</td><td>Matriz de dedicação; cota de TI; suplentes</td><td>Sabe quanto braço tem antes de aceitar item novo.</td></tr>
<tr><td><strong>As regras e as alçadas</strong></td><td>Fórum de Negócio, com o grupo</td><td>Dez regras publicadas; tabela de alçadas</td><td>Sabe o que pode decidir e quando sobe.</td></tr>
<tr><td><strong>O resultado</strong></td><td>Estratégia, com Controladoria</td><td>Linha de base e leitura em 30 e 90 dias</td><td>Responde pelo número, não pelo relatório.</td></tr>
<tr><td><strong>A tarefa de cada um</strong></td><td>A própria pessoa</td><td>Ficha de demanda com dono, prazo e critério de pronto</td><td>Não recebe lembrete; recebe alçada e critério.</td></tr>
</tbody>
</table>
<p>''' + SP + '''</p>
'''
I = load("frag_I.html")
m = re.search(r"(<h3>[^<]*Quantas reuniões[^<]*</h3>)", I)
if m: I = I.replace(m.group(1), SEC + m.group(1), 1); print("ok")
else: print("MISS")
save("frag_I.html", I)
