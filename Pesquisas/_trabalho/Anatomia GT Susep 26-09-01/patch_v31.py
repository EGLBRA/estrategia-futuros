# -*- coding: utf-8 -*-
"""v31: aplica o parecer de português e clareza (parecer_portugues_final.md) mais os itens a) a e) do validador.
Cada troca é literal e confere a contagem esperada; nada é substituído às cegas."""
import io, os, re, sys
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SV = '<span class="sel sel-v">Verificado</span>'; SI = '<span class="sel sel-i">Inferência</span>'; SP = '<span class="sel sel-p">Proposta</span>'
FILES = {k: f"frag_{k}.html" for k in "ABCDEFGHIJKL"}; FILES["P"] = "pratica.py"; FILES["BUILD"] = "build.py"
F = {k: load(n) for k, n in FILES.items()}
MISS = []; DONE = []
def R(k, old, new, n=1, tag=""):
    c = F[k].count(old)
    if c != n:
        MISS.append((tag, FILES[k], c, n, old[:80])); return
    F[k] = F[k].replace(old, new); DONE.append((tag, FILES[k], n))
def RX(k, pat, rep, n=1, tag=""):
    s2, c = re.subn(pat, rep, F[k], flags=re.S)
    if c != n:
        MISS.append((tag, FILES[k], c, n, pat[:80])); return
    F[k] = s2; DONE.append((tag, FILES[k], n))

# ---------------- build.py (só manchete e rodapé)
R("BUILD", "Diagnóstico Rápido &middot; SU GT Evoluir Modelo de Negócio SUSEP Vida e RE", "Diagnóstico Rápido &middot; Seguros Unimed &middot; GT Evoluir Modelo de Negócio SUSEP Vida e RE", tag="26")
R("BUILD", "Uso interno<br>Material sensível: não circular", "Uso interno &middot; Material sensível: não circular", tag="21")

# ---------------- frag_A: Destaque, Entenda, Ecossistema, Processos
R("A", '<span class="num">115% x 99%</span><small>1º trimestre contra a meta', '<span class="num">115% x 99%</span><small>no 1º trimestre contra a meta', tag="8")
R("A", "Esgotamento de comissão, prestamista prêmio único, meios de pagamento", "Esgotamento de comissão, prestamista de prêmio único, meios de pagamento", tag="35")
R("A", "Três consultores saíram, a líder absorveu o operacional", "Três consultores saíram, a liderança absorveu o operacional", tag="36")
R("A", "Dia 11, às duas da tarde, a semanal: a operação avisa que não cabe OKR novo; a planilha de necessidades segue sem preenchimento; a reunião com os mentores fica para a semana seguinte; uma mentora está de férias até o fim do mês.<sup>20, 22</sup>",
       "Dia 11, às duas da tarde, a semanal. A operação avisa que não cabe OKR novo. A planilha de necessidades segue sem preenchimento. A reunião com os mentores fica para a semana seguinte; um dos mentores está de férias até o fim do mês.<sup>20, 22</sup>", tag="Destaque 4 / 56")
R("A", "sinistro e inteligência, e a facilitadora da Estratégia.<sup>2, 10</sup>", "sinistro e inteligência, e a facilitação da Estratégia.<sup>2, 10</sup>", tag="56")
R("A", "<tr><td><strong>Diretoria executiva</strong></td>", "<tr><td><strong>Diretoria Executiva</strong></td>", tag="29")
R("A", "<h3>O fluxo oficial, na descrição da facilitadora</h3>", "<h3>O fluxo oficial, na descrição da facilitação</h3>", tag="56")
R("A", '<p class="tese">O núcleo depende de treze atores e não comanda nenhum.</p>', '<p class="tese">Treze atores dão diretriz, prazo, dado, capacidade ou pressão ao grupo; nenhum responde a ele.</p>', tag="Ecossistema 1")
R("A", "O ecossistema da frente: um núcleo pequeno que depende de treze atores e não comanda nenhum. O que cada um dá ao grupo está na tabela abaixo.", "Quem dá o quê ao grupo, ator por ator. O detalhe de cada um está na tabela abaixo.", tag="Ecossistema 1")
R("A", "<tr><td><strong>Diretoria executiva, RDS, COMEX</strong></td>", "<tr><td><strong>Diretoria Executiva, RDS, COMEX</strong></td>", tag="29")
R("A", "sem triagem, e saem sem registro de saída: resolvidos", "sem triagem, e saem sem registro: resolvidos", tag="51")
R("A", "<strong>Prestamista prêmio único (Unicred).</strong>", "<strong>Prestamista de prêmio único (Unicred).</strong>", tag="35")
R("A", "Corretor, cooperativa ou Unimed cotam (Calcule+, multicálculos Agger, Quiver e SIGAS); subscrição, aceitação médica e, às vezes, compliance analisam; a apólice é emitida e cobrada (boleto, GEM, sem Pix recorrente para todos os produtos), renova ou cancela; o sinistro é regulado no RGS, com IA na assistência funeral.",
       "Corretor, cooperativa ou Unimed cotam (Calcule+, multicálculos Agger, Quiver e SIGAS). Subscrição, aceitação médica e, às vezes, compliance analisam. A apólice é emitida e cobrada (boleto, GEM, sem Pix recorrente para todos os produtos), renova ou cancela. O sinistro é regulado no RGS, com IA na assistência funeral.", tag="Processos 3")
R("A", "É aqui que entra o desenho: a cotação recusada gera ficha de não-ganho na fila única; a triagem soma dezenas iguais e enquadra um estrutural (aceitação descolada do mercado); a descoberta compara com o mercado; o comitê decide com a auditoria médica na mesa.",
       "É aqui que entra o desenho. A cotação recusada gera ficha de não-ganho na fila única. A triagem soma dezenas iguais e enquadra um estrutural: aceitação descolada do mercado. A descoberta compara com o mercado; o comitê decide com a auditoria médica na mesa.", tag="Processos 4")

# ---------------- frag_B: Sintomas, Normas, Papéis, Sistemas
R("B", '>Org. do Trabalho</text>', '>Organização do Trabalho</text>', tag="Sintomas 7")
R("B", '>Org. do Trabalho (3.1 m · 3.1 doc)</text>', '>Organização do Trabalho (3.1 m · 3.1 doc)</text>', tag="Sintomas 7")
R("B", "COMEX, cursos (Dom Cabral, VMO, formação de líderes às terças e quintas à tarde), férias escalonadas (uma pessoa em julho, duas em agosto, uma em setembro), feriados, jogos da seleção, eventos setoriais (Suemg, Rio) e abertura de orçamento colidem com as agendas do GT.",
       "COMEX; cursos (Dom Cabral, VMO, formação de líderes às terças e quintas à tarde); férias escalonadas (uma pessoa em julho, duas em agosto, uma em setembro); feriados e jogos da seleção; eventos setoriais (Suemg, Rio); abertura de orçamento. Todos colidem com as agendas do GT.", tag="Sintomas 5")
R("B", "Em junho a segregação ainda é 'prometida há meses'", 'Em junho a segregação ainda é "prometida há meses"', tag="18")
R("B", "A reestruturação do Estratos em duas esteiras", "A reestruturação do Stratws em duas esteiras", tag="33")
R("B", "Fórum de junho oscila entre 22/06, 29/06 e 06/07 por causa de jogos do Brasil. Mentores de férias em julho e agosto (uma mentora até 31/08).",
       "Fórum de junho oscila entre 22 de junho, 29 de junho e 6 de julho por causa de jogos do Brasil. Mentores de férias em julho e agosto (um dos mentores até 31 de agosto).", tag="40 / 56")
R("B", "sem avanço entre agendas e 'lições de casa' não feitas", 'sem avanço entre agendas e "lições de casa" não feitas', tag="18")
R("B", "Em agosto o grupo 'não organizou as próximas iniciativas'.", 'Em agosto o grupo "não organizou as próximas iniciativas".', tag="18")
R("B", "Mentor cita '13' como fatia acordada", 'Mentor cita "13" como fatia acordada', tag="18")
R("B", "Frentes cogitam pedir 'refluctuação' de metas", 'Frentes cogitam pedir "refluctuação" de metas', tag="18")
R("B", "(Jira para Stratws em jan/26, Stratws para Jira em jun/26), zerando histórico", "(Jira para Stratws em janeiro de 2026, Stratws para Jira em junho de 2026), zerando histórico", tag="40")
R("B", "Jira substituído por Stratws em jan/26; em jun/26 a companhia decide voltar ao Jira", "Jira substituído por Stratws em janeiro de 2026; em junho de 2026 a companhia decide voltar ao Jira", tag="40")
R("B", "Ciclo 'Pós-PI' encerrado administrativamente com percentuais de maio congelados para iniciar 'histórico limpo'. Percentuais de conclusão confundem 'fase de entrega' com 'resultado de vendas'.",
       'Ciclo "Pós-PI" encerrado administrativamente com percentuais de maio congelados para iniciar "histórico limpo". Percentuais de conclusão confundem "fase de entrega" com "resultado de vendas".', tag="18")
R("B", "Mapfre 'compram' balcões e assediam cooperativas 'a cada 30 segundos'.", 'Mapfre "compram" balcões e assediam cooperativas "a cada 30 segundos".', tag="18")
R("B", "<tr><td>Fóruns preparados para evitar questionamentos</td>", "<tr><td>Fóruns preparados com foco em resultados positivos</td>", tag="55")
R("B", "Jira para Stratws (jan), Stratws para Jira (jun); histórico zerado.", "Jira para Stratws (janeiro), Stratws para Jira (junho); histórico zerado.", tag="40")
R("B", "retenção depende da reprecificação feita por uma única atuária.", "retenção depende da reprecificação feita por uma única pessoa da Atuarial.", tag="56")
R("B", "Declínio automático por IMC acima de 38 só abolido em nov/25.", "Declínio automático por IMC acima de 38 só abolido em novembro de 2025.", tag="40")
R("B", "<p>Recorrência não é gravidade. Pela régua de quanto negócio cada um custa: esgotamento de comissão, o maior obstáculo em RE segundo o mentor;<sup>23</sup> aceitação do Vida, em que o corretor orienta a nem cotar;<sup>18</sup> prestamista de prêmio único, com prazo externo em janeiro de 2027;<sup>17</sup> fila da TI sem cota para a SUSEP;<sup>22</sup> e a mistura de Vida e RE, que esconde os outros quatro.<sup>13</sup> " + SI + "</p>",
       "<p>Recorrência não é gravidade. Pela régua de quanto negócio cada um custa:</p>\n<ol>\n<li>esgotamento de comissão, o maior obstáculo em RE segundo o mentor;<sup>23</sup></li>\n<li>aceitação do Vida, em que o corretor orienta a nem cotar;<sup>18</sup></li>\n<li>prestamista de prêmio único, com prazo externo em janeiro de 2027;<sup>17</sup></li>\n<li>fila da TI sem cota para a SUSEP;<sup>22</sup></li>\n<li>a mistura de Vida e RE, que esconde os outros quatro.<sup>13</sup></li>\n</ol>\n<p>" + SI + "</p>", tag="Sintomas 4")
# Estrutura: subseções em h4 (blocos ficam em h3 na montagem)
H4 = '<h4 style="font-size:14px;font-weight:700;margin:14px 0 6px">'
for t in ["As regras vigentes", "O que está em aberto em 1º de setembro", "O que não existe e precisaria existir", "As normas externas que o grupo precisa cumprir",
          "O que a reunião de 1º de setembro diz sobre papéis", "O que o desenho precisaria definir sobre pessoas", "O inventário que as atas revelam", "Quatro dados que não existem e de que o negócio precisa"]:
    R("B", f"<h3>{t}</h3>", f"{H4}{t}</h4>", tag="Estrutura 2")
R("B", "Nove pessoas no núcleo, contando a facilitadora, e três mentores", "Nove pessoas no núcleo, contando a facilitação, e três mentores", tag="56")
R("B", "Responsável em dezenas de tarefas; curso às terças à tarde.", "Responsável por dezenas de tarefas; curso às terças à tarde.", tag="3")
R("B", 'Prazo da Unicred crítico pela "complexidade contábil/sistêmica', 'Prazo da Unicred crítico devido à "complexidade contábil/sistêmica', tag="4")
R("B", "Some as tarefas da líder e da facilitadora nas atas de junho", "Some as tarefas da liderança e da facilitação nas atas de junho", tag="56")
R("B", "Depois some as horas que cada uma tem para a frente.", "Depois some as horas que cada pessoa tem para a frente.", tag="56")
R("B", "<tr><td>Hubspot (renovações)</td>", "<tr><td>HubSpot (renovações)</td>", tag="34")

# ---------------- frag_C: Laços, Análise, Sutilezas
R("C", "<p><strong>Operação saturada</strong> não abre frente nova<sup>20</sup> <strong>e a frente não tem alçada</strong>, escala para mentores e diretoria<sup>22</sup> <strong>cujas agendas são curtas ou adiadas</strong><sup>13, 24</sup>, <strong>o que atrasa a decisão por meses</strong> (esgotamento de comissão, prestamista)<sup>17, 23</sup>, <strong>e o atraso obriga a operação a sustentar paliativos manuais</strong><sup>9, 15</sup>, <strong>que consomem ainda mais braço.</strong> Volta ao início.</p>",
       "<ol>\n<li><strong>Operação saturada</strong> não abre frente nova.<sup>20</sup></li>\n<li><strong>A frente não tem alçada</strong> e escala para mentores e diretoria.<sup>22</sup></li>\n<li><strong>As agendas são curtas ou adiadas.</strong><sup>13, 24</sup></li>\n<li><strong>A decisão atrasa por meses</strong> (esgotamento de comissão, prestamista).<sup>17, 23</sup></li>\n<li><strong>O atraso obriga a operação a sustentar paliativos manuais.</strong><sup>9, 15</sup></li>\n<li><strong>Os paliativos consomem ainda mais braço.</strong> Volta ao 1.</li>\n</ol>", tag="15 / Laços 2")
R("C", '<p><strong>Regras de aceitação rígidas</strong><sup>10</sup> <strong>fazem o corretor nem cotar</strong> ("nem calcular na Unimed")<sup>18</sup>; <strong>a cotação que não acontece não gera dado</strong> (o "número invisível")<sup>18</sup>; <strong>sem dado, o problema parece ser preço</strong><sup>18</sup>; <strong>a regra não muda</strong> porque a regra só é revista quando o dado chega à auditoria médica<sup>23</sup>; <strong>e o corretor migra</strong> para quem aceita automaticamente.<sup>11</sup> Volta ao início.</p>',
       '<ol>\n<li><strong>Regras de aceitação rígidas</strong><sup>10</sup> <strong>fazem o corretor nem cotar</strong> ("nem calcular na Unimed").<sup>18</sup></li>\n<li><strong>A cotação que não acontece não gera dado</strong> (o "número invisível").<sup>18</sup></li>\n<li><strong>Sem dado, o problema parece ser preço.</strong><sup>18</sup></li>\n<li><strong>A regra não muda</strong>, porque só é revista quando o dado chega à auditoria médica.<sup>23</sup></li>\n<li><strong>O corretor migra</strong> para quem aceita automaticamente.<sup>11</sup> Volta ao 1.</li>\n</ol>', tag="16 / Laços 2")
R("C", "<p><strong>Reprecificação ágil e contínua</strong> (notas de tarifa em abril, Residencial 16% a 19% mais barato em agosto, quase um quinto do preço)<sup>3, 20</sup> <strong>mantém o preço competitivo</strong>; <strong>o cotador funciona</strong> (Calcule+ e Agger no Residencial)<sup>4, 7</sup>; <strong>o corretor cota e fecha</strong>; <strong>o RE bate 115% da meta</strong><sup>7</sup> <strong>e ganha crédito para focar o suporte no que falta</strong> (Vida)<sup>4</sup>; <strong>o crédito vira patrocínio</strong> para o próximo ajuste. Volta ao início.</p>",
       "<ol>\n<li><strong>Reprecificação ágil e contínua mantém o preço competitivo</strong> (notas de tarifa em abril, Residencial 16% a 19% mais barato em agosto, quase um quinto do preço).<sup>3, 20</sup></li>\n<li><strong>O cotador funciona</strong> (Calcule+ e Agger no Residencial).<sup>4, 7</sup></li>\n<li><strong>O corretor cota e fecha.</strong></li>\n<li><strong>RE bate 115% da meta.</strong><sup>7</sup></li>\n<li><strong>RE ganha crédito para focar o suporte no que falta</strong> (Vida).<sup>4</sup></li>\n<li><strong>O crédito vira patrocínio</strong> para o próximo ajuste. Volta ao 1.</li>\n</ol>", tag="16 / Laços 2")
R("C", "Em RE, a atuária ajusta o preço a cada trimestre", "Em RE, a Atuarial ajusta o preço a cada trimestre", tag="56")
R("C", 'A alavanca que você pode levar aos mentores é revisar a regra de aceitação a cada trimestre, com dado de mercado, a medicina na mesa e alçada por faixas: o comitê com alçada do desenho, que a frente chamou em agosto de "tarifação adaptada por patologia".<sup>23</sup>',
       'A alavanca que você pode levar aos mentores: revisar a regra de aceitação a cada trimestre, com dado de mercado, a medicina na mesa e alçada por faixas. É o comitê com alçada do desenho; a frente chamou a ideia, em agosto, de "tarifação adaptada por patologia".<sup>23</sup>', tag="Laços 3")
R("C", '<p class="tese">O maior risco não é o mercado: é o desenho continuar igual enquanto o prazo da Unicred, a campanha de VG e a meta de 20% correm.</p>',
       '<p class="tese">Dos três cenários, o mais provável hoje é o desenho parcial: separa Vida de RE e abre salas de guerra, mas sem alçada nem time dedicado.</p>', tag="Análise 2")
# SWOT: ponto e vírgula antes do sobrescrito (só dentro dos quatro cartões)
def swot_fix(m):
    return re.sub(r"<sup>([^<]*)</sup>;", r";<sup>\1</sup>", m.group(0))
s2, c = re.subn(r'<div class="card"><strong>(Forças|Fraquezas|Oportunidades|Ameaças)\.</strong>.*?</div>', swot_fix, F["C"], flags=re.S)
if c == 4:
    n_before = len(re.findall(r"</sup>;", F["C"])); F["C"] = s2; DONE.append(("17", "frag_C.html", n_before - len(re.findall(r"</sup>;", F["C"]))))
else: MISS.append(("17", "frag_C.html", c, 4, "SWOT cards"))
R("C", 'ao invés da meta anual de 20% a.a.".<sup>3</sup>', 'ao invés da meta anual de 20% a.a."<sup>3</sup>', tag="19")
R("C", "dados de sinistro à mão pela atuária, retaguarda humana", "dados de sinistro à mão pela Atuarial, retaguarda humana", tag="56")

# ---------------- frag_D: Perguntas, Glossário, Fontes
R("D", 'Focando resultados positivos e evitando "abrir brechas para questionamentos".', 'Foca resultados positivos e evita "abrir brechas para questionamentos".', tag="12")
R("D", "Depender de uma só cadeira (canais, sem suplente), falta de dados e dependência da área de Projetos.", "Dependência de uma só cadeira (canais, sem suplente), falta de dados e dependência da área de Projetos.", tag="13")
R("D", "Não de forma integrada; a atuária fornece à mão.", "Não de forma integrada; a Atuarial fornece à mão.", tag="56")
R("D", "<strong>Qual o sintoma mais recorrente?</strong>", "<strong>Qual é o sintoma mais recorrente?</strong>", tag="14")
R("D", "<strong>Qual a defasagem tecnológica?</strong>", "<strong>Qual é a defasagem tecnológica?</strong>", tag="14")
R("D", "<strong>Quais os quatro tipos de demanda?</strong>", "<strong>Quais são os quatro tipos de demanda?</strong>", tag="14")
R("D", "Encontro mensal com a diretoria executiva para deliberações.", "Encontro mensal com a Diretoria Executiva para deliberações.", tag="29")
R("D", "Comissão paga ao corretor proporcional ao prêmio recebido, à frente do parcelamento; não é adiantamento.", "Comissão paga ao corretor na proporção do prêmio já recebido, sem esperar o fim do parcelamento; não é adiantamento.", tag="50")
R("D", "Ata de alinhamento entre líder e facilitadora (engajamento, canais, Estratos).", "Ata de alinhamento entre a liderança e a facilitação da frente (engajamento, canais, Stratws).", tag="33 / 56")

# ---------------- frag_E: Fluxo
R("E", "e as três esteiras absorvidas (S&amp;OP, Diagnóstico, frente). Todas levam", "e as três agendas absorvidas (S&amp;OP, Diagnóstico, Frente). Todas levam", tag="38 / 30")
R("E", "S&amp;OP, Diagnóstico SUSEP e frente aparecem como origens absorvidas", "S&amp;OP, Diagnóstico SUSEP e Frente aparecem como origens absorvidas", tag="30")
R("E", "<tr><td>S&amp;OP, Diagnóstico, frente</td><td>Fórum de Negócio (absorvidos)</td>", "<tr><td>S&amp;OP, Diagnóstico, Frente</td><td>Fórum de Negócio (absorvidos)</td>", tag="30")
R("E", '<strong>De onde vem o problema.</strong> De cinco origens: a ponta comercial (corretor que "nem calcular na Unimed");<sup>18</sup> as áreas (operação saturada, subscrição, produtos);<sup>20</sup> os dados (funil com 418 itens, 40% dos 362 ativos parados há mais de 180 dias, meio ano sem movimento);<sup>27</sup> o mundo externo (Unicred, Banco Central, Nova Lei, patrocínio);<sup>2, 10, 17</sup> e as três esteiras absorvidas.<sup>26</sup> Hoje cada origem tem uma porta; no desenho, uma só. ' + SV + ' ' + SP + '</div>',
       '<strong>De onde vem o problema.</strong> De cinco origens. A ponta comercial: corretor orientado a "nem calcular na Unimed".<sup>18</sup> As áreas: operação saturada, subscrição, produtos.<sup>20</sup> Os dados: funil com 418 itens, 40% dos 362 ativos parados há mais de 180 dias, meio ano sem movimento.<sup>27</sup> O mundo externo: Unicred, Banco Central, Nova Lei, patrocínio.<sup>2, 10, 17</sup> E as três agendas absorvidas.<sup>26</sup> Hoje cada origem tem uma porta. ' + SV + ' No desenho, uma só. ' + SP + '</div>', tag="9 / 38 / 25 / Fluxo 3")
R("E", 'É a etapa que a Agilidade descreveu: o problema chega à TI com diagnóstico, não cru.<sup>27</sup> A sustentação não passa por ela. ' + SV + ' ' + SP + '</div>',
       'É a etapa que a Agilidade descreveu: o problema chega à TI com diagnóstico, não cru.<sup>27</sup> ' + SV + ' A sustentação não passa por ela. ' + SP + '</div>', tag="25")
R("E", 'a resposta hoje é "tudo": frente, S&amp;OP, diagnóstico, corretor, TI.', 'a resposta hoje é "tudo": Frente, S&amp;OP, Diagnóstico, corretor, TI.', tag="30 / 31")

# ---------------- frag_F: Desenho
R("F", "<h3>Como eu sei o que é relevante</h3>", "<h3>Como saber o que é relevante</h3>", tag="53")
R("F", "Qual o impacto contra o esforço?<sup>13</sup>", "Qual é o impacto contra o esforço?<sup>13</sup>", tag="14")
R("F", "<h3>Que tipo de problema é: estrutural, sustentação ou adequação</h3>", "<h3>Que tipo de problema é: estrutural, sustentação, adequação ou oportunidade</h3>", tag="39")
R("F", "<h3>Vamos estudar o quê? O que vamos terceirizar? Como vamos controlar? Como vamos medir sucesso?</h3>", "<h3>Estudar, construir, comprar ou paliativo</h3>", tag="Desenho 6")
R("F", "<h3>Avaliação dirigida ou descoberta aberta? Olhar mercado? Decupar escopo com TI?</h3>", "<h3>Modos de descoberta</h3>", tag="Desenho 6")
R("F", "<strong>5. Três agendas com as mesmas pessoas é duplicação estrutural.</strong>", "<strong>5. Ter três agendas com as mesmas pessoas é duplicação estrutural.</strong>", tag="6")
R("F", " " + SV + " Interpretação do autor. " + SI + "</div>", "</div>", n=7, tag="Desenho 4")
R("F", '<div class="card"><strong>8. A Estratégia registrou em 1º de setembro',
       '<div class="card"><strong>8. A Estratégia registrou em 1º de setembro', tag="anchor")
RX("F", r'(<strong>8\. A Estratégia registrou em 1º de setembro.*?</div>\n</div>\n)',
       r'\1<p class="note">Os fatos de cada item vêm das atas. ' + SV + ' A leitura de cada um é deste documento. ' + SI + '</p>\n', tag="Desenho 4")

# ---------------- frag_G: Executiva, Caminho
R("G", "<strong>O braço acabou.</strong>", "<strong>O braço encolheu.</strong>", tag="37")
R("G", "Meta de 20% mantida como acordo com mentores; o grupo trabalha com o número da Controladoria; o fechamento de 2024 não está registrado nas atas; nenhuma ata registra a memória de cálculo do número do KR nem se o OKR foi construído com o grupo ou comunicado a ele; a origem apontada é o planejamento estratégico.<sup>1, 3, 6, 20, 24</sup>",
       "A meta de 20% é acordo com mentores, mas o grupo trabalha com o número da Controladoria. O fechamento de 2024 não está nas atas. Nenhuma ata registra a memória de cálculo do KR nem se o OKR foi construído com o grupo; a origem apontada é o planejamento estratégico.<sup>1, 3, 6, 20, 24</sup>", tag="Executiva 4")
R("G", "<p>Quinze semanas entre a retomada do esgotamento de comissão (5 de maio) e a autorização de um estudo (17 de agosto), após cerca de dois anos parado.<sup>9, 23</sup> Prazo de parceiro (janeiro de 2027) para um produto discutido desde 2024, com automação estimada em três anos.<sup>11, 17</sup> Corretores que cotam uma vez e não voltam (36% em São Paulo); negócios perdidos sem registro.<sup>12, 18</sup> " + SV + " Reuniões, a R$ 125 a hora: R$ 381.625 por ano no sistema proposto (481 encontros) contra R$ 286.500 no atual (101); a diferença, cerca de R$ 95.125 por ano, compra triagem, descoberta e revisão de resultado, que hoje não existem (aba Reuniões). " + SP + "</p>",
       "<p>O esgotamento de comissão levou quinze semanas entre a retomada (5 de maio) e a autorização de um estudo (17 de agosto), após cerca de dois anos parado.<sup>9, 23</sup> O prestamista tem prazo de parceiro em janeiro de 2027, é discutido desde 2024 e tem automação estimada em três anos.<sup>11, 17</sup> Em São Paulo, 36% dos corretores cotam uma vez e não voltam; os negócios perdidos não são registrados.<sup>12, 18</sup> " + SV + " A R$ 125 a hora, o sistema proposto custa R$ 381.625 por ano (481 encontros) e o atual R$ 286.500 (101). A diferença, cerca de R$ 95.125, compra triagem, descoberta e revisão de resultado, que hoje não existem (aba Reuniões). " + SP + "</p>", tag="10 / Executiva 5")
R("G", "RE em 115% com as mesmas pessoas que seguram Vida em 99%", "RE em 115% com as mesmas pessoas que entregam Vida em 99%", tag="54")
R("G", "Três decisões cabem só à diretoria; duas, a mentores e Estratégia (tabela acima).", "Três decisões cabem só à diretoria; três, a mentores e Estratégia (tabela acima).", tag="41")
R("G", '>resolvido, recusado, parado</text>', '>resolvido, recusado, estacionado</text>', tag="45 (figura do Caminho)")
R("G", "Fórum de Negócio (porta única) + triagem quinzenal<br>", "Fórum de Negócio (porta única) e triagem quinzenal<br>", tag="20")
R("G", "Os sobrescritos apontam o sintoma que cada critério evita.", "Os sobrescritos apontam a fonte do sintoma que cada critério evita.", tag="23")
R("G", 'O prestamista de prêmio único é o prazo mais duro à frente: "altamente crítico" na ata de 29 de junho, com a Unicred exigindo capital fixo, prêmio antecipado e aceitação automática para janeiro de 2027, e o tema discutido desde 2024.<sup>17</sup>',
       'O prestamista de prêmio único é o prazo mais duro à frente: "altamente crítico" na ata de 29 de junho. A Unicred exige capital fixo, prêmio antecipado e aceitação automática para janeiro de 2027; o tema é discutido desde 2024.<sup>17</sup>', tag="Caminho 4")
R("G", "A descoberta de quatro semanas responderia uma pergunta:", "A descoberta de quatro semanas responderia a uma pergunta:", tag="5")

# ---------------- frag_H: Proposta, Reuniões
R("H", "<p>Um trabalho conduzido pela Estratégia com o grupo, em encontros de quantidade e duração negociadas com os participantes, com nove entregas (aba Problema):", "<p>Propõe-se um trabalho conduzido pela Estratégia com o grupo, em encontros negociados com os participantes, com nove entregas (aba Problema):", tag="11")
# tabela dos seis desenhos: sai a coluna "O que responde" (repete a tabela As entregas da aba Problema)
R("H", "<thead><tr><th>Desenho</th><th>O que responde</th><th>Ponto de partida neste documento</th><th>Sai do encontro</th></tr></thead>", "<thead><tr><th>Desenho</th><th>Ponto de partida neste documento</th><th>Sai do encontro</th></tr></thead>", tag="Proposta 3")
RX("H", r"(<tr><td><strong>[1-6]\. [^<]*</strong>(?: \(por último\))?</td>)<td>[^<]*</td>(<td>(?:Os 72|Exemplo|Aba)[^<]*</td>)", r"\1\2", n=6, tag="Proposta 3")
for old, new in [
    ("<td>Ficha única de demanda; lista dos problemas escrita pelas áreas; a planilha extensa vira fila carimbada; medir o tempo entre entrada e decisão dos itens abertos; publicar o painel com a linha de base das atas; registrar os não-ganhos.</td>",
     "<td><ul><li>Ficha única de demanda;</li><li>lista dos problemas escrita pelas áreas;</li><li>a planilha extensa vira fila carimbada;</li><li>medir o tempo entre entrada e decisão dos itens abertos;</li><li>publicar o painel com a linha de base das atas;</li><li>registrar os não-ganhos.</li></ul></td>"),
    ("<td>Tabela de alçadas assinada; duas esteiras com dono e indicador; uma sala de guerra por tema crítico (prestamista de prêmio único em Vida; esgotamento de comissão em RE); dedicação declarada por pessoa; agilista de melhoria contínua com tempo protegido.</td>",
     "<td><ul><li>Tabela de alçadas assinada;</li><li>duas esteiras com dono e indicador;</li><li>uma sala de guerra por tema crítico (prestamista de prêmio único em Vida; esgotamento de comissão em RE);</li><li>dedicação declarada por pessoa;</li><li>agilista de melhoria contínua com tempo protegido.</li></ul></td>"),
    ("<td>Número-base da meta assinado e aberto por ramo; cota de TI reservada à SUSEP e critério de despriorização; orçamento de reposição de consultores; fronteira entre Fórum de Negócio e Fórum de Gestão.</td>",
     "<td><ul><li>Número-base da meta assinado e aberto por ramo;</li><li>cota de TI reservada à SUSEP e critério de despriorização;</li><li>orçamento de reposição de consultores;</li><li>fronteira entre Fórum de Negócio e Fórum de Gestão.</li></ul></td>")]:
    R("H", old, new, tag="Proposta 7")
R("H", "<td>Diretoria Comercial, Controladoria e diretoria de TI.</td>", "<td>Diretoria Comercial, Controladoria e Diretoria de TI.</td>", tag="27")
R("H", '<p>Cada encontro começa pelo espelho: as palavras do grupo nas atas ("focar em tudo resulta em não entregar nada", "sala de guerra", "número invisível") e os casos que todos viveram (esgotamento de comissão, prestamista, BI fora do ar).<sup>11, 17, 18, 20</sup>',
       '<p>Cada encontro começa pelo espelho. De um lado, as palavras do grupo nas atas ("focar em tudo resulta em não entregar nada", "sala de guerra", "número invisível"); de outro, os casos que todos viveram (esgotamento de comissão, prestamista, BI fora do ar).<sup>11, 17, 18, 20</sup>', tag="Proposta 7")
R("H", "depois de frentes, S&amp;OP, diagnóstico e duas trocas de ferramenta.", "depois de frentes, S&amp;OP, Diagnóstico e duas trocas de ferramenta.", tag="31")
R("H", "<strong>Se tivermos sucesso.</strong> Em 90 dias, dois temas críticos em execução com dono, prazo e braço; uma fila única com poucas dezenas de itens carimbados; um fórum que delibera em duas horas; um desenho que a frente reconhece como seu e outras frentes podem copiar.",
       "<strong>Se der certo.</strong> Em 90 dias, dois temas críticos em execução com dono, prazo e braço; uma fila única com poucas dezenas de itens carimbados. Um fórum que delibera em duas horas; um desenho que a frente reconhece como seu e outras frentes podem copiar.", tag="52 / Proposta 5")
R("H", "<p>Em 90 dias: os oito indicadores do painel (aba Modelo), medidos primeiro nos dois temas da sala de guerra. Linha de base reconstruída com as atas de março a agosto; meta definida no encontro de piloto e medição. Se os indicadores não mexerem, o desenho muda, não as pessoas. </p>",
       "<p>Em 90 dias, pelos oito indicadores do painel, medidos primeiro nos dois temas da sala de guerra, com linha de base das atas e meta definida no encontro de piloto e medição (aba Modelo, seção Como se mede o sucesso). Se os indicadores não mexerem, o desenho muda, não as pessoas.</p>", tag="Proposta 4")
# Reuniões: as duas tabelas de "Em números" repetem as de "O custo da sala"
RX("H", r"<table>\n<thead><tr><th>Rito</th><th>Por ano</th><th>Por mês</th><th>Duração \(h\)</th><th>Pessoas</th><th>Custo por encontro</th><th>Custo por ano</th></tr></thead>\n<tbody>\n.*?</tbody>\n</table>\n", "", n=2, tag="Reuniões 1")
R("H", "<p><strong>Sistema atual, estimado.</strong> 101 encontros por ano, cerca de 8 por mês; R$ 286.500 por ano; custo médio por encontro de R$ 2.837.</p>",
       "<p><strong>Sistema atual, estimado.</strong> 101 encontros por ano, cerca de 8 por mês; R$ 286.500 por ano; custo médio por encontro de R$ 2.837.</p>\n<p>Rito a rito, com horas-pessoa e total, na seção O custo da sala, abaixo.</p>", tag="Reuniões 1")
R("H", "S&amp;OP e diagnóstico com cadência assumida mensal", "S&amp;OP e Diagnóstico com cadência assumida mensal", tag="31")
R("H", "mais a leitura que não houve antes e o material preparado para uma pauta que não existia.<sup>3, 10, 21</sup>", "sem leitura prévia e com material preparado sem pauta combinada.<sup>3, 10, 21</sup>", tag="Reuniões 4")

# ---------------- frag_I: Modelo
R("I", '<div class="alerta"><strong>VISÃO ATUAL, NÃO FINAL.</strong> Leitura de hoje, montada das atas e das reuniões de 1º de setembro. O modelo será desenhado com o time nos encontros da aba Proposta; o que sair de lá substitui isto.</div>',
       '<div class="alerta"><strong>VISÃO ATUAL, NÃO FINAL.</strong> Leitura de hoje, montada das atas e das reuniões de 1º de setembro; os fatos vêm das atas, o modelo é desenho a validar com o time nos encontros da aba Proposta, e o que sair de lá substitui isto.</div>', tag="Modelo 1")
R("I", '\n<div class="alerta"><strong>PROPOSTA.</strong> Os fatos citados vêm das atas; o modelo é desenho a validar com o time.</div>\n', '\n', tag="Modelo 1")
R("I", '>quinzenal, 1h30</text>', '>semanal, 1h30</text>', tag="44")
R("I", "Duas camadas e o contrato entre elas; o sucesso é do sistema, nunca da adoção do modelo.</figcaption>", "Duas camadas e o contrato entre elas: o que desce e o que sobe.</figcaption>", tag="Modelo 2")
R("I", "<td>Lê o painel dos oito indicadores e as fricções registradas nas fichas de reunião; identifica onde o fluxo trava (porta, triagem, alçada, capacidade, retorno); propõe a correção com dado; executa o que cabe nos ritos; articula com TI, Processos e líderes de esteira o que exige mudança fora deles; registra o que mudou e o efeito medido.</td>",
       "<td><ul><li>Lê o painel dos oito indicadores e as fricções registradas nas fichas de reunião;</li><li>identifica onde o fluxo trava (porta, triagem, alçada, capacidade, retorno);</li><li>propõe a correção com dado;</li><li>executa o que cabe nos ritos;</li><li>articula com TI, Processos e líderes de esteira o que exige mudança fora deles;</li><li>registra o que mudou e o efeito medido.</li></ul></td>", tag="Modelo 5")
R("I", "(S&amp;OP, Diagnóstico e frente como agendas separadas)", "(S&amp;OP, Diagnóstico e Frente como agendas separadas)", tag="30")
R("I", "critério de despriorização definidos pela diretoria de TI.", "critério de despriorização definidos pela Diretoria de TI.", tag="27")
R("I", "Três planos a acompanham desde o primeiro dia: mudança (o que muda para cada ator e quando), comunicação (quem diz o quê, antes, a cada mês e na leitura de três meses) e regressão (como se volta sem perder o aprendido).", "Três planos a acompanham desde o primeiro dia: mudança, comunicação e regressão (tabela acima).", tag="Modelo 6")

# ---------------- frag_J: Alçadas
R("J", "<td>Diretoria técnica acima da faixa</td>", "<td>Diretoria Técnica acima da faixa</td>", tag="28")
R("J", "<td>Diretoria técnica só em mudança de tábua ou de estrutura</td>", "<td>Diretoria Técnica só em mudança de tábua ou de estrutura</td>", tag="28")
R("J", "<td>Diretoria de riscos acima da faixa</td>", "<td>Diretoria de Riscos acima da faixa</td>", tag="28")
R("J", "<td>Estrutura (Papéis e pessoas); Proposta, sessão 5</td>", "<td>Estrutura (Papéis e pessoas); Proposta, desenho 6 (Papéis e dedicação)</td>", tag="22")
R("J", "<td>Estratégia a entrega; Fluxo funcional</td>", "<td>Aba Caminho; Fluxo funcional (aba Fluxo)</td>", tag="1 / e")
R("J", "<td>Estratégia a entrega (capacidade)</td>", "<td>Aba Caminho (capacidade)</td>", tag="2 / e")
R("J", "No esgotamento de comissão, o Fórum de Negócio decide dentro do orçamento aprovado, consultando Controladoria, Canais e TI; acima do orçamento, recomendação única ao COMEX em cinco dias úteis, levada pelo mentor na reunião seguinte, com resposta por escrito em até 30 dias.",
       "No esgotamento de comissão, o Fórum de Negócio decide dentro do orçamento aprovado, consultando Controladoria, Canais e TI. Acima do orçamento, o líder da esteira escreve a recomendação única em cinco dias úteis; o mentor a leva na reunião seguinte; a resposta volta por escrito em até 30 dias.", tag="Alçadas 4")

# ---------------- frag_K: Problema
R("K", "critério de despriorização pedido à diretoria de TI (aba Modelo).", "critério de despriorização pedido à Diretoria de TI (aba Modelo).", tag="27")
R("K", "em julho o fechamento de 2024 ainda não estava com o grupo; nenhuma ata registra se o OKR", "em julho o fechamento de 2024 ainda não estava com o grupo. Nenhuma ata registra se o OKR", tag="Problema (frase longa)")
R("K", "nenhum time, cargo ou ferramenta novos.", "nenhum time, cargo ou ferramenta nova.", tag="7")

# ---------------- frag_L: Riscos
R("L", "As áreas já viram frentes, S&amp;OP, diagnóstico, Jira", "As áreas já viram frentes, S&amp;OP, Diagnóstico, Jira", tag="31")
R("L", "por não entregar prestamista prêmio único em janeiro de 2027", "por não entregar prestamista de prêmio único em janeiro de 2027", tag="35")
R("L", "Cota reservada e critério de despriorização pedidos à diretoria de TI.", "Cota reservada e critério de despriorização pedidos à Diretoria de TI.", tag="27")
R("L", "aceitação médica e compliance decidem caso a caso, sem via de reconsideração registrada.<sup>10, 11, 18</sup>", "aceitação médica e compliance decidem caso a caso, sem alçada compartilhada; as atas não registram via de reconsideração.<sup>10, 11, 18</sup>", tag="b")
R("L", "<h3>Juntar S&amp;OP, Diagnóstico e frente numa agenda só", "<h3>Juntar S&amp;OP, Diagnóstico e Frente numa agenda só", tag="30")
R("L", "o que deixa de existir (as três agendas separadas) para em data marcada.", "o que deixa de existir (as três agendas separadas) é encerrado em data marcada.", tag="46")
R("L", "<li>Duas decisões que só a diretoria toma e que condicionam tudo: número-base assinado e capacidade de TI reservada (aba Executiva).</li>", "<li>Três decisões que só a diretoria toma e que condicionam tudo: número-base assinado, alçada do fórum e capacidade de TI reservada (aba Executiva).</li>", tag="42")
R("L", "o encontro de papéis formaliza o pedido à diretoria de TI.<sup>27</sup>", "o encontro de papéis formaliza o pedido à Diretoria de TI.<sup>27</sup>", tag="27")
R("L", "<li><strong>Quem é o dono do canal Unimed e do pós-venda de pessoa física.</strong> Duas cadeiras sem ocupante nas atas; o encontro de papéis nomeia as duas.<sup>15, 17</sup></li>",
       "<li><strong>Quem responde pelo pós-venda de pessoa física.</strong> A coordenação do canal Unimed tem responsável desde junho; o que falta é a estrutura comercial formalizada, com prazo a definir. O encontro de papéis nomeia quem responde pelo pós-venda.<sup>15, 17, 22</sup></li>", tag="a")
R("L", "A proposta é parar, para não somar salas.", "A proposta é encerrá-las, para não somar salas.", tag="47")
R("L", "Parado de 2024 a agosto de 2026, antes de a frente existir, foi encaminhado numa reunião curta", "Parado desde 2024, antes de a frente existir, até agosto de 2026, foi encaminhado numa reunião curta", tag="48")
R("L", "Se o modelo que entrega relatório ficar sem marcação", 'Se o risco "um modelo que entrega relatório" ficar sem marcação', tag="49")

# ---------------- pratica.py (dicionário legado; mantém-se coerente)
R("P", "uma das mentoras está de férias", "um dos mentores está de férias", tag="56")
R("P", "Tarefas da líder e da facilitadora nas atas de junho", "Tarefas da liderança e da facilitação nas atas de junho", tag="56")
R("P", "As horas que cada uma tem para a frente", "As horas que cada pessoa tem para a frente", tag="56")
R("P", "a atuária ajusta preço a cada trimestre", "a Atuarial ajusta preço a cada trimestre", tag="56")
R("P", 'a resposta hoje é "tudo": frente, S&amp;OP, diagnóstico, corretor, TI.', 'a resposta hoje é "tudo": Frente, S&amp;OP, Diagnóstico, corretor, TI.', tag="30 / 31")

for k, n in FILES.items(): save(n, F[k])
print("APLICADOS:", len(DONE))
for d in DONE: print("  ok", d)
print("NAO APLICADOS:", len(MISS))
for m in MISS: print("  MISS", m)
sys.exit(1 if MISS else 0)
