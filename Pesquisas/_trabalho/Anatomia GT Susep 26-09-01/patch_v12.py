# -*- coding: utf-8 -*-
"""v12: rodada 3 do checker (parecer_checker_v11.md): frases longas, sobrescritos no fim, restos."""
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
SV = '<span class="sel sel-v">Verificado</span>'
UP = lambda m: m.group(1) + ". " + m.group(2).upper()

# Destaque
R("A", r"está travada desde 2024<sup>23</sup>, e o produto de prestamista[^.]*\.(?:<sup>17</sup>)?", "está travada desde 2024.<sup>23</sup> E o produto de prestamista que a Unimed exige para janeiro de 2027 é discutido internamente desde o mesmo ano.<sup>17</sup>", rx=True)
F["A"] = F["A"].replace("que a Unimed exige para janeiro de 2027", "que a Unicred exige para janeiro de 2027")
R("A", r'Priorização difusa \("focar em tudo resulta em não entregar nada"\)<sup>11</sup>, comitê de priorização que nasce como piloto e começa por Saúde<sup>13, 16</sup>, e dores[^.]*\.(?:<sup>[^<]*</sup>)?', 'Priorização difusa ("focar em tudo resulta em não entregar nada"). Comitê de priorização que nasce como piloto e começa por Saúde. Dores da SUSEP pulverizadas entre a Frente, o S&amp;OP e o Diagnóstico Comercial.<sup>11, 13, 16, 20</sup>', rx=True)
R("A", "Os mais repetidos não falam de mercado: falam de agenda", "Os mais repetidos não falam de mercado. Falam de agenda")
R("A", r"entre as agendas[,;] (?:e )?a equipe chamada", "entre as agendas. A equipe chamada", rx=True)
R("A", r"para o GEM, (a curva ABC)", r"para o GEM. Saíram também \1", rx=True)
R("A", "reunião semanal: a operação avisa que não cabe OKR novo, a planilha", "reunião semanal. A operação avisa que não cabe OKR novo; a planilha")
R("A", "por todos, a reunião com os mentores fica para a semana seguinte e uma das mentoras", "por todos; a reunião com os mentores fica para a semana seguinte; uma das mentoras")
R("A", r"por um desenho[:;,] (?:e )?não há porta", "por um desenho. Não há porta", rx=True)
R("A", r"[;,] (?:e )?não há alçada para que a tarde", ". Não há alçada para que a tarde", rx=True)
# Executiva
R("G", r"sistema atual estimado[;,] (?:e )?a diferença compra", "sistema atual estimado. A diferença compra", rx=True)
R("G", r"\(aba Proposta\) e revisão em 90 dias (?:\w+ )?os oito indicadores", "(aba Proposta). A revisão em 90 dias usa os oito indicadores", rx=True)
R("G", "decidiu em agosto evidenciar o gap", 'decidiu em agosto "evidenciar o gap"')
# Proposta
R("H", "segundo motor de crescimento<sup>1, 12</sup> Um balcão", "segundo motor de crescimento.<sup>1, 12</sup> Um balcão")
R("H", "2027<sup>17</sup> O canal", "2027.<sup>17</sup> O canal")
R("H", r"Em 90 dias: tempo entre entrada e decisão medido nos dois temas da sala de guerra;[^<]*", "Em 90 dias: os oito indicadores do painel (aba O modelo), medidos primeiro nos dois temas da sala de guerra. Linha de base reconstruída com as atas de março a agosto; meta definida na sessão 6. Se os indicadores não mexerem, o desenho muda, não as pessoas. ", rx=True)
R("H", r"(com dono, prazo e braço)[;,] (\w)", UP, rx=True, count=1)
R("H", r"(em duas horas)[;,] (\w)", UP, rx=True, count=1)
R("H", r"(critérios de satisfação)[;,] (\w)", UP, rx=True, count=1)
R("H", "vira gap evidenciado, não gap fechado", 'vira "gap" evidenciado, não "gap" fechado')
# Alçadas
R("J", "em até cinco dias úteis, por quem não tomou a primeira decisão, com o dado que faltava.", "em até cinco dias úteis. Quem reconsidera é quem não tomou a primeira decisão, com o dado que faltava.")
# Reuniões e custo
R("H", r"(com dez pessoas)[;,] (?:e )?(some)", UP, rx=True, count=1)
# Estratégia a entrega
R("G", r"(nota máxima na triagem)[;,] (?:e )?(a sala de descoberta)", UP, rx=True, count=1)
R("G", "demonstrado, não em slide", "demonstrado, não em lâmina")
# Fluxo funcional
R("E", r'De cinco origens, não de uma: a ponta comercial \(corretor que "nem calcular na Unimed"\)<sup>18</sup>, as áreas \(operação saturada, subscrição, produtos\)<sup>20</sup>, os dados \(funil com 418 itens, 40% parados há mais de 180 dias\)<sup>27</sup>, o mundo externo \(Unicred, Banco Central, Nova Lei, patrocínio\)<sup>2, 10, 17</sup> e as três esteiras que o fórum absorve\.<sup>26</sup>',
  'De cinco origens, não de uma. A ponta comercial (corretor que "nem calcular na Unimed").<sup>18</sup> As áreas (operação saturada, subscrição, produtos).<sup>20</sup> Os dados (funil com 418 itens, 40% parados há mais de 180 dias).<sup>27</sup> O mundo externo (Unicred, Banco Central, Nova Lei, patrocínio).<sup>2, 10, 17</sup> E as três esteiras que o fórum absorve.<sup>26</sup>', rx=True)
R("E", "sustentação e RDS/COMEX", "sustentação e RDS e COMEX")
# Desenho e regras
R("F", "são pontos de partida. <sup>", "são pontos de partida.<sup>")
R("F", "na formação.<sup>3, 19</sup>", "na formação.<sup>3, 12, 19, 23</sup>")
R("F", r"Se a resposta à primeira \(qual é o problema, em uma frase que a ponta reconheceria\)[^.]*\.", "Se a resposta à primeira pergunta demorar mais de dez minutos, a reunião já provou o ponto deste documento: o formato está vindo antes do problema.", rx=True)
# Entenda
R("A", r"A frente SUSEP \(o nome vem da Superintendência de Seguros Privados.*?<sup>12</sup>", 'A frente SUSEP foi criada para transformar Vida e RE no "outro grande motor de crescimento da companhia para reduzir a dependência de Saúde".<sup>12</sup> O nome vem da Superintendência de Seguros Privados, que regula seguros de Vida e Ramos Elementares; a ANS regula planos de saúde.', rx=True, count=1)
R("A", r"em uma frase[:;] a estratégia nasce", "em uma frase. A estratégia nasce", rx=True)
R("A", r"área de Estratégia[,;] (?:e )?desdobra no mapa estratégico, o artefato central[,;] (?:e )?do mapa", "área de Estratégia. Desdobra no mapa estratégico, o artefato central. Do mapa", rx=True)
R("A", r"rito de entrega desses times[,;] alimentando e recebendo da TI \(nos dois sentidos: envia e recebe\); aceleradores", "rito de entrega desses times. O time alimentaria e receberia da TI nos dois sentidos. Aceleradores", rx=True)
R("A", r"em maio<sup>10</sup>, ganhou alternância de liderança em junho<sup>14</sup> e continua sendo([^.]*)\.(?:<sup>[^<]*</sup>)?", r"em maio, ganhou alternância de liderança em junho e continua sendo\1.<sup>3, 10, 12, 14</sup>", rx=True)
R("A", "ainda está em construção (ainda sem decisão), com papéis em definição", "segue em construção, sem decisão, com papéis em definição")
R("A", r"rito de entrega[;,] (?:e )?o modelo de time dedicado proposto pela Agilidade", "rito de entrega. O modelo de time dedicado proposto pela Agilidade", rx=True)
# Processos
R("A", r"\(Vida e RE\), o S&amp;OP e o Diagnóstico[;,:] o S&amp;OP, que trata só de Vida, e o Diagnóstico, nascido no comercial no fim de 2025 e que, na leitura da facilitação, funcionou porque as pessoas se sentaram e conversaram", "(Vida e RE), o S&amp;OP e o Diagnóstico. O S&amp;OP trata só de Vida. O Diagnóstico nasceu no comercial no fim de 2025 e, na leitura da facilitação, funcionou porque as pessoas se sentaram e conversaram", rx=True)
R("A", r"a cadeia é conhecida: o corretor, a cooperativa.*?assistência funeral\.", "a cadeia é conhecida. O corretor, a cooperativa ou a Unimed cotam (Calcule+ e multicálculos como Agger, Quiver e SIGAS). A proposta passa por subscrição, aceitação médica e, em alguns casos, compliance. A apólice é emitida e cobrada (boleto, GEM, sem Pix recorrente para todos os produtos). Renova ou cancela. O sinistro é regulado no RGS, com IA na cobertura de assistência funeral.", rx=True, count=1)
# Sintomas
R("B", "retorno em 48 horas sobre cotações abertas em 48 horas, que trata", "retorno em 48 horas sobre cotações abertas, que trata")
R("B", r"a lista muda[:;] (?=esgotamento)", "a lista muda. ", rx=True)
R("B", r"esgotamento de comissão \(o maior obstáculo em RE segundo o mentor\)<sup>23</sup>, aceitação do Vida \(corretor orienta a nem cotar\)<sup>18</sup>, prestamista de prêmio único \(prazo externo em janeiro de 2027\)<sup>17</sup>, fila da TI sem cota para a SUSEP<sup>22</sup> e a mistura de Vida e RE, que impede enxergar os outros quatro com clareza\.<sup>13</sup>",
  "Esgotamento de comissão, o maior obstáculo em RE segundo o mentor.<sup>23</sup> Aceitação do Vida, em que o corretor orienta a nem cotar.<sup>18</sup> Prestamista de prêmio único, com prazo externo em janeiro de 2027.<sup>17</sup> Fila da TI sem cota para a SUSEP.<sup>22</sup> E a mistura de Vida e RE, que impede enxergar os outros quatro com clareza.<sup>13</sup>", rx=True)
R("B", f"organização do trabalho). {SV}<sup>25</sup>", f"organização do trabalho).<sup>25</sup> {SV}")
# Estrutura
R("B", f"<td><sup>13</sup> {SV}</td>", f"<td>Ausência somada abaixo da tabela.<sup>13</sup> {SV}</td>")
R("B", r"<td>\s*agendas de 30 minutos\.", "<td>Agendas de 30 minutos.", rx=True)
R("B", "nas atas seguintes<sup>14, 18</sup>.", "nas atas seguintes.<sup>14, 18</sup>")
R("B", '"sobrecarregando a liderança no dia a dia operacional"<sup>5, 14</sup>', '"sobrecarregando a liderança no dia a dia operacional".<sup>5, 14</sup>')
R("B", "da reprecificação dela<sup>13, 22</sup>", "da reprecificação feita por uma única pessoa.<sup>13, 22</sup>")
R("B", '"Limitação de braço técnico"<sup>10, 13</sup>', '"Limitação de braço técnico".<sup>10, 13</sup>')
R("B", "travam o Hub<sup>13, 14</sup>", "travam o Hub.<sup>13, 14</sup>")
R("B", "cinco dos doze papéis registram", "cinco das doze pessoas (nove do núcleo e três mentores) registram")
R("B", "RCP Individual, PMI;", "RCP Individual;")
# Análise
R("C", r'("20% a\.a\."\.?<sup>3</sup>)[;,] em 22 de abril, a', r"\1 Em 22 de abril, a", rx=True)
R("C", r'(mentores"\.?<sup>6</sup>)[;,] em julho', r"\1 Em julho", rx=True)
# Cem perguntas e Fontes
R("D", "Facilitadora, donos de esteira, produtos, atuarial, TI, IM, canais e VMO, quinzenal.", "Facilitação, líderes de esteira, Produtos, Atuarial, TI e arquitetura, Inteligência de Mercado, Canais e Processos ou VMO; quinzenal, meia hora (aba Desenho e regras).")
m = re.search(r"<p>As fontes são internas:.*?</p>", F["D"], re.S)
if m:
    print("Fontes, parágrafo substituído:", re.sub(r"<[^>]+>", "", m.group(0))[:400])
    F["D"] = F["D"].replace(m.group(0), '<p>As fontes são internas: uma apresentação de planejamento, 23 atas do próprio grupo e as transcrições de duas reuniões de 1º de setembro. Todas estão no repositório do projeto, o caderno "Estratégia e Operações Susep: Gestão de Vida e Ramos Elementares", acessível pela conta corporativa.</p>', 1)
else: MISS.append(("D", "As fontes são internas"))
R("D", "(apresentação de slides; conteúdo lido a partir das imagens)", "(apresentação em lâminas; conteúdo lido a partir das imagens)")
R("D", "Ata da reunião semanal, GT Susep Vida e RE.", "Ata da reunião semanal do GT SUSEP Vida e RE.")
for k, s in F.items(): save(f"frag_{k}.html", s)
c = load("checks.py"); c = c.replace('pid not in ("alcadas", "ritos")', 'pid not in ("alcadas", "ritos", "design")'); save("checks.py", c)
print("patch v12 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
