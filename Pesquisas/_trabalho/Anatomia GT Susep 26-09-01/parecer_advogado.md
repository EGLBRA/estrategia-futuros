# Parecer do advogado do diabo: Anatomia Profunda GT Susep Vida e RE (26-09-01)

Objeto: `Pesquisas\Anatomia Profunda - GT Susep Vida e RE - 26-09-01\Anatomia Profunda - GT Susep Vida e RE - 26-09-01.html` (+ espelho .md). Base: 24 fontes do notebook, planilha de 72 sintomas (fonte 25) e transcrição da reunião de 01/09/2026 (fonte 26, só falas de Fabíola e Camila).

## Rodada 1: REPROVA
1. QA de forma acusou 20 "setas": eram o `-->` dos comentários de seção. Verificador corrigido (build.py), texto intacto.
2. 12 citações entre aspas não literais (conferência automática normalizada contra corpus.md): paráfrase do mentor (F01), "Soluções paliativas..." (F09, aspas internas em "perfeita"), "Visto/vista por grandes corretores" (F23), "Incapacidade sistêmica de rastrear..." (F15, faltava "atual" e "mapear"), "voltado/voltados à fundação" (F12), "quanto negócio isso trava" (frase própria com aspas), "Operação bastante sobrecarregada" (F20), "dado o histórico de lentidão" (F17), "concorrência desleal de preços" (F12), duas paráfrases da meta (F03, F06), "transbordo de ideias positivas" (F02, adjetivo fora das aspas), "não entende o produto" (F11). Todas reescritas na forma literal ou sem aspas.
3. Números-âncora: 45 conferidos literalmente no corpus, 0 ausentes.

## Rodada 2: REPROVA
1. Enxerto da fonte 26: 3 citações normalizadas indevidamente ("frente estratégica" vs "frente estratégico"; "S&OP" dentro das aspas onde a fala diz "Senop"; "PM, PO, scrum master" entre aspas). Corrigidas; nota de grafia acrescentada.
2. Frase de Fabíola citada ("E eu também tava achando que vocês já estavam trabalhando") não constava do extrato da fonte 26; acrescentada ao extrato.
3. QA acusou "transcri" como menção a processo: avaliado como tipo de documento (a fonte É uma transcrição), mantido; padrão do QA ajustado.

## Rodada 3: APROVA com ressalvas (registradas na aba Check)
- 20 rádios = 20 rótulos = 20 painéis; travessão 0; en-dash 0; setas 0.
- 168 citações entre aspas conferidas contra corpus + transcrição: 0 não literais.
- Sobrescritos: todos em 1..26; 26 fontes citadas, 0 órfãs.
- Marcas proibidas (HackMarket, Hack News, Panorama Mercado, FATO/HIPÓTESE, siglas de selo): 0.
- Espelho .md: 98 KB, sem selo duplicado.
- Ressalvas honestas: fonte única e interna; tese "não decide" é inferência; números de vitrine frágeis (115/99, 36%, 5 anos, "13", R$ 9 bi Icatu); 72 é contagem de classificação; fonte 26 circular (autor presente), mitigada pela regra de uso.
