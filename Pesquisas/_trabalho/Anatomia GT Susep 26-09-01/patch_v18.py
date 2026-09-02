# -*- coding: utf-8 -*-
"""v18: aba 'Riscos e tensões' (riscos, tensões, desafios, partes confusas, o que ninguém fala); Glossário e Fontes viram uma aba;
menu continua com 2 x 10."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SV = '<span class="sel sel-v">Verificado</span>'; SI = '<span class="sel sel-i">Inferência</span>'
MISS = []
def cut(fn, pattern, label):
    s = load(fn); m = re.search(pattern, s, re.S)
    if not m: MISS.append((fn, label)); return ""
    save(fn, s.replace(m.group(0), "", 1)); return m.group(0)

# 1. mover seções para a aba nova
ning = cut("frag_A.html", r"<h3>O que ninguém está falando</h3>.*?<p>Os fatos vêm das atas e das transcrições\..*?</p>\n", "ninguém")
A = load("frag_A.html")
if "<h3>O que ninguém está falando</h3>" not in A and ning:
    A = A.replace("<h3>Em resumo</h3>", "<h3>Em resumo</h3>", 1)
    m = re.search(r"<h3>Em resumo</h3>.*?</ul>", A, re.S)
    if m: A = A.replace(m.group(0), m.group(0) + '\n<p class="note">O que as atas mostram e nenhuma reunião diz em voz alta está na aba Riscos e tensões.</p>', 1)
    save("frag_A.html", A)
confusas = cut("frag_H.html", r"<h3>Quais partes ainda estão confusas</h3>.*?(?=<h3>)", "confusas")
riscos = cut("frag_H.html", r"<h3>Riscos identificados</h3>.*?(?=<h3>)", "riscos")
matriz = cut("frag_C.html", r"<h3>Matriz de riscos</h3>.*?</table>\s*(?:<p>[^<]*<span class=\"sel sel-i\">Inferência</span></p>\s*)?", "matriz")
H = load("frag_H.html")
H = H.replace("<h3>Uma planta organizacional de cada encontro, com custo</h3>", '<p class="note">Riscos, partes ainda confusas e tensões do desenho estão na aba Riscos e tensões.</p>\n<h3>Uma planta organizacional de cada encontro, com custo</h3>', 1)
save("frag_H.html", H)
C = load("frag_C.html")
C = C.replace("<h2>Análise: o maior risco é o desenho continuar igual</h2>", "<h2>Análise: SWOT e três cenários</h2>", 1)
save("frag_C.html", C)

TENS = '''
<h3>Tensões estruturais</h3>
<p>Seis tensões que o desenho atual não resolve e o novo desenho precisa nomear. Cada uma tem um lado que ganha hoje.</p>
<table>
<thead><tr><th>Tensão</th><th>Quem ganha hoje</th><th>O que o desenho precisa decidir</th></tr></thead>
<tbody>
<tr><td><strong>Rotina da área × trabalho da frente</strong></td><td>A rotina: é nela que estão a meta e a remuneração.<sup>26</sup></td><td>Dedicação declarada por pessoa e meta da frente ligada à meta da área.</td></tr>
<tr><td><strong>Vida × Ramos Elementares na mesma sala</strong></td><td>RE: preço e cotador sob controle do grupo; Vida espera a aceitação.<sup>7, 23</sup></td><td>Duas esteiras com dono, indicador e relatório próprios.</td></tr>
<tr><td><strong>Velocidade × alçada</strong></td><td>A alçada: tudo sobe e espera a janela do mentor.<sup>9, 22, 23</sup></td><td>Tabela de alçadas assinada e escada de escalada com prazo (aba Alçadas).</td></tr>
<tr><td><strong>Método × problema</strong></td><td>O método: times, fórum e papéis entram antes da lista de problemas.<sup>26</sup></td><td>O primeiro encontro é só problemas; formato vem depois.</td></tr>
<tr><td><strong>Fila da TI × frente sem cota</strong></td><td>As emergências: trocam projetos e não têm critério de despriorização.<sup>22, 27</sup></td><td>Cota reservada e critério de despriorização pedidos à diretoria de TI.</td></tr>
<tr><td><strong>Crescer × apetite de risco</strong></td><td>O apetite: aceitação médica e compliance decidem caso a caso, sem via de reconsideração registrada.<sup>10, 11, 18</sup></td><td>Faixas de capital por trimestre e reconsideração em cinco dias úteis.</td></tr>
</tbody>
</table>
<p>Os fatos de cada linha vêm das atas. ''' + SV + ''' A leitura da tensão é deste documento. ''' + SI + ''' A coluna do desenho é proposta. ''' + SP + '''</p>

<h3>Desafios abertos</h3>
<ul>
<li>Seis subproblemas a resolver, cada um ligado a uma entrega (aba Problema e entregas).</li>
<li>Duas decisões que só a diretoria toma e que condicionam tudo: número-base assinado e capacidade de TI reservada (aba Executiva).</li>
<li>Um prazo externo que não espera o desenho: prestamista de prêmio único para a Unicred em janeiro de 2027.<sup>17</sup></li>
<li>Um modelo de time dedicado ainda em construção na Agilidade, com papéis em definição e participação da TI em aberto.<sup>26, 27</sup></li>
</ul>
'''
L = '''<!-- ============================== RISCOS ============================== -->
<section id="p-riscos" class="pane">
<h2>Riscos e tensões: o que pode fazer o desenho falhar</h2>
<p class="tese">O maior risco não é o mercado: é um modelo que entrega relatório, adotado como meta, enquanto o prazo da Unicred, a campanha de VG e a meta de 20% correm.</p>
<p class="gancho">Quais riscos a proposta trata desde o primeiro dia, e quais ficam em aberto?</p>
''' + riscos + matriz + '\n' + TENS + confusas + '''
''' + ning + '''
<div class="pratica">
<h3>Na prática</h3>
<p>Leve esta aba para o primeiro encontro com o grupo e peça três marcações: o risco que mais assusta, a tensão que mais dói e a parte confusa que precisa ser resolvida primeiro. O que o grupo marcar vira a pauta do encontro de alçadas e o primeiro item do plano de comunicação. Se ninguém marcar "um modelo que entrega relatório", a régua de sucesso da aba O modelo precisa ser lida em voz alta antes de continuar.</p>
</div>
</section>
'''
save("frag_L.html", L)

# 2. build.py: abas, mescla glossário + fontes, fragmentos
b = load("build.py")
b2, n1 = re.subn(r'\("loops", "Loops"\), \("analise", "Análise"\), \("cem", "Cem perguntas"\), \("gloss", "Glossário"\), \("fontes", "Fontes"\)\]',
                 '("loops", "Loops"), ("analise", "Análise"), ("riscos", "Riscos e tensões"), ("cem", "Cem perguntas"), ("gloss", "Glossário e fontes")]', b)
b2, n2 = re.subn(r'MERGE = \{"estrutura": \["normas", "papeis", "sist"\], "analise": \["analise", "sut"\]\}',
                 'MERGE = {"estrutura": ["normas", "papeis", "sist"], "analise": ["analise", "sut"], "gloss": ["gloss", "fontes"]}', b2)
b2, n3 = re.subn(r'for x in "ABCDEFGHIJK"\)', 'for x in "ABCDEFGHIJKL")', b2)
if not (n1 and n2 and n3): MISS.append(("build", "tabs %d merge %d frags %d" % (n1, n2, n3)))
save("build.py", b2)
c = load("checks.py")
c = c.replace('NOPRAT = {"cem", "gloss", "fontes"}', 'NOPRAT = {"cem", "gloss"}')
save("checks.py", c)
print("patch v18 ok; faltas:", MISS)
