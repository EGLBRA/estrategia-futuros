# -*- coding: utf-8 -*-
"""v9: correções do checker de qualidade (parecer_checker_v8.md): CSS sel-p, selos no fim da frase, nomes por função,
anglicismos, gênero de 'time dedicado', contagens, referências, SVGs legíveis, hierarquia das abas mescladas."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
F = {k: load(f"frag_{k}.html") for k in "ABCDEFGHIJK"}
MISS = []
def R(k, old, new, rx=False, count=0):
    s = F[k]
    if rx:
        s2, n = re.subn(old, new, s, count=count, flags=re.S)
    else:
        n = s.count(old); s2 = s.replace(old, new) if n else s
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

# ---------- 1. selos no fim da frase
R("K", f'<p>{SV} nas evidências; {SP} nas entregas.</p>', f'<p>As evidências vêm das atas. {SV} As entregas são desenho a validar nas sessões. {SP}</p>')
R("J", f'<p>{SV} na coluna "hoje"; {SP} nas demais.</p>', f'<p>A coluna "hoje" vem das atas. {SV} As demais colunas são desenho a assinar. {SP}</p>')
RA(re.escape(SV) + r' (n[ao]s? [^;<]+); ' + re.escape(SP) + r' (n[ao]s? [^.<]+)\.', r'O que está \1 vem das atas. ' + SV + r' O que está \2 é desenho. ' + SP, rx=True)
R("B", f'{SV}<sup>25</sup> A classificação', f'Sintomas e citações conferidos nas atas. {SV}<sup>25</sup> A classificação')
R("B", f'{SV} Nota de leitura:', f'Falas conferidas na transcrição. {SV} Nota de leitura:')
R("A", f'{SV} o contraste é leitura deste documento. {SI}', f'As duas colunas vêm do PIE e das atas. {SV} O contraste é leitura deste documento. {SI}')
R("B", f'{SV} apoiada nas mesmas atas.', f'Inventário apoiado nas mesmas atas. {SV}')
R("C", f'{SV} as duas leituras são {SI}', f'O sinal está na ata. {SV} As duas leituras são deste documento. {SI}')
R("G", f'evita {SP} e as durações são {SP}', f'evita. Critérios e durações são desenho a calibrar nas sessões. {SP}')
R("G", r'<p>\s*' + re.escape(SP) + r' Leitura:(.*?)</p>', r'<p>Leitura:\1 ' + SP + '</p>', rx=True)
R("E", f'que sustenta cada relação {SP} e o formato de porta única é {SP}', f'que sustenta cada relação. O formato de porta única é desenho a validar. {SP}')
R("F", f'{SP}: cada item responde a um sintoma verificado.', f'Cada item responde a um sintoma verificado. {SP}')
R("F", r'leva (<span[^>]*>)?Inferência(</span>)? ou (<span[^>]*>)?Especulativo(</span>)?', 'leva o selo ' + SP, rx=True)

# ---------- 2. nomes por função
R("A", r' \((Jacqueline), líder\)', ' (líder)', rx=True); R("A", r' \(Alan, colíder\)', ' (colíder)', rx=True)
R("A", r' \((Tatiane|Glace|Aretha|Alessandra|Landi|Daniel|Fabíola)\)', '', rx=True)
R("A", "Mentor Aguiar propõe", "O mentor comercial propõe")
RA("Mentores (Aguiar, Lara, Alex)", "Mentores (três superintendentes)")
R("A", "Área de Estratégia (Fabíola, Caio, Daniele/VMO)", "Área de Estratégia (facilitação, método e VMO)")
R("A", "Inteligência de Mercado (Daniel, Amanda, V4)", "Inteligência de Mercado (analistas e painel V4)")
R("A", "falta de dados de Landi", "falta de dados do responsável por canais")
R("B", "Saídas de Aline, Márcio e Cibele", "Saída de três consultores")
R("B", "Hub trava com ausências de Landi; retenção depende da reprecificação de Glace", "Hub trava com ausências do responsável por canais; retenção depende da reprecificação feita por uma única atuária")
R("B", "Liderança rotativa Jacqueline e Alan", "Liderança rotativa entre líder e colíder")
R("B", "Jacqueline A. Martins (líder; estratégia comercial Vida e RE)", "Líder da frente (estratégia comercial Vida e RE)")
R("B", "Alan Schiavoni Reynol (colíder; subscrição e operação de RE)", "Colíder (subscrição e operação de RE)")
R("B", "Fabíola Pereira Brandão (facilitadora, Estratégia)", "Facilitação (área de Estratégia)")
R("B", "Glace Anne Carvas da Silva (atuarial)", "Atuarial")
R("B", "Christian Ramos Landi (canais)", "Canais")
R("B", "Daniel Vicentini (sinistro e inteligência)", "Sinistro e inteligência")
R("B", r'<td>(?:[A-ZÁ-Ú][\wáéíóúãõâêôç.]+ ){1,4}[A-ZÁ-Ú][\wáéíóúãõâêôç.]+ \(([^)]+)\)</td>', lambda m: '<td>' + m.group(1)[0].upper() + m.group(1)[1:] + '</td>', rx=True)
R("B", "plano diretivo de retenção (Alex)", "plano diretivo de retenção (um dos mentores)")
R("B", "<th>Pessoa (papel)</th>", "<th>Papel</th>")
R("B", "participação intermitente nas atas", "presença irregular nas atas")
R("B", "férias em julho", "ausência em julho"); R("B", "Férias em agosto", "Ausência em agosto"); R("B", "Férias em julho e agosto", "Ausências em julho e agosto")
R("C", "Esteira Vida (líder Jacqueline;", "Esteira Vida (líder da frente;"); R("C", "Esteira RE (líder Alan;", "Esteira RE (colíder;")
R("C", "Aguiar desmistifica", "o mentor comercial desmistifica")
R("D", "Jacqueline (líder), Alan (colíder), Fabíola (Estratégia), Tatiane, Glace, Alessandra, Landi, Aretha, Daniel.", "Nove pessoas: líder e colíder, facilitação da Estratégia, produtos, atuarial, tecnologia, canais, subscrição de Vida e operações, sinistro e inteligência.")
R("D", "Rodrigo Aguiar (Diretoria Comercial), Lara Facchini e Alex Rocha.", "Três superintendentes, um deles da Diretoria Comercial.")
R("D", "Três (Aline, Márcio, Cibele)", "Três")
R("D", "coloca Landi na liderança", "coloca o responsável por canais na liderança")
R("D", "Ausências de Landi", "Ausências do responsável por canais")
R("D", "De Landi; sem suplente", "Do responsável por canais; sem suplente")
R("D", "com Camila Fernanda Silva Gomes, Eric Leite e Fabíola Brandão", "com duas integrantes da área de Estratégia e o autor deste documento")
R("D", "com Camila Fernanda Silva Gomes, Fabíola Brandão, Ingrid Guaiato Campos Alves e Kelly Cristina Alonso Adolpho", "com integrantes das áreas de Estratégia e Agilidade")
R("D", "Usada nas abas Fluxo funcional e Perguntas de design", "Usada nas abas de proposta, sobretudo Fluxo funcional e Desenho e regras")

# ---------- 3. anglicismos
RA("blueprint organizacional", "planta organizacional"); RA("blueprint da Previdência", "planta organizacional da Previdência"); RA("O blueprint macro", "A planta macro"); RA("blueprint", "planta organizacional")
RA("cíclico na prática", "cíclica na prática")
for a, b in [("o deck", "a apresentação"), ("do deck", "da apresentação"), ("no deck", "na apresentação"), ("um deck", "uma apresentação"), ("deck de", "apresentação de"), ("O deck", "A apresentação"), ("deck", "apresentação")]:
    for k in F: F[k] = F[k].replace(a, b)
RA("renovação as-is", "renovação sem alteração"); RA("sobe só o as-is", "sobe só o que já existe"); RA("as-is", "sem alteração")
RA("cota e SLA", "cota e prazo"); RA("nem SLA", "nem prazo de atendimento"); RA("SLA", "prazo de atendimento")
RA("POC", "prova de conceito"); RA("motor, front e API", "motor, tela de uso e API"); RA("leads do Coopday", "contatos do Coopday")
RA("expertise", "conhecimento especializado"); RA("home office", "trabalho remoto"); RA("book de cooperativas", "carteira de cooperativas"); RA("Pipeline de renovações", "Esteira de renovações")
RA("Weeklys semanais", 'reuniões semanais ("Weeklys")'); RA("uma PM aqui, um PO ali", "um gestor de produto aqui, um dono de carteira ali"); RA("SPFC", "São Paulo FC")
R("E", "alimenta a squad; a squad faz discovery e concepção", "alimenta o time dedicado; o time faz descoberta e concepção")

# ---------- 4. gênero e resíduos
for a, b in [("a time dedicado", "o time dedicado"), ("A time dedicado", "O time dedicado"), ("da time dedicado", "do time dedicado"), ("na time dedicado", "no time dedicado"), ("numa time dedicado única", "num time dedicado único"),
             ("uma time dedicado", "um time dedicado"), ("as times dedicados", "os times dedicados"), ("das times dedicados", "dos times dedicados"), ("essa time dedicado", "esse time dedicado"),
             ("time dedicado dedicada", "time dedicado"), ("time dedicado alocada", "time dedicado alocado"), ("o descoberta", "a descoberta"), ("pelo descoberta", "pela descoberta"), ("Descoberta curto", "Descoberta curta"),
             ("demandas acumulado", "demandas acumulada"), ("Sustentação (sustentação)", "Sustentação (fila própria)"), ("sustentação triado, direto, sem descoberta", "Item de sustentação triado; segue direto, sem descoberta"),
             ("do carteira", "da carteira"), ("etapa. sustentação não passa por ela", "etapa. A sustentação não passa por ela"), ("fórum de negócio", "Fórum de Negócio"), ("fórum de gestão", "Fórum de Gestão"),
             ("conforme governança, a confirmar", "Conforme governança, a confirmar"), ("Estrutural, sustentação, Adequação e Oportunidade", "Estrutural, Sustentação, Adequação e Oportunidade"), (". .", "."), ("nove papéis assinados", "nove entregas assinadas")]:
    RA(a, b)
R("E", "O que a Agilidade descreveu como o problema não chega cru à TI, chega com diagnóstico é exatamente essa etapa.", "O que a Agilidade descreveu (o problema não chega cru à TI; chega com diagnóstico) é exatamente essa etapa.<sup>27</sup>")

# ---------- 5. texto por aba
R("A", "<h2>Em resumo</h2>", "<h3>Em resumo</h3>"); R("A", "Setenta e dois sintomas em 24 atas", "Setenta e dois sintomas em 24 documentos")
R("A", "sem saber que os repetia<sup>26</sup>, e os mais repetidos não falam", "sem perceber que os repete.<sup>26</sup> Os mais repetidos não falam"); R("A", "sem saber que os repetia", "sem perceber que os repete")
R("A", "está de férias até o fim do mês.<sup>20</sup>", "está de férias até o fim do mês.<sup>20, 22</sup>")
R("A", "cercado por onze atores", "cercado por treze atores")
R("A", "Quinze meses entre a segunda entrada e a primeira decisão de estudar.", "Quinze semanas entre a retomada, em maio, e a primeira decisão de estudar, em agosto; mais de dois anos desde o primeiro pedido.")
R("A", "seriam os times dedicados, com o Fórum de Negócio como rito de entrega dos times dedicados", "seriam os times dedicados, com o Fórum de Negócio como rito de entrega desses times")
R("G", r"Quinze meses entre a segunda entrada do esgotamento[^.<]*", "Quinze semanas entre a retomada do esgotamento de comissão (5 de maio) e a autorização de um estudo (17 de agosto), depois de dois anos parado", rx=True)
m = list(re.finditer(r'<h3>A proposta, em duas linhas</h3>\s*<p>.*?</p>\s*', F["G"], re.S))
if len(m) >= 2: F["G"] = F["G"][:m[-1].start()] + F["G"][m[-1].end():]
else: MISS.append(("G", "duplicata A proposta, em duas linhas"))
R("G", "ou a capacidade aumenta: sem isso o time dedicado diagnostica", "Ou a capacidade aumenta; sem isso, o time dedicado diagnostica")
R("G", "que hoje não existem (aba Estratégia a entrega)", "que hoje não existem (aba Reuniões e custo)")
R("G", "duas que a Estratégia toma sozinha (esteiras separadas, porta única)", "duas que mentores e Estratégia resolvem sem a diretoria (esteiras separadas, porta única)")
R("G", "A tabela abaixo estima o sistema de ritos proposto e, para comparação", "A aba Reuniões e custo estima o sistema de ritos proposto e, para comparação")
R("G", "o prazo mais duro que a frente tem pela frente", "o prazo mais duro que o grupo tem à frente")
R("H", "É o que evita as áreas acabam fazendo", "É o que evita que as áreas acabem fazendo")
R("H", "produz cinco desenhos assinados pelo time e uma decisão de piloto", "produz seis desenhos assinados pelo time e um plano de piloto; ao todo, as nove entregas da aba Problema e entregas")
R("H", "Aba Papéis e pessoas", "Aba Estrutura, seção Papéis e pessoas")
R("H", "O que está em jogo, o que muda, e se falharmos, e se tivermos sucesso", "O que está em jogo, o que muda, o que acontece se falharmos e se tivermos sucesso")
R("H", r"<td>(\d)\.(\d{1,2})</td>", r"<td>\1,\2</td>", rx=True); R("H", "<h4>", "<h3>"); R("H", "</h4>", "</h3>")
R("J", "consulta Controladoria e Canais e, se o valor exceder o orçamento, escreve", "consulta Controladoria, Canais e TI. Se o valor exceder o orçamento, escreve")
R("F", "<h2>Perguntas de design: as respostas, uma a uma</h2>", "<h2>Desenho e regras: as perguntas de desenho organizacional, uma a uma</h2>")
R("F", r"(oito elos[^<]*?)Concepção, ", r"\1", rx=True)
R("F", "Plano de entregas único produto, motor, tela de uso e API", "Plano de entregas único (produto, motor, tela de uso e API)")
R("F", "antes do problema.</strong> trocar o formato sem definir o que se está tratando; o método está sendo discutido antes do problema.", "antes do problema.</strong> Nas palavras da reunião: trocar o formato sem definir o que se está tratando é discutir o método antes do problema.")
R("F", ", porque hoje o Hub de Cooperativas parou", "; o Hub de Cooperativas parou")
t = list(re.finditer(r'<p class="tese">', F["F"]))
if len(t) >= 2: F["F"] = F["F"][:t[1].start()] + '<p class="note">' + F["F"][t[1].end():]
R("B", "Três dados que não existem e que o negócio precisa", "Quatro dados que não existem e de que o negócio precisa")
R("K", "critério de despriorização pedido à diretoria de TI.</td>", "critério de despriorização pedido à diretoria de TI (aba O modelo).</td>")

# ---------- 6. Fluxo funcional (frag_E): faixa, textos e setas
E = F["E"]
E = re.sub(r'<div style="background:#d0342c[^"]*">\s*<b[^>]*>RASCUNHO</b>\s*<span[^>]*>.*?</span>\s*</div>',
 '<div class="alerta"><strong>EXEMPLO PARA DISCUSSÃO.</strong> O mapa parte do esboço da Estratégia (Planejamento, Mapa, Times dedicados, Fórum de Negócio, Aceleradores, Projetos de torre) e acrescenta o que faltava nele: de onde nasce o problema, quando acontece a descoberta, para onde a solução vai e onde entram RDS e COMEX.<sup>26, 27</sup></div>', E, count=1, flags=re.S)
SV_FIX = [
 ('<text x="310" y="90" font-size="13.5" fill="#4a4f57">decidem política comercial, orçamento e o que envolve mais de um negócio; recebem exceção com recomendação única; devolvem decisão e patrocínio</text>',
  '<text x="310" y="88" font-size="13.5" fill="#4a4f57">decidem política comercial, orçamento e o que envolve mais de um negócio;</text><text x="310" y="105" font-size="13.5" fill="#4a4f57">recebem exceção com recomendação única; devolvem decisão e patrocínio</text>'),
 ('diretoria, superintendentes, Estratégia</text>', 'diretoria, superint., Estratégia</text>'),
 ('metas (diretores) e KRs (superintendentes)</text>', 'metas e KRs por diretoria e área</text>'),
 ('alimenta: prioridades do fórum e do time dedicado</text>', 'alimenta: prioridades do fórum</text>'),
 ('recebe: resultado do ciclo e lições</text>', 'recebe: resultado e lições</text>'),
 ('alimenta: KRs e capacidade do trimestre</text>', 'alimenta: KRs e capacidade</text>'),
 ('comercial, subscrição, atuarial,</text>', 'comercial, subscrição,</text>'), ('produtos, operação, canais</text>', 'atuarial, produtos, canais</text>'),
 ('Controladoria, Inteligência de</text>', 'Controladoria, IM, funil,</text>'), ('Mercado, funil, BI, sinistro</text>', 'BI, sinistro</text>'),
 ('SUSEP, Banco Central, ressegurador,</text>', 'SUSEP, BC, ressegurador,</text>'), ('Unicred, Marketing e patrocínio</text>', 'Unicred, Marketing</text>'),
 ('S&amp;OP Vida, Diagnóstico SUSEP,</text>', 'S&amp;OP Vida, Diagnóstico,</text>'), ('frente (absorvidos pelo fórum)</text>', 'frente; vão para o fórum</text>'),
 ('<rect x="335" y="352" width="190" height="56" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="371" font-weight="600">1. Recebe</text><text x="345" y="387" fill="#5a6068">problemas, pedidos, metas,</text><text x="345" y="401" fill="#5a6068">dados e resultados</text>',
  '<rect x="335" y="350" width="190" height="60" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="369" font-weight="600">1. Recebe</text><text x="345" y="385" fill="#5a6068">problemas, pedidos, metas,</text><text x="345" y="399" fill="#5a6068">dados e resultados</text>'),
 ('<rect x="335" y="418" width="190" height="56" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="437" font-weight="600">2. Tria e prioriza</text><text x="345" y="453" fill="#5a6068">estrutural, sustentação, adequação,</text><text x="345" y="467" fill="#5a6068">oportunidade; contra capacidade</text>',
  '<rect x="335" y="414" width="190" height="60" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="433" font-weight="600">2. Tria e prioriza</text><text x="345" y="447" fill="#5a6068">estrutural, sustentação,</text><text x="345" y="459" fill="#5a6068">adequação, oportunidade;</text><text x="345" y="471" fill="#5a6068">contra a capacidade</text>'),
 ('<rect x="335" y="484" width="190" height="56" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="503" font-weight="600">3. Decide na alçada</text><text x="345" y="519" fill="#5a6068">o que vai para o time dedicado; o que</text><text x="345" y="533" fill="#5a6068">sobe para RDS/COMEX</text>',
  '<rect x="335" y="478" width="190" height="60" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="497" font-weight="600">3. Decide na alçada</text><text x="345" y="513" fill="#5a6068">o que vai ao time; o que</text><text x="345" y="527" fill="#5a6068">sobe para RDS e COMEX</text>'),
 ('<rect x="335" y="550" width="190" height="56" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="569" font-weight="600">4. Recebe a entrega</text><text x="345" y="585" fill="#5a6068">e o resultado medido;</text><text x="345" y="599" fill="#5a6068">fecha ou devolve</text>',
  '<rect x="335" y="542" width="190" height="60" rx="5" fill="#fff" stroke="#c9e6d4"/><text x="345" y="561" font-weight="600">4. Recebe a entrega</text><text x="345" y="577" fill="#5a6068">e o resultado medido;</text><text x="345" y="591" fill="#5a6068">fecha ou devolve</text>'),
 ('aqui acontece: causa raiz, ouve a</text><text x="625" y="401" fill="#5a6068">ponta, olha o mercado, mede o valor;</text>', 'causa raiz, ouve a ponta,</text><text x="625" y="401" fill="#5a6068">olha o mercado, mede o valor;</text>'),
 ('paliativo, política, não fazer;</text>', 'paliativo, política, não fazer</text>'),
 ('indicador por item; segue a entrega</text><text x="625" y="581" fill="#5a6068">no destino; lê o resultado em</text><text x="625" y="595" fill="#5a6068">30 e 90 dias</text>', 'indicador por item; segue</text><text x="625" y="581" fill="#5a6068">a entrega no destino; lê o</text><text x="625" y="595" fill="#5a6068">resultado em 30 e 90 dias</text>'),
 ('fila de desenvolvimento; exige</text><text x="918" y="372" fill="#5a6068">critério de despriorização</text>', 'fila da TI; exige critério</text><text x="918" y="372" fill="#5a6068">de despriorização</text>'),
 ('dinheiro: sobe para RDS/COMEX</text>', 'orçamento: sobe a RDS e COMEX</text>'),
 ('<rect x="320" y="670" width="800" height="60" rx="8" fill="#f6f7f9" stroke="#5b626a" stroke-dasharray="5 4"/>', '<rect x="320" y="670" width="800" height="76" rx="8" fill="#f6f7f9" stroke="#5b626a" stroke-dasharray="5 4"/>'),
 ('<text x="340" y="713" font-size="13.5" fill="#4a4f57">a solução volta ao fórum como entrega validada pela operação e pela ponta; o resultado medido em 30 e 90 dias e os não-ganhos alimentam o PIE e o próximo mapa</text>',
  '<text x="340" y="713" font-size="13.5" fill="#4a4f57">a solução volta ao fórum como entrega validada pela operação e pela ponta;</text><text x="340" y="730" font-size="13.5" fill="#4a4f57">o resultado medido em 30 e 90 dias e os não-ganhos alimentam o PIE e o próximo mapa</text>'),
 # setas
 ('<path d="M540,505 L570,505 L570,506 L870,506 L898,506"/>', '<path d="M480,620 L480,632 L860,632 L860,506 L898,506"/>'),
 ('<path d="M1010,616 L1010,700 L1122,700"/>', '<path d="M1010,616 L1010,668"/>'),
 ('<path d="M990,199 L990,230 L1180,230 L1180,700 L1122,700"/>\n', ''),
 ('<path d="M990,135 L990,110 L410,110 L410,135 L410,135"/>\n', ''),
 ('<path d="M1010,552 L1010,116"/>', '<path d="M1120,584 L1150,584 L1150,80 L1112,80"/>'),
 ('<path d="M560,116 L560,300 L598,300"/>', '<path d="M570,116 L570,300 L598,300"/>'),
 ('<path d="M400,290 L400,116"/>', '<path d="M540,300 L550,300 L550,116"/>'),
 # rotulos
 ('<rect x="236" y="300" width="80" height="16" rx="4" fill="#fff" stroke="#c9e6d4"/><text x="276" y="312"', '<rect x="230" y="300" width="88" height="16" rx="4" fill="#fff" stroke="#c9e6d4"/><text x="274" y="312"'),
 ('<rect x="236" y="470" width="80" height="16" rx="4" fill="#fff" stroke="#c9e6d4"/><text x="276" y="482"', '<rect x="230" y="470" width="88" height="16" rx="4" fill="#fff" stroke="#c9e6d4"/><text x="274" y="482"'),
 ('<rect x="1030" y="640" width="120" height="16" rx="4" fill="#fff" stroke="#e2e6ea"/><text x="1090" y="652" text-anchor="middle">entrega em produção</text>', '<rect x="1020" y="634" width="130" height="16" rx="4" fill="#fff" stroke="#e2e6ea"/><text x="1085" y="646" text-anchor="middle">entrega em produção</text>'),
 ('<rect x="640" y="102" width="150" height="16" rx="4" fill="#fff" stroke="#e2e6ea"/><text x="715" y="114" text-anchor="middle">direção anual desce ao fórum</text>\n', ''),
 ('<rect x="1020" y="330" width="120" height="16" rx="4" fill="#fff" stroke="#e2d6f0"/><text x="1080" y="342" text-anchor="middle" fill="#6410ab">exceção sobe, decisão desce</text>', '<rect x="1158" y="322" width="176" height="16" rx="4" fill="#fff" stroke="#e2d6f0"/><text x="1246" y="334" text-anchor="middle" fill="#6410ab">exceção sobe, decisão desce</text>'),
 ('<rect x="452" y="200" width="150" height="16" rx="4" fill="#fff" stroke="#e2d6f0"/><text x="527" y="212" text-anchor="middle" fill="#6410ab">fora da alçada sobe</text>', '<rect x="386" y="258" width="130" height="16" rx="4" fill="#fff" stroke="#e2d6f0"/><text x="451" y="270" text-anchor="middle" fill="#6410ab">fora da alçada sobe</text>\n    <rect x="596" y="258" width="96" height="16" rx="4" fill="#fff" stroke="#e2d6f0"/><text x="644" y="270" text-anchor="middle" fill="#6410ab">decisão desce</text>\n    <rect x="640" y="624" width="180" height="16" rx="4" fill="#fff" stroke="#c9e6d4"/><text x="730" y="636" text-anchor="middle" fill="#00995d">sustentação vai direto à fila</text>'),
 ('<rect x="560" y="640" width="100" height="16" rx="4" fill="#fff" stroke="#e2e6ea"/><text x="610" y="652" text-anchor="middle">resultado medido</text>', '<rect x="728" y="644" width="104" height="16" rx="4" fill="#fff" stroke="#e2e6ea"/><text x="780" y="656" text-anchor="middle">resultado medido</text>'),
]
for a, b in SV_FIX:
    if a not in E: MISS.append(("E-svg", a[:70]))
    E = E.replace(a, b)
F["E"] = E

# ---------- 7. Estratégia a entrega (frag_G): tarja, fontes, textos
m = re.search(r'(<svg viewBox="0 0 1600 640".*?</svg>)', F["G"], re.S); svg = m.group(1)
for a, b in [('font-size="10"', 'font-size="12.5"'), ('font-size="11.5"', 'font-size="12.5"'), ('font-size="11"', 'font-size="12.5"'), ('font-size="12"', 'font-size="12.5"'),
             ('style="display:block;min-width:1180px;width:100%;height:auto;font-family:system-ui,sans-serif"', 'style="display:block;width:1600px;height:auto;font-family:system-ui,sans-serif"'),
             ('<text x="20" y="34" font-size="12.5" letter-spacing="2" fill="#666">FÓRUNS E RITOS</text>', '<text x="20" y="34" font-size="12.5" letter-spacing="2" fill="#666">FÓRUNS E RITOS</text><text x="1580" y="34" text-anchor="end" font-size="15" font-weight="700" letter-spacing="3" fill="#b71c1c">EXEMPLO</text>'),
             ('reconciliados com Controladoria', 'com Controladoria'), ('dono + Produtos, TI, IM, externos', 'dono, Produtos, TI, IM'), ('anual · diretoria, superint.,', 'anual · diretoria e Estratégia'), ('Estratégia · PIE trimestral', 'PIE trimestral'),
             ('exceção sobe com uma recomendação', 'exceção sobe com recomendação'), ('mensal · porta única de entrada', 'mensal · porta única'), ('+ triagem quinzenal (30 min)', 'triagem quinzenal (30 min)'), ('sala de guerra para críticos', 'sala de guerra (críticos)'),
             ('resolvido, recusado, estacionado', 'resolvido, recusado, parado'), ('e KRs por esteira (Vida, RE),', 'KRs por esteira (Vida e RE)'), ('desafios, capacidade por nome', 'desafios, gente por nome'), ('ponta, olha o mercado, decupa', 'ponta e mercado, decupa o'),
             ('o escopo com a TI; gera opções', 'escopo com TI; gera opções'), ('fila contra a capacidade real;', 'fila contra a capacidade;'), ('dono, prazo, braço, indicador</text>', 'dono, prazo, braço, medida</text>'), ('Processos, Dados) e volantes;', 'Processos, Dados) e áreas;'),
             ('completa, comunicação à ponta', 'completa, aviso à ponta'), ('não-ganhos e fecha cada item:', 'não-ganhos, fecha o item:'), ('problema, valor, opções, esforço', 'problema, valor, opções'), ('protege a cota de sustentação', 'protege a cota de sustentação')]:
    if a not in svg: MISS.append(("G-svg", a[:70]))
    svg = svg.replace(a, b)
F["G"] = F["G"].replace(m.group(1), svg)

for k, s in F.items(): save(f"frag_{k}.html", s)

# ---------- 8. build.py: CSS sel-p, conversor, hierarquia das abas mescladas
b = load("build.py")
if ".sel-p{" not in b:
    b = b.replace('.tabs{grid-template-columns:repeat(10,1fr)', '.sel-p{background:#e8f0fe;color:#1a4a8a} .tabs{grid-template-columns:repeat(10,1fr)', 1)
b = b.replace("SEL = {'sel-v': '[Verificado]', 'sel-i': '[Inferência]', 'sel-e': '[Especulativo]'}", "SEL = {'sel-v': '[Verificado]', 'sel-i': '[Inferência]', 'sel-e': '[Especulativo]', 'sel-p': '[Proposta]'}")
old = "        if j < len(parts) - 1:\n            body = re.sub(r'<div class=\"pratica\">.*?</div>\\s*(?=$)', '', body, flags=re.S)\n"
new = old + "        if j > 0:\n            body = body.replace('<h2>', '<h3>').replace('</h2>', '</h3>').replace('<p class=\"tese\">', '<p>')\n        elif tgt == 'estrutura':\n            body = re.sub(r'<h2>(.*?)</h2>', r'<h2>Estrutura: normas, papéis e sistemas</h2>\\n<h3>\\1</h3>', body, count=1, flags=re.S)\n"
assert old in b, "bloco MERGE nao encontrado"; b = b.replace(old, new)
save("build.py", b)
print("patch v9 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
