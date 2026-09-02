# -*- coding: utf-8 -*-
"""v3: troca a secao Reunioes por Fluxo funcional; renomeia aba; corrige regex FATO; gera o arquivo avulso."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)

# frag_E: substituir a secao p-reun inteira
e = load("frag_E.html")
new = load("frag_reun.html")
e2 = re.sub(r'<!-- =+ REUNIOES =+ -->\s*<section id="p-reun" class="pane">.*?</section>\s*$', new, e, flags=re.S)
assert e2 != e, "secao p-reun nao encontrada"
save("frag_E.html", e2)

# build.py: nome da aba e regex FATO
b = load("build.py")
b = b.replace('("reun", "Reuniões e fluxo")', '("reun", "Fluxo funcional")')
b = b.replace('Panorama Mercado|FATO\\b|', 'Panorama Mercado|\\bFATO\\b|')
assert '\\bFATO\\b' in b, "regex FATO nao ajustada"
b = b.replace("o rascunho das reuniões e do fluxo de informação.", "o rascunho do fluxo funcional entre áreas, grupos e fóruns.")
save("build.py", b)

# frag_A e frag_check: renomear referencia
a = load("frag_A.html")
a = a.replace("Reuniões e fluxo, 5W2H.</strong> O desenho proposto: tipos de demanda, governança, times e ritos; o blueprint linear em oito etapas; o rascunho das reuniões e do fluxo mínimo de informação no formato do blueprint da Previdência;",
              "Fluxo funcional, 5W2H.</strong> O desenho proposto: tipos de demanda, governança, times e ritos; o blueprint linear em oito etapas; o rascunho do fluxo funcional (quem alimenta quem, da origem do problema à solução entregue);")
save("frag_A.html", a)
c = load("frag_check.html")
c = c.replace('"Reuniões e fluxo" (rascunho no formato do blueprint da Previdência, com base na transcrição da reunião "Modelo de Squads", fonte 27)',
              '"Fluxo funcional" (rascunho de quem alimenta quem, da origem do problema à solução, a partir do esboço da Estratégia e das transcrições de 1º de setembro, fontes 26 e 27; papéis ficaram de fora a pedido)')
c = c.replace("A aba Reuniões e fluxo carrega uma faixa de RASCUNHO", "A aba Fluxo funcional carrega uma faixa de RASCUNHO")
save("frag_check.html", c)
d = load("frag_D.html")
d = d.replace("Usada apenas na aba Reuniões e fluxo.", "Usada apenas na aba Fluxo funcional.")
save("frag_D.html", d)

# arquivo avulso: mesma secao, na casca simples do rascunho
OUT = r"A:\_01 Projetos\Estrategia\Pesquisas\Blueprint Estrategia a Entrega SUSEP - 26-09-01\Fluxo Funcional SUSEP - rascunho.html"
body = re.sub(r'<!-- =+ REUNIOES =+ -->\s*<section id="p-reun" class="pane">', '', new).replace("</section>", "")
body = re.sub(r'<sup>[^<]*</sup>', '', body)  # sem sobrescritos fora do documento-mae
body = re.sub(r'<span class="sel sel-[vie]">[^<]*</span>', '', body)
html = '''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fluxo Funcional · SUSEP Vida · rascunho</title>
<style>
body{margin:0;font-family:"Segoe UI",system-ui,sans-serif;color:#1a1a1a;background:#f6f7f9;font-size:15px;line-height:1.5}
header{background:#00995d;color:#fff;padding:18px 28px 14px}header h1{margin:0;font-size:23px;font-weight:600}header p{margin:6px 0 0;font-size:13.5px;color:#e6f6ee;max-width:1100px}
main{padding:22px 28px 60px;max-width:1400px;margin:0 auto}
h2{font-size:20px;margin:0 0 6px}h3{font-size:16px;margin:26px 0 6px}
.tese{font-style:italic;color:#444;margin:0 0 12px;max-width:1080px}
table{border-collapse:collapse;width:100%;font-size:13px;background:#fff;border:1px solid #e3e6ea;margin:8px 0}
th,td{border-bottom:1px solid #e3e6ea;padding:8px 10px;text-align:left;vertical-align:top}
th{background:#f0f0ec;font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:#5a5f66}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:700px){.g2{grid-template-columns:1fr}}
.card{background:#fff;border:1px solid #e3e6ea;border-left:5px solid #00995d;border-radius:6px;padding:12px 14px;font-size:13.5px}
.note{font-size:12.5px;color:#666;margin-top:6px}
footer{border-top:1px solid #e3e6ea;margin-top:40px;padding-top:12px;font-size:11px;color:#5a6068;letter-spacing:.06em;text-transform:uppercase}
</style></head><body>
<header><h1>Fluxo Funcional <span style="color:#a9e0c6;font-weight:300">· SUSEP Vida · quem alimenta quem</span></h1><p>Versão avulsa da aba "Fluxo funcional" da Anatomia Profunda do GT. Sem papéis por enquanto: primeiro o fluxo, depois quem faz.</p></header>
<main>''' + body + '''
<footer>Rascunho · versão 0.2 · SUSEP Vida · fluxo funcional · 1º de setembro de 2026 · Eric Leite · sem travessão</footer>
</main></body></html>'''
io.open(OUT, "w", encoding="utf-8", newline="\n").write(html)
old = r"A:\_01 Projetos\Estrategia\Pesquisas\Blueprint Estrategia a Entrega SUSEP - 26-09-01\Fluxo de Informacao e Reunioes SUSEP - rascunho.html"
if os.path.exists(old):
    os.makedirs(os.path.join(W, "OLD"), exist_ok=True)
    os.replace(old, os.path.join(W, "OLD", "Fluxo de Informacao e Reunioes SUSEP - rascunho (v0.1, reunioes).html"))
print("patch v3 ok")
