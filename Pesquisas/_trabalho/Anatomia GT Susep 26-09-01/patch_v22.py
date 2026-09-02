# -*- coding: utf-8 -*-
"""v22: quem entrega o quê, quando; o que é entrega e o que é relatório, por time e por papel."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'
SEC = '''
<h3>Quem entrega o quê, em que ciclo, e o que é relatório</h3>
<p>Entrega é o que muda algo: um incremento em produção, uma ficha carimbada na fila, uma decisão registrada com dono e prazo, um resultado lido. Relatório é o que só descreve andamento. O relatório existe (o painel), mas não conta como entrega de ninguém.</p>
<table>
<thead><tr><th>Time ou papel</th><th>Entrega</th><th>Ciclo e momento</th><th>O que não conta</th></tr></thead>
<tbody>
<tr><td><strong>Time dedicado</strong></td><td>Incremento demonstrado, funcionando, com a operação na sala.</td><td>Quinzenal, na revisão do time.</td><td>Lâmina de andamento; percentual concluído.</td></tr>
<tr><td><strong>Dono do desafio</strong></td><td>Síntese da descoberta: problema, valor, opções e esforço.</td><td>Ao fim de 4 a 8 semanas de descoberta; leitura parcial na segunda semana.</td><td>Relatório de progresso da descoberta.</td></tr>
<tr><td><strong>Líder da esteira</strong></td><td>Carteira triada, decisões dentro da alçada registradas, recomendação única para o que sobe.</td><td>Quinzenal na reunião da esteira; mensal no comitê.</td><td>Reunião de status; lista de pendências sem dono.</td></tr>
<tr><td><strong>Time de triagem</strong></td><td>Fichas carimbadas (tipo, nota, destino) e itens recusados ou estacionados com motivo.</td><td>Quinzenal, 30 minutos.</td><td>Planilha extensa sem carimbo.</td></tr>
<tr><td><strong>Comitê de priorização</strong></td><td>Ata de decisão: dono, prazo, braço e indicador por item; fila ordenada contra a capacidade.</td><td>Mensal, 1 hora.</td><td>Repriorização sem número; pauta que só informa.</td></tr>
<tr><td><strong>Fórum de Negócio</strong></td><td>Decisão registrada na alçada; resultado lido em 30 e 90 dias; item fechado, recusado ou estacionado com data.</td><td>Mensal, 2 horas.</td><td>Apresentação de andamento; fórum que só ouve.</td></tr>
<tr><td><strong>Mentor</strong></td><td>Patrocínio do tema e decisão que volta por escrito.</td><td>1 hora por tema; resposta em até 30 dias.</td><td>Agenda de 30 minutos para tudo.</td></tr>
<tr><td><strong>Agilista de melhoria contínua</strong></td><td>Uma melhoria do fluxo implementada, com antes e depois medidos.</td><td>Mensal, na retrospectiva do fluxo.</td><td>Lista de problemas sem correção executada.</td></tr>
<tr><td><strong>Inteligência Estratégica e de Mercado</strong></td><td>Uma página de contexto antes do fórum; dado de mercado na abertura de cada descoberta.</td><td>Mensal; na abertura da descoberta; em 48 horas para sala de guerra.</td><td>Painel que ninguém pediu e ninguém lê.</td></tr>
<tr><td><strong>Área de Estratégia</strong></td><td>Painel dos oito indicadores publicado; encontros de desenho facilitados; leitura de 1 e 3 meses do piloto.</td><td>Mensal; leitura em 1 e 3 meses.</td><td>Relatório do fórum; ata sem decisão.</td></tr>
<tr><td><strong>TI</strong></td><td>Incrementos da cota SUSEP na fila; esforço decupado por opção na descoberta.</td><td>Quinzenal, na revisão do time.</td><td>Estimativa sem compromisso; emergência que troca projeto sem registro.</td></tr>
<tr><td><strong>Áreas de negócio</strong></td><td>Ficha de demanda escrita por quem vive o problema; validação do pronto na entrega.</td><td>Na entrada; na revisão do time.</td><td>Pedido por mensagem ou em reunião, sem ficha.</td></tr>
</tbody>
</table>
<p>''' + SP + '''</p>
'''
I = load("frag_I.html")
m = re.search(r"(<h3>[^<]*Quantas reuniões[^<]*</h3>)", I)
if m: I = I.replace(m.group(1), SEC + m.group(1), 1); print("ok")
else: print("MISS")
save("frag_I.html", I)
