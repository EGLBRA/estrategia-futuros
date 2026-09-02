# -*- coding: utf-8 -*-
"""v19: cabeçalho e rodapé com frente, data, uso interno e material sensível; desenho do ecossistema; desenho dos papéis;
tabela 'o que cada ator precisa conseguir fazer'."""
import io, os, re, math
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SV = '<span class="sel sel-v">Verificado</span>'; SI = '<span class="sel sel-i">Inferência</span>'
MISS = []
ST = 'style="display:block;width:100%;height:auto;font-family:system-ui,sans-serif"'
def fig(svg, cap): return '<figure style="margin:14px 0 22px">\n' + svg + '\n<figcaption class="note" style="margin-top:6px">' + cap + '</figcaption>\n</figure>\n'

# 1. cabeçalho e rodapé
b = load("build.py")
old = '<p class="lbl">A Anatomia Profunda &middot; Diagnóstico funcional de uma frente estratégica &middot; Uso interno</p>'
new = '<p class="lbl">GT Evoluir Modelo de Negócio SUSEP Vida e RE, Seguros Unimed &middot; Diagnóstico funcional em 1º de setembro de 2026 &middot; Uso interno &middot; Material sensível</p>'
if old in b: b = b.replace(old, new, 1)
else: MISS.append("kicker")
foot = '<div class="W"><p class="lbl" style="margin:40px 0 24px;border-top:1px solid #ddd;padding-top:12px">GT Evoluir Modelo de Negócio SUSEP Vida e RE, Seguros Unimed &middot; Diagnóstico de 1º de setembro de 2026 &middot; Uso interno &middot; Material sensível: não circular fora da área de Estratégia</p></div>\n</body>'
if "Material sensível: não circular" not in b:
    if "\n</body>" in b: b = b.replace("\n</body>", "\n" + foot, 1)
    else: MISS.append("footer")
save("build.py", b)

# 2. ecossistema: desenho da estrela
atores = [("Mentores", "diretriz e patrocínio", "#1a4a8a"), ("Diretoria, RDS e COMEX", "decisão e orçamento", "#1a4a8a"), ("Área de Estratégia", "método e ritos", "#1a4a8a"), ("Transformação das frentes", "modelo de times", "#1a4a8a"),
         ("Esteiras executoras", "fila de TI e projetos", "#b47c00"), ("Controladoria", "número e meta", "#b47c00"), ("Inteligência de Mercado", "dados de mercado", "#b47c00"), ("Gente de fora", "método e pesquisa", "#b47c00"),
         ("Canal corretor", "demanda e cotação", "#00995d"), ("Cooperativas de crédito", "prazo e balcão", "#00995d"), ("Sistema Unimed", "canal e clientes", "#00995d"), ("Marketing e Corretora Digital", "ofertas e campanhas", "#00995d"), ("Concorrentes", "pressão de preço e aceitação", "#b71c1c")]
cx, cy, rx, ry = 550, 250, 440, 190
s = '<svg viewBox="0 0 1100 500" role="img" aria-label="O núcleo da frente no centro e os treze atores em volta: governança em azul, execução e dados em âmbar, mercado em verde, concorrentes em vermelho" xmlns="http://www.w3.org/2000/svg" %s>' % ST
pos = []
for i, (n, d, c) in enumerate(atores):
    a = -math.pi / 2 + 2 * math.pi * i / len(atores)
    x, y = cx + rx * math.cos(a), cy + ry * math.sin(a); pos.append((x, y))
    s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#d7dbe0" stroke-width="1.4"/>' % (cx, cy, x, y)
s += '<circle cx="%d" cy="%d" r="78" fill="#fff8e6" stroke="#b47c00" stroke-width="2"/>' % (cx, cy)
s += '<text x="%d" y="%d" text-anchor="middle" font-size="14" font-weight="700" fill="#1a1a1a">Núcleo da frente</text><text x="%d" y="%d" text-anchor="middle" font-size="12.5" fill="#5a6068">9 papéis, 3 mentores,</text><text x="%d" y="%d" text-anchor="middle" font-size="12.5" fill="#5a6068">1 facilitação</text>' % (cx, cy - 8, cx, cy + 12, cx, cy + 29)
for (n, d, c), (x, y) in zip(atores, pos):
    w = 176; h = 44; bx = x - w / 2; by = y - h / 2
    s += '<rect x="%d" y="%d" width="%d" height="%d" rx="7" fill="#fff" stroke="%s" stroke-width="1.4"/>' % (bx, by, w, h, c)
    s += '<text x="%d" y="%d" text-anchor="middle" font-size="12.5" font-weight="600" fill="#1a1a1a">%s</text><text x="%d" y="%d" text-anchor="middle" font-size="11.5" fill="#5a6068">%s</text>' % (x, y - 4, n, x, y + 13, d)
s += '<text x="20" y="490" font-size="12" fill="#5a6068">azul: governança · âmbar: execução e dados · verde: mercado · vermelho: concorrência</text>'
s += '</svg>'
FIG_ECO = fig(s, "O ecossistema da frente: um núcleo pequeno que depende de treze atores e não comanda nenhum. O que cada um dá ao grupo está na tabela abaixo.")

# 3. o que cada ator precisa conseguir fazer
JOBS = '''
<h3>O que cada ator precisa conseguir fazer</h3>
<p>Cada ator entra na frente para realizar algo concreto. O desenho atual entrega parte; o que falta é o que o novo desenho precisa dar.</p>
<table>
<thead><tr><th>Ator</th><th>O que precisa conseguir</th><th>O que o desenho atual dá</th><th>O que falta</th></tr></thead>
<tbody>
<tr><td><strong>Corretor</strong></td><td>Cotar e fechar Vida sem esperar semanas pela aceitação.</td><td>Preço competitivo; aceitação lenta, documentos em excesso, pendências paradas há mais de 40 dias.<sup>18, 23</sup></td><td>Resposta em 48 horas para cotação aberta; reconsideração de recusa em cinco dias.</td></tr>
<tr><td><strong>Cooperativa (Unicred)</strong></td><td>Ter no balcão o prestamista de prêmio único até janeiro de 2027.</td><td>Tema discutido desde 2024; automação estimada em três anos.<sup>11, 17</sup></td><td>Decisão com escopo mínimo e paliativo com data.</td></tr>
<tr><td><strong>Líder da esteira</strong></td><td>Decidir dentro de uma alçada e proteger o braço da esteira.</td><td>Tudo sobe; a liderança absorve o operacional com três consultores a menos.<sup>14, 22</sup></td><td>Alçada escrita, suplente, matriz de dedicação.</td></tr>
<tr><td><strong>Mentor</strong></td><td>Destravar temas sem ser o único ponto de decisão.</td><td>Agendas de 30 minutos e férias sem suplente; quando presente, destrava em 36 minutos.<sup>13, 18, 23</sup></td><td>Temas com dono e recomendação única; escada de escalada com prazo.</td></tr>
<tr><td><strong>Diretoria e COMEX</strong></td><td>Decidir política e orçamento com uma recomendação, não com uma disputa.</td><td>Esgotamento de comissão esperou de 2024 a agosto de 2026.<sup>9, 23</sup></td><td>Recomendação única em cinco dias úteis; resposta em até 30 dias.</td></tr>
<tr><td><strong>TI</strong></td><td>Receber pedidos diagnosticados, com impacto e esforço, e sustentar o que já roda.</td><td>Emergências trocam projetos; sem equipe dedicada à SUSEP.<sup>22</sup></td><td>Cota reservada e critério de despriorização.<sup>27</sup></td></tr>
<tr><td><strong>Operação e subscrição</strong></td><td>Sustentar a carteira sem receber OKR novo sem braço.</td><td>A operação declarou que não cabe OKR novo.<sup>20</sup></td><td>Fila de sustentação própria, fora da descoberta.</td></tr>
<tr><td><strong>Área de Estratégia</strong></td><td>Facilitar sem virar dona do problema e sem perder credibilidade com as áreas.</td><td>Método discutido antes do problema; receio de mais um modelo dito internamente.<sup>15, 26</sup></td><td>Encontros que partem dos problemas; desenhos assinados pelo grupo.</td></tr>
</tbody>
</table>
<p>Os fatos vêm das atas. ''' + SV + ''' O que cada ator precisa conseguir é leitura deste documento. ''' + SI + ''' O que falta é desenho. ''' + SP + '''</p>
'''
A = load("frag_A.html")
m = re.search(r'<section id="p-eco" class="pane">.*?<p class="gancho">.*?</p>\n', A, re.S)
if m: A = A.replace(m.group(0), m.group(0) + FIG_ECO, 1)
else: MISS.append("eco gancho")
sec = re.search(r'(<section id="p-eco" class="pane">.*?)(<div class="pratica">)', A, re.S)
if sec: A = A.replace(sec.group(0), sec.group(1) + JOBS + sec.group(2), 1)
else: MISS.append("eco pratica")
save("frag_A.html", A)

# 4. papéis: desenho do núcleo
s = '<svg viewBox="0 0 1100 330" role="img" aria-label="Papéis da frente: três mentores acima, o núcleo de nove papéis no meio, as áreas volantes abaixo, a facilitação da Estratégia ao lado" xmlns="http://www.w3.org/2000/svg" %s>' % ST
s += '<rect x="330" y="20" width="440" height="50" rx="8" fill="#eef3fb" stroke="#1a4a8a"/><text x="550" y="41" text-anchor="middle" font-size="14" font-weight="700" fill="#1a4a8a">Mentores: três superintendentes</text><text x="550" y="59" text-anchor="middle" font-size="12.5" fill="#5a6068">diretriz, patrocínio, arbitragem; agendas de 30 minutos</text>'
s += '<rect x="20" y="110" width="200" height="90" rx="8" fill="#f3ecfa" stroke="#6410ab"/><text x="120" y="140" text-anchor="middle" font-size="13.5" font-weight="700" fill="#6410ab">Facilitação</text><text x="120" y="160" text-anchor="middle" font-size="12.5" fill="#5a6068">área de Estratégia</text><text x="120" y="178" text-anchor="middle" font-size="12.5" fill="#5a6068">ritos, atas, planilhas, radar</text>'
s += '<rect x="240" y="95" width="840" height="120" rx="10" fill="#fff8e6" stroke="#b47c00" stroke-width="1.6"/><text x="256" y="118" font-size="13.5" font-weight="700" letter-spacing="1.2" fill="#b47c00">NÚCLEO: NOVE PAPÉIS, LIDERANÇA ROTATIVA ENTRE LÍDER E COLÍDER</text>'
nuc = ["Líder: estratégia comercial", "Colíder: subscrição e operação RE", "Produtos", "Atuarial", "Subscrição Vida e operações", "Tecnologia", "Canais", "Sinistro e inteligência"]
for i, n in enumerate(nuc):
    x = 256 + (i % 4) * 206; y = 132 + (i // 4) * 40
    s += '<rect x="%d" y="%d" width="196" height="32" rx="6" fill="#fff" stroke="#f3dca3"/><text x="%d" y="%d" text-anchor="middle" font-size="12.5" fill="#1a1a1a">%s</text>' % (x, y, x + 98, y + 20, n)
s += '<rect x="240" y="245" width="840" height="60" rx="8" fill="#f6f7f9" stroke="#5b626a" stroke-dasharray="5 4"/><text x="256" y="268" font-size="13" font-weight="700" fill="#1a1a1a">Áreas volantes, chamadas por tema</text><text x="256" y="290" font-size="12.5" fill="#5a6068">Medicina e aceitação · Compliance · Controladoria · Inteligência de Mercado · TI e arquitetura · Marketing · Processos e VMO</text>'
s += '<line x1="550" y1="70" x2="550" y2="95" stroke="#1a4a8a" stroke-width="1.6"/><line x1="220" y1="155" x2="240" y2="155" stroke="#6410ab" stroke-width="1.6"/><line x1="550" y1="215" x2="550" y2="245" stroke="#5b626a" stroke-width="1.6" stroke-dasharray="4 3"/>'
s += '</svg>'
FIG_PAP = fig(s, "Quem está na frente e em que posição. Nove papéis no núcleo, três mentores acima, a facilitação ao lado e as áreas que entram por tema. A tabela abaixo diz o que cada papel carrega e onde está sobrecarregado.")
B = load("frag_B.html")
m = re.search(r'<section id="p-papeis" class="pane">.*?<p class="tese">.*?</p>\n', B, re.S)
if m: B = B.replace(m.group(0), m.group(0) + FIG_PAP, 1)
else: MISS.append("papeis tese")
save("frag_B.html", B)
print("patch v19 ok; faltas:", MISS)
