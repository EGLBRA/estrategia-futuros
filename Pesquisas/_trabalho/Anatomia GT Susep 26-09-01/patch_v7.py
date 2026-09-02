# -*- coding: utf-8 -*-
"""v7: diagramação (abas, tese, tabelas) e limpeza de selos."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)

# ---------- build.py: CSS das abas e das tabelas; tese curta
b = load("build.py")
css = (".tabs{display:flex;flex-wrap:wrap;gap:4px 20px;justify-content:flex-start;padding-bottom:8px}\n"
       ".tab{font-size:13px}\n"
       "table{font-size:12.5px}th,td{padding:6px 8px}\n"
       ".pane h2{margin-top:6px}\n"
       ".g2 .card{font-size:13.5px}\n"
       "ol li,ul li{margin-bottom:5px}\n")
if ".tabs{display:flex" not in b:
    b = b.replace('head = head.replace("</style>", ".sel-p{', 'head = head.replace("</style>", """' + css.replace("\n", "\\n") + '""" + ".sel-p{', 1)
b = b.replace("Setenta e dois sintomas em 24 atas mostram uma frente competente operando num desenho sem alçada definida, sem braço reservado e sem porta única para os desafios. Ramos Elementares cresce apesar disso. Vida trava por causa disso. O remédio já está escrito pelo próprio grupo; falta o desenho que o sustente. Este documento reúne o diagnóstico, a visão executiva, a proposta de construir o desenho com o time e três exemplos de partida: o fluxo da estratégia à entrega, o fluxo funcional entre áreas e o sistema de reuniões com custo.",
              "Setenta e dois sintomas em 24 atas mostram uma frente competente operando sem alçada definida, sem braço reservado e sem porta única para os desafios. O diagnóstico, a proposta de construir o desenho com o time e três exemplos de partida.")
save("build.py", b)

frags = {k: load(f"frag_{k}.html") for k in "ABCDEFGH"}

# ---------- tabela etapa a etapa (linear): 8 -> 6 colunas
G = frags["G"]
G = G.replace("<thead><tr><th>Etapa</th><th>Pergunta que responde</th><th>Entra</th><th>Rito ou fórum</th><th>Sai (artefato)</th><th>Alçada</th><th>Duração</th><th>Critério para a próxima</th></tr></thead>",
              "<thead><tr><th>Etapa e pergunta</th><th>Entra</th><th>Rito e duração</th><th>Sai (artefato)</th><th>Alçada</th><th>Critério para a próxima</th></tr></thead>")
def merge_row(m):
    cells = re.findall(r"<td>(.*?)</td>", m.group(0), re.S)
    if len(cells) != 8: return m.group(0)
    etapa, perg, entra, rito, sai, alc, dur, crit = cells
    return f"<tr><td>{etapa}<br><em>{perg}</em></td><td>{entra}</td><td>{rito}<br><em>{dur}</em></td><td>{sai}</td><td>{alc}</td><td>{crit}</td></tr>"
sec = re.search(r'<h3>Etapa a etapa: o que entra, o que sai, quem aprova, quanto dura</h3>\s*<table>.*?</table>', G, re.S).group(0)
G = G.replace(sec, re.sub(r"<tr><td>.*?</td></tr>", merge_row, sec, flags=re.S))
frags["G"] = G

# ---------- tabela de ritos (ritos): ciclo + duração numa coluna
H = frags["H"]
H = H.replace("<thead><tr><th>Rito</th><th>Camada</th><th>Ciclo</th><th>Duração</th><th>Dono da pauta</th><th>Entra</th><th>Sai</th><th>Origem</th></tr></thead>",
              "<thead><tr><th>Rito</th><th>Camada</th><th>Ciclo e duração</th><th>Dono da pauta</th><th>Entra</th><th>Sai</th><th>Origem</th></tr></thead>")
def merge_rito(m):
    cells = re.findall(r"<td>(.*?)</td>", m.group(0), re.S)
    if len(cells) != 8: return m.group(0)
    r, cam, cic, dur, dono, ent, sai, org = cells
    return f"<tr><td>{r}</td><td>{cam}</td><td>{cic}, {dur}</td><td>{dono}</td><td>{ent}</td><td>{sai}</td><td>{org}</td></tr>"
sec = re.search(r'<h3>Os ritos propostos</h3>\s*<table>.*?</table>', H, re.S).group(0)
H = H.replace(sec, re.sub(r"<tr><td>.*?</td></tr>", merge_rito, sec, flags=re.S))
frags["H"] = H

# ---------- selos: sempre no fim, sem restos
SEL = r'<span class="sel sel-[vipe]">[^<]+</span>'
def clean_selos(html):
    # "Verificado o fato; a leitura de ausência de alçada é Proposta." -> "Verificado"
    html = re.sub(r'(' + SEL + r')\s+o fato; a leitura de ausência de alçada é\s*' + SEL + r'\s*\.', r'\1', html)
    # "Verificado a proposta" / "Verificado nos registros" / "Proposta no custo;" etc: remove qualificador curto sem letra maiúscula, até ponto, ponto e vírgula ou fim de tag
    html = re.sub(r'(' + SEL + r')\s+(?:a|o|as|os|na|no|nas|nos|em|sobre|quanto)\b[^<.;]{0,90}?(?=[.;<])', r'\1', html)
    # "; a leitura é <selo>" / "; o encadeamento é <selo>" -> " <selo>"
    html = re.sub(r';\s*(?:a|o)\s+[^<;.]{2,60}?\s+é\s+(' + SEL + r')', r' \1', html)
    # ponto ou ";" logo após selo
    html = re.sub(r'(' + SEL + r')\s*[.;]', r'\1', html)
    # selos duplicados consecutivos
    html = re.sub(r'(' + SEL + r')(\s*' + SEL + r')+', r'\1', html)
    return html
for k in frags: frags[k] = clean_selos(frags[k])
for k, s in frags.items(): save(f"frag_{k}.html", s)
print("patch v7 ok")
