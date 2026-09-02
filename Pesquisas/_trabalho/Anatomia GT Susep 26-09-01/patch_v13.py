# -*- coding: utf-8 -*-
"""v13: síntese + gancho em cada aba, título do Destaque igual ao do documento, encontros sem tempo fixo,
número do KR sem origem, seção 'O que ninguém está falando', Executiva sem explicar o artefato."""
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
def RA(old, new, rx=False):
    n = 0
    for k in F:
        if rx: F[k], m = re.subn(old, new, F[k], flags=re.S)
        else: m = F[k].count(old); F[k] = F[k].replace(old, new)
        n += m
    if n == 0: MISS.append(("*", old[:70]))
SV = '<span class="sel sel-v">Verificado</span>'; SI = '<span class="sel sel-i">Inferência</span>'; SP = '<span class="sel sel-p">Proposta</span>'
def frag_of(pid):
    for k in F:
        if 'id="p-%s"' % pid in F[k]: return k
    return None

# ---------- 1. síntese + gancho
TESES = {
 "dest": ("A frente SUSEP entrega mais do que consegue decidir: um ano e meio de trabalho sem alçada própria, sem braço reservado e sem uma porta única por onde os desafios entram e saem.", "Por que as mesmas pessoas que fazem Ramos Elementares crescer não conseguem destravar Vida?"),
 "exec": ("O que trava a frente vem antes da execução, e três decisões que só a diretoria pode tomar destravam o resto.", "Quais são as três decisões e o que muda em 90 dias se elas forem tomadas?"),
 "problema": ("A frente tem gente, ideias e entregas, mas não tem um sistema que leve um problema da ponta até uma decisão com alçada e um resultado medido.", "O que exatamente sai deste trabalho e como se sabe que funcionou?"),
 "proposta": ("A proposta é desenhar com o próprio grupo o caminho da estratégia à entrega, o fluxo entre áreas, o sistema de reuniões e as alçadas, a partir dos problemas que ele já registrou. " + SP, "Como evitar que isso vire mais um modelo que entrega relatório?"),
 "omodelo": ("O modelo separa quem dirige de quem entrega, define o que cada camada deve à outra e mede o sucesso do sistema, nunca da adoção do modelo.", "Quantas reuniões isso exige e o que a execução tem de entregar a cada ciclo?"),
 "alcadas": ("Nenhuma ata define alçada, e por isso toda decisão relevante sobe; aqui estão dez decisões com dono, consultados, escalada e prazo.", "Quem decide o esgotamento de comissão e em quantos dias a resposta volta?"),
 "ritos": ("O sistema de reuniões proposto custa R$ 381.625 por ano a R$ 125 a hora, contra R$ 286.500 do atual, e a diferença compra triagem, descoberta e revisão de resultado. " + SP, "Que reunião deixa de existir e o que cada uma passa a decidir?"),
 "linear": ("Um desafio percorre oito etapas, cada uma com entrada, saída, alçada e critério de passagem, e volta ao planejamento como resultado ou lição.", "Onde o prestamista de prêmio único teria parado neste caminho, e onde parou de fato?"),
 "reun": ("O problema nasce em cinco origens, entra por uma porta única, é descoberto e concebido pelo time dedicado e sai por um de cinco destinos.", "Quando acontece a descoberta e o que sobe para RDS e COMEX?"),
 "design": ("O que a frente tem é um problema de desenho, não de pessoas: as vinte perguntas de desenho organizacional mostram onde faltam porta, alçada, tipologia e regra.", "Quais são as dez regras sem as quais o fluxo não funciona?"),
 "entenda": ("A frente nasceu em abril de 2025 para fazer Vida e Ramos Elementares crescerem 20% ao ano, com papéis definidos no papel e sem o caminho da informação entre eles.", "O que o planejamento previu e o que as atas mostram que aconteceu?"),
 "eco": ("O núcleo depende de treze atores e não comanda nenhum.", "De quem a frente recebe o quê, e quem recebe dela?"),
 "proc": ("Os desafios entram por oito portas, sem triagem, e saem sem registro: resolvidos, esquecidos, estacionados ou fechados para limpar o histórico.", "Por onde entrou o esgotamento de comissão e onde ele parou?"),
 "sint": ("Setenta e dois sintomas em seis categorias repetem um padrão: os mais frequentes são de agenda; os mais caros são os que travam decisão.", "Quais cinco sintomas custam mais negócio?"),
 "estrutura": ("O grupo tem regras de convivência muito boas e regras de decisão quase inexistentes; papéis e sistemas seguem o mesmo padrão.", "O que a frente é obrigada a cumprir e o que ninguém definiu?"),
 "loops": ("Dois laços viciosos explicam por que Vida não repete o que RE conseguiu; o laço virtuoso prova que o grupo sabe fazer.", "Qual alavanca quebra o laço sem trazer a medicina para dentro da frente?"),
 "analise": ("O maior risco não é o mercado: é o desenho continuar igual enquanto o prazo da Unicred, a campanha de VG e a meta de 20% correm.", "Qual dos três cenários está mais perto de acontecer?"),
}
for pid, (sint, gancho) in TESES.items():
    k = frag_of(pid)
    if not k: MISS.append(("?", "aba " + pid)); continue
    sec = re.search(r'(<section id="p-%s" class="pane">.*?</section>)' % pid, F[k], re.S).group(1)
    new = re.sub(r'<p class="tese">.*?</p>', '<p class="tese">%s</p>\n<p class="gancho">%s</p>' % (sint, gancho), sec, count=1, flags=re.S)
    if new == sec: MISS.append((k, "tese " + pid))
    F[k] = F[k].replace(sec, new)

# ---------- 2. título do Destaque igual ao do documento
R("A", "<h2>A matéria de capa: a frente que entrega mais do que consegue decidir</h2>", "<h2>A frente que entrega mais do que consegue decidir</h2>")

# ---------- 3. encontros sem tempo fixo
R("G", "Construir o desenho com o próprio grupo em seis sessões, em seis semanas, partindo dos problemas que ele registrou:", "Construir o desenho com o próprio grupo, em encontros cuja quantidade e duração se negociam com a disponibilidade dos participantes, partindo dos problemas que ele registrou:")
R("G", "Seis sessões em seis semanas com o próprio grupo (aba Proposta).", "Encontros de desenho com o próprio grupo, em agenda negociada com os participantes (aba Proposta).")
R("G", "calibrar nas sessões (aba Proposta)", "calibrar nos encontros com o time (aba Proposta)")
R("H", "Um trabalho de seis semanas, conduzido pela Estratégia com o grupo, que produz seis desenhos", "Um trabalho conduzido pela Estratégia com o grupo, em encontros cuja quantidade e duração se negociam com a disponibilidade dos participantes, que produz seis desenhos")
R("H", "<th>Sai da sessão</th>", "<th>Sai do encontro</th>")
R("H", "<h3>As seis sessões</h3>", "<h3>Os encontros de desenho</h3>")
R("H", "<th>Semana</th><th>Sessão</th><th>Quem</th><th>Duração</th><th>Entra</th><th>Sai</th>", "<th>Encontro</th><th>Quem</th><th>Entra</th><th>Sai</th>")
sec = re.search(r"<h3>Os encontros de desenho</h3>\s*<table>.*?</table>", F["H"], re.S)
if sec:
    t = sec.group(0)
    t2 = re.sub(r"<tr><td>\d</td>(<td>.*?</td>)(<td>.*?</td>)<td>[^<]*</td>(<td>.*?</td>)(<td>.*?</td>)</tr>", r"<tr>\1\2\3\4</tr>", t)
    F["H"] = F["H"].replace(t, t2)
else: MISS.append(("H", "tabela encontros"))
R("H", r"Cerca de 12 horas do núcleo, 2 horas de mentores, 2 de superintendentes, ao longo de seis semanas\. A R\$ 125 a hora e com dez pessoas por sessão, o trabalho custa perto de R\$ 16 mil em horas de sala, menos que um mês do sistema de reuniões atual \(aba Reuniões e custo\)\.", "A quantidade, a duração e a ordem dos encontros são negociadas com os participantes conforme a disponibilidade de cada um. O custo em horas de sala é calculado com a mesma ficha das reuniões (aba Reuniões e custo) assim que a agenda existir.", rx=True)
R("H", "Acordo de que a primeira sessão é sobre problemas, não sobre formato, e de que o formato sai das sessões.", "Acordo de que o primeiro encontro é sobre problemas, não sobre formato, e de que o formato sai dos encontros.")
R("H", "Duas horas de mentores na semana 4, para as alçadas.", "Presença dos mentores no encontro de alçadas.")
R("H", "Uma resposta, até a semana 5, sobre capacidade", "Uma resposta, antes do encontro de papéis, sobre capacidade")
R("H", "Cada sessão começa pelo espelho", "Cada encontro começa pelo espelho")
R("H", "Nenhuma sessão discute", "Nenhum encontro discute")
R("H", "O custo não é o das seis sessões", "O custo não é o dos encontros")
R("H", "a sessão 3 decide", "o encontro de reuniões e custo decide")
R("H", "a sessão 5 formaliza o pedido", "o encontro de papéis formaliza o pedido")
R("H", "Sessão 1 é só problemas; papéis ficam para a sessão 5.", "O primeiro encontro é só problemas; papéis ficam para o último.")
R("H", "Dedicação declarada por pessoa na sessão 5", "Dedicação declarada por pessoa no encontro de papéis")
R("H", "Sessão 4 com mentores; tabela de alçadas assinada", "Encontro de alçadas com os mentores; tabela assinada")
R("H", "As sessões 1 e 2 cabem antes do primeiro fórum", "Os encontros de problemas e de fluxo cabem antes do primeiro fórum")
R("H", "insumo da sessão 2; a Agilidade participa das sessões 2 e 3", "insumo do encontro de fluxo; a Agilidade participa dos encontros de fluxo e de reuniões")
R("H", "Sala de guerra desde a semana 2", "Sala de guerra desde o encontro de fluxo")
R("H", "meta definida na sessão 6", "meta definida no encontro de piloto e medição")
R("H", "as sessões partem dos problemas das áreas", "os encontros partem dos problemas das áreas")
R("H", "se depois das sessões o grupo concluir", "se depois dos encontros o grupo concluir")
R("H", "validar nas sessões", "validar nos encontros com o time")
R("K", "<th>Semana</th>", "")
sec = re.search(r"<h3>As entregas</h3>\s*<table>.*?</table>", F["K"], re.S)
if sec:
    t = sec.group(0)
    t2 = re.sub(r"(<tr>(?:<td>.*?</td>){3})<td>\d</td>", r"\1", t)
    F["K"] = F["K"].replace(t, t2)
else: MISS.append(("K", "tabela entregas"))
R("K", "Na semana 6, a mesa tem nove entregas", "Ao fim dos encontros, a mesa tem nove entregas")
R("K", "lista de problemas da semana 1", "lista de problemas do primeiro encontro")
R("J", "na sessão 4 (aba Proposta)", "no encontro de alçadas (aba Proposta)")
R("C", "Em duas sessões o grupo terá feito", "Em dois encontros o grupo terá feito")
R("C", " ao longo de seis semanas; sem contratação externa", "; sem contratação externa")
R("C", "Sessões 1 a 6 realizadas até novembro", "Encontros de desenho realizados até novembro")
R("D", "Seis sessões em seis semanas; cerca de 12 horas do núcleo.", "O que a disponibilidade dos participantes permitir: a quantidade e a duração dos encontros são negociadas com o grupo, e o custo em horas de sala é calculado antes de começar.")
R("D", "validação nas sessões", "validação nos encontros com o time")
R("I", "desenho a validar nas sessões com o time", "desenho a validar nos encontros com o time")
RA("nas sessões", "nos encontros"); RA("das sessões", "dos encontros"); RA("a primeira sessão", "o primeiro encontro"); RA("A primeira sessão", "O primeiro encontro"); RA("por sessão", "por encontro")

# ---------- 4. número do KR sem origem explicada
R("K", r"(<tr><td><strong>5\. Resultado não medido\.</strong>.*?</tr>)", r"\1\n<tr><td><strong>6. Número sem origem explicada.</strong> Ninguém consegue explicar de onde vem o número do KR.</td><td>A meta de 20% é mantida como acordo com mentores, o grupo trabalha com o número da Controladoria, em julho ninguém sabe o fechamento de 2024; nenhuma ata registra se o OKR foi construído com o grupo ou comunicado a ele.<sup>3, 6, 20, 24</sup></td><td>Número-base assinado e aberto por ramo; cada KR com origem escrita, dono e forma de cálculo (abas Alçadas e O modelo).</td></tr>", rx=True, count=1)
R("K", "<h3>O problema que a proposta resolve</h3>", "<h3>O problema que a proposta resolve</h3>\n<p>Seis subproblemas, cada um com a evidência nas atas e o que a proposta entrega para ele.</p>")
R("J", "Controladoria e Estratégia em sistemas separados; número de 2024 desconhecido.<sup>20, 24</sup>", "Controladoria e Estratégia em sistemas separados; número de 2024 desconhecido; as atas não registram de onde vem o número do KR nem se o OKR foi construído com o grupo ou comunicado.<sup>3, 6, 20, 24</sup>")
R("F", r"(<td><strong>Direção e metas</strong></td><td>)(.*?)(</td>)", r"\1\2 Ninguém explica de onde vem o número do KR; as atas não dizem se o OKR foi construído com o grupo ou comunicado a ele.<sup>3, 6, 20, 24</sup>\3", rx=True, count=1)
R("G", r'(<div class="card"><strong>Vida perde na porta, não no preço\.</strong>.*?</div>)', r'\1\n<div class="card"><strong>O número não tem dono.</strong> A meta de 20% é mantida como acordo com mentores, o grupo trabalha com o número da Controladoria, ninguém sabe o fechamento de 2024, e nenhuma ata diz de onde vem o número do KR nem se o OKR foi construído com o grupo ou comunicado a ele.<sup>3, 6, 20, 24</sup> ' + SV + '</div>', rx=True, count=1)

# ---------- 5. O que ninguém está falando (Destaque)
NING = '''
<h3>O que ninguém está falando</h3>
<p>Seis coisas que as atas mostram e nenhuma reunião diz em voz alta.</p>
<ul>
<li><strong>A frente não tem alçada, e ninguém escreveu isso.</strong> Toda decisão relevante sobe; nenhuma ata define o que o grupo pode decidir sozinho. Fala-se de agenda, de método e de fórum; não se fala de poder de decidir.<sup>9, 17, 22</sup></li>
<li><strong>Ninguém explica de onde vem o número do KR.</strong> A meta de 20% é mantida como acordo com mentores, o grupo trabalha com o número da Controladoria, ninguém sabe o fechamento de 2024, e nenhuma ata registra se o OKR foi construído com o grupo ou comunicado a ele.<sup>3, 6, 20, 24</sup></li>
<li><strong>Vida não trava na frente; trava numa regra que a frente não controla.</strong> Aceitação médica e compliance decidem caso a caso, sem alçada compartilhada e sem via de reconsideração registrada; a frente discute cotador e campanha.<sup>10, 11, 18, 23</sup></li>
<li><strong>O braço acabou e a meta continuou a mesma.</strong> Três consultores saíram sem data de reposição, a operação declarou que não cabe OKR novo, e nenhuma ata liga uma coisa à outra.<sup>14, 16, 20, 22</sup></li>
<li><strong>O esgotamento de comissão esperou dois anos por 36 minutos.</strong> O tema mais caro para RE ficou parado de 2024 a agosto de 2026 e foi destravado numa reunião curta; o que faltou não foi análise, foi acesso a quem decide.<sup>9, 23</sup></li>
<li><strong>O novo modelo está sendo discutido antes de dizer o que ele entrega.</strong> Times dedicados, fórum e papéis entram na conversa antes da lista de problemas, com as mesmas pessoas em todos os fóruns; o receio de mais um modelo sem resultado foi dito dentro da própria Estratégia.<sup>26, 27</sup></li>
</ul>
<p>Os fatos vêm das atas e das transcrições. ''' + SV + ''' A ligação entre eles é leitura deste documento. ''' + SI + '''</p>
'''
m = re.search(r"<h3>Em resumo</h3>.*?</ul>", F["A"], re.S)
if m: F["A"] = F["A"].replace(m.group(0), m.group(0) + NING, 1)
else: MISS.append(("A", "Em resumo"))

for k, s in F.items(): save(f"frag_{k}.html", s)

# ---------- 6. Na prática (pratica.py): Executiva sem explicar o artefato; Destaque sem meta
p = load("pratica.py")
old = "Se a Estratégia levar uma única folha para a diretoria, é esta. A frase de abertura: a frente SUSEP entrega mais do que consegue decidir."
new = "O diagnóstico cabe em uma frase: a frente SUSEP entrega mais do que consegue decidir."
if old in p: p = p.replace(old, new)
else: MISS.append(("pratica", "única folha"))
p = p.replace("O pedido: três decisões que só a diretoria pode tomar", "O que ele envolve: três decisões que só a diretoria pode tomar")
p = p.replace("Antes de abrir as demais abas, vale olhar", "Vale olhar")
p = p.replace("que o restante do documento mede", "que este diagnóstico mede")
p = p.replace("A primeira sessão cabe numa quinta de manhã", "O primeiro encontro cabe numa quinta de manhã")
p = p.replace("Em duas sessões o grupo terá feito", "Em dois encontros o grupo terá feito")
p = p.replace("nas sessões", "nos encontros").replace("das sessões", "dos encontros")
save("pratica.py", p)
# ---------- 7. CSS do gancho
b = load("build.py")
if ".gancho{" not in b:
    b = b.replace(".sel-p{background:#e8f0fe;color:#1a4a8a}", ".sel-p{background:#e8f0fe;color:#1a4a8a} .gancho{font-family:Georgia,serif;font-style:italic;font-size:16.5px;color:#4a4a4a;margin:-10px 0 22px;padding-left:14px;border-left:3px solid #b71c1c}", 1)
save("build.py", b)
print("patch v13 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
