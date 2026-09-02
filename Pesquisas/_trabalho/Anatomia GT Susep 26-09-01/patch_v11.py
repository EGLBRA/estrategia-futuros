# -*- coding: utf-8 -*-
"""v11: rodada 2 (parecer_checker_v10.md + parecer_advogado_v10.md)."""
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
def section(k, pid): return re.search(r'(<section id="p-%s" class="pane">.*?</section>)' % pid, F[k], re.S).group(1)
def set_section(k, pid, new): F[k] = F[k].replace(section(k, pid), new)

# ---- concordância e restos
for a, b in [("numo time dedicado única", "num time dedicado único"), ("numo time dedicado", "num time dedicado"), ("umo time dedicado", "um time dedicado"), ("esso time dedicado", "esse time dedicado"),
             ("O apresentação", "A apresentação"), ("o carteira", "a carteira"), ("renovações iniciado", "renovações iniciada"), ("CoLíder", "Colíder"), ("S&amp;OP , que", "S&amp;OP, que"),
             ("decisão. .", "decisão."), ("<sup>27</sup><sup>27</sup> sustentação não passa por ela", "<sup>27</sup> A sustentação não passa por ela"), ("Deck do PIE", "Apresentação do PIE"),
             ("<h3>Deck de planejamento (1)</h3>", "<h3>Apresentação de planejamento (1)</h3>"), ("Ata do checkpoint semanal", "Ata da reunião semanal"), ("checkpoint semanal", "reunião semanal"),
             ("RDS/COMEX (política e orçamento)", "RDS e COMEX (política e orçamento)"), ("Três perguntas que o esboço não respondia", "Quatro perguntas que o esboço não respondia"),
             ("lente de design organizacional", "lente de desenho organizacional"), ("definiu?</strong> reuniões semanais", "definiu?</strong> Reuniões semanais"), ("Sobe só o sem alteração", "Sobe só o que já existe"),
             ("accountability", "responsabilização"), ("follow-up de cotações abertas", "retorno em 48 horas sobre cotações abertas"), ("nenhum slide de andamento", "nenhuma lâmina de andamento"),
             ("Diretoria comercial com Controladoria", "Diretoria Comercial com Controladoria"), ("<td>3, 14</td>", "<td><sup>3, 14</sup></td>"), ("Existem sete.", "Existem oito."),
             ("em vez de sete pedidos avulsos", "em vez de pedidos avulsos"), ("três semanas depois descobre", "uma semana depois descobre"), ("Mais de duas dezenas de entregas entre 2025 e 2026", "Mais de trinta entregas entre 2025 e 2026"),
             ("Entre novembro de 2025 e maio de 2026 saíram", "Entre novembro de 2025 e março de 2026 saíram"), (" sem perceber que os repete", ""),
             ("como a frente já propôs;<sup>18</sup> reconsideração", "como a frente já propôs.<sup>18</sup> Reconsideração"), ("pedido de reposição.</td>", "pedido de reposição (abas Estrutura e Proposta).</td>"),
             ("regra contra o relatório.</td>", "regra contra o relatório (aba O modelo).</td>"), ("<td>Desenho e regras</td>", "<td>Aba Desenho e regras</td>"),
             ("concorrentes.<sup>9, 22</sup>; e a credibilidade", "concorrentes.<sup>9, 22</sup> E a credibilidade"), ("</sup>; um balcão", "</sup> Um balcão"), ("</sup>; o canal", "</sup> O canal"),
             ("com as falas citadas por função. Falas parafraseadas e atribuídas por função.", "com as falas parafraseadas e atribuídas por função."), ("juízo de intensidade e proposta de desenho está nesta categoria", "juízo de intensidade está nesta categoria"),
             ("sem instância de recurso", "sem via de reconsideração registrada"), ("sem via de recurso para recusas", "recusas sem via de reconsideração registrada"),
             ("3 a 17 de agosto. Treinamento de OKR.", "3 a 17 de agosto. Balanço do treinamento de OKR."), ("guardados no notebook", "guardados no repositório do projeto, o caderno")]:
    RA(a, b)
RA(f'{SP}<sup>3, 11, 15, 21, 22</sup>', f'<sup>3, 11, 15, 21, 22</sup> {SP}')
RA('<span class="sel sel-p">Exemplo</span>', '<small style="font-size:14px;color:#777;font-weight:400">(exemplo para discussão)</small>')

# ---- Destaque
R("A", "práticas da corretora digital, fila da TI: cada um sobe para mentores, RDS ou COMEX.<sup>22</sup>", "práticas da corretora digital, modelo comercial dos canais: cada um sobe para mentores, RDS ou COMEX.<sup>9, 16, 17, 22</sup>")

# ---- piloto: dois temas de Vida; esgotamento vai para a esteira RE
RA("esgotamento de comissão e prestamista de prêmio único", "prestamista de prêmio único e aceitação do Vida")
R("G", "três estruturais em execução, uma sala de guerra.", "três estruturais em execução, uma sala de guerra (duas no piloto de Vida; o esgotamento de comissão abre a sala de guerra da esteira RE).")
R("G", "ao resultado medido: cerca de 6 meses", "ao resultado medido em 90 dias: cerca de nove meses")
R("G", "A tabela completa, com o sistema atual para comparação, está na aba Reuniões e custo. ", "")
R("G", r"(que ninguém registra\.<sup>12, 18</sup>)", r"\1 " + SV, rx=True, count=1)
R("H", "produz seis desenhos assinados pelo time e um plano de piloto; ao todo, as nove entregas da aba Problema e entregas", "produz seis desenhos assinados pelo time, as regras publicadas, o painel de indicadores e um plano de piloto: as nove entregas da aba Problema e entregas")
R("H", r"<strong>(A fronteira entre Fórum de Negócio e Fórum de Gestão\.)(.*?)</strong>", r"<strong>\1</strong>\2", rx=True, count=1)
R("H", "Uma esteira (Vida), dois temas em sala de guerra", "Uma esteira (Vida), dois temas de Vida em sala de guerra")
m = re.search(r"De oito portas para uma;.*?</", F["H"], re.S)
if m: F["H"] = F["H"].replace(m.group(0), m.group(0).replace("; de ", ". De ").replace("; e de ", ". De "), 1)
else: MISS.append(("H", "De oito portas para uma;"))
sec = section("H", "proposta")
m = re.search(r"(<h3>O que está em jogo, o que muda, o que acontece se falharmos e se tivermos sucesso</h3>)(.*?)(<h3>)", sec, re.S)
if m:
    ps = re.findall(r"<p>.*?</p>", m.group(2), re.S)
    new = m.group(2)
    for i, p in enumerate(ps[:4]):
        if "sel-" in p: continue
        new = new.replace(p, p[:-4] + " " + (SV if i == 0 else SP) + "</p>", 1)
    sec = sec.replace(m.group(2), new, 1); set_section("H", "proposta", sec)
else: MISS.append(("H", "seção em jogo"))
R("H", r"\(semanal mista de uma hora e meia, S&amp;OP e diagnóstico com cadência assumida como mensal, não registrada nas fontes, Fórum de Gestão de até quatro horas, mentoria de meia hora\)", ": semanal mista de uma hora e meia; S&amp;OP e diagnóstico com cadência assumida como mensal, não registrada nas fontes; Fórum de Gestão de até quatro horas; mentoria de meia hora", rx=True)

# ---- O modelo
R("I", r"O sistema inteiro, num mês de pico com duas esteiras.*?(A maioria é de encontros curtos)", "O sistema inteiro, num mês de pico com duas esteiras, dois desafios em descoberta e um tema em sala de guerra, tem 51 encontros. São 8 reuniões de esteira (1h30), 2 triagens (30 min), 1 comitê (1h), 1 Fórum de Negócio (2h), 1 mentoria por tema (1h), 2 revisões de time (45 min), 8 encontros de descoberta (2h), 8 de sala de guerra (1h) e cerca de 20 reuniões diárias do núcleo (15 min). A média anual custeada na aba Reuniões e custo fica perto de 40 por mês, porque descoberta e sala de guerra não rodam todos os meses. " + r"\1", rx=True, count=1)
R("I", r"(Hoje as duas camadas moram na mesma reunião semanal[^<]*(?:<sup>[^<]*</sup>)?)(\s*</p>)", r"\1 " + SV + r"\2", rx=True, count=1)
R("I", "Time dedicado por esteira: núcleo fixo", "Time dedicado, um por esteira quando houver (no piloto, só Vida): núcleo fixo")

# ---- Desenho e regras
R("F", r"Vale também para um responsável de produto contratado no mercado[^.]*\.", "Vale também para contratar quem assume a rotina de quem se dedica ao time, para que o responsável de produto seja da casa, como a Agilidade sugeriu.", rx=True)
R("F", r"(<li><strong>1\. As mesmas pessoas.*?)" + re.escape(SV) + r"(</li>)", r"\1" + SV + " A leitura da alavanca é deste documento. " + SI + r"\2", rx=True, count=1)
R("F", r"(<li><strong>4\. A rotina vence a frente.*?)" + re.escape(SV) + r"(</li>)", r"\1" + SV + " A leitura do incentivo é deste documento. " + SI + r"\2", rx=True, count=1)
R("F", r"(<li><strong>7\. .*?)" + re.escape(SV) + r"(</li>)", r"\1" + SV + " A comparação entre março e junho é deste documento. " + SI + r"\2", rx=True, count=1)
R("F", r"de um ano e meio<sup>12</sup>, pesquisa com usuários no Espaço Corretor<sup>19</sup>, o ressegurador na padronização documental<sup>23</sup>,", "de um ano e meio, pesquisa com usuários no Espaço Corretor, o ressegurador na padronização documental,", rx=True)

# ---- Fluxo funcional
R("E", '<text x="1080" y="30" text-anchor="middle">DESTINO DA SOLUÇÃO</text>\n  </g>', '<text x="1080" y="30" text-anchor="middle">DESTINO DA SOLUÇÃO</text>\n  </g>\n  <text x="1385" y="30" text-anchor="end" font-size="15" font-weight="700" letter-spacing="3" fill="#b71c1c">EXEMPLO</text>')
R("E", 'font-weight="600">Sustentação (fila própria)</text>', 'font-weight="600">Sustentação</text>')
R("E", "Projetos de torre) e acrescenta o que faltava nele:", "Projetos de torre). Acrescenta o que faltava nele:")

# ---- Sintomas
R("B", f"Sintomas e citações conferidos nas atas. {SV}<sup>25</sup>", f"Sintomas e citações conferidos nas atas, exceto dois que a planilha classifica como inferidos (reconsideração de recusas e um de organização do trabalho). {SV}<sup>25</sup>")

# ---- Estrutura: férias por função e normas em lista
sec = section("B", "papeis") if re.search(r'id="p-papeis"', F["B"]) else None
if sec:
    s2 = re.sub(r";?\s*[Ff]érias em [^.;<]+[.;]?", "", sec); s2 = re.sub(r";?\s*[Aa]usências? em [^.;<]+[.;]?", "", s2)
    s2 = re.sub(r"(<th>Papel</th>.*?</table>)", r"\1\n<p>Entre abril e setembro, cinco dos doze papéis registram férias ou ausência sem suplente.<sup>5, 10, 13, 14, 22</sup> " + SV + "</p>", s2, count=1, flags=re.S)
    set_section("B", "papeis", s2)
else: MISS.append(("B", "secao papeis"))
R("B", r"<p>Aparecem nas atas: a Nova Lei de Seguros, que exigiu revisão de cartas, produtos de RC e uma nova pergunta aberta na DPS(<sup>10</sup>); o movimento do Banco Central para substituir boletos por Pix e encerrar contas em agências subsidiárias(<sup>2</sup>); o saneamento da SUSEP que inativa corretores irregulares e muda os indicadores da carteira(<sup>14</sup>); as exigências documentais do ressegurador, adotadas como padrão no projeto Unicred(<sup>23</sup>); e a auditoria interna, que apontou o risco climático \(El Niño\) no ano anterior e cobra formalização\.(<sup>15</sup>)\s*" + re.escape(SV) + r"</p>",
  r"<p>Aparecem nas atas cinco normas ou exigências externas:</p>\n<ul>\n<li>A Nova Lei de Seguros, que exigiu revisão de cartas, produtos de RC e uma nova pergunta aberta na DPS.\1</li>\n<li>O movimento do Banco Central para substituir boletos por Pix e encerrar contas em agências subsidiárias.\2</li>\n<li>O saneamento da SUSEP, que inativa corretores irregulares e muda os indicadores da carteira.\3</li>\n<li>As exigências documentais do ressegurador, adotadas como padrão no projeto Unicred.\4</li>\n<li>A auditoria interna, que apontou o risco climático (El Niño) no ano anterior e cobra formalização.\5</li>\n</ul>\n<p>" + SV + "</p>", rx=True, count=1)
R("B", "Reforçada em junho e agosto; não cumprida de forma consistente.", "Reforçada em junho e agosto; não cumprida de forma consistente.<sup>14, 20</sup>")
R("B", "Calendário informal; conflitos continuam.", "Calendário informal; conflitos continuam.<sup>13, 18</sup>")
R("B", "horário voltou a variar (10h às 11h) nas atas seguintes", "horário voltou a variar (10h às 11h) nas atas seguintes<sup>14, 18</sup>")
R("B", r"O modelo do Fórum de Negócio SUSEP e do time dedicado ainda sem decisão; os papéis ainda estão pouco definidos[^<]*<sup>26</sup>", "O modelo do Fórum de Negócio SUSEP e do time dedicado segue sem decisão. Os papéis estão pouco definidos e a participação da TI no time está em aberto. A Estratégia pondera entre esperar o modelo evoluir ou pôr na mesa as dores antes.<sup>26</sup>", rx=True)

# ---- Cem perguntas: 92 a 100 são desenho
sec = section("D", "cem")
m = re.search(r"(<li><strong>92\..*?</ol>)", sec, re.S)
if m:
    blk = m.group(1).replace(SI, SP).replace(SE, SP); sec = sec.replace(m.group(1), blk, 1); set_section("D", "cem", sec)
else: MISS.append(("D", "bloco 92-100"))
R("D", "Tempo de ciclo de decisão, decisões com dono e braço, quórum, tarefas entre reuniões, não-ganhos registrados", "Os oito indicadores do painel (aba O modelo), a começar pelo tempo entre entrada e decisão; e, na régua da facilitação da frente, se as áreas reconhecerem valor real")

# ---- Glossário
R("D", "<strong>RCP e PMI.</strong> Responsabilidade Civil Profissional e outros produtos de Ramos Elementares citados nas atas.", "<strong>RCP.</strong> Responsabilidade Civil Profissional, produto de Ramos Elementares.")
R("D", r'<div class="card"><strong>(Churn|Mega broker|Placement)[^<]*</strong>.*?</div>\n?', "", rx=True)

# ---- Fontes: nota de método e links
R("D", r"<p>Nota de método\..*?</p>", "<p>Nota de método. Afirmação apoiada em documento identificado, lido na íntegra em 1º de setembro de 2026, ou em fala transcrita da reunião do mesmo dia. " + SV + " Raciocínio construído a partir de documentos verificados, sem que nenhum o afirme diretamente; toda classificação, encadeamento causal e juízo de intensidade está aqui. " + SI + " Hipótese sem base direta: cenários, dimensionamentos, valores de regra. " + SE + " Desenho proposto para validação nas sessões; não é afirmação sobre a realidade. " + SP + "</p>", rx=True, count=1)
n_links = F["D"].count('<a href="https://notebook.google.com/notebook/ede3f19c-4ce2-4ccf-a50c-ddcfd4d96e95">notebook.google.com</a>')
F["D"] = F["D"].replace(' <a href="https://notebook.google.com/notebook/ede3f19c-4ce2-4ccf-a50c-ddcfd4d96e95">notebook.google.com</a>', "")
if n_links:
    F["D"] = F["D"].replace("<h3>Documento derivado (25)</h3>", '<p class="note">Repositório das fontes 1 a 24: caderno "Estratégia e Operações Susep: Gestão de Vida e Ramos Elementares", acessível pela conta corporativa (<a href="https://notebook.google.com/notebook/ede3f19c-4ce2-4ccf-a50c-ddcfd4d96e95">endereço</a>).</p>\n<h3>Documento derivado (25)</h3>', 1)
else: MISS.append(("D", "links notebook"))

for k, s in F.items(): save(f"frag_{k}.html", s)

# ---- checks.py: Inferência/Especulativo aceitos em Alçadas e Reuniões (coluna hoje, sistema atual)
c = load("checks.py"); c = c.replace('sel_ok = not (pid in PROPOSAL and ("sel-i" in body or "sel-e" in body))', 'sel_ok = not (pid in PROPOSAL and pid not in ("alcadas", "ritos") and ("sel-i" in body or "sel-e" in body))'); save("checks.py", c)
# ---- build.py: conversor ignora o conteúdo dos SVGs
b = load("build.py")
if "tag=='svg'" not in b:
    b = b.replace("        elif tag=='sup': self.w(' [')", "        elif tag=='sup': self.w(' [')\n        elif tag=='svg': self.skip+=1", 1)
    b = b.replace("    def handle_endtag(self,tag):\n", "    def handle_endtag(self,tag):\n        if tag=='svg': self.skip-=1; return\n", 1)
save("build.py", b)
print("patch v11 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
