# -*- coding: utf-8 -*-
"""v15: diagramas em O modelo (duas camadas; mês de pico), Alçadas (escada de escalada), Proposta (ciclo da fundação),
Problema e entregas (mapa subproblema para entregas)."""
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
ST = 'style="display:block;width:100%;height:auto;font-family:system-ui,sans-serif"'
DEFS = '<defs><marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>'
def box(x, y, w, h, t1, t2="", t3="", fill="#fff", stroke="#808080", tc="#1a1a1a", sc="#5a6068", fs=14):
    s = '<rect x="%d" y="%d" width="%d" height="%d" rx="7" fill="%s" stroke="%s" stroke-width="1.4"/>' % (x, y, w, h, fill, stroke)
    s += '<text x="%d" y="%d" font-size="%d" font-weight="600" fill="%s">%s</text>' % (x + 12, y + 22, fs, tc, t1)
    if t2: s += '<text x="%d" y="%d" font-size="13" fill="%s">%s</text>' % (x + 12, y + 41, sc, t2)
    if t3: s += '<text x="%d" y="%d" font-size="13" fill="%s">%s</text>' % (x + 12, y + 58, sc, t3)
    return s
def fig(svg, cap): return '<figure style="margin:14px 0 22px">\n' + svg + '\n<figcaption class="note" style="margin-top:6px">' + cap + '</figcaption>\n</figure>\n'

# ---------- Fig 1: duas camadas
s = '<svg viewBox="0 0 1100 400" role="img" aria-label="Duas camadas: estratégia decide, prioriza e mede; execução resolve e entrega; o que desce e o que sobe entre elas; o sucesso é medido no sistema" xmlns="http://www.w3.org/2000/svg" %s>' % ST
s += DEFS % ("m1", "#1a4a8a") + DEFS % ("m2", "#b47c00")
s += '<rect x="40" y="30" width="760" height="140" rx="10" fill="#eef3fb" stroke="#1a4a8a"/>'
s += '<text x="60" y="58" font-size="15" font-weight="700" letter-spacing="1.5" fill="#1a4a8a">CAMADA DE ESTRATÉGIA</text><text x="60" y="80" font-size="13" fill="#4a4f57">decide, prioriza e mede resultado; ritmo mensal e trimestral</text>'
for i, (a, b) in enumerate([("Fórum de Negócio SUSEP", "mensal, 2h; porta única"), ("Comitê de priorização", "mensal, 1h; decide na alçada"), ("Mentoria por tema", "1h; patrocina e destrava"), ("RDS e COMEX", "política e orçamento")]):
    s += box(60 + i * 185, 100, 170, 54, a, b, stroke="#1a4a8a")
s += '<rect x="40" y="240" width="760" height="140" rx="10" fill="#fff8e6" stroke="#b47c00"/>'
s += '<text x="60" y="268" font-size="15" font-weight="700" letter-spacing="1.5" fill="#b47c00">CAMADA DE EXECUÇÃO</text><text x="60" y="290" font-size="13" fill="#4a4f57">resolve problemas em ciclos de duas semanas e entrega incrementos</text>'
for i, (a, b) in enumerate([("Time dedicado Vida", "núcleo fixo e áreas volantes"), ("Descoberta", "4 a 8 semanas por desafio"), ("Sala de guerra", "temas críticos, 2 por semana"), ("Reunião da esteira", "quinzenal, 1h30")]):
    s += box(60 + i * 185, 310, 170, 54, a, b, stroke="#b47c00")
s += '<path d="M250,170 L250,238" stroke="#1a4a8a" stroke-width="2" fill="none" marker-end="url(#m1)"/><text x="262" y="200" font-size="13" fill="#1a4a8a">desce: prioridade, alçada,</text><text x="262" y="218" font-size="13" fill="#1a4a8a">capacidade e KRs</text>'
s += '<path d="M600,240 L600,172" stroke="#b47c00" stroke-width="2" fill="none" marker-end="url(#m2)"/><text x="612" y="200" font-size="13" fill="#b47c00">sobe: incremento demonstrado, resultado</text><text x="612" y="218" font-size="13" fill="#b47c00">medido, exceção com recomendação única</text>'
s += '<rect x="830" y="30" width="250" height="350" rx="10" fill="#f6f7f9" stroke="#5b626a" stroke-dasharray="5 4"/>'
s += '<text x="846" y="58" font-size="14" font-weight="700" letter-spacing="1.5" fill="#1a1a1a">SUCESSO DO SISTEMA</text>'
y = 88
for t in ["medido em:", "entregas em produção", "tempo entre entrada e decisão", "tempo de ciclo da ficha ao pronto", "adoção pela ponta", "resultado em 90 dias"]:
    s += '<text x="%d" y="%d" font-size="13" fill="%s"%s>%s</text>' % (846 if t.endswith(":") else 860, y, "#1a1a1a" if t.endswith(":") else "#4a4f57", ' font-weight="600"' if t.endswith(":") else "", t); y += 22
y += 10
for t in ["nunca em:", "times criados", "ritos realizados", "papéis preenchidos"]:
    s += '<text x="%d" y="%d" font-size="13" fill="%s"%s>%s</text>' % (846 if t.endswith(":") else 860, y, "#b71c1c", ' font-weight="600"' if t.endswith(":") else "", t); y += 22
s += '</svg>'
FIG1 = fig(s, "Duas camadas e o contrato entre elas. A estratégia decide e mede; a execução resolve e entrega. O sucesso é do sistema, nunca da adoção do modelo.")

# ---------- Fig 2: mês de pico
rows = [("Reunião da esteira (1h30)", [2, 2, 2, 2], "#1a4a8a"), ("Triagem (30 min)", [0, 1, 0, 1], "#1a4a8a"), ("Comitê de priorização (1h)", [0, 0, 1, 0], "#1a4a8a"), ("Fórum de Negócio (2h)", [0, 0, 0, 1], "#1a4a8a"), ("Mentoria por tema (1h)", [0, 1, 0, 0], "#1a4a8a"),
        ("Revisão do time (45 min)", [0, 1, 0, 1], "#b47c00"), ("Descoberta (2h)", [2, 2, 2, 2], "#b47c00"), ("Sala de guerra (1h)", [2, 2, 2, 2], "#b47c00"), ("Diárias do núcleo (15 min)", [5, 5, 5, 5], "#b47c00")]
s = '<svg viewBox="0 0 1100 360" role="img" aria-label="Um mês de pico: 51 encontros distribuídos em quatro semanas, por rito" xmlns="http://www.w3.org/2000/svg" %s>' % ST
s += '<text x="20" y="28" font-size="15" font-weight="700" fill="#1a1a1a">51 encontros num mês de pico</text><text x="330" y="28" font-size="13" fill="#4a4f57">cada ponto é um encontro; azul, camada de estratégia; âmbar, execução</text>'
for w in range(4):
    x0 = 300 + w * 175
    s += '<rect x="%d" y="44" width="171" height="%d" fill="%s" stroke="none"/>' % (x0, 28 * len(rows) + 8, "#fafafa" if w % 2 == 0 else "#f2f3f5")
    s += '<text x="%d" y="62" font-size="13" font-weight="600" fill="#5a6068" text-anchor="middle">semana %d</text>' % (x0 + 85, w + 1)
s += '<text x="1060" y="62" font-size="13" font-weight="600" fill="#5a6068" text-anchor="middle">no mês</text>'
tot = 0
for i, (name, counts, col) in enumerate(rows):
    yc = 84 + i * 28
    s += '<text x="20" y="%d" font-size="13.5" fill="#1a1a1a">%s</text>' % (yc + 5, name)
    for w, n in enumerate(counts):
        x0 = 300 + w * 175
        for k in range(n):
            s += '<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (x0 + 22 + k * (30 if n <= 4 else 26), yc, 6 if n <= 4 else 5, col)
    s += '<text x="1060" y="%d" font-size="13.5" font-weight="600" fill="%s" text-anchor="middle">%d</text>' % (yc + 5, col, sum(counts)); tot += sum(counts)
yb = 84 + len(rows) * 28 + 6
s += '<line x1="20" y1="%d" x2="1085" y2="%d" stroke="#d7dbe0"/>' % (yb, yb)
s += '<text x="20" y="%d" font-size="13.5" font-weight="700" fill="#1a1a1a">Total no mês de pico</text><text x="1060" y="%d" font-size="14" font-weight="700" fill="#1a1a1a" text-anchor="middle">%d</text>' % (yb + 22, yb + 22, tot)
s += '</svg>'
FIG2 = fig(s, "Como os 51 encontros do mês de pico se distribuem. A maioria é curta e com poucas pessoas; a média anual custeada fica perto de 40 por mês (aba Reuniões e custo).")

# ---------- Fig 3: escada de escalada
s = '<svg viewBox="0 0 1100 230" role="img" aria-label="Como um tema sobe e volta: tentativa na alçada, recomendação única em cinco dias úteis, patrocínio do mentor em até 30 dias, retorno por escrito; sem resposta em 45 dias, o item é estacionado" xmlns="http://www.w3.org/2000/svg" %s>' % ST
s += DEFS % ("m3", "#5b626a")
steps = [("1. Tentativa na alçada", "fórum ou comitê decide", "e registra; na reunião"), ("2. Recomendação única", "uma página: problema, opções,", "custo da espera; 5 dias úteis"), ("3. Patrocínio", "mentor leva à diretoria", "ou ao COMEX; até 30 dias"), ("4. Retorno por escrito", "dono e prazo, ou motivo", "da recusa; reunião seguinte")]
for i, (a, b, c) in enumerate(steps):
    s += box(20 + i * 215, 40, 200, 78, a, b, c, stroke="#1a4a8a")
    if i < 3: s += '<path d="M%d,79 L%d,79" stroke="#5b626a" stroke-width="2" fill="none" marker-end="url(#m3)"/>' % (220 + i * 215, 233 + i * 215)
s += box(880, 40, 200, 78, "5. Silêncio de 45 dias", "item estacionado por falta", "de decisão; publicado no PIE", fill="#fdecea", stroke="#b71c1c", tc="#b71c1c")
s += '<path d="M765,118 L765,150 L980,150 L980,120" stroke="#b71c1c" stroke-width="1.6" stroke-dasharray="5 4" fill="none" marker-end="url(#m3)"/><text x="800" y="170" font-size="13" fill="#b71c1c">se a resposta não vier</text>'
s += '<path d="M660,118 L660,195 L120,195 L120,120" stroke="#1a4a8a" stroke-width="1.6" stroke-dasharray="5 4" fill="none" marker-end="url(#m3)"/><text x="300" y="215" font-size="13" fill="#1a4a8a">a decisão volta ao fórum com dono e prazo, e o item sai da fila de espera</text>'
s += '</svg>'
FIG3 = fig(s, "A escada de escalada. Cada degrau tem um prazo; o que hoje espera meses por uma janela do mentor passa a ter data de resposta desde o primeiro dia.")

# ---------- Fig 4: ciclo da fundação
s = '<svg viewBox="0 0 1100 300" role="img" aria-label="Ciclo da fundação: captar o problema, ofertar valor, solucionar e validar com o negócio; o aprendizado volta ao próximo problema" xmlns="http://www.w3.org/2000/svg" %s>' % ST
s += DEFS % ("m4", "#00995d")
caps = [("Captar o problema", "ficha de demanda;", "registro de não-ganhos"), ("Ofertar valor", "enquadramento com valor;", "nota de relevância"), ("Solucionar", "sala de descoberta;", "opções com esforço"), ("Validar com o negócio", "lista de pronto;", "leitura em 30 e 90 dias")]
for i, (a, b, c) in enumerate(caps):
    s += box(30 + i * 265, 70, 235, 84, a, b, c, fill="#eefaf1", stroke="#00995d", tc="#00995d")
    if i < 3: s += '<path d="M%d,112 L%d,112" stroke="#00995d" stroke-width="2" fill="none" marker-end="url(#m4)"/>' % (265 + i * 265, 293 + i * 265)
s += '<path d="M942,70 L942,36 L148,36 L148,68" stroke="#00995d" stroke-width="1.8" stroke-dasharray="6 4" fill="none" marker-end="url(#m4)"/><text x="545" y="28" font-size="13" fill="#00995d" text-anchor="middle">o aprendizado e o não-ganho voltam ao próximo problema</text>'
s += '<rect x="30" y="190" width="1040" height="80" rx="8" fill="#f6f7f9" stroke="#5b626a" stroke-dasharray="5 4"/>'
s += '<text x="50" y="218" font-size="14" font-weight="700" fill="#1a1a1a">O que a fundação produz, independentemente de quem ocupa cada cadeira</text>'
s += '<text x="50" y="246" font-size="13.5" fill="#4a4f57">decisões mais bem informadas (dado, valor e opções antes de decidir) · autonomia (alçada escrita para decidir sem subir) · velocidade (semanas entre entrada e decisão, não meses)</text>'
s += '</svg>'
FIG4 = fig(s, "A fundação em quatro capacidades. Não é um formato de time; é o que passa a existir para decidir melhor, com instrumento simples em cada etapa.")

# ---------- Fig 5: subproblemas para entregas
probs = ["1. Decisão sem alçada", "2. Oito portas e nenhuma triagem", "3. Pedido cru à TI", "4. Braço não reservado", "5. Resultado não medido", "6. Número sem origem explicada"]
ents = ["1. Lista de problemas priorizados", "2. Fluxo da estratégia à entrega", "3. Fluxo funcional do time", "4. Sistema de reuniões com custo", "5. Tabela de alçadas", "6. Regras publicadas", "7. Matriz de dedicação e suplentes", "8. Plano do piloto", "9. Painel de indicadores do sistema"]
links = {0: [4, 5], 1: [0, 1, 2], 2: [1, 6], 3: [6], 4: [3, 8], 5: [4, 8]}
s = '<svg viewBox="0 0 1100 430" role="img" aria-label="Cada subproblema ligado às entregas que o tratam" xmlns="http://www.w3.org/2000/svg" %s>' % ST
s += '<text x="20" y="24" font-size="13" font-weight="700" letter-spacing="1.5" fill="#7d848c">SUBPROBLEMA</text><text x="750" y="24" font-size="13" font-weight="700" letter-spacing="1.5" fill="#7d848c">ENTREGA QUE O TRATA</text>'
py = [46 + i * 64 for i in range(6)]; ey = [40 + j * 43 for j in range(9)]
for i, p in enumerate(probs):
    for j in links[i]:
        s += '<path d="M350,%d C550,%d 550,%d 750,%d" stroke="#b9bec4" stroke-width="1.6" fill="none"/>' % (py[i] + 24, py[i] + 24, ey[j] + 18, ey[j] + 18)
for i, p in enumerate(probs):
    s += '<rect x="20" y="%d" width="330" height="48" rx="7" fill="#fdecea" stroke="#b71c1c"/><text x="34" y="%d" font-size="14" font-weight="600" fill="#1a1a1a">%s</text>' % (py[i], py[i] + 30, p)
for j, e in enumerate(ents):
    s += '<rect x="750" y="%d" width="330" height="36" rx="7" fill="#eefaf1" stroke="#00995d"/><text x="764" y="%d" font-size="13.5" font-weight="600" fill="#1a1a1a">%s</text>' % (ey[j], ey[j] + 24, e)
s += '</svg>'
FIG5 = fig(s, "De cada subproblema às entregas que o tratam. Nenhuma entrega existe sem um problema que a justifique; nenhum subproblema fica sem entrega.")

# ---------- inserções
R("I", r'(<div class="alerta"><strong>VISÃO ATUAL, NÃO FINAL\.</strong>.*?</div>)', r'\1\n' + FIG1.replace("\\", "\\\\"), rx=True, count=1)
R("I", r'(<h3>[^<]*Quantas reuniões[^<]*</h3>)', r'\1\n' + FIG2.replace("\\", "\\\\"), rx=True, count=1)
R("J", "<h3>Como um tema sobe e como volta</h3>", "<h3>Como um tema sobe e como volta</h3>\n" + FIG3)
R("H", "<h3>A fundação: captar o problema, ofertar valor, solucionar e validar com o negócio</h3>", "<h3>A fundação: captar o problema, ofertar valor, solucionar e validar com o negócio</h3>\n" + FIG4)
R("K", "<h3>As entregas</h3>", FIG5 + "<h3>As entregas</h3>")
for k, s in F.items(): save(f"frag_{k}.html", s)
print("patch v15 ok; faltas:", len(MISS))
for x in MISS: print("  MISS", x)
