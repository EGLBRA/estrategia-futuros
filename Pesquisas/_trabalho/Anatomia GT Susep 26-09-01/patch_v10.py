# -*- coding: utf-8 -*-
"""v10: itens do advogado do diabo (parecer_advogado_v8.md) e restos do checker."""
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
SV = '<span class="sel sel-v">Verificado</span>'; SI = '<span class="sel sel-i">Inferência</span>'; SE = '<span class="sel sel-e">Especulativo</span>'; SP = '<span class="sel sel-p">Proposta</span>'
def section(k, pid):
    m = re.search(r'(<section id="p-%s" class="pane">.*?</section>)' % pid, F[k], re.S); return m.group(1)
def set_section(k, pid, new):
    F[k] = F[k].replace(section(k, pid), new)

# ---------- restos do v9
RA("(Aguiar, Lara, Alex)", "(três superintendentes)")
R("A", "(Fabíola, Caio, Daniele/VMO)", "(facilitação da frente, Estratégia e VMO)")
R("A", "(Daniel, Amanda, V4)", "(analistas e painel V4)")
R("A", "canais (Christian Landi)", "canais")
R("A", "Os mentores são superintendentes: Rodrigo Aguiar (Diretoria Comercial), Lara Facchini e Alex Rocha.", "Os mentores são três superintendentes, um deles da Diretoria Comercial.")
def role(m):
    r = m.group(1)
    r = r.replace("líder;", "Líder da frente;").replace("colíder;", "Colíder;").replace("facilitadora, Estratégia", "Facilitação, área de Estratégia")
    return "<td><strong>" + r[0].upper() + r[1:] + "</strong></td>"
R("B", r'<td><strong>(?:Jacqueline|Alan|Fabíola|Tatiane|Glace|Alessandra|Christian|Aretha|Daniel|Amanda)[^<]*</strong> \(([^)]+)\)</td>', role, rx=True)
R("C", "(líder Jacqueline;", "(líder da frente;"); R("C", "(líder Alan;", "(colíder;")
R("F", "Plano de entregas único</strong> produto, motor, tela de uso e API", "Plano de entregas único</strong> (produto, motor, tela de uso e API)")
R("C", "as 24 atas em sequência", "os 24 documentos em sequência")
R("A", r"repete os principais sem saber que os repet\w+", "repete os principais", rx=True)
RA("Um planta organizacional", "Uma planta organizacional"); RA("o planta organizacional", "a planta organizacional"); RA("no planta organizacional", "na planta organizacional"); RA("do planta organizacional", "da planta organizacional")
R("G", "tempo entre entrada e decisão, decisões com dono, prazo, braço e indicador, quórum dos ritos, itens sem saída explícita", "os oito indicadores do painel (aba O modelo), a começar pelo tempo entre entrada e decisão")

# ---------- Destaque
R("A", "uma única segunda-feira de agosto", "duas segundas-feiras de agosto, 11 e 17,")
R("A", "Às dez da manhã, a reunião semanal:", "Na primeira, às duas da tarde, a reunião semanal:")
R("A", "a reunião com os mentores está marcada para as duas da tarde e uma das mentoras", "a reunião com os mentores fica para a semana seguinte e uma das mentoras")
R("A", "Às duas, em 36 minutos", "Na segunda, às duas da tarde, em 36 minutos")

# ---------- Executiva
R("G", "Mais de vinte entregas entre novembro de 2025 e maio de 2026", "Catorze entregas entre novembro de 2025 e março de 2026, mais de trinta desde o início de 2025")
R("G", "Fórum de agosto pediu evidenciar o gap", "O grupo decidiu em agosto evidenciar o gap no próximo fórum")
R("G", "Ou a capacidade aumenta; sem isso, o time dedicado diagnostica", "Sem critério de despriorização no acelerador, ou mais capacidade, o time dedicado diagnostica")
RA("R$ 382.000", "R$ 381.625"); RA("R$ 286.000", "R$ 286.500"); RA("perto de R$ 381.625", "R$ 381.625"); RA("perto de R$ 286.500", "R$ 286.500")
RA("Sete portas", "Oito portas"); RA("sete portas", "oito portas")
R("K", "Demandas entram por reunião, mensagens, planilhas, S&amp;OP, diagnóstico, Marketing e parceiros.", "Demandas entram por reunião, mensagens, e-mail, planilhas coletivas, S&amp;OP, RDS, Marketing e parceiros.")
R("G", "práticas da corretora digital e fila da TI sobem", "práticas da corretora digital e modelo comercial dos canais sobem")
R("F", "Hoje são oito portas e nenhuma triagem.<sup>21</sup>", "Hoje são oito portas e nenhuma triagem.<sup>21, 26</sup>")

# ---------- Problema e entregas
R("K", "Resposta em 48 horas para cotação aberta;", "Resposta em 48 horas para cotação aberta, como a frente já propôs;<sup>18</sup>")

# ---------- Proposta: selos
R("H", "Primeiro fórum já marcado para setembro", "Primeira agenda do fórum prevista para setembro")
RA(r"já migra para quem paga esgotamento\.?<sup>22, 23</sup>", "perde grandes corretoras para concorrentes.<sup>9, 22</sup>", rx=True)
R("H", r"(A fronteira entre Fórum de Negócio e Fórum de Gestão[^.]*\.)", r"\1 O desenho de partida assume que o Fórum de Negócio substitui o Fórum de Gestão nos temas SUSEP (aba Reuniões e custo).", rx=True, count=1)
sec = section("H", "proposta")
sec2 = re.sub(r"</table>\s*(?!<p><span class=\"sel)", "</table>\n<p>" + SP + "</p>\n", sec)
sec2 = re.sub(r'(<p class="tese">.*?)</p>', r'\1 ' + SP + '</p>', sec2, count=1, flags=re.S)
sec2 = re.sub(r"(<sup>26</sup>)(?!\s*<span)", r"\1 " + SV, sec2, count=1)
set_section("H", "proposta", sec2)

# ---------- O modelo
R("I", "São 51 encontros, a maioria curtos", "São 51 encontros num mês de pico; a média anual custeada na aba Reuniões e custo fica perto de 40 por mês, porque descoberta e sala de guerra não rodam todos os meses. A maioria é de encontros curtos")
R("I", "num mês típico com duas esteiras", "num mês de pico com duas esteiras")
R("I", r"Cinco temas escalados a mentores, RDS ou COMEX entre maio e agosto\.", "Temas escalados entre maio e agosto: esgotamento e pagamentos ao COMEX, práticas da corretora digital à diretoria, Hub e prestamista à RDS, esgotamento e canais aos mentores.", rx=True)
R("I", "nas atas de agosto.<sup>22, 24</sup>", "nas atas de julho e agosto.<sup>22, 24</sup>")
R("I", r"(no mesmo rito)\.(?!<sup>)", r"\1.<sup>3, 12</sup> " + SV, rx=True, count=1)

# ---------- Alçadas
R("J", "Compliance, sem instância de recurso.<sup>11</sup>", "Compliance; a ata não registra via de reconsideração.<sup>11</sup>")
R("J", "Diretoria; reposição de consultores sem data.<sup>16</sup>", "Não registrado nas atas; reposição de consultores em andamento, sem data.<sup>16</sup>")
R("J", "funciona (reprecificação trimestral).<sup>5, 20</sup>", "funciona (reprecificação trimestral).<sup>5, 15, 20</sup>")
R("J", f'<p>A coluna "hoje" vem das atas. {SV} As demais colunas são desenho a assinar. {SP}</p>', f'<p>Os fatos da coluna "hoje" vêm das atas. {SV} As leituras "sem regra" e "não registrado" são deste documento. {SI} As demais colunas são desenho a assinar. {SP}</p>')

# ---------- Reuniões e custo: selos e cadência assumida
sec = section("H", "ritos")
sec2 = sec.replace("<h3>O custo da sala</h3>", f"<p>Cadências, durações e participantes dos ritos são desenho. {SP} A existência e a cadência atual dos ritos citados como existentes vêm das atas. {SV}</p>\n<h3>O custo da sala</h3>", 1)
sec2 = sec2.replace("<h3>Sistema atual (estimado a partir das atas)</h3>", f"<p>{SP}</p>\n<h3>Sistema atual (estimado a partir das atas)</h3>", 1)
sec2 = sec2.replace("<h3>Regras de funcionamento dos ritos</h3>", f"<p>Estimativa deste documento: o número de sessões e de pessoas do S&amp;OP, do Diagnóstico e do Fórum de Gestão não está nas atas. {SE}</p>\n<h3>Regras de funcionamento dos ritos</h3>", 1)
sec2 = re.sub(r'(<p class="tese">.*?)</p>', r'\1 ' + SP + '</p>', sec2, count=1, flags=re.S)
set_section("H", "ritos", sec2)
R("H", "S&amp;OP mensal, diagnóstico mensal", "S&amp;OP e diagnóstico com cadência assumida como mensal, não registrada nas fontes")
R("H", "Conforme governança, a confirmar", "Conforme governança, a confirmar; fora da conta")

# ---------- Estratégia a entrega
R("G", "em três a cinco meses, da ficha ao resultado medido", "em quatro a seis meses da ficha à entrega, e cerca de nove meses até a leitura de 90 dias")
RA("Fórum de Gestão para o que excede a alçada", "Fórum de Negócio para o que excede a alçada"); RA("Fórum de Gestão (30 e 90 dias)", "Fórum de Negócio (30 e 90 dias)")
R("G", "acima dela, Fórum de Gestão", "acima dela, Fórum de Negócio"); R("G", "Fórum de Gestão + PIE", "Fórum de Negócio + PIE")
R("G", "Pedido do canal corretor em 2024; travado por", "Discutido internamente em 2024; travado por")
R("A", "Entra em 2024 como pedido do canal corretor", "Discutido internamente desde 2024")
R("G", "desde o primeiro pedido: mais de dois anos", "desde a primeira discussão, em 2024: cerca de dois anos")
RA("depois de dois anos parado", "depois de cerca de dois anos parado"); RA("mais de dois anos desde o primeiro pedido", "cerca de dois anos desde a primeira discussão")

# ---------- Fluxo funcional: selo Proposta nos cartões de desenho
R("E", r'(<strong>De onde vem o problema\.</strong>.*?' + re.escape(SV) + r')', r'\1 ' + SP, rx=True, count=1)
R("E", r'(<strong>Quando acontece a descoberta\.</strong>.*?' + re.escape(SV) + r')', r'\1 ' + SP, rx=True, count=1)

# ---------- Entenda
R("A", "alimentando e recebendo da TI, dos aceleradores e dos projetos de torre (nos dois sentidos: envia e recebe).<sup>26</sup>", "alimentando e recebendo da TI (nos dois sentidos: envia e recebe); aceleradores e projetos de torre aparecem no esboço da Estratégia e na reunião sobre times dedicados.<sup>26, 27</sup>")

# ---------- Processos
R("A", '("só vida")', ", que trata só de Vida,")
R("A", 'que "funcionou bem, as pessoas sentaram, conversaram"', "que, na leitura da facilitação, funcionou porque as pessoas se sentaram e conversaram")
R("A", "Três casos que mostram o fluxo inteiro", "Quatro casos que mostram o fluxo inteiro")

# ---------- Sintomas e Estrutura
R("B", "<th>Fala literal</th>", "<th>Fala, em paráfrase</th>")
RA(r"a transcrição é automática; grafias foram mantidas como estão\.", "transcrição automática, parafraseada; falas atribuídas por função.", rx=True)
R("B", 'os papéis estão "nebulosos"', "os papéis ainda estão pouco definidos"); R("B", '"colocar na mesa"', "pôr na mesa")
R("B", "Nove pessoas no núcleo, três mentores, uma facilitadora.", "Nove pessoas no núcleo, contando a facilitadora, e três mentores.")

# ---------- Loops
sec = section("C", "loops")
sec2 = sec.replace(f"<p>{SV}</p>", f"<p>Cada elo tem fonte. {SV} O encadeamento causal é leitura deste documento. {SI}</p>")
sec2 = sec2.replace("a auditoria médica só vê as recusas que registrou", "a regra só é revista quando o dado chega à auditoria médica")
sec2 = sec2.replace("ajusta preço trimestralmente e o resultado aparece no mês seguinte.<sup>3, 20</sup>", "ajusta preço trimestralmente e o efeito é acompanhado nas vendas seguintes.<sup>15, 20</sup>")
set_section("C", "loops", sec2)

# ---------- Análise: matriz de riscos ganha o risco principal
R("C", r'(<h3>Matriz de riscos</h3>\s*<table>\s*<thead>.*?</thead>\s*<tbody>\s*)', r'\1<tr><td>O novo modelo passa a entregar relatório e a adoção vira a meta</td><td>Alta</td><td>Alto</td><td>Fórum recebendo percentuais de conclusão em vez de incrementos demonstrados; ritos contados como sucesso (aba Proposta)</td><td>3, 14</td></tr>\n', rx=True, count=1)
RA(' cogitam "refluctuar" a meta', ' cogitaram a "refluctuação" da meta'); RA('"refluctuar"', '"refluctuação"')

# ---------- Glossário
R("D", "Time dedicado (squad)", 'Time dedicado ("squad")'); R("D", "Sustentação (BAU)", 'Sustentação ("BAU")'); R("D", "business as usual", '"business as usual"')
R("D", "Avaliação dirigida (assessment) e descoberta (discovery)", 'Avaliação dirigida ("assessment") e descoberta ("discovery")')
RA('ainda "nebulosos"', "ainda pouco definidos"); R("D", "(PM, PO, scrum master)", '("PM", "PO", "scrum master")')
R("D", "Planning, revisão, reunião diária e retrô.", "Planejamento do ciclo, revisão, reunião diária e retrospectiva.")
R("D", '<div class="card"><strong>OKR e KR.</strong>', '<div class="card"><strong>IM.</strong> Inteligência de Mercado, área que produz painéis de mercado, concorrentes e sinistralidade comparada.</div>\n<div class="card"><strong>PMO.</strong> Escritório de projetos; esteira executora ao lado de TI, Processos e Inovação.</div>\n<div class="card"><strong>VG, VI e AP Escolar.</strong> Vida em Grupo, Vida Individual e Acidentes Pessoais Escolar, produtos da esteira Vida.</div>\n<div class="card"><strong>RCP e PMI.</strong> Responsabilidade Civil Profissional e outros produtos de Ramos Elementares citados nas atas.</div>\n<div class="card"><strong>Prazo de atendimento.</strong> Tempo máximo combinado para responder a um pedido; o que as atas chamam pela sigla em inglês.</div>\n<div class="card"><strong>OKR e KR.</strong>')

# ---------- Fontes
R("D", r"(Nota de método\..*?)</p>", r"\1 Proposta indica desenho proposto para validação nas sessões; não é afirmação sobre a realidade.</p>", rx=True, count=1)
RA("Grafias da transcrição mantidas entre aspas.", "Falas parafraseadas e atribuídas por função.")
R("D", "valem como evidência, citadas por função", "valem como evidência, parafraseadas e citadas por função")
m = re.search(r'<h3>Documento derivado \(25\)</h3>\s*<ol start="25">.*?</ol>\s*', F["D"], re.S)
if m:
    blk = m.group(0); F["D"] = F["D"].replace(blk, "", 1); F["D"] = F["D"].replace("<h3>Reunião de 1º de setembro de 2026 (26)</h3>", blk + "<h3>Reunião de 1º de setembro de 2026 (26)</h3>", 1)
else: MISS.append(("D", "bloco fonte 25"))

for k, s in F.items(): save(f"frag_{k}.html", s)
b = load("build.py"); b = b.replace("Setenta e dois sintomas em 24 atas", "Setenta e dois sintomas em 24 documentos"); save("build.py", b)
print("patch v10 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
