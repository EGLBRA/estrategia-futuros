# -*- coding: utf-8 -*-
"""v20: Inteligência Estratégica e Inteligência de Mercado como parte da solução (contexto para decidir)."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SV = '<span class="sel sel-v">Verificado</span>'
MISS = []
def rep(fn, old, new, rx=False, label=""):
    s = load(fn)
    if rx: s2, n = re.subn(old, new, s, count=1, flags=re.S)
    else: n = s.count(old); s2 = s.replace(old, new, 1)
    if n == 0: MISS.append((fn, label or old[:60]))
    save(fn, s2)

# O modelo: seção própria
SEC = '''
<h3>Inteligência Estratégica e Inteligência de Mercado: o contexto antes da decisão</h3>
<p>Nenhuma decisão do fórum ou da descoberta se toma só com o pedido na mão. As duas inteligências entram no desenho como fornecedoras fixas de contexto, com pauta e prazo.</p>
<table>
<thead><tr><th>Quem</th><th>O que entrega</th><th>Para qual rito</th><th>Quando</th></tr></thead>
<tbody>
<tr><td><strong>Inteligência Estratégica</strong> (área de Estratégia)</td><td>Leitura do mapa e dos KRs por esteira; cenários e sinais que mudam a prioridade; o que outras frentes e o mercado já aprenderam; número-base e desvio contra a meta.</td><td>Fórum de Negócio; comitê de priorização; encontro de piloto e medição.</td><td>Uma página por mês, antes do fórum; leitura trimestral no PIE.</td></tr>
<tr><td><strong>Inteligência de Mercado</strong></td><td>Concorrentes (preço, aceitação, comissão), sinistralidade comparada, painel V4, radar de Vida e RE, comportamento do canal corretor e das cooperativas.<sup>6, 15</sup></td><td>Sala de descoberta (olhar o mercado); triagem (nota de relevância); fórum (contexto do tema).</td><td>Na abertura de cada descoberta e a cada fórum; sob demanda para sala de guerra em 48 horas.</td></tr>
</tbody>
</table>
<p>Hoje o insumo de mercado chega tarde e manual, e o painel de sinistralidade não conversa com o RGS.<sup>6, 15</sup> ''' + SV + ''' No desenho, as duas inteligências têm assento, pauta e prazo; a decisão que chega ao fórum já vem com o contexto, não o pede na hora. ''' + SP + '''</p>
'''
rep("frag_I.html", r"(<h3>[^<]*Quantas reuniões[^<]*</h3>)", SEC + r"\1", rx=True, label="h3 quantas")
# Fig 1: faixas com a fonte de contexto
rep("frag_I.html", "decide, prioriza e mede resultado; ritmo mensal e trimestral</text>", "decide, prioriza e mede resultado, com contexto da Inteligência Estratégica e de Mercado</text>")
rep("frag_I.html", "resolve problemas em ciclos de duas semanas e entrega incrementos</text>", "resolve problemas em ciclos de duas semanas; a descoberta usa dados de mercado</text>")
# Alçadas: consultados
rep("frag_J.html", "<td>Controladoria, Canais, TI</td>", "<td>Controladoria, Canais, TI, Inteligência de Mercado</td>")
# Proposta: instrumento de ofertar valor
rep("frag_H.html", "Enquadramento com valor estimado; nota de relevância na triagem.", "Enquadramento com valor estimado; nota de relevância na triagem; contexto de mercado da Inteligência de Mercado e leitura do mapa da Inteligência Estratégica.")
# Ecossistema: o que cada ator precisa conseguir
rep("frag_A.html", "<tr><td><strong>Área de Estratégia</strong></td><td>Facilitar sem virar dona do problema", "<tr><td><strong>Inteligência Estratégica e de Mercado</strong></td><td>Levar contexto (mercado, concorrentes, sinistralidade, cenários) antes de a decisão ser tomada.</td><td>Painel V4 e radar existem; o insumo chega tarde e manual.<sup>6, 15</sup></td><td>Assento fixo no fórum e na descoberta, com pauta e prazo (aba O modelo).</td></tr>\n<tr><td><strong>Área de Estratégia</strong></td><td>Facilitar sem virar dona do problema")
# Fluxo funcional: texto de origem dos dados
rep("frag_E.html", "dados (Controladoria, Inteligência de Mercado, funil, sinistro)", "dados (Controladoria, Inteligência Estratégica e de Mercado, funil, sinistro)")
print("patch v20 ok; faltas:", MISS)
