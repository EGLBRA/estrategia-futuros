# -*- coding: utf-8 -*-
"""v21: juntar S&OP, Diagnóstico e frente numa agenda só pede mais estrutura e contorno, não menos."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SV = '<span class="sel sel-v">Verificado</span>'; SI = '<span class="sel sel-i">Inferência</span>'
SEC = '''
<h3>Juntar S&amp;OP, Diagnóstico e frente numa agenda só pede mais estrutura, não menos</h3>
<p>A ideia de reunir as três agendas num único fórum ou time nasce de um fato real: as mesmas pessoas em todos os fóruns e os assuntos se misturando entre as agendas.<sup>26</sup> ''' + SV + ''' Mas juntar sem contorno troca três salas confusas por uma sala maior e igualmente confusa. Quanto mais assunto entra pela mesma porta, mais o desenho precisa dizer o que entra, o que não entra e quem decide o quê. ''' + SI + '''</p>
<table>
<thead><tr><th>O que a mistura traz</th><th>O contorno que ela exige</th></tr></thead>
<tbody>
<tr><td>Planejamento de vendas e operação (o que era do S&amp;OP) na mesma mesa que problemas estruturais.</td><td>Tipologia na entrada: estrutural, sustentação, adequação, oportunidade. O que é rotina de vendas e operação fica com as áreas e só sobe ao fórum como número, não como pauta.</td></tr>
<tr><td>Dores das áreas (o que era do Diagnóstico) sem filtro.</td><td>Ficha única e triagem quinzenal com nota de relevância; a planilha extensa vira fila carimbada, não pauta de reunião.</td></tr>
<tr><td>Vida e Ramos Elementares, dois negócios, na mesma reunião.</td><td>Duas esteiras com dono, indicador e relatório próprios; o fórum é um, as esteiras são duas.</td></tr>
<tr><td>Mais decisões pedidas ao mesmo fórum.</td><td>Alçada escrita por tipo de decisão e escada de escalada com prazo; sem isso, o fórum único vira o novo gargalo.</td></tr>
<tr><td>Mais gente e mais tempo de sala.</td><td>Custo de cada rito à vista e limite de itens em andamento; o que deixa de existir (as três agendas separadas) para em data marcada.</td></tr>
<tr><td>Um só lugar para tudo, sem dizer o que fica de fora.</td><td>Lista explícita do que o fórum não trata: pauta operacional do dia a dia, disputa de recursos entre áreas e temas de outras frentes.</td></tr>
</tbody>
</table>
<p>''' + SP + '''</p>
'''
L = load("frag_L.html")
if "<h3>Desafios abertos</h3>" in L: L = L.replace("<h3>Desafios abertos</h3>", SEC + "<h3>Desafios abertos</h3>", 1); print("ok")
else: print("MISS desafios")
L = L.replace("<tr><td><strong>Método × problema</strong></td>", "<tr><td><strong>Uma agenda para tudo × contorno</strong></td><td>A mistura: três agendas com quase as mesmas pessoas e assuntos confusos.<sup>26</sup></td><td>Tipologia, triagem, alçada e a lista do que o fórum não trata (seção abaixo).</td></tr>\n<tr><td><strong>Método × problema</strong></td>", 1)
L = L.replace("Seis tensões que o desenho atual não resolve", "Sete tensões que o desenho atual não resolve", 1)
save("frag_L.html", L)
