# Parecer do advogado do diabo, v8

Documento atacado: `A:\_01 Projetos\Estrategia\Pesquisas\Anatomia Profunda - GT Susep Vida e RE - 26-09-01\Anatomia Profunda - GT Susep Vida e RE - 26-09-01.html` (20 abas, lido na íntegra; espelho .md usado para localizar trechos).
Fontes conferidas: corpus das 24 fontes do NotebookLM (fontes 1 a 24, lidas na íntegra), planilha de sintomas (fonte 25, abas Resumo e Sintomas), transcrições parafraseadas (fontes 26 e 27).
Data do parecer: 2026-09-01 21:38.

## (a) Veredito geral: REPROVA

Resumo do porquê. O documento está muito perto de aprovar: os números-âncora batem com as fontes (20%, 115% e 99%, 36%, 5 anos, 36 minutos, R$ 1 milhão, 65%, 3 consultores, 40 dias, 22%, contagens dos 72 sintomas por categoria e por recorrência, custos de reunião e horas-pessoa, 51 encontros, 8 indicadores, 10 direitos decisórios), as citações literais das atas foram conferidas uma a uma e estão corretas, o conteúdo obrigatório está presente (duas camadas, sucesso do sistema, reuniões por papel, alçadas, problema e entregas, os dois riscos no topo da tabela, o risco de descrédito, caixa "Na prática" em 17 abas, tese em cada aba), não há travessão, seta, marca HackMarket ou selos antigos. O que reprova é um conjunto de falhas objetivas contra as regras do documento, algumas graves:

1. Um número-âncora errado e contraditório: "Quinze meses" entre a retomada do esgotamento de comissão (5/5/2026) e a autorização do estudo (17/8/2026) aparece na Executiva e em Processos; o intervalo é de quinze semanas, como as abas O modelo e Estratégia a entrega dizem corretamente.
2. Duas abas de proposta sem nenhum selo (Proposta e Reuniões e custo), violando a regra 1; o selo `Proposta` não está definido na nota de método da aba Fontes.
3. Aspas residuais vindas das transcrições (Processos, Estrutura, Glossário), contra a regra 3, mais um cabeçalho de tabela "Fala literal" e duas notas dizendo que as grafias foram mantidas entre aspas, quando o texto está parafraseado.
4. Anglicismos proibidos fora de aspas no Glossário (squad, BAU, assessment, discovery) e no rótulo acessível do mapa funcional (squad, discovery).
5. Contradições entre abas: reuniões por mês (O modelo) contra sessões por ano (Reuniões e custo); "Fórum de Gestão" como instância de escalada e de leitura de resultado (Estratégia a entrega) contra "Fórum de Negócio substitui o Fórum de Gestão" (Reuniões e custo, O modelo); "sete portas" com três enumerações diferentes; "cinco desenhos" contra seis; "onze atores" contra treze; "três casos" contra quatro.
6. Restos de edição visíveis ao leitor: seção "A proposta, em duas linhas" duplicada, célula truncada ("ou a capacidade aumenta: sem isso"), ponto duplo, duas frases quebradas por selos inseridos no meio ("as durações são Proposta"), e cerca de vinte erros de concordância deixados pela troca automática de squad, BAU e discovery por "time dedicado", "sustentação" e "descoberta" ("o descoberta", "a time dedicado", "Sustentação (sustentação)").
7. Inferência disfarçada de fato em colunas "hoje" e em linhas de base marcadas Verificado (contagem de temas escalados, "sem instância de recurso", "Diretoria" como decisora de orçamento, laços causais marcados Verificado).
8. O selo Proposta não tem regra de estilo na folha CSS (`.sel-p` não existe), e por isso as 31 ocorrências aparecem sem a cor de selo; o espelho .md descarta esse selo e deixa frases truncadas.

Nenhuma dessas falhas exige nova pesquisa; todas se corrigem em uma passada de edição. Lista completa por aba abaixo.

---

## (b) Por aba

### Destaque: REPROVA (falhas leves, mas uma delas é de fato)

1. Aba Destaque. Trecho: "Às dez da manhã, a reunião semanal: a operação avisa que não cabe OKR novo, a planilha de necessidades ainda não foi preenchida por todos, a reunião com os mentores está marcada para as duas da tarde e uma das mentoras está de férias até o fim do mês. [20] Às duas, em 36 minutos". O que está errado: a caixa apresenta "uma única segunda-feira de agosto", mas junta duas segundas: o conteúdo atribuído à manhã vem da ata de 11/8 (fonte 20), cuja reunião foi das 14:00 às 15:03, e a reunião de 36 minutos com o mentor foi em 17/8 (fonte 23). Evidência: fonte 20, "Horário: 14:00 - 15:03", "Data: 11 de agosto de 2026"; fonte 22 (17/8, 10:00 - 11:00) traz a decisão de não abrir novas frentes sem braço e "Lara em férias", mas não a planilha. Correção: ou abrir dizendo "duas segundas-feiras de agosto, 11 e 17", ou manter uma só (17/8) citando [22] para a manhã (não abrir frentes sem braço; mentora de férias) e [23] para a tarde, retirando a planilha de necessidades.
2. Aba Destaque. Trecho: "Setenta e dois sintomas em 24 atas mostram uma frente competente" (subtítulo). O que está errado: são 23 atas e um deck de planejamento (fonte 1); a própria aba Fontes diz "um deck de planejamento e 23 atas". Correção: "em 24 documentos do próprio grupo" (como já está no corpo da matéria).
3. Aba Destaque. Trecho: "a reunião de 1º de setembro sobre o futuro Fórum de Negócio SUSEP repete os principais sem saber que os repetia [26]". O que está errado: "sem saber que os repetia" é juízo do analista dentro de um parágrafo que fecha com Verificado. Evidência: a transcrição não diz que as participantes desconheciam as atas; ao contrário, a facilitação lista as planilhas e apresentações que precisariam ser cruzadas. Correção: "repete os principais" e ponto; ou mover a frase para uma sentença com selo Inferência.

### Executiva: REPROVA

4. Aba Executiva. Trecho: "Quinze meses entre a segunda entrada do esgotamento de comissão e a autorização de um estudo". O que está errado: a segunda entrada é 5/5/2026 (fonte 9, proposta para o COMEX) e a autorização é 17/8/2026 (fonte 23): 104 dias, quinze semanas. A aba O modelo diz "quinze semanas da retomada à autorização de estudo" e a aba Estratégia a entrega diz "15 semanas". Correção: "Quinze semanas".
5. Aba Executiva. Trecho: "Mais de vinte entregas entre novembro de 2025 e maio de 2026". O que está errado: o deck (fonte 1, slide 11) lista 14 entregas de novembro de 2025 a março de 2026 (6 ligadas à PIE de novembro, 8 à PIE de março/abril); as demais 18 do slide 10 são de fevereiro a outubro de 2025. "Mais de vinte" só vale para o total de 2025 e 2026 (como diz corretamente a pergunta 10 da aba Cem perguntas). Correção: "Catorze entregas entre novembro de 2025 e março de 2026, mais de trinta desde o início de 2025".
6. Aba Executiva. Trecho: "Fórum de agosto pediu evidenciar o gap; o grupo não sabe o fechamento de 2024. [20, 24]". O que está errado: não foi pedido de fórum; foi decisão do próprio grupo na semanal de 11/8. Evidência: fonte 20, "O gap em relação à meta de 20% será evidenciado de forma clara (a exemplo do que é feito nas frentes de Saúde e Odonto)". Correção: "O grupo decidiu em agosto evidenciar o gap no próximo fórum".
7. Aba Executiva. Trecho: célula "ou a capacidade aumenta: sem isso o time dedicado diagnostica e não entrega. [27]". O que está errado: frase truncada (falta o início: "Critério de despriorização no acelerador, ou a capacidade aumenta"). Correção: "Sem critério de despriorização no acelerador, ou mais capacidade, o time dedicado diagnostica e não entrega. [27]".
8. Aba Executiva. Trecho: a seção "A proposta, em duas linhas" aparece duas vezes, uma após a outra, com texto idêntico. Correção: remover a segunda.
9. Aba Executiva. Trecho: "quórum dos ritos, itens sem saída explícita. ." Correção: remover o segundo ponto.
10. Aba Executiva. Trecho: "contra cerca de R$ 286.000 do sistema atual estimado; ... (aba Estratégia a entrega)". O que está errado: (i) R$ 286.500 arredonda para R$ 287.000, não R$ 286.000; (ii) a tabela de custo está na aba Reuniões e custo, não em Estratégia a entrega. Correção: "cerca de R$ 287.000 (ou R$ 286.500) ... (aba Reuniões e custo)".
11. Aba Executiva. Trecho: "Sete portas de entrada e nenhuma triagem ... [13, 16, 20] Verificado". O que está errado: "sete" é contagem do analista, e a enumeração muda de aba para aba (ver Contradições, item C4); agregado calculado é Inferência, não Verificado. Correção: fechar o item com Inferência ou trocar por "várias portas de entrada e nenhuma triagem".
12. Aba Executiva. Trecho: "Esgotamento de comissão, prestamista de prêmio único, meios de pagamento, práticas da corretora digital e fila da TI sobem para mentores, RDS ou COMEX". O que está errado: a "fila da TI" não sobe; o que a ata registra é que o grupo decidiu não trocar prioridades na fila e levar aos mentores dois temas (esgotamento e modelo comercial dos canais). Evidência: fonte 22, ponto 6, "O grupo priorizará dois temas centrais para levar à reunião com os mentores: a viabilização do esgotamento de comissão e o modelo comercial dos canais Cooperativas/Unimeds". Correção: trocar "fila da TI" por "modelo comercial dos canais".

### Problema e entregas: REPROVA (uma falha de forma, uma de conteúdo)

13. Aba Problema e entregas. Trecho: "Na semana 6, a mesa tem nove papéis assinados e um piloto com data." O que está errado: "papéis" aqui significa folhas, mas o documento inteiro usa "papéis" no sentido de funções, e a entrega 7 é justamente "papéis e dedicação"; o leitor lê "nove funções assinadas". Correção: "nove artefatos assinados" ou "nove entregas assinadas".
14. Aba Problema e entregas. Trecho: "2. Sete portas e nenhuma triagem. Demandas entram por reunião, mensagens, planilhas, S&OP, diagnóstico, Marketing e parceiros." O que está errado: esta lista (7 itens) difere da lista de Processos e de Desenho e regras (reunião, mensagens, e-mail, planilhas coletivas, S&OP, RDS, Marketing e parceiros: 8 itens). Ver C4. Correção: uma única enumeração em todas as abas, e o número coerente com ela.
15. Aba Problema e entregas. Trecho: "Ponta comercial. Resposta em 48 horas para cotação aberta; reconsideração de recusa em cinco dias". Observação: o retorno em 48 horas é proposta do próprio grupo (fonte 18) e poderia levar o sobrescrito [18]; a reconsideração em cinco dias é desenho. Sem sobrescrito, o leitor não distingue. Correção: "Resposta em 48 horas para cotação aberta, como a frente já propôs [18]".

### Proposta: REPROVA

16. Aba Proposta. Trecho: toda a aba. O que está errado: é aba de proposta e não tem nenhum selo, nem `Proposta` nos desenhos, nem `Verificado` nas afirmações factuais com fonte ("Foi a conclusão da própria Estratégia em 1º de setembro [26]", "Primeiro fórum já marcado para setembro [13, 27]", "o canal que representa 65% da operação [22, 23]", "o horário que o próprio grupo apontou como o melhor para agendas extensas [11]"). Regra 1. Correção: selo `Proposta` no abre da aba e ao pé de cada bloco de desenho (tabelas de desenhos, sessões, fundação, riscos, ficha de reunião); `Verificado` nas frases com fonte.
17. Aba Proposta. Trecho: "que produz cinco desenhos assinados pelo time e uma decisão de piloto". O que está errado: a tabela logo abaixo lista seis desenhos (lista de problemas, fluxo da estratégia à entrega, fluxo funcional, reuniões e custo, alçadas e regras, papéis e dedicação). Correção: "seis desenhos" (ou "cinco desenhos e a matriz de papéis, por último").
18. Aba Proposta. Trecho: "6. Papéis e dedicação (por último) | Quem faz o quê, com quantas horas | Aba Papéis e pessoas". O que está errado: não existe aba "Papéis e pessoas"; é uma seção da aba Estrutura. Correção: "Aba Estrutura (Papéis e pessoas)".
19. Aba Proposta. Trecho: "Primeiro fórum já marcado para setembro; agendas de mentores e da diretoria em conflito. [13, 27]". O que está errado: "já marcado" diz mais do que a transcrição. Evidência: fonte 27, fala da facilitação: "a ideia do Caio do Flávio é que a gente tem a primeira agenda já esse mês de setembro". Correção: "Primeira agenda do fórum prevista para setembro".
20. Aba Proposta. Trecho: "o canal que representa 65% da operação e que já migra para quem paga esgotamento [22, 23]". O que está errado: a migração por causa do esgotamento é inferência. Evidência: fonte 22 fala em "insatisfação em assessorias e perda de atratividade frente aos concorrentes"; fonte 23 fala em migração de corretores para concorrentes por causa da aceitação no Vida, não do esgotamento; a perda de grandes corretoras para Porto e Icatu (fonte 9) é registrada ao lado da discussão do esgotamento, sem nexo causal explícito. Correção: "e que perde grandes corretoras para concorrentes [9, 22]".
21. Aba Proposta. Trecho: "A fronteira entre Fórum de Negócio e Fórum de Gestão ... a sessão 3 decide." Observação: coerente como dúvida declarada, mas a aba Reuniões e custo já decidiu (Fórum de Negócio é "evolução do Fórum de Gestão" e o Fórum de Gestão não aparece no sistema proposto) enquanto a aba Estratégia a entrega usa "Fórum de Gestão" como instância de escalada e de leitura em 30 e 90 dias. Ver C2. Correção: alinhar as três abas; se a dúvida fica em aberto, o macroprocesso e a tabela de ritos precisam dizer "Fórum de Negócio (ou a instância que a sessão 3 definir)".
22. Aba Proposta. Trecho: "A régua é a mesma usada no blueprint organizacional da Previdência." Observação: "blueprint" é anglicismo fora da lista proibida; aceitável porque é o nome do trabalho anterior, mas vale grafar entre aspas ou como nome próprio ("no Blueprint da Previdência") para não parecer jargão.

### O modelo: REPROVA (contradição de contagem e duas inferências como fato)

23. Aba O modelo. Trecho: "8 encontros de descoberta (2h), 8 encontros de sala de guerra (1h) e cerca de 20 reuniões diárias do núcleo (15 min). São 51 encontros". O que está errado: a aba Reuniões e custo prevê 36 sessões de descoberta por ano (3 por mês) e 32 de sala de guerra por ano (menos de 3 por mês) e 220 diárias por ano (18 por mês); o "mês típico" descrito aqui tem 51 encontros, mas o sistema anual custeado tem 481 sessões (40 por mês). O leitor que somar as duas abas encontra dois sistemas diferentes. Correção: ou declarar que o mês típico é um mês de pico (dois desafios em descoberta e um tema em sala de guerra ao mesmo tempo) e que a média anual é menor, ou ajustar a tabela anual (descoberta 96 sessões, sala de guerra 96) e recalcular o custo.
24. Aba O modelo. Trecho: "Cinco temas escalados a mentores, RDS ou COMEX entre maio e agosto. [9, 16, 17, 22]" (linha de base, marcada Verificado no rodapé). O que está errado: a contagem "cinco" é agregado do analista; e um dos cinco (fila da TI) não foi escalado (ver item 12). Evidência: fonte 9 (esgotamento ao COMEX; nova ferramenta de pagamentos ao COMEX), fonte 16 (práticas da corretora digital à diretoria; Hub à RDS), fonte 17 (prestamista à RDS), fonte 22 (esgotamento e canais aos mentores). Correção: listar os temas em vez de contar, ou marcar a linha de base como Inferência.
25. Aba O modelo. Trecho: "Tarefas com prazo 'a definir' nas atas de agosto. [22, 24]". O que está errado: a fonte 24 é de 27 e 28 de julho. Correção: "nas atas de julho e agosto".
26. Aba O modelo. Trecho: "Hoje as duas camadas moram na mesma reunião semanal: status, deliberação e início de discussões no mesmo rito". Observação: correto (fontes 3 e 12), mas a frase está no meio de uma seção sem selo Verificado próprio; o rodapé da tabela anterior não a cobre. Correção: acrescentar Verificado ao fim da frase.

### Alçadas: REPROVA (inferência disfarçada de fato na coluna "hoje")

27. Aba Alçadas. Trecho: "Exceção de compliance ... | Compliance, sem instância de recurso. [11]" com o rodapé "Verificado na coluna hoje". O que está errado: "sem instância de recurso" é inferência (a própria planilha de sintomas classifica GV-04 como "Inferida", e a aba Estrutura marca "Recurso contra recusa" como Inferência). Evidência: fonte 11 descreve o caso da proposta de R$ 1 milhão recusada e encaminhada ao Compliance; não diz que não há recurso. Correção: "Compliance; a ata não registra via de reconsideração [11]" e rodapé "Verificado nos fatos citados; Inferência nas leituras 'sem regra' e 'sem instância'; Proposta nas demais colunas".
28. Aba Alçadas. Trecho: "Orçamento e contratação ... | Diretoria; reposição de consultores sem data. [16]". O que está errado: a fonte 16 registra "andamento da contratação de consultores", sem dizer quem decide o orçamento. "Diretoria" é dedução. Correção: "Não registrado nas atas; reposição de consultores em andamento, sem data [16]".
29. Aba Alçadas. Trecho: "Preço e tarifa | Atuarial com Produtos; funciona (reprecificação trimestral). [5, 20]". O que está errado: a periodicidade trimestral está na fonte 15 ("calibrações trimestrais de preço feitas por Glace"), não nas fontes 5 e 20. Correção: acrescentar [15].
30. Aba Alçadas. Trecho: "Abrir, estacionar ou encerrar iniciativa | Sem regra; itens somem ou são encerrados para limpar histórico. [9, 14]". Observação: "sem regra" é inferência razoável; deixar, mas coberta pelo rodapé sugerido no item 27.

### Reuniões e custo: REPROVA

31. Aba Reuniões e custo. Trecho: toda a aba. O que está errado: nenhum selo. A tabela "Sistema atual (estimado a partir das atas)" é estimativa do analista (número de sessões e de pessoas de S&OP, Diagnóstico e Fórum de Gestão não estão nas atas) e deveria levar `Especulativo` ou `Inferência`; a tabela de ritos propostos e a de custo do sistema proposto deveriam levar `Proposta`; as afirmações "Existente, hoje em 30 minutos [13]", "Substitui a semanal mista [10, 14]", "Proposto pelo grupo [20]" deveriam levar `Verificado`. Correção: selos ao pé de cada tabela e no abre da aba.
32. Aba Reuniões e custo. Trecho: "O sistema atual foi estimado a partir das atas (semanal mista de uma hora e meia, S&OP mensal, diagnóstico mensal, fórum de gestão de até quatro horas, mentoria de meia hora). [10, 11, 26, 27]". O que está errado: "S&OP mensal" e "diagnóstico mensal" não estão em nenhuma das quatro fontes; só a existência das três agendas está (fonte 26). Correção: "S&OP e diagnóstico com cadência assumida como mensal (não registrada nas fontes)" e selo Especulativo.
33. Aba Reuniões e custo. Trecho: "RDS e COMEX | Governança | conforme governança, a confirmar". Observação: linha sem custo e sem fonte; aceitável, mas vale dizer "fora da conta".

### Estratégia a entrega: REPROVA

34. Aba Estratégia a entrega. Trecho: "Os sobrescritos apontam para o sintoma que cada critério evita [Proposta] e as durações são [Proposta]". O que está errado: frase quebrada; os selos foram inseridos no lugar das palavras que fechavam a frase. Correção: "Os sobrescritos apontam para o sintoma que cada critério evita; as durações são pontos de partida. Proposta".
35. Aba Estratégia a entrega. Trecho: "Somadas as durações, um desafio estrutural percorre o caminho em três a cinco meses, da ficha ao resultado medido." O que está errado: na mesma aba, o caso simulado termina em "ao resultado medido: cerca de 6 meses", e a soma das durações declaradas (até 15 dias de triagem, 4 a 8 semanas de descoberta, até 30 dias de decisão, 1 a 3 meses de execução, entrega no fórum seguinte, leitura em 90 dias) dá de seis a dez meses até a leitura de 90 dias. Correção: "em quatro a seis meses da ficha à entrega, e cerca de nove meses até a leitura de 90 dias" (ou recalcular).
36. Aba Estratégia a entrega. Trecho: "Comitê de priorização (mensal); Fórum de Gestão para o que excede a alçada; RDS e COMEX acima" e "Fórum de Gestão (30 e 90 dias); PIE (fechamento)" e, no macroprocesso, "acima dela, Fórum de Gestão" e "Fórum de Gestão + PIE leitura em 30 e 90 dias". O que está errado: contradiz a aba Reuniões e custo (o Fórum de Negócio é "evolução do Fórum de Gestão" e o sistema proposto não tem Fórum de Gestão) e a aba O modelo (o Fórum de Negócio recebe "resultado medido em 30 e 90 dias"). Ver C2. Correção: "Fórum de Negócio" nas quatro ocorrências (ou explicitar que Fórum de Gestão continua existindo e incluí-lo na tabela de custo).
37. Aba Estratégia a entrega. Trecho: "Entrada | Pedido do canal corretor em 2024; travado por 'receios financeiros e de escopo'. [23]". O que está errado: a fonte 23 registra que "Tatiane e Jacqueline relembraram discussões de 2024 travadas por receios financeiros e de escopo"; não diz que o pedido veio do canal corretor. A mesma leitura aparece em Processos ("Entra em 2024 como pedido do canal corretor"), marcada Verificado. Correção: "Discutido internamente em 2024; travado por 'receios financeiros e de escopo' [23]".
38. Aba Estratégia a entrega. Trecho: "desde o primeiro pedido: mais de dois anos. Verificado". O que está errado: a fonte diz apenas "2024"; de 2024 a agosto de 2026 pode ser de vinte a trinta e dois meses. Correção: "desde a primeira discussão, em 2024: cerca de dois anos".
39. Aba Estratégia a entrega. Trecho: "Resumo: sistema proposto perto de R$ 381.625 por ano; sistema atual estimado perto de R$ 286.500". Observação: "perto de" com número exato; escolher um. Correção: "R$ 381.625 e R$ 286.500 (a R$ 125 a hora)".

### Fluxo funcional: REPROVA (português e anglicismo escondido)

40. Aba Fluxo funcional. Trecho: "Os sobrescritos apontam para o registro nas atas ou nas reuniões de 1º de setembro que sustenta cada relação [Proposta] e o formato de porta única é [Proposta]". O que está errado: frase quebrada, mesmo caso do item 34. Correção: "...que sustenta cada relação; o formato de porta única é desenho. Proposta".
41. Aba Fluxo funcional. Trecho: rótulo acessível do mapa (atributo aria-label do SVG): "Mapa funcional: origens do problema alimentam o Fórum de Negócio, que alimenta a squad; a squad faz discovery e concepção". O que está errado: "squad" e "discovery" fora de aspas, lidos por leitores de tela e por quem inspeciona a página. Correção: "que alimenta o time dedicado; o time dedicado faz descoberta e concepção".
42. Aba Fluxo funcional. Trecho: "De onde vem o problema ... Hoje cada origem tem uma porta diferente; no desenho, uma só. Verificado" e "Quando acontece o descoberta ... Verificado". O que está errado: os dois cartões misturam fato e desenho e fecham com Verificado; o desenho ("no desenho, uma só"; "É a primeira coisa que o time dedicado faz") é Proposta. Correção: Verificado após a parte factual e Proposta ao fim do cartão.
43. Aba Fluxo funcional. Trecho: "Fórum de Negócio | Sustentação | sustentação triado, direto, sem descoberta". O que está errado: resto da troca de "BAU" por "sustentação" (era "BAU triado"). Correção: "Item de sustentação triado, direto, sem descoberta".
44. Aba Fluxo funcional. Trecho: "Sustentação (sustentação)" (duas ocorrências, no mapa e no cartão "Para onde vai"). Correção: "Sustentação (rotina)" ou apenas "Sustentação".
45. Aba Fluxo funcional. Trecho: "Versão 0.2." e selo "RASCUNHO". Observação: a aba usa o rótulo RASCUNHO no lugar do selo Proposta; o padrão do documento é o selo por extenso. Correção: manter "Rascunho, versão 0.2" como texto, e acrescentar o selo Proposta.

### Desenho e regras: REPROVA (contagens e um selo)

46. Aba Desenho e regras. Trecho: "Como chegam hoje. Por reunião, mensagens, e-mail, planilhas coletivas, S&OP, RDS, Marketing e parceiros ... [21, 26] Verificado" e "6. Por onde um problema entra, e quem o vê primeiro? Hoje são sete portas e nenhuma triagem. [21]". O que está errado: a lista tem oito itens e o número diz sete; a fonte 21 registra apenas demandas sem filtro à Estratégia Comercial, não o inventário de portas. Ver C4. Correção: unificar a enumeração e marcar a contagem como Inferência.
47. Aba Desenho e regras. Trecho: "Proposta: cada item responde a um sintoma verificado." Observação: no HTML o selo está presente e a frase é correta; só o espelho .md perde o selo e deixa os dois-pontos soltos. Não é falha do HTML; é falha do gerador do espelho (ver item 87).
48. Aba Desenho e regras. Trecho: "Uma cadeia com oito elos ... Direção, Desdobramento, Entrada e triagem, Descoberta, Concepção, Decisão, Execução, Entrega e adoção, Medição e aprendizado." O que está errado: são nove nomes para "oito elos" (Concepção não é etapa na aba Estratégia a entrega, que tem oito). Correção: retirar "Concepção" da lista ou dizer "nove elos".
49. Aba Desenho e regras. Trecho: "Descoberta curto; só entra se não tirar braço" (tabela de tipos, linha Oportunidade). Correção: "Descoberta curta".
50. Aba Desenho e regras. Trecho: "Fundir as três numa time dedicado resolve a duplicação, mas só se a time dedicado tiver porta" e "a time dedicado e o fórum vão resolver". Correção: "num time dedicado", "o time dedicado" (ver seção Português).
51. Aba Desenho e regras. Trecho: "8. A própria Estratégia reconheceu, na reunião de 1º de setembro, que o formato vinha antes do problema. trocar o formato sem definir o que se está tratando; o método está sendo discutido antes do problema. [26]". O que está errado: frase iniciada em minúscula depois de ponto; resto de aspas removidas. Correção: "...antes do problema: trocar o formato sem definir o que se está tratando, o método discutido antes do problema. [26]".
52. Aba Desenho e regras. Trecho: "Ritos e memória | ... retrospectiva vira espaço de desabafo. | [3, 5, 13, 21, 26]". Observação: correto (fonte 26, "Susep foi muro das lamentações"), parafraseado sem aspas como manda a regra; sem falha.

### Entenda: APROVA com reparos

53. Aba Entenda. Trecho: "alimentando e recebendo da TI, dos aceleradores e dos projetos de torre (nos dois sentidos: envia e recebe). [26]". O que está errado: a paráfrase diz um pouco mais do que a transcrição: o trecho registrado é "verificar todo o que tem de priorizado ou não dentro da TI" e "Ele não só joga, como ele também recebe"; "aceleradores" e "projetos de torre" vêm do esboço da Estratégia e da fonte 27, não da fala registrada na fonte 26. Correção: "alimentando e recebendo da TI (nos dois sentidos: envia e recebe) [26]; aceleradores e projetos de torre aparecem no esboço da Estratégia e na fonte 27".
54. Aba Entenda. Trecho: "Verificado; o contraste é leitura deste documento. Inferência" (rodapé da tabela de papéis). Observação: correto e bem marcado.

### Ecossistema: REPROVA (contagem e nomes)

55. Aba Ecossistema. Trecho: "O grupo é um núcleo pequeno cercado por onze atores." O que está errado: a tabela tem treze linhas (Mentores; Diretoria, RDS e COMEX; Área de Estratégia; Esteiras executoras; Controladoria; Inteligência de Mercado; Canal corretor; Cooperativas de crédito; Sistema Unimed; Marketing e Corretora Digital; Transformação das frentes; Gente de fora; Concorrentes). Correção: "treze atores".
56. Aba Ecossistema. Trecho: "Área de Estratégia (Fabíola, Caio, Daniele/VMO)". O que está errado: Caio e Daniele aparecem nas atas (fontes 9, 12, 13, 15), o que autoriza a menção pela regra das atas, mas são exatamente os colegas discutidos na transcrição 26 (a quem "convencer" do modelo), e a linha "Transformação das frentes" da mesma tabela já os cita só por função ("diretoria, Estratégia e VMO, Agilidade"). Correção, por prudência e coerência: "Área de Estratégia (facilitação da frente, Estratégia e VMO)".

### Processos: REPROVA

57. Aba Processos. Trecho: "Quinze meses entre a segunda entrada e a primeira decisão de estudar. [9, 22, 23] Verificado". O que está errado: mesmo erro do item 4; são quinze semanas. Correção: "Quinze semanas".
58. Aba Processos. Trecho: "o S&OP ('só vida') e o Diagnóstico, nascido no comercial no fim de 2025 e que 'funcionou bem, as pessoas sentaram, conversaram'". O que está errado: duas citações literais da transcrição 26 entre aspas, contra a regra 3 (transcrições parafraseadas sem aspas). Correção: "o S&OP, que trata só de Vida, e o Diagnóstico, nascido no comercial no fim de 2025 e que, na leitura da facilitação, funcionou porque as pessoas se sentaram e conversaram".
59. Aba Processos. Trecho: "Três casos que mostram o fluxo inteiro" seguido de quatro cartões (esgotamento, prestamista, BI, patrocínio). Correção: "Quatro casos".
60. Aba Processos. Trecho: "Esgotamento de comissão (RE). Entra em 2024 como pedido do canal corretor". O que está errado: ver item 37. Correção: "Discutido internamente desde 2024".
61. Aba Processos. Trecho: "8. Execução | Projetos trocados por emergências operacionais; sem time dedicado dedicada". Correção: "sem time dedicado".
62. Aba Processos. Trecho: "A proposta é reunir as três agendas num único time dedicado ... O que a proposta ainda não diz é o que essa time dedicado vai entregar". Correção: "esse time dedicado".

### Sintomas: REPROVA

63. Aba Sintomas. Trecho: cabeçalho de coluna "Fala literal" na tabela "O que a reunião de 1º de setembro acrescenta". O que está errado: as células são paráfrases (por decisão do cliente); o cabeçalho promete literalidade que não existe. Correção: "Fala, em paráfrase".
64. Aba Sintomas. Trecho: "Nota de leitura: a transcrição é automática; grafias foram mantidas como estão." O que está errado: não há grafia mantida, porque não há citação literal. Correção: "Nota de leitura: transcrição automática, parafraseada; falas atribuídas por função."
65. Aba Sintomas. Trecho: "Desfalque de consultores sobrecarrega a liderança | Saídas de Aline, Márcio e Cibele" (e pergunta 14 da aba Cem perguntas). O que está errado: nomes de pessoas que deixaram a área, com exposição desnecessária para o público da Estratégia; a informação relevante é "três consultores". Correção: "Saída de três consultores".
66. Aba Sintomas. Trecho: "Verificado [25] A classificação em categoria e elemento é Inferência". Observação: correto. Contagens conferidas contra a planilha: 16, 10, 10, 16, 9, 11 (total 72); recorrências 9, 7, 7, 6 batem com a aba Resumo.

### Estrutura: REPROVA (aspas residuais e contagem)

67. Aba Estrutura. Trecho: "os papéis estão 'nebulosos'; a participação da TI no time está em aberto; e a Estratégia pondera entre esperar o modelo evoluir ou 'colocar na mesa' as dores antes. [26]". O que está errado: duas aspas vindas da transcrição. Correção: "os papéis ainda estão pouco definidos ... ou pôr as dores na mesa antes".
68. Aba Estrutura. Trecho: "Nove pessoas no núcleo, três mentores, uma facilitadora." O que está errado: a tabela abaixo e a aba Entenda contam nove nomes incluindo a facilitadora; a frase soma dez. Correção: "Oito pessoas no núcleo, uma facilitadora, três mentores" (ou "Nove pessoas, contando a facilitadora, e três mentores").
69. Aba Estrutura. Trecho: "Liderança rotativa Jacqueline e Alan, uma semana cada. | 11 de junho. [14] | Decidida; atas seguintes não registram a alternância de condução. Inferência". Observação: bem marcado; sem falha.

### Loops: REPROVA (selo)

70. Aba Loops. Trecho: os três laços fecham com "Verificado". O que está errado: cada elo tem fonte, mas o encadeamento ("cujas agendas são curtas ... o que atrasa a decisão ... e o atraso obriga a operação a sustentar paliativos"; "a regra não muda porque a auditoria médica só vê as recusas que registrou [23]") é causal, e a nota de método da aba Fontes diz que "todo encadeamento causal ... está nesta categoria [Inferência]". A fonte 23 não diz que a auditoria só vê as recusas registradas. Correção: "Verificado nos elos; Inferência no encadeamento" ao fim de cada laço, e reescrever o elo da auditoria médica como "a regra só é revista quando o dado chega à auditoria médica [23]".
71. Aba Loops. Trecho: "a atuária ajusta preço trimestralmente e o resultado aparece no mês seguinte. [3, 20]". O que está errado: "trimestralmente" está na fonte 15; "o resultado aparece no mês seguinte" não está em nenhuma. Correção: citar [15] e trocar por "e o efeito é acompanhado nas vendas seguintes [20]".

### Análise: APROVA com reparos

72. Aba Análise. Trecho: "Especificação recebida sem time dedicado alocada até outubro" e "Lançar a time dedicado e o Fórum de Negócio". Correção: "sem time dedicado alocado", "Lançar o time dedicado".
73. Aba Análise. Trecho: "Sutilezas ... frentes cogitam 'refluctuar' a meta" (na verdade em Desenho e regras, dimensão Direção e metas). O que está errado: a ata diz "refluctuação de metas"; a forma verbal entre aspas não é literal. Correção: "frentes cogitaram a 'refluctuação' da meta [12]".
74. Aba Análise. Trecho: "o que só quem lê as 24 atas em sequência percebe". Correção: "os 24 documentos" (ver item 2).

### Cem perguntas: APROVA com reparos

75. Aba Cem perguntas. Trecho: "92. Quais os quatro tipos de demanda? Estrutural, sustentação, Adequação e Oportunidade." Correção: "Estrutural, Sustentação, Adequação e Oportunidade".
76. Aba Cem perguntas. Trecho: "38. ... em setembro a Estratégia quer fundi-los numa time dedicado única." Correção: "num time dedicado único".
77. Aba Cem perguntas. Trecho: "14. Quantos consultores saíram? Três (Aline, Márcio, Cibele)". Ver item 65. Correção: "Três".

### Glossário: REPROVA (anglicismos e aspas)

78. Aba Glossário. Trecho: "Time dedicado (squad)", "Sustentação (BAU) ... business as usual", "Avaliação dirigida (assessment) e descoberta (discovery)". O que está errado: quatro anglicismos da lista proibida fora de aspas. Correção: entre aspas ("squad", "BAU", "assessment", "discovery"), já que o glossário existe para traduzir o jargão das atas; ou retirar os originais.
79. Aba Glossário. Trecho: "citados como ainda 'nebulosos' no modelo em discussão". O que está errado: aspas vindas da transcrição 26. Correção: "citados como ainda pouco definidos".
80. Aba Glossário. Trecho: "Responsáveis de um time dedicado (PM, PO, scrum master). Papéis típicos de time dedicado (gestor do produto, dono do carteira de demandas, facilitador de impedimentos)". Correção: "dono da carteira de demandas"; e "scrum master" entre aspas.
81. Aba Glossário. Trecho: "Planning, revisão, reunião diária e retrô. Os quatro ritos de uma time dedicado". Correção: "Planejamento do ciclo, revisão, reunião diária e retrospectiva. Os quatro ritos de um time dedicado".
82. Aba Glossário. Trecho: "Fórum de Negócio SUSEP. Rito proposto ... como lugar de entrega das times dedicados". Correção: "dos times dedicados".

### Fontes: REPROVA

83. Aba Fontes. Trecho: nota de método define Verificado, Inferência e Especulativo e não define o selo Proposta, usado 31 vezes no documento. Correção: acrescentar "Proposta indica desenho proposto para validação nas sessões; não é afirmação sobre a realidade".
84. Aba Fontes. Trecho: fonte 27, "Usada nas abas Fluxo funcional e Perguntas de design, com as falas citadas por função. Grafias da transcrição mantidas entre aspas." O que está errado: (i) não existe aba "Perguntas de design" (a aba chama-se Desenho e regras; o título interno é que diz "Perguntas de design"); (ii) a fonte 27 é citada também em Executiva, Proposta, O modelo, Alçadas, Reuniões e custo, Ecossistema e Glossário; (iii) não há aspas mantidas, porque a transcrição foi parafraseada. Correção: "Usada nas abas de proposta, Fluxo funcional, Desenho e regras e Glossário, com as falas parafraseadas e atribuídas por função."
85. Aba Fontes. Trecho: fonte 26, "Regra de uso: apenas as falas das duas participantes da Estratégia valem como evidência, citadas por função". Observação: correto; acrescentar "parafraseadas".
86. Aba Fontes. Trecho: ordem das seções "Reunião de 1º de setembro (26)", "(27)", "Documento derivado (25)". Observação: a numeração 26, 27, 25 não é erro, mas a fonte 25 é citada antes das outras no texto; vale colocá-la antes.

### Formato (todas as abas): REPROVA

87. Todas as abas de proposta. Trecho: `<span class="sel sel-p">Proposta</span>` (31 ocorrências). O que está errado: a folha de estilo define `.sel`, `.sel-v`, `.sel-i` e `.sel-e`, mas não define `.sel-p`; o selo Proposta é renderizado sem cor de fundo e sem cor de texto próprias, visualmente diferente dos outros três selos e sem a identidade que a regra 1 pressupõe. Evidência: busca no bloco `<style>` do HTML; zero regras para `.sel-p`. Correção: acrescentar, por exemplo, `.sel-p{background:#f3e9f5;color:#5b2d6e}`. Consequência colateral: o espelho .md descarta os selos `sel-p` e deixa frases truncadas ("as durações são", "o formato de porta única é", ": cada item responde"), o que confirma que o gerador do espelho não conhece a classe; corrigir o gerador junto.

---

## (c) Contradições entre abas

- C1. Quinze meses (Executiva; Processos) contra quinze semanas (O modelo; Estratégia a entrega). O correto é quinze semanas, de 5/5 a 17/8/2026.
- C2. Fórum de Gestão. Reuniões e custo: o Fórum de Negócio é "evolução do Fórum de Gestão" e o sistema proposto não tem Fórum de Gestão; O modelo: o Fórum de Negócio recebe resultado em 30 e 90 dias e o que excede a alçada do comitê; Estratégia a entrega: "acima dela, Fórum de Gestão", "Fórum de Gestão para o que excede a alçada", "Fórum de Gestão (30 e 90 dias)"; Alçadas: escalada para COMEX e Diretoria; Proposta: declara a fronteira como dúvida a resolver na sessão 3. Quatro respostas para a mesma pergunta.
- C3. Reuniões por mês. O modelo: 8 descobertas, 8 salas de guerra e 20 diárias por mês (51 encontros). Reuniões e custo: 36 descobertas, 32 salas de guerra e 220 diárias por ano (3, 2,7 e 18 por mês). O total anual custeado (481 sessões) é 20% menor que doze vezes o mês típico (612).
- C4. Sete portas. Problema e entregas: reunião, mensagens, planilhas, S&OP, diagnóstico, Marketing e parceiros (7). Processos e Desenho e regras: reunião, mensagens, e-mail, planilhas coletivas, S&OP, RDS, Marketing e parceiros (8). Executiva, Estratégia a entrega e Cem perguntas usam "sete" sem lista. Escolher uma lista e um número.
- C5. Cinco desenhos (texto da aba Proposta) contra seis desenhos (tabela da mesma aba) contra nove entregas (Problema e entregas). As seis sessões da Proposta e as nove entregas (semanas 1, 2, 2, 3, 4, 4, 5, 6, 6) são coerentes entre si; só o "cinco" está errado.
- C6. Três a cinco meses (Estratégia a entrega, texto) contra cerca de seis meses (Estratégia a entrega, caso simulado).
- C7. Onze atores (tese da aba Ecossistema) contra treze linhas na tabela.
- C8. Três casos (título em Processos) contra quatro cartões.
- C9. Nove pessoas no núcleo mais uma facilitadora (Estrutura) contra nove nomes incluindo a facilitadora (Entenda; Cem perguntas, pergunta 4).
- C10. "Mais de vinte entregas entre novembro de 2025 e maio de 2026" (Executiva) contra as seis entregas nomeadas no Destaque, todas de novembro de 2025 a março de 2026, e contra "mais de duas dezenas de entregas entre 2025 e 2026" (Cem perguntas). O deck tem 14 no período e 32 no total.
- C11. Custos: Executiva "R$ 382.000 contra R$ 286.000" contra Reuniões e custo "R$ 381.625 contra R$ 286.500". Arredondamento errado no segundo número (o certo seria 287.000). Estratégia a entrega e Proposta (R$ 16 mil das sessões, menos que um mês do sistema atual) batem.
- C12. Referências a abas: "Aba Papéis e pessoas" (Proposta) e "Perguntas de design" (Fontes) não são nomes de aba; "(aba Estratégia a entrega)" para a conta das reuniões (Executiva) aponta para a aba errada; a tabela está em Reuniões e custo.
- C13. Regra 3 contra o texto: Sintomas ("Fala literal"; "grafias foram mantidas") e Fontes ("Grafias da transcrição mantidas entre aspas") afirmam literalidade; o texto está parafraseado, exceto pelos quatro trechos ainda entre aspas apontados nos itens 58, 67 e 79.

Números-âncora conferidos e corretos (para registro): 20% (fontes 1, 12); 115% e 99% (fonte 7); 36%, 59%, 72% (fonte 18); 5 anos e "enterrar canos" (fonte 12); 36 minutos (fonte 23, 14:00 a 14:36); 30 minutos com mentores (fontes 13 e 18); 3 consultores (fontes 14 e 16); R$ 1 milhão (fonte 11); 65% (fonte 22); 40 dias e 22% (fonte 23); 35 para 5 dias e 96 painéis (fonte 1); 40% de projeção do RE (fonte 20); prestamista desde 2024 e janeiro de 2027 (fonte 17); três anos de automação (fonte 11); R$ 45 milhões e R$ 15 milhões (fonte 12); 350% (fonte 16); 338 e 20 apólices (fonte 9); fórum de 4 horas (fonte 27); custos R$ 286.500 (2.292 horas-pessoa) e R$ 381.625 (3.053 horas-pessoa), diferença R$ 95.125 e 761 horas, todos recalculados e corretos; 51 encontros (soma correta); horas por papel (11, 6 a 14, 16, 3 a 4) coerentes com as durações declaradas; linhas de base dos 8 indicadores conferidas (ressalvas nos itens 24 e 25); os 10 direitos decisórios "hoje" conferidos (ressalvas nos itens 27 a 29). Citações literais das atas conferidas e corretas em todas as ocorrências verificadas (31 trechos), com a única ressalva de "refluctuar" (item 73).

Pontos de atenção que não contam como falha, para decisão do autor: (i) a sigla "IA" aparece seis vezes como conteúdo de negócio das atas (aceitação automática por IA nos concorrentes; IA na regulação de sinistro funeral); a regra 5 proíbe menção a IA, mas o sentido ali parece ser o de não expor o mecanismo de produção do documento; se a leitura for literal, trocar por "aceitação automática" e "regulação automatizada"; (ii) "Weekly", "Placement", "as-is", "Hubspot", "Mega broker", "Churn" e "one-shot" são estrangeirismos fora da lista proibida, todos vindos das atas; (iii) nomes de integrantes do grupo (Jacqueline, Alan, Tatiane, Glace, Alessandra, Christian Landi, Aretha, Daniel, Amanda) e dos mentores vêm das atas, não das transcrições, e por isso não foram contados como falha; ainda assim, a aba Estrutura publica sinais de sobrecarga por pessoa, o que pode ser lido como exposição individual por quem não participou do grupo.

---

## (d) Português

1. "É o que evita as áreas acabam fazendo o que a Estratégia quer" (Proposta) → "É o que evita que as áreas acabem fazendo o que a Estratégia quer".
2. "quórum dos ritos, itens sem saída explícita. ." (Executiva) → um único ponto.
3. "ou a capacidade aumenta: sem isso o time dedicado diagnostica e não entrega." (Executiva, célula truncada) → ver item 7.
4. "quando acontece o descoberta" (Fluxo funcional, abre e cartão) → "quando acontece a descoberta".
5. "não passa pelo descoberta" (Fluxo funcional, mapa) → "não passa pela descoberta".
6. "é descoberto e concebido na time dedicado" (Fluxo funcional) → "no time dedicado".
7. "alimenta: prioridades do fórum e da time dedicado" (Fluxo funcional, mapa) → "e do time dedicado".
8. "o que vai para a time dedicado" (Fluxo funcional, mapa) → "para o time dedicado".
9. "É a primeira coisa que a time dedicado faz" (Fluxo funcional) → "que o time dedicado faz".
10. "recebem da time dedicado, via fórum" (Fluxo funcional) → "recebem do time dedicado".
11. "Sustentação (sustentação)" (Fluxo funcional, duas vezes) → "Sustentação".
12. "sustentação triado, direto, sem descoberta" (Fluxo funcional, tabela) → "item de sustentação triado, direto, sem descoberta".
13. "Descoberta curto" (Desenho e regras) → "Descoberta curta".
14. "Fundir as três numa time dedicado resolve a duplicação, mas só se a time dedicado tiver porta" (Desenho e regras) → "num time dedicado ... se o time dedicado tiver".
15. "Qual é o problema que a time dedicado e o fórum vão resolver" (Desenho e regras) → "que o time dedicado e o fórum".
16. "que o formato vinha antes do problema. trocar o formato sem definir" (Desenho e regras) → dois-pontos e minúscula, ou ponto e maiúscula.
17. ": cada item responde a um sintoma verificado." (Desenho e regras): no HTML a frase está correta, com o selo Proposta antes dos dois-pontos; só o espelho .md a mutila. Sem correção no HTML.
18. "seriam as times dedicados, com o fórum de negócio como rito de entrega dos times dedicados" (Entenda) → "seriam os times dedicados"; e evitar a repetição: "com o fórum de negócio como seu rito de entrega".
19. "sem time dedicado dedicada" (Processos) → "sem time dedicado".
20. "o que essa time dedicado vai entregar" (Processos) → "o que esse time dedicado vai entregar".
21. "fundi-los numa time dedicado única" (Cem perguntas, 38) → "num time dedicado único".
22. "Estrutural, sustentação, Adequação e Oportunidade" (Cem perguntas, 92) → "Estrutural, Sustentação, Adequação e Oportunidade".
23. "Especificação recebida sem time dedicado alocada" (Análise) → "alocado".
24. "Lançar a time dedicado e o Fórum de Negócio" (Análise) → "Lançar o time dedicado".
25. "lugar de entrega das times dedicados" (Glossário) → "dos times dedicados".
26. "Os quatro ritos de uma time dedicado" (Glossário) → "de um time dedicado".
27. "dono do carteira de demandas" (Glossário) → "dono da carteira de demandas".
28. "Os sobrescritos apontam para o sintoma que cada critério evita Proposta e as durações são Proposta" (Estratégia a entrega) → frase completa antes dos selos (item 34).
29. "que sustenta cada relação Proposta e o formato de porta única é Proposta" (Fluxo funcional) → frase completa antes dos selos (item 40).
30. "Na semana 6, a mesa tem nove papéis assinados" (Problema e entregas) → "nove artefatos assinados" (ambiguidade com "papéis" no sentido de funções).
31. "Três casos que mostram o fluxo inteiro" (Processos) com quatro casos → "Quatro casos".
32. "Nove pessoas no núcleo, três mentores, uma facilitadora" (Estrutura) → ver item 68.
33. "Carteira de demandas acumulado" (Fluxo funcional, tabela "Quem alimenta quem") → "carteira de demandas acumulada".
34. "com a Unicred exigindo capital fixo, prêmio antecipado e aceitação automática para janeiro de 2027, e a companhia discutindo o tema desde 2024" (Estratégia a entrega, Na prática): correto; sem falha.
35. "A proposta, em duas linhas" duplicada (Executiva) → remover a repetição.
