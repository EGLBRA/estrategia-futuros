# -*- coding: utf-8 -*-
"""v8: 20 abas em 2x10, abas novas (O modelo, Alçadas, Problema e entregas), paráfrase das transcrições,
título e analogia curtos, fluxo funcional legível, risco 'modelo como fim', referências cruzadas."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
F = {k: load(f"frag_{k}.html") for k in "ABCDEFGHIJK"}

# ---------------- 1. paráfrase das transcrições (fontes 26 e 27)
PAR = [
 ('"são sempre quase as mesmas pessoas nos demais fóruns"', 'as mesmas pessoas participam de quase todos os fóruns'),
 ('"os assuntos eles entram e eles se confundem nas agendas"', 'os assuntos se misturam entre as agendas'),
 ('"existe uma pressa das coisas acontecerem, mas ainda eu sinto que tá sem estrutura"', 'há pressa para que as coisas aconteçam, mas ainda falta estrutura'),
 ('"a gente tá atrás com método antes do problema, antes do porquê"', 'o método vem antes do problema e do porquê'),
 ('"a gente tá atrás com método antes do problema"', 'o método está sendo discutido antes do problema'),
 ('"nasce no planejamento estratégico, né, que aí é diretores, superintendentes e área da estratégia mesmo"', 'nasce no planejamento estratégico, com diretores, superintendentes e a área de Estratégia'),
 ('desdobra "no mapa estratégico" (o "artefato")', 'desdobra no mapa estratégico, o artefato central'),
 ('"do mapa a gente desdobrou já para as frentes estratégicas, né, para execução"', 'do mapa desdobra-se para as frentes estratégicas, para execução'),
 ('com "o fórum de negócio" como "o rito de entrega das squads"', 'com o fórum de negócio como rito de entrega dos times dedicados'),
 ('("Ele não só joga, como ele também recebe")', '(nos dois sentidos: envia e recebe)'),
 ('"não está batido o martelo ainda"', 'ainda sem decisão'),
 ('("não está batido o martelo")', '(ainda sem decisão)'),
 ('"não está batido o martelo"', 'ainda sem decisão'),
 ('com "quase as mesmas pessoas"', 'com quase as mesmas pessoas'),
 ('as pessoas "não conseguem falar" no S&amp;OP "só do que é operacional e do que é de vendas" nem "só do que é estratégico na frente estratégico" (grafia da transcrição)', 'as pessoas não conseguem tratar só do operacional e das vendas no S&amp;OP, nem só do estratégico na frente'),
 ('"pegar essas três agendas e virar uma squad onde a gente possa falar de todos os assuntos que permeiam a SUSEP"', 'reunir as três agendas num único time dedicado, onde se tratem todos os assuntos da SUSEP'),
 ('"cada área vê o seu próprio problema"', 'cada área olha o próprio problema'),
 ('"Não tem um um o todo trabalhando em prol"', 'não há um todo trabalhando em conjunto'),
 ('"As pessoas dão mais atenção mesmo paraas suas coisas diárias do que para as coisas da frente, porque é onde tá ligada a meta, onde no final do mês vai bater o dinheiro dele."', 'As pessoas priorizam a rotina da própria área, porque é nela que estão a meta e a remuneração.'),
 ('"as pessoas dão mais atenção mesmo paraas suas coisas diárias do que para as coisas da frente, porque é onde tá ligada a meta, onde no final do mês vai bater o dinheiro dele"', 'as pessoas priorizam a rotina da própria área, porque é nela que estão a meta e a remuneração'),
 ('"as pessoas dão mais atenção mesmo paraas suas coisas diárias do que para as coisas da frente, porque é onde tá ligada a meta"', 'as pessoas priorizam a rotina da própria área, porque é nela que está a meta'),
 ('"Para mim é só um formato, mudei de uma coisa para outra, mas o que que eu tô tratando?"', 'trocar o formato sem definir o que se está tratando'),
 ('"Me fala qual é o teu problema, eu quero resolver, mas você precisa me falar qual é"', 'perguntar às áreas qual é o problema delas, em vez de deduzi-lo'),
 ('"se eu não tiver uma engrenagem para fazer isso funcionar, não adianta nada eu ter rito"', 'sem uma engrenagem que faça o trabalho acontecer, o rito não adianta'),
 ('"ainda um pouco nebuloso essa questão dos papéis"', 'os papéis ainda pouco definidos'),
 ('"esse é o meu medo"', 'o receio declarado'),
 ('"a frente tá nesse ponto de não temos tempo, tá todo mundo corrido, tá todo mundo desesperado"', 'a frente chegou ao ponto de não ter tempo, com todos sobrecarregados'),
 ('"Funcionou quando a gente bota eles na mesa e fala assim: O que que você quer trabalhar?"', 'funcionou quando as áreas foram postas à mesa e perguntadas sobre o que queriam trabalhar'),
 ('"eles fizeram uma planilha gigantesca de uma segunda fase que aí eles não conseguem ou não querem ou não tem tempo [...] de fazer essa priorização"', 'a segunda fase virou uma planilha extensa que as áreas não conseguem, ou não têm tempo de, priorizar'),
 ('"Todo mundo fica só preocupado em venda, venda, venda e esquece que existe uma uma matriz estruturante por trás"', 'a preocupação fica só na venda e esquece a matriz estruturante por trás dela'),
 ('"eu achava que vocês já estavam trabalhando nisso"; "E eu também tava achando que vocês já estavam trabalhando"', 'cada parte achava que a outra já estava trabalhando nisso'),
 ('"pessoas com tempo integral para trabalhar aquele assunto"', 'pessoas com tempo integral para o assunto'),
 ('"toma muito mais do que o 100% do tempo"', 'consome mais do que todo o tempo disponível'),
 ('"planilha gigantesca"', 'planilha extensa'),
 ('"uma planilha gigantesca"', 'uma planilha extensa'),
 ('("me fala qual é o teu problema")', '(perguntar às áreas qual é o problema)'),
 ('"verificarem que realmente tem valor"', 'reconhecerem valor real'),
 ('"o problema ele não vai chegar cru, ele vai chegar com um diagnóstico"', 'o problema não chega cru à TI, chega com diagnóstico'),
 ('"O problema ele não vai chegar cru, ele vai chegar com um diagnóstico."', 'O problema não chega cru à TI; chega com diagnóstico.'),
 ('"as pessoas estão atoladas nas suas próprias áreas"', 'as pessoas estão sobrecarregadas nas próprias áreas'),
 ('retrospectiva vira "muro das lamentações"', 'retrospectiva vira espaço de desabafo'),
 ('"tem que haver o critério de despriorização dentro do acelerador ou eles aumentam a capacidade"', 'é preciso um critério de despriorização no acelerador, ou aumentar a capacidade'),
 ('"Ou eles aumentam a capacidade."', 'Ou a capacidade aumenta.'),
 ('"Ou eles aumentam a capacidade"', 'ou a capacidade aumenta'),
 ('"eles acabam fazendo o que a gente quer e não o que deveria ser feito"', 'as áreas acabam fazendo o que a Estratégia quer, e não o que deveria ser feito'),
 ('"método antes do problema"', 'método antes do problema'),
 ('"gerando retrabalho"', 'gerando retrabalho'),
 ('"Fórum de Negócio"', 'Fórum de Negócio'),
]
for k in F:
    for a, b in PAR: F[k] = F[k].replace(a, b)

# ---------------- 2. título e analogia
F["A"] = re.sub(r'<div class="apex">\s*<p><strong>Para o leigo, em uma imagem\.</strong>.*?</p>\s*</div>',
    '<div class="apex">\n<p><strong>Para o leigo, em uma imagem.</strong> Pense num hospital com bons médicos e sem triagem na porta. O mesmo plantão atende tudo. O diretor aparece 30 minutos por mês. Ninguém autoriza uma cirurgia sem subir três andares. Os casos fáceis saem; os difíceis esperam no corredor. É a frente: a sala de cirurgia funciona; falta o hospital em volta.</p>\n</div>', F["A"], count=1, flags=re.S)

# ---------------- 3. fluxo funcional legível (frag_E)
E = F["E"]
E = re.sub(r'<text x="700" y="440"[^>]*>EXEMPLO</text>\s*', '', E)
def bump(m):
    v = float(m.group(1)); return f'font-size="{v + 1.5:g}"'
# só dentro do svg do fluxo funcional
m = re.search(r'(<svg viewBox="0 0 1400 820".*?</svg>)', E, re.S)
svg = m.group(1)
svg = re.sub(r'font-size="(1[0-5](?:\.5)?)"', bump, svg)
svg = svg.replace('style="display:block;min-width:1180px;width:100%;height:auto;font-family:system-ui,sans-serif"', 'style="display:block;width:1400px;height:auto;font-family:system-ui,sans-serif"')
E = E.replace(m.group(1), svg)
E = E.replace('<h3>O mapa funcional</h3>', '''<h3>O mapa em quatro blocos</h3>
<div class="g2">
<div class="card"><strong>Origem do problema.</strong> Ponta comercial (corretores, assessorias, cooperativas, Unimeds); áreas de negócio; dados (Controladoria, Inteligência de Mercado, funil, sinistro); regulador e parceiros; e as três esteiras que o fórum absorve (S&amp;OP, Diagnóstico, frente). Todas alimentam a porta única com dores, pedidos, prazos e regras.</div>
<div class="card"><strong>Porta única: Fórum de Negócio SUSEP.</strong> Recebe, tria e prioriza contra a capacidade, decide na alçada e recebe a entrega de volta. Sustentação sai daqui direto para a fila própria. O que excede a alçada sobe a RDS e COMEX com uma recomendação única.</div>
<div class="card"><strong>Time dedicado Vida.</strong> Descoberta (causa raiz, ponta, mercado, valor), concepção (opções: processo, tecnologia, parceiro, paliativo, não fazer) e acompanhamento (indicador por item, leitura em 30 e 90 dias).</div>
<div class="card"><strong>Destino da solução.</strong> Processos (resolve na área), Aceleradores (fila de TI), Projetos de torre (estruturantes), Sustentação, ou Política e orçamento (RDS e COMEX). A entrega volta ao fórum validada pela operação e pela ponta; o resultado alimenta o PIE.</div>
</div>
<h3>O mapa funcional</h3>''')
F["E"] = E

# ---------------- 4. Proposta: risco 'modelo que entrega relatório' e 'adoção como sucesso'
H = F["H"]
H = H.replace('<tr><td><strong>Mais um modelo, e descrédito na Estratégia</strong></td>',
'''<tr><td><strong>Um modelo que entrega relatório</strong></td><td>Fóruns de status, planilhas de acompanhamento, percentuais de conclusão no lugar de resultado; o grupo já confunde "fase de entrega" com "resultado de vendas".<sup>3, 14</sup></td><td>Regra contra o relatório: toda reunião sai com decisão ou incremento; o Fórum recebe demonstração e resultado medido; indicador mensal de reuniões com saída válida (aba O modelo).</td></tr>
<tr><td><strong>A adoção do modelo vira a meta</strong></td><td>Contam-se times criados, ritos realizados e papéis preenchidos como sucesso, sem o desenho que os sustenta; o sistema continua sem entregar.</td><td>Nenhum indicador de adoção no painel; só entregas, tempo de decisão, tempo de ciclo, adoção pela ponta e resultado em 90 dias (abas O modelo e Problema e entregas).</td></tr>
<tr><td><strong>Mais um modelo, e descrédito na Estratégia</strong></td>''')
H = H.replace("<h3>Riscos identificados</h3>\n<table>", "<h3>Riscos identificados</h3>\n<p>Os dois primeiros são os que mais custam, porque fazem o modelo parecer funcionar enquanto o sistema não muda.</p>\n<table>")
F["H"] = H

# ---------------- 5. referências cruzadas
REF = [("(aba 5W2H)", "(aba Proposta)"), ("aba 5W2H", "aba Proposta"), ("aba Blueprint", "aba Desenho e regras"), ("aba Papéis e pessoas", "aba Estrutura"),
       ("aba Sistemas e dados", "aba Estrutura"), ("aba Perguntas de design", "aba Desenho e regras"), ("aba Da estratégia à entrega", "aba Estratégia a entrega"),
       ("abas Da estratégia à entrega e Fluxo funcional", "abas Estratégia a entrega e Fluxo funcional"), ("aba Sutilezas", "aba Análise"), ("aba Modelo", "aba O modelo"),
       ("(aba Modelo)", "(aba O modelo)"), ("Perguntas de design e as dez regras", "Desenho e regras"), ("aba Normas", "aba Estrutura")]
for k in F:
    for a, b in REF: F[k] = F[k].replace(a, b)
for k, s in F.items(): save(f"frag_{k}.html", s)

# ---------------- 6. build.py: abas 20 (2x10), MERGE, fragmentos, CSS, título
b = load("build.py")
b = re.sub(r'TABS = \[.*?\]\n', '''TABS = [("dest", "Destaque"), ("exec", "Executiva"), ("problema", "Problema e entregas"), ("proposta", "Proposta"), ("omodelo", "O modelo"),
        ("alcadas", "Alçadas"), ("ritos", "Reuniões e custo"), ("linear", "Estratégia a entrega"), ("reun", "Fluxo funcional"), ("design", "Desenho e regras"),
        ("entenda", "Entenda"), ("eco", "Ecossistema"), ("proc", "Processos"), ("sint", "Sintomas"), ("estrutura", "Estrutura"),
        ("loops", "Loops"), ("analise", "Análise"), ("cem", "Cem perguntas"), ("gloss", "Glossário"), ("fontes", "Fontes")]
MERGE = {"estrutura": ["normas", "papeis", "sist"], "analise": ["analise", "sut"]}
''', b, count=1, flags=re.S)
b = b.replace('for x in "ABCDEFGH")', 'for x in "ABCDEFGHIJK")')
b = b.replace('''missing = [i for i in ids if i not in panels]''', '''for tgt, parts in MERGE.items():
    inner = []
    for j, p in enumerate(parts):
        body = re.sub(r'^<!-- =+ [A-Z0-9 ]+ =+ -->\\s*<section id="p-[a-z0-9]+" class="pane">', '', panels[p].strip())
        body = re.sub(r'</section>\\s*$', '', body)
        if j < len(parts) - 1:
            body = re.sub(r'<div class="pratica">.*?</div>\\s*(?=$)', '', body, flags=re.S)
        inner.append(body)
    panels[tgt] = '<!-- ============================== %s ============================== -->\\n<section id="p-%s" class="pane">\\n' % (tgt.upper(), tgt) + "\\n<hr style=\\"border:0;border-top:1px solid #e0e0e0;margin:28px 0\\">\\n".join(inner) + '\\n</section>'
missing = [i for i in ids if i not in panels]''')
b = b.replace('head = head.replace("grid-template-columns:repeat(11,max-content)", "grid-template-columns:repeat(12,max-content)")', 'pass')
css = (".tabs{display:grid;grid-template-columns:repeat(10,1fr);column-gap:8px;row-gap:6px;justify-content:stretch;padding-bottom:8px}\\n"
       ".tab{font-size:12.5px;text-align:center;white-space:nowrap;padding:3px 0}\\n"
       "table{font-size:12.5px}th,td{padding:6px 8px}\\n.pane h2{margin-top:6px}\\n.g2 .card{font-size:13.5px}\\nol li,ul li{margin-bottom:5px}\\n")
b = re.sub(r'head = head\.replace\("</style>", """.*?""" \+ ".sel-p\{', 'head = head.replace("</style>", """' + css + '""" + ".sel-p{', b, count=1, flags=re.S)
b = b.replace("<h1>A frente que entrega mais do que consegue decidir: anatomia do GT SUSEP Vida e RE da Seguros Unimed</h1>", "<h1>A frente que entrega mais do que consegue decidir</h1>")
save("build.py", b)
print("patch v8 ok")
