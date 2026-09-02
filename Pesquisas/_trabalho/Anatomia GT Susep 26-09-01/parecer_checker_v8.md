# Parecer do checker de qualidade (v8): Anatomia Profunda GT Susep Vida e RE (26-09-01)

Objeto: `A:\_01 Projetos\Estrategia\Pesquisas\Anatomia Profunda - GT Susep Vida e RE - 26-09-01\Anatomia Profunda - GT Susep Vida e RE - 26-09-01.html` (20 abas) e o espelho `.md` no mesmo diretório.
Régua automática (`checks.py`): 20 abas, média 9,9, só "selos" em Fluxo funcional e Sintomas. A régua é piso; as notas abaixo são de leitura integral, aba por aba, com os dez critérios do pedido.
Data: 2026-09-01, 21h40.

## 1. Notas por aba

| Aba | Nota | Principais falhas |
|---|---|---|
| Destaque | 7 | Frase de 97 palavras na tese com sobrescrito no meio e erro de tempo verbal ("repete... sem saber que os repetia"); "24 atas" no subtítulo (são 23 atas e um deck); "Em resumo" em h2 dentro da aba; seis frases acima de 35 palavras |
| Executiva | 5 | Seção "A proposta, em duas linhas" duplicada (título e parágrafo); "Quinze meses" onde o documento inteiro diz quinze semanas; ". ." no fim de parágrafo; célula que começa em minúscula ("ou a capacidade aumenta:"); custo remete à aba errada; tabela diz que mentores decidem as esteiras e o "Na prática" diz que a Estratégia decide sozinha |
| Problema e entregas | 8 | "nove papéis assinados" (ambíguo com papéis no sentido de cargos); selos no meio da frase ("Verificado nas evidências; Proposta nas entregas"), que no espelho .md viram frase quebrada |
| Proposta | 7 | Erro grave de sintaxe ("evita as áreas acabam fazendo"); "cinco desenhos" no texto contra seis na tabela e nove entregas na aba anterior; remete a "Aba Papéis e pessoas", que não existe; três "blueprint" fora de aspas; título de seção mal construído; lista de indicadores diferente da do painel |
| O modelo | 8 | Selos no meio da frase em três parágrafos; frase de 70 palavras em "Quantas reuniões"; de resto sólida e coerente com Reuniões e custo (51 encontros, R$ 381.625 conferem) |
| Alçadas | 9 | "Na prática" com frase de 52 palavras e que omite a TI entre os consultados; selo no meio da frase |
| Reuniões e custo | 7 | Decimais com ponto ("0.5", "1.5", "0.75", "0.25") na mesma tabela em que o ponto é milhar ("1.152", "3.053"); dois h4 (hierarquia é h2/h3); "conforme governança" em minúscula; "fórum de gestão" em minúscula; "blueprint" |
| Estratégia a entrega | 6 | Selo "Exemplo"/"Proposta" (classe `sel-p`) sem estilo no CSS; frase truncada com dois selos ("evita Proposta e as durações são Proposta"); "A tabela abaixo" sem tabela abaixo; selo no início de parágrafo; SVG sem tarja EXEMPLO dentro do desenho, fontes de 10 a 12 px num viewBox de 1600 (7 a 9 px na tela) e textos que ultrapassam as caixas de 170 px; "blueprint" |
| Fluxo funcional | 4 | Dez erros de gênero deixados pela troca squad/discovery ("o descoberta", "a time dedicado", "Sustentação (sustentação)", "sustentação triado", "acumulado"); frase sem sujeito no banner; banner "RASCUNHO" contradiz a regra de tarja EXEMPLO e a Proposta ("exemplos de partida"); frase com dois selos truncada; SVG com "squad" e "discovery" no aria-label, textos que estouram as caixas (governança, base, direção, fórum), seta roxa cruzando três caixas de destino, seta verde atravessando o time dedicado, linha roxa cruzando o Planejamento; "SLA" |
| Desenho e regras | 6 | Tese diz que proposta leva "Inferência ou Especulativo" (o documento usa Proposta); h2 "Perguntas de design" não é o nome da aba; "oito elos" com nove itens listados; "Plano de entregas único produto, motor, front e API" sem pontuação; "Descoberta curto"; quatro erros de gênero; item 8 começa em minúscula; anglicismos (front, leads, SLA, as-is, expertise, PM/PO sem aspas); "SPFC"; segunda tese no meio da aba |
| Entenda | 7 | Todos os membros nomeados; "seriam as times dedicados"; "fórum de negócio" em minúscula; selo sem frase ("Verificado o contraste é leitura"); "Weeklys" sem aspas; "deck" quatro vezes; nove frases acima de 35 palavras |
| Ecossistema | 7 | Tese diz "onze atores", a tabela tem treze; nomes de colegas entre parênteses; "fórum de negócio" em minúscula; PMO sem glossário |
| Processos | 6 | "Quinze meses" (é quinze semanas); "sem time dedicado dedicada"; "essa time dedicado"; frase de 67 palavras; nome de colega ("dados de Landi"); "SLA" |
| Sintomas | 8 | Duas frases de selo quebradas ("Verificado 25 A classificação... é Inferência"; "Verificado Nota de leitura"); nomes de consultores e de dois membros; frase de 64 palavras |
| Estrutura | 5 | Três h2 e três teses numa só aba (a aba "Estrutura" não tem h2 com esse nome); tabela com nome completo de nove pessoas, férias e "participação intermitente" (exposição de colegas); "Três dados" com quatro cartões; "Verificado apoiada nas mesmas atas" sem sujeito; frase de 81 palavras; "home office", "book", "pipeline", "as-is" |
| Loops | 9 | "parece ser preço" é descrição do laço, aceitável; frases longas são a forma do laço; nada a corrigir além de uma quebra opcional |
| Análise | 7 | Dois h2 e duas teses (Sutilezas dentro de Análise); "a time dedicado", "time dedicado alocada"; frase de selo quebrada ("Verificado as duas leituras são Inferência"); nome de mentor; matriz não traz os dois riscos que a régua pede no topo (estão só na Proposta) |
| Cem perguntas | 8 | "numa time dedicado única"; "Estrutural, sustentação, Adequação" com maiúscula inconsistente; nomes de colegas em seis respostas; "Weeklys" |
| Glossário | 7 | Quatro erros de gênero/regência ("uma time dedicado", "do carteira", "a time dedicado", "das times dedicados"); faltam SLA, VG, POC, PMO, IM, RCP, PMI, que o texto usa |
| Fontes | 6 | Nomes das participantes das transcrições (contradiz a própria regra "citadas por função"); nome do autor; fonte 25 listada depois de 26 e 27; fonte 27 remete a "Perguntas de design" (aba não existe); links para notebook.google.com expõem a ferramenta; frase de 65 palavras |

Média: 6,9. Duas falhas são transversais e valem para todas as abas de proposta: (a) a classe `sel-p` (selo Proposta e Exemplo, 33 ocorrências) não existe no CSS, então o selo aparece sem cor e sem fundo; (b) o espelho .md descarta o selo Proposta e deixa frases mutiladas ("[Verificado] nas evidências; nas entregas.", "e as durações são").

## 2. Falhas transversais (corrigir antes de qualquer aba)

1. **CSS.** Trecho: `.sel-v{background:#e6f2ea;color:#1b6b39}.sel-i{...}.sel-e{...}`. Acrescentar: `.sel-p{background:#efe9f7;color:#4a2c7a}`. Sem isso, "Proposta" e "Exemplo" saem em texto cru de 9 px.
2. **Espelho .md.** O conversor traduz sel-v/i/e para colchetes e ignora sel-p. Fazer o mesmo para `[Proposta]` e `[Exemplo]`, e reconferir as linhas 84, 265, 486 e 693 do .md, que hoje estão truncadas.
3. **Padrão "Verificado nas X; Proposta nas Y".** Aparece em Problema, O modelo (3x), Alçadas, Sintomas, Entenda, Estrutura, Análise. Trocar por frases inteiras com o selo no fim: "As evidências vêm das atas. [Verificado] As entregas são desenho a validar. [Proposta]".
4. **Gênero de "time dedicado".** A substituição de "squad" por "time dedicado" deixou 19 resíduos femininos. Lista completa na seção Português (itens P8 a P22, P29, P30, P38, P39, P44, P45, P47, P49 a P52).
5. **Nomes de colegas.** O documento nomeia 22 pessoas (membros, mentores, consultores que saíram, participantes das transcrições, autor). O checks.py só bloqueia quatro. Decidir um padrão único: função em todo o corpo (líder da frente, colíder, facilitação, atuarial, canais, mentor comercial), nomes só se houver aval do cliente. A tabela "Papéis e pessoas" (Estrutura), com nome completo, férias e "participação intermitente", é a mais sensível.
6. **"Quinze meses" versus "quinze semanas".** De 5 de maio a 17 de agosto de 2026 são quinze semanas; O modelo, Estratégia a entrega e Reuniões e custo dizem semanas; Executiva e Processos dizem meses. Corrigir os dois.
7. **Anglicismos fora de aspas** (a régua do checks.py não os pega): blueprint (5), deck (5), as-is (4), SLA (4), POC (4), front (1), leads (1), expertise (1), home office (1), book (1), pipeline (1), Weeklys (2), PM/PO (1). Sugestões na seção Português (P70 a P82).
8. **Contagens que não batem entre abas:** cinco desenhos (Proposta, texto) / seis (Proposta, tabela) / nove entregas (Problema); onze atores (Ecossistema, tese) / treze (tabela); oito elos (Desenho e regras) / nove listados; três dados (Estrutura, h3) / quatro cartões; lista de indicadores de sucesso em quatro versões (Executiva 5, Proposta 5, O modelo 8, Cem perguntas 5). Adotar os oito do painel de O modelo como lista canônica e citá-la nas outras abas.
9. **Referências a abas que não existem:** "Aba Papéis e pessoas" (Proposta, tabela dos desenhos), "Perguntas de design" (Fontes 27 e h2 da aba Desenho e regras).
10. **Tarja EXEMPLO nos SVGs.** Nenhum dos dois SVGs tem a tarja dentro do desenho. Estratégia a entrega tem uma caixa "EXEMPLO PARA DISCUSSÃO" acima; Fluxo funcional tem um banner "RASCUNHO". Colocar `<text>EXEMPLO</text>` no canto superior direito dos dois SVGs e renomear o banner de Fluxo funcional para EXEMPLO, alinhado à tese da Proposta ("os desenhos deste documento são exemplos de partida").

## 3. Por aba: o que corrigir para chegar a 9

### Destaque (7)
1. Trecho: "aparecem 72 sintomas organizacionais distintos, e a reunião de 1º de setembro". Frase de 97 palavras. Sugestão: "Em 24 documentos produzidos pelo próprio grupo entre 30 de março e 17 de agosto de 2026 aparecem 72 sintomas organizacionais distintos.<sup>25</sup> A reunião de 1º de setembro sobre o futuro Fórum de Negócio SUSEP repete os principais sem perceber que os repete.<sup>26</sup> Os mais repetidos não falam de mercado. Falam de agenda (nove fontes registram conflito de agenda ou falta de quórum), de dois negócios espremidos num único grupo e relatório (sete), de ritos com mentores comprimidos ou adiados (sete) e de engajamento que só existe durante a reunião (seis).<sup>25</sup>"
2. Trecho: "Setenta e dois sintomas em 24 atas mostram" (subtítulo do h1). Sugestão: "Setenta e dois sintomas em 24 documentos do próprio grupo mostram".
3. Trecho: "<h2>Em resumo</h2>". Sugestão: h3 (o h2 é só o título da aba).
4. Trecho: "A facilitação da frente registra que as mesmas pessoas participam" (55 palavras). Sugestão: "A facilitação da frente registra que as mesmas pessoas participam de quase todos os fóruns e que os assuntos se misturam entre as agendas. A equipe chamada a estruturar o novo modelo observa que há pressa, mas falta estrutura, e que o método está sendo discutido antes do problema.<sup>26</sup>"
5. Trecho: "está de férias até o fim do mês.<sup>20</sup> Às duas". A cena é 17 de agosto (fontes 22 e 23); a fonte 20 é 11 de agosto. Sugestão: "<sup>20, 22</sup>".
6. Trecho: "Entre novembro de 2025 e maio de 2026 saíram, entre outras," (50 palavras). Sugestão: fechar a lista em "96 painéis técnicos.<sup>1</sup>" e abrir nova frase para o resultado do RE (já é o que o texto faz; basta trocar a vírgula antes de "o RE fechou" por ponto).

### Executiva (5)
1. Trecho: "<h3>A proposta, em duas linhas</h3>" (segunda ocorrência, com o parágrafo). Apagar a duplicata.
2. Trecho: "Quinze meses entre a segunda entrada do esgotamento". Sugestão: "Quinze semanas entre a retomada do esgotamento de comissão (5 de maio) e a autorização de um estudo (17 de agosto), depois de dois anos parado".
3. Trecho: "itens sem saída explícita. .". Sugestão: "itens sem saída explícita."
4. Trecho: "ou a capacidade aumenta: sem isso o time dedicado diagnostica". Sugestão: "Ou a capacidade aumenta; sem isso, o time dedicado diagnostica e não entrega.<sup>27</sup>"
5. Trecho: "que hoje não existem (aba Estratégia a entrega)". Sugestão: "(aba Reuniões e custo)".
6. Trecho: "duas que a Estratégia toma sozinha (esteiras separadas, porta única)". A tabela diz que as esteiras são decisão dos mentores. Sugestão: "e duas que mentores e Estratégia resolvem sem a diretoria (esteiras separadas, porta única)".
7. Trecho: "tempo entre entrada e decisão, decisões com dono, prazo, braço e indicador, quórum dos ritos, itens sem saída explícita". Sugestão: "os oito indicadores do painel (aba O modelo), a começar pelo tempo entre entrada e decisão".
8. Trecho: "Em horas de sala, o sistema de reuniões proposto custa cerca de" (47 palavras). Sugestão: dividir em duas frases: "...contra cerca de R$ 286.000 do sistema atual estimado. A diferença compra triagem, descoberta e revisão de resultado, que hoje não existem (aba Reuniões e custo)."

### Problema e entregas (8)
1. Trecho: "a mesa tem nove papéis assinados e um piloto com data". Sugestão: "a mesa tem nove entregas assinadas e um piloto com data".
2. Trecho: "Verificado nas evidências; Proposta nas entregas." Sugestão: "As evidências vêm das atas. [Verificado] As entregas são desenho a validar nas sessões. [Proposta]"
3. Trecho: "Sala de descoberta com opções e esforço decupado; cota de sustentação; critério de despriorização pedido à diretoria de TI." Faltou "(aba O modelo)" como nas outras linhas. Sugestão: acrescentar.

### Proposta (7)
1. Trecho: "É o que evita as áreas acabam fazendo o que a Estratégia quer". Sugestão: "É o que evita que as áreas acabem fazendo o que a Estratégia quer, e não o que deveria ser feito.<sup>26</sup>"
2. Trecho: "que produz cinco desenhos assinados pelo time e uma decisão de piloto". Sugestão: "que produz seis desenhos assinados pelo time (o sexto, papéis, por último) e um plano de piloto; ao todo, as nove entregas da aba Problema e entregas".
3. Trecho: "Aba Papéis e pessoas" (linha 6 da tabela de desenhos). Sugestão: "Aba Estrutura, seção Papéis e pessoas". Na linha 5, "Desenho e regras" vira "Aba Desenho e regras".
4. Trecho: "O que está em jogo, o que muda, e se falharmos, e se tivermos sucesso". Sugestão: "O que está em jogo, o que muda, o que acontece se falharmos e se tivermos sucesso".
5. Trecho: "A régua é a mesma usada no blueprint organizacional da Previdência." Sugestão: "A régua é a mesma usada na planta organizacional da Previdência." (mesma troca em "Um blueprint organizacional de cada encontro" e "a mesma ficha usada no blueprint da Previdência").
6. Trecho: "tempo entre entrada e decisão medido nos dois temas da sala de guerra; percentual de decisões". Sugestão: "os oito indicadores do painel (aba O modelo), medidos primeiro nos dois temas da sala de guerra; linha de base reconstruída...".
7. Trecho: "Uma meta de 20% ao ano no ramo que a companhia escolheu" (60 palavras). Sugestão: quebrar em quatro frases, uma por item: "Uma meta de 20% ao ano no ramo escolhido como segundo motor de crescimento.<sup>1, 12</sup> Um balcão de cooperativa com prazo em janeiro de 2027.<sup>17</sup> O canal que representa 65% da operação e já migra para quem paga esgotamento.<sup>22, 23</sup> E a credibilidade da Estratégia diante das áreas, depois de frentes, S&OP, diagnóstico e duas trocas de ferramenta.<sup>15, 26</sup>"
8. Trecho: "Em 90 dias, dois temas críticos decididos e em execução" (47 palavras). Sugestão: ponto depois de "braço" e depois de "duas horas".
9. Trecho: "Cada reunião que sair das sessões recebe a mesma ficha" (42 palavras). Sugestão: ponto depois de "custo da sala"; a frase seguinte já começa em "A ficha é o contrato".

### O modelo (8)
1. Trecho: "Verificado nas linhas de base; Proposta nos indicadores." Sugestão: "As linhas de base vêm das atas. [Verificado] Os indicadores são desenho. [Proposta]" Mesmo padrão em "nos exemplos; ... na tipologia" e "nos fatos; ... nas interfaces".
2. Trecho: "O sistema inteiro, num mês típico com duas esteiras" (70 palavras). Sugestão: "O sistema inteiro, num mês típico com duas esteiras, dois desafios em descoberta e um tema em sala de guerra, tem 51 encontros. São 8 reuniões de esteira (1h30), 2 triagens (30 min), 1 comitê (1h), 1 Fórum de Negócio (2h), 1 mentoria por tema (1h), 2 revisões de time (45 min), 8 encontros de descoberta (2h), 8 de sala de guerra (1h) e cerca de 20 reuniões diárias do núcleo (15 min). A maioria é curta e com poucas pessoas. O que cada pessoa vive é o que importa:"
3. Trecho: "No modelo, a reunião da esteira só aceita enquadramentos e entregas" (39 palavras). Sugestão: ponto depois de "recomendação única".

### Alçadas (9)
1. Trecho: "Verificado na coluna "hoje"; Proposta nas demais." Sugestão: "A coluna "hoje" vem das atas. [Verificado] As demais são desenho a assinar. [Proposta]"
2. Trecho: "consulta Controladoria e Canais e, se o valor exceder" (52 palavras). Sugestão: "consulta Controladoria, Canais e TI. Se o valor exceder o orçamento, escreve uma recomendação única para o COMEX em cinco dias úteis; o mentor a leva na reunião seguinte; a resposta volta por escrito em até 30 dias."

### Reuniões e custo (7)
1. Trecho: "0.5", "1.5", "0.75", "0.25" (coluna Duração nas duas tabelas). Sugestão: "0,5", "1,5", "0,75", "0,25". Hoje o ponto é decimal numa coluna e milhar na vizinha ("1.152").
2. Trecho: "<h4>Sistema proposto</h4>" e "<h4>Sistema atual (estimado a partir das atas)</h4>". Sugestão: h3, ou `<p><strong>`.
3. Trecho: "conforme governança, a confirmar". Sugestão: "Conforme governança, a confirmar".
4. Trecho: "fórum de gestão de até quatro horas, mentoria de meia hora". Sugestão: "Fórum de Gestão de até quatro horas".
5. Trecho: "No mesmo formato do blueprint organizacional da Previdência". Sugestão: "No mesmo formato da planta organizacional da Previdência".
6. Trecho: "Some o que a frente gasta hoje numa segunda-feira típica" (47 palavras). Sugestão: ponto depois de "dez pessoas"; "Some o tempo de quem chega sem ter lido nada e a hora de quem preparou um material que não será discutido porque a pauta não existia."

### Estratégia a entrega (6)
1. Trecho: "Os sobrescritos apontam para o sintoma que cada critério evita Proposta e as durações são Proposta". Sugestão: "Os sobrescritos apontam o sintoma que cada critério evita. Critérios e durações são desenho a calibrar nas sessões. [Proposta]"
2. Trecho: "A tabela abaixo estima o sistema de ritos proposto e, para comparação". Não há tabela abaixo. Sugestão: fundir os dois parágrafos: "Toda reunião é uma entrega que custa horas de sala. A aba Reuniões e custo estima o sistema proposto e o atual com o mesmo parâmetro, valor-hora médio de R$ 125 (a planilha anexa recalcula com outro valor). Resumo: proposto perto de R$ 381.625 por ano; atual estimado perto de R$ 286.500."
3. Trecho: "<p> Proposta Leitura: o desenho proposto custa mais horas". Sugestão: mover o selo para o fim: "...cabe no custo de uma única decisão travada por quinze semanas. [Proposta]"
4. Trecho: "o prazo mais duro que a frente tem pela frente". Sugestão: "o prazo mais duro que o grupo tem à frente".
5. Trecho: "O blueprint macro, linear na leitura e cíclico na prática." Sugestão: "A planta macro, linear na leitura e cíclica na prática."
6. SVG, tarja: acrescentar `<text x="1560" y="30" text-anchor="end" font-size="14" font-weight="700" fill="#b71c1c">EXEMPLO</text>`.
7. SVG, legibilidade: os menores textos têm `font-size="10"` a `"12"` num viewBox de 1600 exibido em 1100 px, o que dá 7 a 9 px na tela. Sugestão: mínimo 13 nos rótulos ("mapa", "carteira", "ficha"), 14 no corpo das caixas; ou reduzir o viewBox para 1400 e encurtar textos.
8. SVG, transbordo: "reconciliados com Controladoria", "dono + Produtos, TI, IM, externos", "anual · diretoria, superint.," e "exceção sobe com uma recomendação" ultrapassam a caixa de 170 px (a 12 px, cerca de 190 a 215 px). Sugestão: "com Controladoria"; "dono, Produtos, TI, IM"; "anual · diretoria e Estratégia"; "exceção sobe com recomendação".
9. Trecho: "Com dois temas em sala de guerra (esgotamento de comissão e prestamista de prêmio único)" (42 palavras). Sugestão: ponto depois de "começa cheia".

### Fluxo funcional (4)
1. Trecho: "Parte do esboço da Estratégia (Planejamento, Mapa, Times dedicados". Sugestão: "O mapa parte do esboço da Estratégia (...) e acrescenta o que faltava nele: de onde nasce o problema, quando acontece a descoberta, para onde a solução vai e onde entram RDS e COMEX."
2. Trecho: "RASCUNHO" (banner vermelho). Sugestão: "EXEMPLO", com o mesmo texto de apoio; a Proposta chama os desenhos de exemplos de partida, não de rascunho.
3. Trecho: "é descoberto e concebido na time dedicado e sai". Sugestão: "no time dedicado".
4. Trecho: "sustentação triado, direto, sem descoberta". Sugestão: "Item de sustentação triado; segue direto, sem descoberta".
5. Trecho: "Carteira de demandas acumulado, planilha de necessidades". Sugestão: "Carteira de demandas acumulada".
6. Trecho: "que sustenta cada relação Proposta e o formato de porta única é Proposta". Sugestão: "Os sobrescritos apontam o registro, nas atas ou nas reuniões de 1º de setembro, que sustenta cada relação. O formato de porta única é desenho a validar. [Proposta]"
7. Trecho: "Quando acontece o descoberta." Sugestão: "Quando acontece a descoberta."
8. Trecho: "É a primeira coisa que a time dedicado faz com um problema". Sugestão: "que o time dedicado faz".
9. Trecho: "O que a Agilidade descreveu como o problema não chega cru à TI, chega com diagnóstico é exatamente essa etapa. sustentação não passa por ela." Sugestão: "O que a Agilidade descreveu (o problema não chega cru à TI; chega com diagnóstico) é exatamente essa etapa.<sup>27</sup> A sustentação não passa por ela."
10. Trecho: "Sustentação (sustentação) ou RDS/COMEX (política e orçamento)". Sugestão: "Sustentação (fila própria) ou RDS e COMEX (política e orçamento)". Mesma correção na caixa do SVG "Sustentação (sustentação)".
11. Trecho: "recebem da time dedicado, via fórum". Sugestão: "do time dedicado".
12. SVG, aria-label: "alimenta a squad; a squad faz discovery e concepção". Sugestão: "alimenta o time dedicado; o time faz descoberta e concepção".
13. SVG, caixa "não passa pelo descoberta". Sugestão: "não passa pela descoberta". E "fila própria, cota e SLA" vira "fila própria, cota e prazo".
14. SVG, transbordo: a linha de 150 caracteres da caixa COMEX e RDS (y=90) e a de 165 da caixa Entrega e medição (y=713) medem cerca de 1000 e 1100 px a 13,5 px e as caixas têm 820 e 800 px. Quebrar em duas linhas cada. Também estouram: "diretoria, superintendentes, Estratégia" (caixa de 240), "alimenta: prioridades do fórum e da time dedicado" (caixa de 240), "alimenta: KRs e capacidade do trimestre" (240), "estrutural, sustentação, adequação," (sub-caixa de 190), "o que vai para a time dedicado; o que" (190). Encurtar ou quebrar.
15. SVG, rótulos: "dores, pedidos" e "prazos, regras" em caixas de 80 px, "exceção sobe, decisão desce" e "direção anual desce ao fórum" em caixas de 120 e 150 px; o texto passa da borda. Alargar para 100, 100, 180 e 190.
16. SVG, sobreposições: (a) a seta roxa `M1010,552 L1010,116` sobe atravessando as caixas Processos, Aceleradores e Projetos de torre; levar por x=1140 (à direita das caixas). (b) A seta verde `M540,505 ... L870,506 L898,506` atravessa a caixa do time dedicado até Sustentação; contornar por baixo (y=640). (c) A linha roxa `M400,290 L400,116` corta a caixa Planejamento estratégico (x 290 a 530); mover para x=275. (d) O caminho `M990,135 L990,110 L410,110` corre dentro da caixa COMEX e RDS (y 45 a 115); usar y=125.
17. SVG, largura: `style="width:1400px"` obriga rolagem horizontal em qualquer tela. Sugestão: `min-width:1100px;width:100%`.
18. Trecho: "De cinco origens, não de uma: a ponta comercial" (51 palavras). Sugestão: ponto depois de "as três esteiras que o fórum absorve.<sup>26</sup>" já existe; quebrar a enumeração em "a ponta comercial...<sup>18</sup>; as áreas...<sup>20</sup>; os dados...<sup>27</sup>." com ponto e vírgula, e nova frase "Hoje cada origem tem uma porta diferente."

### Desenho e regras (6)
1. Trecho: "o que é proposta leva Inferência ou Especulativo". Sugestão: "o que é proposta leva o selo Proposta".
2. Trecho: "<h2>Perguntas de design: as respostas, uma a uma</h2>". Sugestão: "Desenho e regras: as perguntas de desenho organizacional, uma a uma".
3. Trecho: "Uma cadeia com oito elos, cada um com entrada, saída, dono e critério de passagem". A lista tem nove nomes. Sugestão: retirar "Concepção" (na aba Estratégia a entrega ela está dentro da Descoberta).
4. Trecho: "Plano de entregas único produto, motor, front e API". Sugestão: "Plano de entregas único (produto, motor, tela de uso e API)".
5. Trecho: "Descoberta curto; só entra se não tirar braço". Sugestão: "Descoberta curta".
6. Trecho: "Patrocínio do SPFC, Espaço Corretor, leads do Coopday." Sugestão: "Patrocínio do São Paulo FC, Espaço Corretor, contatos do Coopday." (também "Aconteceu com o SPFC" na pergunta 18).
7. Trecho: "renovação as-is" e "Fila própria com cota e SLA". Sugestão: "renovação sem alteração" e "Fila própria com cota e prazo de atendimento".
8. Trecho: "Fundir as três numa time dedicado resolve a duplicação, mas só se a time dedicado tiver". Sugestão: "num time dedicado ... só se o time dedicado tiver".
9. Trecho: "Qual é o problema que a time dedicado e o fórum vão resolver". Sugestão: "que o time dedicado e o fórum vão resolver".
10. Trecho: "que o formato vinha antes do problema.</strong> trocar o formato sem definir". Sugestão: "Nas palavras da reunião: trocar o formato sem definir o que se está tratando é discutir o método antes do problema.<sup>26</sup>"
11. Trecho: "Proposta: cada item responde a um sintoma verificado." Sugestão: "Cada item responde a um sintoma verificado. [Proposta]"
12. Trecho: "neutralidade ou expertise que não vale internalizar". Sugestão: "conhecimento especializado que não vale internalizar".
13. Trecho: "uma PM aqui, um PO ali, um facilitador do time". Sugestão: 'um "PM" aqui, um "PO" ali' (entre aspas, como o glossário faz) ou "um gestor de produto aqui, um dono de carteira ali".
14. Trecho: segunda `<p class="tese">` em "Por que é um problema de desenho". Sugestão: trocar para `<p class="note">` ou parágrafo comum; uma tese por aba.
15. Trecho: "porque hoje o Hub de Cooperativas parou com a ausência de uma pessoa". Sugestão: "; o Hub de Cooperativas parou com a ausência de uma pessoa.<sup>14</sup>" (o "porque" liga causa errada).

### Entenda (7)
1. Trecho: "estratégia comercial (Jacqueline, líder), subscrição e operação de RE (Alan, colíder)". Sugestão: "estratégia comercial (líder), subscrição e operação de RE (colíder), produtos, atuarial, subscrição de Vida e operações, tecnologia, canais, sinistro e inteligência, e a facilitação da área de Estratégia. Os mentores são três superintendentes, um deles da Diretoria Comercial." Mesma regra para "Mentor Aguiar propõe" (linha do tempo): "O mentor comercial propõe".
2. Trecho: "seriam as times dedicados, com o fórum de negócio como rito de entrega dos times dedicados". Sugestão: "seriam os times dedicados, com o Fórum de Negócio como rito de entrega desses times".
3. Trecho: "Verificado o contraste é leitura deste documento. Inferência". Sugestão: "As duas colunas vêm do PIE e das atas. [Verificado] O contraste é leitura deste documento. [Inferência]"
4. Trecho: "O PIE define três ritos: Weeklys semanais de uma hora". Sugestão: 'reuniões semanais de uma hora (as "Weeklys" do deck)'; e "deck" vira "apresentação" nas quatro ocorrências.
5. Trecho: "Em 1º de setembro, a facilitação da frente descreve a cadeia inteira em uma frase" (46 palavras). Sugestão: "...em uma frase. A estratégia nasce no planejamento estratégico, com diretores, superintendentes e a área de Estratégia. Desdobra no mapa estratégico, o artefato central. Do mapa, desdobra-se para as frentes estratégicas, para execução."
6. Trecho: "A frente SUSEP (o nome vem da Superintendência de Seguros Privados" (48 palavras). Sugestão: tirar o parêntese e fazer frase própria: "O nome vem da Superintendência de Seguros Privados, que regula seguros de Vida e Ramos Elementares; a ANS regula planos de saúde."

### Ecossistema (7)
1. Trecho: "O grupo é um núcleo pequeno cercado por onze atores." Sugestão: "cercado por treze atores".
2. Trecho: "(Aguiar, Lara, Alex)", "(Fabíola, Caio, Daniele/VMO)", "(Daniel, Amanda, V4)". Sugestão: "(três superintendentes)", "(facilitação, método e VMO)", "(inteligência de mercado e painel V4)".
3. Trecho: "para times dedicados e fórum de negócio". Sugestão: "Fórum de Negócio".
4. Trecho: "Esteiras executoras (TI, Processos, PMO, Inovação)". Sugestão: acrescentar PMO ao glossário ("escritório de projetos").

### Processos (6)
1. Trecho: "Quinze meses entre a segunda entrada e a primeira decisão de estudar." Sugestão: "Quinze semanas entre a retomada, em maio, e a primeira decisão de estudar, em agosto; mais de dois anos desde o primeiro pedido."
2. Trecho: "sem time dedicado dedicada; dependência da fila da TI". Sugestão: "sem time dedicado; dependência da fila da TI".
3. Trecho: "o que essa time dedicado vai entregar". Sugestão: "o que esse time dedicado vai entregar".
4. Trecho: "Hub atrasado por viagens e falta de dados de Landi." Sugestão: "Hub atrasado por viagens e falta de dados do responsável por canais."
5. Trecho: "Não há fila separada nem SLA." Sugestão: "Não há fila separada nem prazo de atendimento."
6. Trecho: "Do lado do negócio, a cadeia é conhecida: o corretor, a cooperativa" (67 palavras). Sugestão: uma frase por elo: "O corretor, a cooperativa ou a Unimed cotam (Calcule+ e multicálculos como Agger, Quiver e SIGAS). A proposta passa por subscrição, aceitação médica e, em alguns casos, compliance. A apólice é emitida e cobrada (boleto, GEM, sem Pix recorrente para todos os produtos). Renova ou cancela. O sinistro é regulado no RGS, com IA na assistência funeral."

### Sintomas (8)
1. Trecho: "Verificado25 A classificação em categoria e elemento é Inferência". Sugestão: "Sintomas e citações conferidos nas atas. [Verificado]<sup>25</sup> A classificação em categoria e elemento é leitura deste documento. [Inferência]"
2. Trecho: "Verificado Nota de leitura: a transcrição é automática". Sugestão: "Falas conferidas na transcrição. [Verificado] Nota de leitura: a transcrição é automática; grafias mantidas como estão."
3. Trecho: "Saídas de Aline, Márcio e Cibele" e "Hub trava com ausências de Landi; retenção depende da reprecificação de Glace". Sugestão: "Saída de três consultores" e "Hub trava com ausências do responsável por canais; retenção depende da reprecificação feita por uma única atuária".
4. Trecho: "Se a régua for quanto negócio cada um trava, a lista muda" (64 palavras). Sugestão: transformar em lista de cinco itens.

### Estrutura (5)
1. Hierarquia: a aba tem três h2 ("Normas e regras", "Papéis e pessoas", "Sistemas e dados") e três teses. Sugestão: um h2 "Estrutura: normas, papéis e sistemas" com uma tese; as três partes viram h3 e seus h3 atuais viram parágrafos com `<strong>`.
2. Trecho: tabela "Pessoa (papel)" com nove nomes completos, férias e "participação intermitente nas atas". Sugestão: coluna "Papel" com a função ("Líder da frente; estratégia comercial Vida e RE") e retirar férias individuais; manter "sinais de sobrecarga" no plural da função. Idem "Liderança rotativa Jacqueline e Alan" vira "Liderança rotativa entre líder e colíder".
3. Trecho: "Três dados que não existem e que o negócio precisa" (quatro cartões). Sugestão: "Quatro dados que não existem e de que o negócio precisa".
4. Trecho: "Verificado apoiada nas mesmas atas." Sugestão: "Inventário apoiado nas mesmas atas. [Verificado]"
5. Trecho: "Aparecem nas atas: a Nova Lei de Seguros, que exigiu revisão" (81 palavras). Sugestão: lista com cinco itens, um por norma.
6. Trecho: "sextas em home office", "book de cooperativas", "Pipeline de renovações", "sobe só o as-is". Sugestão: "sextas em trabalho remoto", "carteira de cooperativas", "Esteira de renovações", "sobe só o que já existe".

### Loops (9)
1. Opcional: "Reprecificação ágil e contínua (notas de tarifa em abril" (61 palavras). O laço é uma cadeia; se quiser, separar em frases curtas terminadas por ponto e vírgula já resolve a leitura.

### Análise (7)
1. Hierarquia: "Sutilezas" é um segundo h2 com segunda tese. Sugestão: h3 "Sutilezas: o que só quem lê as 24 atas em sequência percebe" e tese vira parágrafo.
2. Trecho: "Especificação recebida sem time dedicado alocada até outubro". Sugestão: "sem time dedicado alocado".
3. Trecho: "Lançar a time dedicado e o Fórum de Negócio com formato definido". Sugestão: "Lançar o time dedicado e o Fórum de Negócio".
4. Trecho: "Verificado as duas leituras são Inferência". Sugestão: "O sinal está na ata. [Verificado] As duas leituras são deste documento. [Inferência]"
5. Trecho: "em 36 minutos, Aguiar desmistifica". Sugestão: "o mentor comercial desmistifica".
6. Matriz de riscos: os dois riscos que a régua pede no topo ("um modelo que entrega relatório" e "adoção como sucesso") estão só na Proposta. Sugestão: uma linha na matriz, "O novo modelo passa a entregar relatório e a adoção vira a meta", probabilidade alta, impacto alto, sinal "fórum vendo percentuais em vez de incrementos", remetendo à aba Proposta.

### Cem perguntas (8)
1. Trecho: "fundi-los numa time dedicado única". Sugestão: "num time dedicado único".
2. Trecho: "Estrutural, sustentação, Adequação e Oportunidade." Sugestão: "Estrutural, Sustentação, Adequação e Oportunidade."
3. Trecho: perguntas 4, 5, 14, 19, 35, 56 com nomes. Sugestão: "Nove pessoas: líder e colíder, facilitação da Estratégia, produtos, atuarial, tecnologia, canais, subscrição de Vida e sinistro e inteligência"; "Três superintendentes, um da Diretoria Comercial"; "Três consultores"; "o responsável por canais".
4. Trecho: "Weeklys semanais, Fórum de Gestão mensal". Sugestão: 'reuniões semanais ("Weeklys")'.

### Glossário (7)
1. Trecho: "Os quatro ritos de uma time dedicado". Sugestão: "de um time dedicado".
2. Trecho: "dono do carteira de demandas". Sugestão: "dono da carteira de demandas".
3. Trecho: "com as quais a time dedicado trocaria". Sugestão: "o time dedicado".
4. Trecho: "lugar de entrega das times dedicados". Sugestão: "dos times dedicados".
5. Faltam verbetes usados no corpo: SLA (ou trocar por "prazo de atendimento"), VG (Vida em Grupo), POC (prova de conceito), PMO (escritório de projetos), IM (Inteligência de Mercado), RCP (responsabilidade civil profissional), PMI, AP Escolar, VI (Vida Individual).

### Fontes (6)
1. Trecho: "com Camila Fernanda Silva Gomes, Eric Leite e Fabíola Brandão" e "Ingrid Guaiato Campos Alves e Kelly Cristina Alonso Adolpho". Contradiz a regra de uso escrita duas linhas depois. Sugestão: "com duas integrantes da área de Estratégia e o autor deste documento" e "com quatro integrantes de Estratégia e Agilidade".
2. Trecho: "Usada nas abas Fluxo funcional e Perguntas de design". Sugestão: "Usada nas abas de proposta, sobretudo Fluxo funcional e Desenho e regras".
3. Ordem: "Documento derivado (25)" vem depois de 26 e 27. Sugestão: reordenar 25, 26, 27.
4. Trecho: "guardados no notebook "Estratégia e Operações Susep..." e links notebook.google.com. Expõe a ferramenta de produção. Sugestão: indicar o repositório original (pasta do projeto) e retirar os links, ou mantê-los num único rodapé.
5. Trecho: "Nota de método. Verificado indica afirmação apoiada" (65 palavras). Sugestão: um período por selo.

## 4. Português (consolidado, documento inteiro)

Cada item: trecho exato, depois a correção.

P1. Executiva: "itens sem saída explícita. ." > "itens sem saída explícita."
P2. Executiva: segundo "A proposta, em duas linhas" com parágrafo idêntico > apagar.
P3. Executiva: "ou a capacidade aumenta: sem isso o time dedicado diagnostica e não entrega." > "Ou a capacidade aumenta; sem isso, o time dedicado diagnostica e não entrega."
P4. Executiva e Processos: "Quinze meses entre a segunda entrada" / "Quinze meses entre a segunda entrada e a primeira decisão" > "Quinze semanas entre a retomada e a autorização do estudo".
P5. Destaque: "repete os principais sem saber que os repetia" > "repete os principais sem perceber que os repete".
P6. Destaque (subtítulo): "Setenta e dois sintomas em 24 atas" > "em 24 documentos".
P7. Proposta: "É o que evita as áreas acabam fazendo o que a Estratégia quer" > "É o que evita que as áreas acabem fazendo o que a Estratégia quer".
P8. Fluxo funcional: "quando acontece o descoberta" > "quando acontece a descoberta".
P9. Fluxo funcional: "Parte do esboço da Estratégia (...) e acrescenta o que faltava nele" > "O mapa parte do esboço da Estratégia (...) e acrescenta o que faltava nele".
P10. Fluxo funcional: "é descoberto e concebido na time dedicado" > "no time dedicado".
P11. Fluxo funcional (SVG): "alimenta: prioridades do fórum e da time dedicado" > "do time dedicado".
P12. Fluxo funcional (SVG): "o que vai para a time dedicado; o que" > "para o time dedicado".
P13. Fluxo funcional (SVG e cartão): "Sustentação (sustentação)" > "Sustentação (fila própria)".
P14. Fluxo funcional (SVG): "não passa pelo descoberta" > "não passa pela descoberta".
P15. Fluxo funcional (tabela): "Carteira de demandas acumulado" > "acumulada".
P16. Fluxo funcional (tabela): "sustentação triado, direto, sem descoberta" > "Item de sustentação triado; segue direto, sem descoberta".
P17. Fluxo funcional: "que sustenta cada relação Proposta e o formato de porta única é Proposta" > "que sustenta cada relação. O formato de porta única é desenho a validar. [Proposta]"
P18. Fluxo funcional: "Quando acontece o descoberta." > "Quando acontece a descoberta."
P19. Fluxo funcional: "É a primeira coisa que a time dedicado faz" > "que o time dedicado faz".
P20. Fluxo funcional: "O que a Agilidade descreveu como o problema não chega cru à TI, chega com diagnóstico é exatamente essa etapa." > "O que a Agilidade descreveu (o problema não chega cru à TI; chega com diagnóstico) é exatamente essa etapa."
P21. Fluxo funcional: "sustentação não passa por ela." > "A sustentação não passa por ela."
P22. Fluxo funcional: "recebem da time dedicado, via fórum" > "do time dedicado".
P23. Estratégia a entrega: "evita Proposta e as durações são Proposta" > "evita. Critérios e durações são desenho a calibrar. [Proposta]"
P24. Estratégia a entrega: "<p> Proposta Leitura: o desenho proposto" > selo no fim do parágrafo.
P25. Estratégia a entrega: "A tabela abaixo estima" (não há tabela abaixo) > "A aba Reuniões e custo estima".
P26. Estratégia a entrega: "o prazo mais duro que a frente tem pela frente" > "o prazo mais duro que o grupo tem à frente".
P27. Desenho e regras: "Plano de entregas único produto, motor, front e API" > "Plano de entregas único (produto, motor, tela de uso e API)".
P28. Desenho e regras: "Descoberta curto" > "Descoberta curta".
P29. Desenho e regras: "Fundir as três numa time dedicado" > "num time dedicado".
P30. Desenho e regras: "mas só se a time dedicado tiver porta" > "se o time dedicado tiver porta".
P31. Desenho e regras: "Qual é o problema que a time dedicado e o fórum" > "que o time dedicado e o fórum".
P32. Desenho e regras: "antes do problema.</strong> trocar o formato sem definir o que se está tratando; o método está sendo discutido antes do problema." > "Nas palavras da reunião: trocar o formato sem definir o que se está tratando é discutir o método antes do problema."
P33. Desenho e regras: "Proposta: cada item responde a um sintoma verificado." > "Cada item responde a um sintoma verificado. [Proposta]"
P34. Desenho e regras (tese): "o que é proposta leva Inferência ou Especulativo" > "o que é proposta leva o selo Proposta".
P35. Desenho e regras: "Uma cadeia com oito elos (...) Descoberta, Concepção, Decisão" > retirar "Concepção" (nove nomes para oito elos).
P36. Desenho e regras: "porque hoje o Hub de Cooperativas parou" > "; o Hub de Cooperativas parou" (o "porque" não explica a frase anterior).
P37. Entenda: "seriam as times dedicados, com o fórum de negócio como rito de entrega dos times dedicados" > "seriam os times dedicados, com o Fórum de Negócio como rito de entrega desses times".
P38. Entenda: "Verificado o contraste é leitura deste documento. Inferência" > "As duas colunas vêm do PIE e das atas. [Verificado] O contraste é leitura deste documento. [Inferência]"
P39. Processos: "sem time dedicado dedicada" > "sem time dedicado".
P40. Processos: "o que essa time dedicado vai entregar" > "o que esse time dedicado vai entregar".
P41. Sintomas: "Verificado25 A classificação em categoria e elemento é Inferência" > "Sintomas e citações conferidos nas atas. [Verificado]25 A classificação em categoria e elemento é leitura deste documento. [Inferência]"
P42. Sintomas: "Verificado Nota de leitura:" > "Falas conferidas na transcrição. [Verificado] Nota de leitura:"
P43. Estrutura: "Verificado apoiada nas mesmas atas." > "Inventário apoiado nas mesmas atas. [Verificado]"
P44. Estrutura (h3): "Três dados que não existem e que o negócio precisa" > "Quatro dados que não existem e de que o negócio precisa" (contagem e regência).
P45. Análise: "sem time dedicado alocada até outubro" > "sem time dedicado alocado até outubro".
P46. Análise: "Lançar a time dedicado e o Fórum de Negócio" > "Lançar o time dedicado e o Fórum de Negócio".
P47. Análise: "Verificado as duas leituras são Inferência" > "O sinal está na ata. [Verificado] As duas leituras são deste documento. [Inferência]"
P48. Cem perguntas: "numa time dedicado única" > "num time dedicado único".
P49. Cem perguntas: "Estrutural, sustentação, Adequação e Oportunidade" > "Estrutural, Sustentação, Adequação e Oportunidade".
P50. Glossário: "Os quatro ritos de uma time dedicado" > "de um time dedicado".
P51. Glossário: "dono do carteira de demandas" > "dono da carteira de demandas".
P52. Glossário: "com as quais a time dedicado trocaria" > "com as quais o time dedicado trocaria".
P53. Glossário: "lugar de entrega das times dedicados" > "dos times dedicados".
P54. Reuniões e custo: "conforme governança, a confirmar" > "Conforme governança, a confirmar".
P55. Reuniões e custo: "fórum de gestão de até quatro horas" > "Fórum de Gestão de até quatro horas".
P56. Reuniões e custo: "0.5", "1.5", "0.75", "0.25" > "0,5", "1,5", "0,75", "0,25" (ponto é milhar na coluna ao lado).
P57. Ecossistema: "times dedicados e fórum de negócio" > "Fórum de Negócio".
P58. Ecossistema (tese): "cercado por onze atores" > "cercado por treze atores".
P59. Problema e entregas: "nove papéis assinados" > "nove entregas assinadas".
P60. Proposta: "produz cinco desenhos assinados pelo time e uma decisão de piloto" > "produz seis desenhos assinados pelo time e um plano de piloto; ao todo, nove entregas".
P61. Proposta (tabela): "Aba Papéis e pessoas" > "Aba Estrutura, seção Papéis e pessoas"; "Desenho e regras" > "Aba Desenho e regras".
P62. Proposta (h3): "O que está em jogo, o que muda, e se falharmos, e se tivermos sucesso" > "O que está em jogo, o que muda, o que acontece se falharmos e se tivermos sucesso".
P63. Executiva: "que hoje não existem (aba Estratégia a entrega)" > "(aba Reuniões e custo)".
P64. Executiva: "duas que a Estratégia toma sozinha (esteiras separadas, porta única)" > "duas que mentores e Estratégia resolvem sem a diretoria".
P65. Fontes 27: "Usada nas abas Fluxo funcional e Perguntas de design" > "Usada nas abas de proposta, sobretudo Fluxo funcional e Desenho e regras".
P66. Desenho e regras (h2): "Perguntas de design" > "Desenho e regras" (nome da aba).
P67. Destaque: "<h2>Em resumo</h2>" > h3. Reuniões e custo: dois h4 > h3. Estrutura: três h2 > um h2 e três h3. Análise: h2 "Sutilezas" > h3.
P68. Destaque: sobrescrito no meio da frase ("sem saber que os repetia<sup>26</sup>, e os mais repetidos") > fechar a frase antes do sobrescrito.
P69. Alçadas (Na prática): "consulta Controladoria e Canais" > "consulta Controladoria, Canais e TI" (a tabela lista os três).
P70. Anglicismo: "blueprint" (Proposta 3x, Reuniões e custo, Estratégia a entrega) > "planta organizacional" ("Blueprint" só como nome do trabalho da Previdência, entre aspas).
P71. Anglicismo: "deck" (Entenda 4x, Fontes) > "apresentação".
P72. Anglicismo: "as-is" (Desenho e regras, Sintomas, Estrutura, Cem perguntas) > "sem alteração" / "o que já existe".
P73. Anglicismo: "SLA" (Fluxo funcional SVG, Desenho e regras 2x, Processos) > "prazo de atendimento".
P74. Anglicismo: "POC" (Sintomas, Estrutura 2x, Cem perguntas) > "prova de conceito".
P75. Anglicismo: "front" (Desenho e regras) > "tela de uso".
P76. Anglicismo: "leads do Coopday" > "contatos do Coopday".
P77. Anglicismo: "expertise" > "conhecimento especializado".
P78. Anglicismo: "home office" > "trabalho remoto".
P79. Anglicismo: "book de cooperativas" > "carteira de cooperativas".
P80. Anglicismo: "Pipeline de renovações" > "Esteira de renovações".
P81. Anglicismo: "Weeklys semanais" (Entenda, Cem perguntas) > 'reuniões semanais ("Weeklys")'.
P82. Anglicismo: "uma PM aqui, um PO ali" > entre aspas ou "um gestor de produto aqui, um dono de carteira ali".
P83. Anglicismo no atributo: aria-label "alimenta a squad; a squad faz discovery" > "alimenta o time dedicado; o time faz descoberta".
P84. Maiúsculas: "SPFC" (Desenho e regras 2x) > "São Paulo FC", como nas outras cinco ocorrências.
P85. Maiúsculas: "Susep" fora de aspas (Fontes: "GT Susep", 'notebook "Estratégia e Operações Susep"') > manter só quando for título de documento; no corpo, "SUSEP".
P86. Selo no início de frase: "Proposta: cada item" (Desenho e regras), "Proposta Leitura:" (Estratégia a entrega), "Verificado Nota de leitura" (Sintomas), "Verificado o contraste" (Entenda), "Verificado apoiada" (Estrutura) > selo sempre no fim.
P87. Frases acima de 35 palavras (contagem por aba): Destaque 6, Executiva 4, Proposta 7, O modelo 2, Alçadas 2, Reuniões e custo 2, Estratégia a entrega 4, Fluxo funcional 2, Desenho e regras 1, Entenda 9, Ecossistema 1, Processos 6, Sintomas 1, Estrutura 4, Loops 6, Análise 3, Fontes 3. As piores (97, 81, 70, 67, 65, 64, 61, 60, 55) estão marcadas nas seções por aba; as demais resolvem-se com ponto no lugar de ponto e vírgula.

## 5. O que já está bom e não deve ser mexido

Contas de Reuniões e custo conferem linha a linha (3.053 e 2.292 horas-pessoa; R$ 381.625, R$ 286.500, diferença R$ 95.125 e 761 horas); os 51 encontros de O modelo batem com a tabela de ritos; as 72 linhas de Sintomas somam 16+16+10+10+9+11; as seis sessões, as nove entregas e as dez regras são consistentes entre Problema, Proposta e Desenho e regras; os dois riscos exigidos estão no topo da tabela da Proposta; a "regra contra o relatório" e a distinção estratégia/execução em O modelo respondem à substância obrigatória; o descrédito na Estratégia aparece na Proposta, na Análise e no Desenho e regras; "Na prática" existe uma vez em cada uma das 17 abas devidas; zero travessão, en-dash e seta no texto.
