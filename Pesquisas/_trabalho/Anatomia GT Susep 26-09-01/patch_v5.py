# -*- coding: utf-8 -*-
"""v5: passada de linguagem para leitura pela Estratégia.
1) remove 'O mapa dos órgãos'; 2) transcrições citadas por função, sem falas que exponham pessoas;
3) jargão em inglês em português fora das citações literais; 4) título em tom de diagnóstico."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
def rep(s, a, b, must=True):
    if a not in s:
        if must: raise AssertionError("nao achou: " + a[:90])
        return s
    return s.replace(a, b)

F = {k: load(f"frag_{k}.html") for k in "ABCDEF"}
F["check"] = load("frag_check.html")
B = load("build.py")

# ---------------- 1. mapa dos orgaos
F["A"] = re.sub(r'<h2>O mapa dos órgãos</h2>\s*<div class="g2">.*?</div>\s*(?=</section>)', '', F["A"], count=1, flags=re.S)
assert "O mapa dos órgãos" not in F["A"]

# ---------------- 4. titulo e tese
B = rep(B, "O grupo que entrega, mas não decide: anatomia da frente SUSEP Vida e RE da Seguros Unimed",
        "A frente que entrega mais do que consegue decidir: anatomia do GT SUSEP Vida e RE da Seguros Unimed")
B = rep(B, "Setenta e dois sintomas em 24 atas mostram uma frente competente presa num desenho sem alçada, sem braço reservado e sem porta única para os desafios.",
        "Setenta e dois sintomas em 24 atas mostram uma frente competente operando num desenho sem alçada definida, sem braço reservado e sem porta única para os desafios.")
F["A"] = rep(F["A"], "A matéria de capa: o grupo que entrega, mas não decide", "A matéria de capa: a frente que entrega mais do que consegue decidir")
F["A"] = rep(F["A"], "É o que as atas descrevem: a sala de cirurgia funciona; o hospital, não.", "É o que as atas descrevem: a sala de cirurgia funciona; falta o hospital em volta dela.")

# ---------------- 2. transcricoes por funcao; falas sensiveis fora
# Destaque
F["A"] = rep(F["A"], '<li><strong>A reunião de 1º de setembro confirma o diagnóstico pela boca de quem facilita.</strong> Fabíola: "são sempre quase as mesmas pessoas nos demais fóruns", "os assuntos eles entram e eles se confundem nas agendas", "as pessoas elas olham silados", "a gente tá deduzindo por eles". Camila: "existe uma pressa das coisas acontecerem, mas ainda eu sinto que tá sem estrutura", "eu não tô vendo o problema", "a gente tá atrás com método antes do problema".<sup>26</sup>',
    '<li><strong>A reunião de 1º de setembro, na própria Estratégia, chega ao mesmo diagnóstico.</strong> A facilitação da frente registra que "são sempre quase as mesmas pessoas nos demais fóruns" e que "os assuntos eles entram e eles se confundem nas agendas"; a equipe chamada a estruturar o novo modelo observa que "existe uma pressa das coisas acontecerem, mas ainda eu sinto que tá sem estrutura" e que "a gente tá atrás com método antes do problema".<sup>26</sup>')
# Entenda
F["A"] = rep(F["A"], 'A Estratégia quer transformar as frentes: juntar Frente, S&amp;OP e Diagnóstico numa squad única, com o fórum como rito de entrega; o modelo de squad proposto por Ingrid "não está batido o martelo", os papéis estão "nebulosos" e, na versão discutida, "não vai TI".<sup>26</sup>',
    'A Estratégia quer transformar as frentes: juntar Frente, S&amp;OP e Diagnóstico num time dedicado único, com o fórum como rito de entrega; o modelo de time dedicado proposto pela Agilidade ainda está em construção ("não está batido o martelo"), com papéis em definição e a participação da TI em aberto.<sup>26</sup>')
F["A"] = rep(F["A"], "Em 1º de setembro, Fabíola descreve a cadeia inteira em uma frase:", "Em 1º de setembro, a facilitação da frente descreve a cadeia inteira em uma frase:")
# Ecossistema
F["A"] = rep(F["A"], '<tr><td><strong>Patrocínio da transformação</strong> (Flávio; Caio e Dani na Estratégia; Ingrid no desenho da squad)</td><td>Quem quer transformar as frentes em squad e fórum de negócio.</td><td>Flávio "tem pressa"; Caio e Dani conversam com Ingrid; o modelo "não está batido o martelo"; Camila: "A grande questão é você convencer Caio e Daniel Dani disso".<sup>26</sup></td><td>Define o formato antes do problema, na leitura de Camila. <span class="sel sel-v">Verificado</span></td></tr>',
    '<tr><td><strong>Transformação das frentes</strong> (diretoria, Estratégia e VMO, Agilidade)</td><td>Quem conduz a mudança das frentes para times dedicados e fórum de negócio.</td><td>Urgência da diretoria; Estratégia e Agilidade desenham o modelo em conjunto; em 1º de setembro "não está batido o martelo".<sup>26</sup></td><td>O formato está sendo definido antes do problema, na leitura da própria reunião. <span class="sel sel-v">Verificado</span></td></tr>')
# Processos
F["A"] = rep(F["A"], 'é exatamente a pergunta de Camila: "o que que essa squad vai entregar? Porque se ela não tem TI...".<sup>26</sup>',
    'é a pergunta feita na própria reunião: o que o time dedicado vai entregar se a TI não fizer parte dele.<sup>26</sup>')
F["A"] = rep(F["A"], "A proposta é \"pegar essas três agendas e virar uma squad onde a gente possa falar de todos os assuntos que permeiam a SUSEP\", começando por Vida.",
    "A proposta é \"pegar essas três agendas e virar uma squad onde a gente possa falar de todos os assuntos que permeiam a SUSEP\", começando por Vida.")
# Sintomas: tabela da fonte 26
F["B"] = rep(F["B"], '<p>Nenhum sintoma novo de categoria; todos reforçam os existentes. A novidade é que aparecem na fala de quem facilita a frente (Fabíola) e de quem é chamada a estruturar o novo modelo (Camila), a semanas de uma decisão de formato.<sup>26</sup></p>',
    '<p>Nenhum sintoma novo de categoria; todos reforçam os existentes. A novidade é que aparecem na fala da própria Estratégia, a semanas de uma decisão de formato.<sup>26</sup> As falas são citadas por função, não por pessoa.</p>')
F["B"] = rep(F["B"], '<thead><tr><th>Sintoma reforçado</th><th>Fala literal</th><th>Quem</th></tr></thead>', '<thead><tr><th>Sintoma reforçado</th><th>Fala literal</th><th>Função</th></tr></thead>')
rows_old = re.search(r'(<tr><td>Comitês paralelos com as mesmas pessoas.*?</tbody>)', F["B"], re.S).group(1)
rows_new = '''<tr><td>Comitês paralelos com as mesmas pessoas; assuntos confusos</td><td>"são sempre quase as mesmas pessoas nos demais fóruns"; "os assuntos eles entram e eles se confundem nas agendas"</td><td>Facilitação da frente</td></tr>
<tr><td>Cada área olha o próprio problema</td><td>"cada área vê o seu próprio problema"; "Não tem um um o todo trabalhando em prol"</td><td>Facilitação da frente</td></tr>
<tr><td>Dedicação: a rotina vence a frente</td><td>"as pessoas dão mais atenção mesmo paraas suas coisas diárias do que para as coisas da frente, porque é onde tá ligada a meta, onde no final do mês vai bater o dinheiro dele"</td><td>Facilitação da frente</td></tr>
<tr><td>Método antes do problema</td><td>"a gente tá atrás com método antes do problema, antes do porquê"; "Para mim é só um formato, mudei de uma coisa para outra, mas o que que eu tô tratando?"</td><td>Estratégia (estruturação do modelo)</td></tr>
<tr><td>Perguntar às áreas em vez de deduzir por elas</td><td>"Me fala qual é o teu problema, eu quero resolver, mas você precisa me falar qual é"</td><td>Facilitação da frente</td></tr>
<tr><td>Time dedicado sem engrenagem</td><td>"se eu não tiver uma engrenagem para fazer isso funcionar, não adianta nada eu ter rito"</td><td>Estratégia (estruturação do modelo)</td></tr>
<tr><td>Papéis ainda em definição</td><td>"ainda um pouco nebuloso essa questão dos papéis"; "não está batido o martelo ainda"</td><td>Facilitação da frente</td></tr>
<tr><td>Urgência e risco de descrédito</td><td>"existe uma pressa das coisas acontecerem, mas ainda eu sinto que tá sem estrutura"; sobre tentar mais um modelo e não funcionar: "esse é o meu medo"</td><td>Estratégia (estruturação do modelo)</td></tr>
<tr><td>Frente longe da ponta e sem tempo</td><td>"a frente tá nesse ponto de não temos tempo, tá todo mundo corrido, tá todo mundo desesperado"</td><td>Facilitação da frente</td></tr>
<tr><td>Diagnóstico que funcionou e priorização que não aconteceu</td><td>"Funcionou quando a gente bota eles na mesa e fala assim: O que que você quer trabalhar?"; "eles fizeram uma planilha gigantesca de uma segunda fase que aí eles não conseguem ou não querem ou não tem tempo [...] de fazer essa priorização"</td><td>Facilitação da frente</td></tr>
<tr><td>Venda sem a matriz estruturante</td><td>"Todo mundo fica só preocupado em venda, venda, venda e esquece que existe uma uma matriz estruturante por trás"</td><td>Estratégia (estruturação do modelo)</td></tr>
<tr><td>Desalinhamento sobre quem está fazendo o quê</td><td>"eu achava que vocês já estavam trabalhando nisso"; "E eu também tava achando que vocês já estavam trabalhando"</td><td>Estratégia e facilitação</td></tr>
</tbody>'''
F["B"] = F["B"].replace(rows_old, rows_new)
F["B"] = rep(F["B"], 'Nota de leitura: a transcrição é automática e traz grafias como "silados", "milp", "TTI" e "Inrid"; foram mantidas como estão.', 'Nota de leitura: a transcrição é automática; grafias foram mantidas como estão.')
# Normas
F["B"] = rep(F["B"], 'O modelo do Fórum de Negócio SUSEP e da squad "não está batido o martelo"; os papéis (PM, PO, scrum master) estão "nebulosos"; a versão discutida "não vai TI"; e a Estratégia hesita entre esperar o modelo evoluir ou "colocar na mesa" as dores antes.<sup>26</sup>',
    'O modelo do Fórum de Negócio SUSEP e do time dedicado "não está batido o martelo"; os papéis estão "nebulosos"; a participação da TI no time está em aberto; e a Estratégia pondera entre esperar o modelo evoluir ou "colocar na mesa" as dores antes.<sup>26</sup>')
# Papeis
F["B"] = rep(F["B"], '<li><strong>Papel antes do problema.</strong> A cogitação de nomear a líder comercial como PM da squad é recebida por Camila como "zero sentido" enquanto o problema não estiver claro.<sup>26</sup> <span class="sel sel-v">Verificado</span></li>\n<li><strong>Mentor isento.</strong> Para Camila, quem arbitra "tinha que ser uma pessoa isenta, porque cada um puxa pro seu".<sup>26</sup> <span class="sel sel-v">Verificado</span></li>\n<li><strong>Tempo integral é ficção.</strong> Fabíola lembra que squad pressupõe',
    '<li><strong>Papel antes do problema.</strong> A nomeação de responsáveis pelo time dedicado foi cogitada antes de o problema estar enunciado, e a própria reunião apontou a inversão.<sup>26</sup> <span class="sel sel-v">Verificado</span></li>\n<li><strong>Arbitragem sem interesse direto.</strong> A reunião sugeriu que a arbitragem entre áreas fique com quem não responde pelo resultado de uma delas.<sup>26</sup> <span class="sel sel-i">Inferência</span> sobre fala verificada.</li>\n<li><strong>Tempo integral é ficção.</strong> A facilitação lembra que um time dedicado pressupõe')
# Loops
F["C"] = rep(F["C"], 'Em 1º de setembro, os dois laços viciosos aparecem em uma única fala de Fabíola:', 'Em 1º de setembro, os dois laços viciosos aparecem em uma única fala da facilitação da frente:')
F["C"] = rep(F["C"], 'e "cada área vê o seu próprio problema. Ela não fala do problema da outra área para não interferir".<sup>26</sup>', 'e "cada área vê o seu próprio problema".<sup>26</sup>')
# Modelo
F["C"] = rep(F["C"], 'braço (Camila: "se ela não tem TI", o que entrega?)', 'braço (o que o time entrega se a TI não estiver nele?)')
# Analise
F["C"] = rep(F["C"], 'Papéis nomeados antes da lista de problemas; squad sem TI; Camila: "esse é o meu medo"', 'Papéis nomeados antes da lista de problemas; time dedicado sem TI; receio de descrédito registrado na própria reunião')
# Sutilezas: remover tres itens
for start in ('<li><strong>"Muro das lamentações".</strong>', '<li><strong>A Estratégia sabe que está deduzindo.</strong>', '<li><strong>Quem dá a notícia ruim.</strong>'):
    F["C"] = re.sub(re.escape(start) + r'.*?</li>\s*', '', F["C"], count=1, flags=re.S)
    assert start not in F["C"]
# Check
F["check"] = rep(F["check"], 'mais uma reunião em que a facilitadora do grupo é uma das duas vozes.', 'mais duas reuniões em que a facilitação do grupo é uma das vozes.')
F["check"] = rep(F["check"], 'O autor deste documento estava na reunião e propôs, várias vezes, a mesma leitura que o documento defende. Camila concorda com ele em voz alta.', 'O autor deste documento estava na reunião e propôs, várias vezes, a mesma leitura que o documento defende, e as participantes concordaram em voz alta.')
F["check"] = rep(F["check"], 'Citar só as falas de Fabíola e Camila mitiga', 'Citar só as falas das participantes da Estratégia mitiga')
F["check"] = rep(F["check"], 'O que sustenta o uso é que as falas mais fortes de Fabíola ("são sempre quase as mesmas pessoas", "as pessoas elas olham silados", "a gente tá deduzindo por eles", "muro das lamentações") descrevem fatos anteriores à reunião e independentes da proposta do autor; e que a preocupação central de Camila ("o que que essa squad vai entregar? Porque se ela não tem TI") nasceu de uma conversa com Ingrid, antes de o autor falar.',
    'O que sustenta o uso é que as falas mais fortes da facilitação ("são sempre quase as mesmas pessoas", "cada área vê o seu próprio problema") descrevem fatos anteriores à reunião e independentes da proposta do autor; e que a preocupação central sobre o que o time dedicado entrega sem a TI nasceu de uma conversa com a Agilidade, antes de o autor falar.')
F["check"] = rep(F["check"], 'com erros de grafia mantidos entre aspas ("silados", "milp", "TTI", "Inrid") e sem revisão das participantes.', 'com erros de grafia mantidos entre aspas e sem revisão das participantes. Neste documento as duas transcrições são citadas por função, não por pessoa.')
# Fluxo funcional
F["E"] = rep(F["E"], 'O que a Ingrid descreveu como "o problema ele não vai chegar cru, ele vai chegar com um diagnóstico" é exatamente essa etapa.<sup>27</sup>', 'O que a Agilidade descreveu como "o problema ele não vai chegar cru, ele vai chegar com um diagnóstico" é exatamente essa etapa.<sup>27</sup>')
F["E"] = rep(F["E"], 'A base é o modelo de squad descrito pela Ingrid em 1º de setembro e o fórum de negócio descrito pela Fabíola.<sup>26, 27</sup>', 'A base é o modelo de time dedicado descrito pela Agilidade em 1º de setembro e o fórum de negócio descrito pela facilitação da frente.<sup>26, 27</sup>', must=False)
# Design
F["F"] = rep(F["F"], 'A fila da TI é uma restrição que não muda com o organograma.</strong> "Projetos são frequentemente trocados por emergências operacionais"; "A fala dela é que não vai TTI"; "tem que haver o critério', 'A fila da TI é uma restrição que não muda com o organograma.</strong> "Projetos são frequentemente trocados por emergências operacionais"; "tem que haver o critério')
F["F"] = rep(F["F"], '<sup>22, 26, 27</sup> Qualquer PM, PO ou scrum master vai esbarrar na mesma fila.', '<sup>22, 27</sup> Qualquer responsável nomeado vai esbarrar na mesma fila.')
F["F"] = rep(F["F"], '<div class="card"><strong>8. A própria Estratégia reconhece que é formato antes de problema.</strong> "Para mim é só um formato, mudei de uma coisa para outra, mas o que que eu tô tratando?"; "a gente tá atrás com método antes do problema"; "a gente tá deduzindo por eles".<sup>26</sup> Nomear a Jaque como PM é "zero sentido" enquanto o problema não estiver claro, na leitura de Camila.<sup>26</sup> <span class="sel sel-v">Verificado</span></div>',
    '<div class="card"><strong>8. A própria Estratégia reconheceu, na reunião de 1º de setembro, que o formato vinha antes do problema.</strong> "Para mim é só um formato, mudei de uma coisa para outra, mas o que que eu tô tratando?"; "a gente tá atrás com método antes do problema".<sup>26</sup> A conclusão da reunião foi começar pela lista de problemas das áreas. <span class="sel sel-v">Verificado</span></div>')
F["F"] = rep(F["F"], 'Hoje, "eu não tô vendo o problema".<sup>26</sup>', 'Na reunião de 1º de setembro, o problema ainda não estava enunciado.<sup>26</sup>')
F["F"] = rep(F["F"], '"Esse é o meu medo": cair em descrédito com as áreas.<sup>26</sup>', 'O receio, dito na reunião, de cair em descrédito com as áreas.<sup>26</sup>')
F["F"] = rep(F["F"], 'Vale também para PO de mercado quando não há perfil interno, com curadoria e transferência de conhecimento, como a própria Ingrid propôs.<sup>27</sup>', 'Vale também para um responsável de produto contratado no mercado quando não há perfil interno, com curadoria e transferência de conhecimento, como a Agilidade propôs.<sup>27</sup>')
F["F"] = rep(F["F"], 'Para levar a Caio, Dani, Flávio e ao próprio grupo.', 'Para levar à Estratégia, à diretoria e ao próprio grupo.')
F["F"] = rep(F["F"], '"Atoladas nas suas próprias áreas."<sup>26</sup>', 'A rotina "toma muito mais do que o 100% do tempo".<sup>26</sup>')
# Cem perguntas e glossario e fontes
F["D"] = rep(F["D"], 'é o que Fabíola ("me fala qual é o teu problema") e Camila ("tudo começa no problema") pedem.<sup>26</sup>', 'é o que a própria Estratégia pediu na reunião de 1º de setembro ("me fala qual é o teu problema").<sup>26</sup>')
F["D"] = rep(F["D"], 'e, na régua de Fabíola, se as áreas "verificarem que realmente tem valor".<sup>26</sup>', 'e, na régua da facilitação da frente, se as áreas "verificarem que realmente tem valor".<sup>26</sup>')
F["D"] = rep(F["D"], 'na descrição da Ingrid, em três camadas', 'na descrição da Agilidade, em três camadas')
F["D"] = rep(F["D"], 'Regra de uso: apenas as falas de Fabíola e Camila valem como evidência; as intervenções de Eric são do autor deste diagnóstico e não são citadas como fonte.', 'Regra de uso: apenas as falas das duas participantes da Estratégia valem como evidência, citadas por função; as intervenções do autor deste diagnóstico não são citadas como fonte.')
F["D"] = rep(F["D"], 'Usada apenas na aba Fluxo funcional. Grafias da transcrição mantidas entre aspas.', 'Usada nas abas Fluxo funcional e Perguntas de design, com as falas citadas por função. Grafias da transcrição mantidas entre aspas.')

# ---------------- 3. jargão em inglês fora das citações e das tags
TERMS = [
    (r"\bSala de discovery\b", "Sala de descoberta"), (r"\bsala de discovery\b", "sala de descoberta"),
    (r"\bDiscovery aberto\b", "Descoberta aberta"), (r"\bdiscovery aberto\b", "descoberta aberta"),
    (r"\bDiscovery\b", "Descoberta"), (r"\bdiscovery\b", "descoberta"),
    (r"\bSquad Vida\b", "Time dedicado Vida"), (r"\bSQUAD VIDA\b", "TIME DEDICADO VIDA"),
    (r"\bSquad SUSEP com núcleo fixo\b", "Time dedicado SUSEP com núcleo fixo"), (r"\bSquad de Corretores\b", "Time de Corretores"),
    (r"\bSquad com núcleo fixo \(TI,", "Time dedicado (TI,"), (r"\bLíder da squad\b", "Líder do time"), (r"\bRevisão da squad\b", "Revisão do time"),
    (r"\bsquads\b", "times dedicados"), (r"\bSquads\b", "Times dedicados"), (r"\bsquad\b", "time dedicado"), (r"\bSquad\b", "Time dedicado"),
    (r"\bBAU \(sustentação\)", "Sustentação (rotina)"), (r"\bProblema de BAU\b", "Problema de sustentação"), (r"\bBAU\b", "sustentação"),
    (r"\bAssessment fechado\b", "Avaliação dirigida"), (r"\bassessment fechado\b", "avaliação dirigida"), (r"\bassessment\b", "avaliação dirigida"), (r"\bAssessment\b", "Avaliação dirigida"),
    (r"\bGate \(critério para passar\)", "Critério de passagem"), (r"\bGate para a próxima\b", "Critério para a próxima"), (r"\bgates\b", "critérios de passagem"), (r"\bgate\b", "critério de passagem"),
    (r"\bBacklog da esteira\b", "Carteira da esteira"), (r"\bbacklog\b", "carteira de demandas"), (r"\bBacklog\b", "Carteira de demandas"),
    (r"\bChecklist de pronto\b", "Lista de pronto"), (r"\bchecklist de pronto\b", "lista de pronto"), (r"\bchecklist\b", "lista de verificação"),
    (r"\bKick-off da esteira\b", "Abertura da esteira"), (r"\bkick-off\b", "abertura"),
    (r"\bcross-selling\b", "venda cruzada"), (r"\bcross-sell\b", "venda cruzada"), (r"\bCross-selling\b", "Venda cruzada"), (r"\bCross-sell\b", "Venda cruzada"),
    (r"\bfront-ends\b", "telas de uso"), (r"\bfront-end\b", "tela de uso"), (r"\bFront-end\b", "Tela de uso"),
    (r"\bLead time\b", "Tempo de ciclo"), (r"\blead time\b", "tempo de ciclo"),
    (r"\bfeedback\b", "retorno"), (r"\bonboarding\b", "integração"), (r"\bOnboarding\b", "Integração"),
    (r"\bInsurtechs\b", "Seguradoras digitais"), (r"\binsurtechs\b", "seguradoras digitais"),
    (r"\bmega brokers\b", "grandes corretoras"), (r"\bMega Brokers\b", "grandes corretoras"), (r"\bmega broker\b", "grande corretora"),
    (r"\bbancassurance\b", "seguro no balcão do banco"), (r"\bchurn\b", "cancelamento"),
    (r"\bhub de integração\b", "central de integração"), (r"\bhub de APIs\b", "central de integrações"),
    (r"\bresearch de UX\b", "pesquisa com usuários"), (r"\bResearch/UX\b", "pesquisa com usuários"), (r"\bresearch\b", "pesquisa"),
    (r"\broadmap\b", "plano de entregas"), (r"\bRoadmap\b", "Plano de entregas"),
    (r"\bplanning\b", "planejamento do ciclo"), (r"\breview\b", "revisão"), (r"\bdaily\b", "reunião diária"),
    (r"\bPM, PO e scrum master\b", "Responsáveis de um time dedicado"),
]
def outside_quotes(text, fn):
    parts = text.split('"'); return '"'.join(fn(p) if i % 2 == 0 else p for i, p in enumerate(parts))
def apply_terms(seg):
    for pat, sub in TERMS: seg = re.sub(pat, sub, seg)
    return seg
def transform(html):
    out = []
    for tok in re.split(r"(<[^>]+>)", html):
        out.append(tok if tok.startswith("<") else outside_quotes(tok, apply_terms))
    return "".join(out)
for k in list(F.keys()): F[k] = transform(F[k])

# glossário: manter o termo em inglês entre parênteses uma vez
F["D"] = rep(F["D"], '<div class="card"><strong>Time dedicado.</strong> Time multidisciplinar dedicado a uma entrega, com núcleo fixo e participantes volantes.</div>',
    '<div class="card"><strong>Time dedicado (squad).</strong> Time multidisciplinar dedicado a uma entrega, com núcleo fixo e participantes volantes.</div>')
F["D"] = rep(F["D"], '<div class="card"><strong>Avaliação dirigida e descoberta.</strong>', '<div class="card"><strong>Avaliação dirigida (assessment) e descoberta (discovery).</strong>')
F["D"] = rep(F["D"], '<div class="card"><strong>sustentação.</strong> Business as usual, a rotina de sustentação.</div>', '<div class="card"><strong>Sustentação (BAU).</strong> A rotina que mantém a operação funcionando; no jargão, business as usual.</div>', must=False)
F["D"] = rep(F["D"], '<div class="card"><strong>Responsáveis de um time dedicado.</strong>', '<div class="card"><strong>Responsáveis de um time dedicado (PM, PO, scrum master).</strong>', must=False)

for k in "ABCDEF": save(f"frag_{k}.html", F[k])
save("frag_check.html", F["check"]); save("build.py", B)
print("patch v5 ok")
