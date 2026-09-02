# -*- coding: utf-8 -*-
"""Rodada 1 do advogado (citações não literais) + enxerto da fonte 26 (reunião de 01/09/2026)."""
import io, os
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(x): return io.open(os.path.join(W, f"frag_{x}.html"), encoding="utf-8").read()
def save(x, s): io.open(os.path.join(W, f"frag_{x}.html"), "w", encoding="utf-8", newline="\n").write(s)
def rep(s, old, new, n=1):
    assert s.count(old) >= 1, f"nao achou: {old[:70]}"
    return s.replace(old, new, n)

A, B, C, D = load("A"), load("B"), load("C"), load("D")

# ---------- citações não literais (rodada 1)
A = rep(A, 'deliberações pedidas em formato "resultados, ações e pontos que exigem deliberação"', 'o mentor pede apresentação estruturada das "ações em curso, os resultados colhidos e os pontos que exigem deliberação"')
A = rep(A, '"Soluções paliativas enquanto a estrutura sistêmica perfeita não é priorizada."', 'O grupo "buscará soluções paliativas (links no pós-venda) enquanto a estrutura sistêmica perfeita não é priorizada".')
B = rep(B, '"Visto por grandes corretores como amadorismo."', '"Vista por grandes corretores como amadorismo."')
B = rep(B, '"Incapacidade sistêmica de rastrear o ponto de venda exato."', '"Incapacidade sistêmica atual de rastrear e mapear o ponto de venda exato."')
B = rep(B, 'Investimento em TI "voltado à fundação estrutural".', 'Investimentos em TI "voltados à fundação estrutural".')
B = rep(B, 'Se a régua for "quanto negócio isso trava", a lista muda', 'Se a régua for quanto negócio cada um trava, a lista muda')
B = rep(B, '"Operação bastante sobrecarregada"; cria comissão', 'A operação "já está bastante sobrecarregada"; cria comissão')
B = rep(B, 'Alerta que o prazo da Unicred é crítico "dado o histórico de lentidão".', 'Alerta que o prazo da Unicred é crítico pela "complexidade contábil/sistêmica e ao histórico de lentidão nos processos internos".')
C = rep(C, 'Meta de 20% contra "concorrência desleal de preços"', 'Meta de 20% contra a "forte e desleal concorrência de preços"')
C = rep(C, 'Em 30 de março o grupo "mantém a meta da Controladoria em vez dos 20%"; em 22 de abril "mantém os 20% conforme acordado com mentores"', 'Em 30 de março registra-se a "manutenção da meta baseada na Controladoria para 2026 ao invés da meta anual de 20% a.a."; em 22 de abril, a "manutenção da meta de 20% de crescimento anual conforme acordado com mentores"')
C = rep(C, 'registra que a mistura gera "transbordo de ideias positivas"', 'registra que a mistura gera "transbordo de ideias" positivas')
C = rep(C, 'sem tradução, a diretoria "não entende o produto"', 'sem tradução, é preciso "um discurso alinhado com a diretoria para que entendam o produto"')
A = rep(A, 'a mistura gera "transbordo de ideias positivas"', 'a mistura gera "transbordo de ideias" positivas') if 'a mistura gera "transbordo de ideias positivas"' in A else A
D = rep(D, 'Não: a mistura gera "transbordo de ideias positivas" entre os ramos.', 'Não: a mistura gera "transbordo de ideias" positivas entre os ramos.')

# ---------- fonte 26: Destaque
A = rep(A, '<li><strong>O remédio já foi receitado pelo próprio grupo.</strong>',
'''<li><strong>A reunião de 1º de setembro confirma o diagnóstico pela boca de quem facilita.</strong> Fabíola: "são sempre quase as mesmas pessoas nos demais fóruns", "os assuntos eles entram e eles se confundem nas agendas", "as pessoas elas olham silados", "a gente tá deduzindo por eles". Camila: "existe uma pressa das coisas acontecerem, mas ainda eu sinto que tá sem estrutura", "eu não tô vendo o problema", "a gente tá atrás com método antes do problema".<sup>26</sup> <span class="sel sel-v">Verificado</span></li>
<li><strong>O remédio já foi receitado pelo próprio grupo.</strong>''')
A = rep(A, 'Em 24 documentos produzidos pelo próprio grupo entre 30 de março e 17 de agosto de 2026, aparecem 72 sintomas organizacionais distintos',
        'Em 24 documentos produzidos pelo próprio grupo entre 30 de março e 17 de agosto de 2026, aparecem 72 sintomas organizacionais distintos, e a reunião de 1º de setembro sobre o futuro Fórum de Negócio SUSEP repete os principais sem saber que os repetia<sup>26</sup>')

# ---------- fonte 26: Entenda (linha do tempo)
A = rep(A, '''<div class="tl-item"><span class="tl-dot"></span><strong>3 a 17 de agosto.</strong>''',
'''<div class="tl-item"><span class="tl-dot"></span><strong>3 a 17 de agosto.</strong>''')
A = rep(A, '''Mentor autoriza estudo do esgotamento de comissão e revisão da aceitação.<sup>20, 21, 22, 23</sup></div>
</div>''',
'''Mentor autoriza estudo do esgotamento de comissão e revisão da aceitação.<sup>20, 21, 22, 23</sup></div>
<div class="tl-item"><span class="tl-dot"></span><strong>1º de setembro.</strong> Reunião sobre a metodologia do Fórum de Negócio SUSEP. A Estratégia quer transformar as frentes: juntar Frente, S&amp;OP e Diagnóstico numa squad única, com o fórum como rito de entrega; o modelo de squad proposto por Ingrid "não está batido o martelo", os papéis estão "nebulosos" e, na versão discutida, "não vai TI".<sup>26</sup></div>
</div>''')
A = rep(A, '''<h3>Os ritos previstos</h3>''',
'''<h3>O fluxo oficial, na descrição da facilitadora</h3>
<p>Em 1º de setembro, Fabíola descreve a cadeia inteira em uma frase: a estratégia "nasce no planejamento estratégico, né, que aí é diretores, superintendentes e área da estratégia mesmo", desdobra "no mapa estratégico" (o "artefato"), e "do mapa a gente desdobrou já para as frentes estratégicas, né, para execução". O passo seguinte, em discussão, seriam as squads, com "o fórum de negócio" como "o rito de entrega das squads", alimentando e recebendo da TI, dos aceleradores e dos projetos de torre ("Ele não só joga, como ele também recebe").<sup>26</sup> <span class="sel sel-v">Verificado</span></p>

<h3>Os ritos previstos</h3>''')

# ---------- fonte 26: Ecossistema (novos atores)
A = rep(A, '''<tr><td><strong>Gente de fora</strong> (Linea, research de UX, ressegurador, Faculdade Unimed, FDC)</td>''',
'''<tr><td><strong>Patrocínio da transformação</strong> (Flávio; Caio e Dani na Estratégia; Ingrid no desenho da squad)</td><td>Quem quer transformar as frentes em squad e fórum de negócio.</td><td>Flávio "tem pressa"; Caio e Dani conversam com Ingrid; o modelo "não está batido o martelo"; Camila: "A grande questão é você convencer Caio e Daniel Dani disso".<sup>26</sup></td><td>Define o formato antes do problema, na leitura de Camila. <span class="sel sel-v">Verificado</span></td></tr>
<tr><td><strong>Gente de fora</strong> (Linea, research de UX, ressegurador, Faculdade Unimed, FDC)</td>''')

# ---------- fonte 26: Processos (três agendas)
A = rep(A, '''<h3>Três casos que mostram o fluxo inteiro</h3>''',
'''<h3>As três agendas que a Estratégia quer fundir</h3>
<p>Na descrição de 1º de setembro, a SUSEP tem hoje três agendas com "quase as mesmas pessoas": a Frente Estratégica (Vida e RE), o S&amp;OP ("só vida") e o Diagnóstico, nascido no comercial no fim de 2025 e que "funcionou bem, as pessoas sentaram, conversaram". O problema é que "as pessoas não conseguem falar no S&amp;OP só do que é operacional e do que é de vendas" nem "só do que é estratégico na frente estratégica". A proposta é "pegar essas três agendas e virar uma squad onde a gente possa falar de todos os assuntos que permeiam a SUSEP", começando por Vida.<sup>26</sup> <span class="sel sel-v">Verificado</span>. O que a proposta ainda não diz é o que essa squad vai entregar, com que braço e decidindo o quê; é exatamente a pergunta de Camila: "o que que essa squad vai entregar? Porque se ela não tem TI...".<sup>26</sup> <span class="sel sel-i">Inferência</span></p>

<h3>Três casos que mostram o fluxo inteiro</h3>''')

# ---------- fonte 26: Sintomas (tabela nova)
B = rep(B, '''<h3>Os que mais custam (leitura deste documento)</h3>''',
'''<h3>O que a reunião de 1º de setembro acrescenta</h3>
<p>Nenhum sintoma novo de categoria; todos reforçam os existentes. A novidade é que aparecem na fala de quem facilita a frente (Fabíola) e de quem é chamada a estruturar o novo modelo (Camila), a semanas de uma decisão de formato.<sup>26</sup></p>
<table>
<thead><tr><th>Sintoma reforçado</th><th>Fala literal</th><th>Quem</th></tr></thead>
<tbody>
<tr><td>Comitês paralelos com as mesmas pessoas; assuntos confusos</td><td>"são sempre quase as mesmas pessoas nos demais fóruns"; "os assuntos eles entram e eles se confundem nas agendas"</td><td>Fabíola</td></tr>
<tr><td>Silos e ausência de dono do todo</td><td>"cada área vê o seu próprio problema. Ela não fala do problema da outra área para não interferir, para também não ser indicada"; "Não tem um um o todo trabalhando em prol"</td><td>Fabíola</td></tr>
<tr><td>Dedicação: a rotina vence a frente</td><td>"as pessoas dão mais atenção mesmo paraas suas coisas diárias do que para as coisas da frente, porque é onde tá ligada a meta, onde no final do mês vai bater o dinheiro dele"; "se hoje as pessoas estão atoladas nas suas próprias áreas"</td><td>Fabíola</td></tr>
<tr><td>Método antes do problema</td><td>"a gente tá atrás com método antes do problema, antes do porquê"; "Para mim é só um formato, mudei de uma coisa para outra, mas o que que eu tô tratando?"</td><td>Camila</td></tr>
<tr><td>Deduzir pelos outros em vez de perguntar</td><td>"A gente tá deduzindo por eles e a gente não tá virando para eles e falando assim: Me fala qual é o teu problema"; "eles acabam fazendo o que a gente quer e não o que deveria ser feito"</td><td>Fabíola</td></tr>
<tr><td>Squad sem engrenagem</td><td>"A fala dela é que não vai TTI"; "se eu não tiver uma engrenagem para fazer isso funcionar, não adianta nada eu ter rito"; "Eu senti hoje a Inrid muito mais preocupada nos ritos"</td><td>Camila</td></tr>
<tr><td>Papéis nebulosos, decididos antes do problema</td><td>"ainda um pouco nebuloso essa questão dos papéis"; "não está batido o martelo ainda"; "nós vamos colocar Jaque com PM. Gente, zero sentido, porque o seguinte, se eu não sei nem o problema"</td><td>Fabíola; Camila</td></tr>
<tr><td>Pressa sem estrutura e risco de descrédito</td><td>"existe uma pressa das coisas acontecerem, mas ainda eu sinto que tá sem estrutura"; "não sei se o Flávio quer isso ou a pressa que ele tem"; sobre tentar mais um modelo e dar errado: "esse é o meu medo"</td><td>Camila</td></tr>
<tr><td>Frente longe da ponta e sem tempo</td><td>"Hoje à frente tá olhando corretor [...] muito a quilômetros de distância"; "a frente tá nesse ponto de não temos tempo, tá todo mundo corrido, tá todo mundo desesperado"</td><td>Fabíola</td></tr>
<tr><td>Diagnóstico que funcionou e priorização que não aconteceu</td><td>"Funcionou quando a gente bota eles na mesa e fala assim: O que que você quer trabalhar?"; "eles fizeram uma planilha gigantesca de uma segunda fase que aí eles não conseguem ou não querem ou não tem tempo [...] de fazer essa priorização"</td><td>Fabíola</td></tr>
<tr><td>Fórum como instância de cobrança; retrospectiva como desabafo</td><td>Sobre a retrospectiva: "Susep foi muro das lamentações"</td><td>Fabíola</td></tr>
<tr><td>Diretoria e mentoria longe da operação; ninguém dá notícia ruim</td><td>"a diretoria ela é milp, ela não vê o problema"; "quem dá notícia ruim para ele de que não funciona sou eu, porque ninguém da equipe dele dá notícia ruim"; mentor "tinha que ser uma pessoa isenta, porque cada um puxa pro seu"</td><td>Camila</td></tr>
<tr><td>Venda sem matriz estruturante</td><td>"Todo mundo fica só preocupado em venda, venda, venda e esquece que existe uma uma matriz estruturante por trás [...] Ninguém tá vendo"</td><td>Camila</td></tr>
<tr><td>Desalinhamento sobre quem está fazendo o quê</td><td>"eu achava que vocês já estavam trabalhando nisso"; "E eu também tava achando que vocês já estavam trabalhando"; "aí a gente tá meio que gerando retrabalho do que já tinha sido pedido paraa Ingrid"</td><td>Camila; Fabíola</td></tr>
</tbody>
</table>
<p><span class="sel sel-v">Verificado</span> nas falas; o casamento com os sintomas do Excel é <span class="sel sel-i">Inferência</span>. Nota de leitura: a transcrição é automática e traz grafias como "silados", "milp", "TTI" e "Inrid"; foram mantidas como estão.</p>

<h3>Os que mais custam (leitura deste documento)</h3>''')

# ---------- fonte 26: Normas (regra em aberto)
B = rep(B, '''<h3>O que não existe e precisaria existir</h3>''',
'''<h3>O que está em aberto em 1º de setembro</h3>
<p>O modelo do Fórum de Negócio SUSEP e da squad "não está batido o martelo"; os papéis ("PM, PO, scrum master") estão "nebulosos"; a versão discutida "não vai TI"; e a Estratégia hesita entre esperar o modelo evoluir ou "colocar na mesa" as dores antes.<sup>26</sup> <span class="sel sel-v">Verificado</span></p>

<h3>O que não existe e precisaria existir</h3>''')

# ---------- fonte 26: Papéis
B = rep(B, '''<h3>O que o desenho precisaria definir sobre pessoas</h3>''',
'''<h3>O que a reunião de 1º de setembro diz sobre papéis</h3>
<ul>
<li><strong>Papel antes do problema.</strong> A cogitação de nomear a líder comercial como PM da squad é recebida por Camila como "zero sentido" enquanto o problema não estiver claro.<sup>26</sup> <span class="sel sel-v">Verificado</span></li>
<li><strong>Mentor isento.</strong> Para Camila, quem arbitra "tinha que ser uma pessoa isenta, porque cada um puxa pro seu".<sup>26</sup> <span class="sel sel-v">Verificado</span></li>
<li><strong>Tempo integral é ficção.</strong> Fabíola lembra que squad pressupõe "pessoas com tempo integral para trabalhar aquele assunto", e que nem o modelo de frentes funciona porque a rotina "toma muito mais do que o 100% do tempo".<sup>26</sup> <span class="sel sel-v">Verificado</span></li>
</ul>

<h3>O que o desenho precisaria definir sobre pessoas</h3>''')

# ---------- fonte 26: Loops (nota)
C = rep(C, '''<p class="note">A diferença entre os laços não é competência''',
'''<p class="note">Em 1º de setembro, os dois laços viciosos aparecem em uma única fala de Fabíola: "as pessoas dão mais atenção mesmo paraas suas coisas diárias do que para as coisas da frente, porque é onde tá ligada a meta", e "cada área vê o seu próprio problema. Ela não fala do problema da outra área para não interferir".<sup>26</sup> <span class="sel sel-v">Verificado</span></p>
<p class="note">A diferença entre os laços não é competência''')

# ---------- fonte 26: Modelo (fórum de negócio)
C = rep(C, '''<h3>Como saber o que é relevante</h3>''',
'''<h3>O Fórum de Negócio SUSEP à luz da tipologia</h3>
<p>A proposta de 1º de setembro (fundir Frente, S&amp;OP e Diagnóstico numa squad com o fórum como rito de entrega) resolve o sintoma dos comitês paralelos.<sup>26</sup> Não resolve, por si, os outros três que esta anatomia aponta como mais caros: alçada (a squad decide o quê?), braço (Camila: "se ela não tem TI", o que entrega?) e porta única com tipologia (sem triagem, a squad herda a "planilha gigantesca" que ninguém priorizou).<sup>26</sup> <span class="sel sel-i">Inferência</span> sobre falas verificadas.</p>

<h3>Como saber o que é relevante</h3>''')

# ---------- fonte 26: Análise (risco)
C = rep(C, '''<tr><td>Corretoras cativas das Unimeds esvaziarem o canal de casa</td>''',
'''<tr><td>Lançar a squad e o Fórum de Negócio com formato definido antes do problema, e cair em descrédito com as áreas</td><td>Alta</td><td>Alto</td><td>Papéis nomeados antes da lista de problemas; squad sem TI; Camila: "esse é o meu medo"</td><td><sup>26</sup></td></tr>
<tr><td>Corretoras cativas das Unimeds esvaziarem o canal de casa</td>''')
C = rep(C, '''<div class="card"><strong>Ameaças.</strong> Prazo de janeiro de 2027<sup>17</sup>; agenciamento de 350%<sup>16</sup>; corretoras cativas<sup>22</sup>; clima<sup>24</sup>; nova determinação corporativa que mude o rito no meio do caminho.<sup>15</sup>''',
'''<div class="card"><strong>Ameaças.</strong> Prazo de janeiro de 2027<sup>17</sup>; agenciamento de 350%<sup>16</sup>; corretoras cativas<sup>22</sup>; clima<sup>24</sup>; nova determinação corporativa que mude o rito no meio do caminho<sup>15</sup>; um novo modelo (squad e fórum) lançado com pressa e sem problema definido.<sup>26</sup>''')

# ---------- fonte 26: Sutilezas
C = rep(C, '''<li><strong>A corretora SAD é um sinal mudo.</strong>''',
'''<li><strong>"Muro das lamentações".</strong> É como Fabíola resume a retrospectiva da SUSEP.<sup>26</sup> Um grupo que só consegue desabafar no rito de aprendizado é um grupo sem lugar para decidir. <span class="sel sel-v">Verificado</span> a fala; a leitura é <span class="sel sel-i">Inferência</span>.</li>
<li><strong>A Estratégia sabe que está deduzindo.</strong> "A gente tá deduzindo por eles", diz Fabíola; e ainda assim o modelo de squad já tinha "um modelão grande" desenhado antes de alguém perguntar às áreas qual é o problema.<sup>26</sup> <span class="sel sel-v">Verificado</span></li>
<li><strong>Quem dá a notícia ruim.</strong> Camila, de um projeto paralelo com estrutura de squad: o superintendente "não tem noção do que acontece na operação dele", e quem avisa é ela, "porque ninguém da equipe dele dá notícia ruim".<sup>26</sup> Se vale para a SUSEP, os fóruns preparados para "evitar brechas" são o mesmo fenômeno visto de baixo.<sup>5</sup> <span class="sel sel-i">Inferência</span></li>
<li><strong>A corretora SAD é um sinal mudo.</strong>''')

# ---------- fonte 26: Cem perguntas (ajustes mantendo 100)
D = rep(D, '''<li><strong>Quantos comitês tratam as mesmas dores?</strong> Pelo menos três: Frente, S&amp;OP e Diagnóstico Comercial.<sup>20</sup></li>''',
'''<li><strong>Quantos comitês tratam as mesmas dores?</strong> Pelo menos três: Frente, S&amp;OP e Diagnóstico Comercial; em setembro a Estratégia quer fundi-los numa squad única.<sup>20, 26</sup></li>''')
D = rep(D, '''<li><strong>Por onde começar?</strong> Pela esteira Vida e duas salas de guerra: esgotamento de comissão e prestamista. <span class="sel sel-e">Especulativo</span></li>''',
'''<li><strong>Por onde começar?</strong> Pela lista de problemas, antes do formato: é o que Fabíola ("me fala qual é o teu problema") e Camila ("tudo começa no problema") pedem.<sup>26</sup> Depois, pela esteira Vida e duas salas de guerra. <span class="sel sel-e">Especulativo</span> na sequência</li>''')
D = rep(D, '''<li><strong>Existe comitê de priorização?</strong> Um piloto, iniciado em junho, que começou por Saúde por dificuldade de preenchimento.<sup>13, 16</sup></li>''',
'''<li><strong>Existe comitê de priorização?</strong> Um piloto, iniciado em junho, que começou por Saúde por dificuldade de preenchimento; a "planilha gigantesca" da segunda fase segue sem priorização.<sup>13, 16, 26</sup></li>''')
D = rep(D, '''<li><strong>Como saber se funcionou?</strong> Lead time de decisão, decisões com dono e braço, quórum, tarefas entre reuniões, não-ganhos registrados. <span class="sel sel-i">Inferência</span></li>''',
'''<li><strong>Como saber se funcionou?</strong> Lead time de decisão, decisões com dono e braço, quórum, tarefas entre reuniões, não-ganhos registrados; e, na régua de Fabíola, se as áreas "verificarem que realmente tem valor".<sup>26</sup> <span class="sel sel-i">Inferência</span></li>''')

# ---------- fonte 26: Glossário
D = rep(D, '''<div class="card"><strong>Sala de guerra.</strong>''',
'''<div class="card"><strong>Fórum de Negócio SUSEP.</strong> Rito proposto em setembro de 2026 como lugar de entrega das squads, reunindo o que hoje é Frente, S&amp;OP e Diagnóstico.</div>
<div class="card"><strong>PM, PO e scrum master.</strong> Papéis típicos de squad (gestor do produto, dono do backlog, facilitador de impedimentos), citados como ainda "nebulosos" no modelo em discussão.</div>
<div class="card"><strong>Aceleradores e projetos de torre.</strong> Esteiras corporativas de execução (acelerador de TI e projetos estruturantes) com as quais a squad trocaria demandas nos dois sentidos.</div>
<div class="card"><strong>Mapa estratégico.</strong> O "artefato" em que o planejamento estratégico é desdobrado antes de virar frentes.</div>
<div class="card"><strong>Sala de guerra.</strong>''')

# ---------- fonte 26: Fontes
D = rep(D, '''<h3>Documento derivado (25)</h3>''',
'''<h3>Reunião de 1º de setembro de 2026 (26)</h3>
<ol start="26">
<li>Transcrição automática da reunião "Sugestão de metodologia para Fórum de Negócio Susep", com Camila Fernanda Silva Gomes, Eric Leite e Fabíola Brandão, 35 minutos. 1º de setembro de 2026. Fornecida pelo autor; guardada na pasta de trabalho deste documento. Regra de uso: apenas as falas de Fabíola e Camila valem como evidência; as intervenções de Eric são do autor deste diagnóstico e não são citadas como fonte.</li>
</ol>
<h3>Documento derivado (25)</h3>''')
D = rep(D, 'lido na íntegra em 1º de setembro de 2026. <span class="sel sel-i">Inferência</span>',
        'lido na íntegra em 1º de setembro de 2026, ou em fala transcrita da reunião do mesmo dia. <span class="sel sel-i">Inferência</span>')
D = rep(D, 'As fontes são internas: um deck de planejamento e 23 atas do próprio grupo, guardados no notebook',
        'As fontes são internas: um deck de planejamento e 23 atas do próprio grupo, mais a transcrição de uma reunião de 1º de setembro, guardados no notebook')

save("A", A); save("B", B); save("C", C); save("D", D)
print("patch f26 ok")
