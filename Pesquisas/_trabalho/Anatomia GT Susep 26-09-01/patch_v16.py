# -*- coding: utf-8 -*-
"""v16: O modelo com hipótese de valor, gatilhos de aborto e planos (mudança, comunicação, regressão); 'Na prática' do modelo
sobre construir em conjunto; alerta das Alçadas com conteúdo."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'
MISS = []
I = load("frag_I.html")
SEC = '''
<h3>Hipótese de valor, gatilhos de aborto e os três planos</h3>
<p>O modelo é uma hipótese, construída com o time, e tem data para provar que vale. Se não provar, é abortado, e o grupo volta ao desenho anterior sem perder o que aprendeu.</p>
<table>
<thead><tr><th>Item</th><th>O que é</th></tr></thead>
<tbody>
<tr><td><strong>Hipótese de valor</strong></td><td>Com porta única, alçada escrita e descoberta antes do pedido, o tempo entre entrada e decisão cai de meses para semanas e dois temas críticos chegam à ponta em 90 dias.</td></tr>
<tr><td><strong>Leitura em 1 mês</strong></td><td>Fila única existe e está carimbada; as duas salas de guerra têm dono, braço e indicador; nenhuma reunião do mês terminou só com status. Se faltar um dos três, corrige-se o desenho no encontro seguinte.</td></tr>
<tr><td><strong>Leitura em 3 meses</strong></td><td>Tempo entre entrada e decisão medido e menor que a linha de base; ao menos um incremento em produção validado pela ponta; fórum recebendo demonstração, não lâmina. Se nenhum dos três acontecer, o modelo é abortado.</td></tr>
<tr><td><strong>Plano de mudança</strong></td><td>O que muda em cada área e para cada ator, quem comunica, o que deixa de existir (S&amp;OP, Diagnóstico e frente como agendas separadas) e a data de cada troca (aba Problema e entregas, "O que muda para cada ator").</td></tr>
<tr><td><strong>Plano de comunicação</strong></td><td>Antes do início: o problema, a hipótese e a data de leitura, ditos às áreas pelo líder da esteira, não pela Estratégia. A cada mês: o painel de indicadores publicado. Na leitura de 3 meses: o resultado e a decisão de seguir, ajustar ou abortar, comunicados no mesmo dia.</td></tr>
<tr><td><strong>Plano de regressão</strong></td><td>Se abortar: as agendas anteriores voltam na semana seguinte; a fila carimbada, a lista de problemas e a tabela de alçadas ficam como legado; os dois temas críticos continuam com dono; ninguém é responsabilizado pela hipótese, só pelo que não foi medido.</td></tr>
</tbody>
</table>
<p>''' + SP + '''</p>
'''
m = re.search(r"(<h3>[^<]*Quantas reuniões[^<]*</h3>)", I)
if m: I = I.replace(m.group(1), SEC + m.group(1), 1)
else: MISS.append("h3 quantas reuniões")
I = I.replace("<h2>O modelo do grupo: duas camadas, dois contratos, uma regra contra o relatório</h2>", "<h2>O modelo do grupo: uma hipótese com data para provar que vale</h2>")
save("frag_I.html", I)

J = load("frag_J.html")
old = re.search(r'<div class="alerta"><strong>PROPOSTA\.</strong>.*?</div>', J, re.S)
if old: J = J.replace(old.group(0), '<div class="alerta"><strong>HOJE, NENHUMA DECISÃO RELEVANTE TEM DONO ESCRITO; TUDO SOBE.</strong> A tabela dá dono, prazo e degrau de escalada a dez decisões. A coluna "hoje" é o que as atas mostram; as outras são desenho para os mentores assinarem.</div>', 1)
else: MISS.append("alerta alcadas")
save("frag_J.html", J)

p = load("pratica.py")
m = re.search(r'("omodelo"\s*:\s*)(""".*?"""|".*?"|\'.*?\')', p, re.S)
if m:
    new = '"""<p>O modelo não é entregue pronto: é construído com o time nos encontros, como hipótese de valor com data para provar que vale. Em um mês, a fila carimbada e as duas salas de guerra com dono e braço; em três, o tempo entre entrada e decisão menor que a linha de base e um incremento na ponta. Se não provar, é abortado: as agendas anteriores voltam, o que foi desenhado fica como legado e ninguém responde pela hipótese, só pelo que não foi medido. Três planos acompanham a hipótese desde o primeiro dia: o de mudança (o que muda para cada ator e quando), o de comunicação (quem diz o quê, antes, a cada mês e na leitura de três meses) e o de regressão (como se volta, sem perder o que se aprendeu).</p>"""'
    p = p[:m.start(2)] + new + p[m.end(2):]
else: MISS.append("pratica omodelo")
save("pratica.py", p)
print("patch v16 ok; faltas:", MISS)
