# -*- coding: utf-8 -*-
"""v32: restaura a conta por cima (encontros e custo por encontro e por ano) na aba Reuniões no lugar das tabelas antigas;
gancho da Estrutura logo abaixo da tese."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'; SE = '<span class="sel sel-e">Especulativo</span>'
s = load("frag_H.html")
sec = re.search(r'<section id="p-ritos" class="pane">.*?</section>', s, re.S).group(0)
def table_after(h3):
    m = re.search(r"<h3>" + re.escape(h3) + r"</h3>\s*<table>(.*?)</table>", sec, re.S); return m
def rows(t):
    out = []
    for tr in re.findall(r"<tr>(.*?)</tr>", t, re.S):
        tds = [re.sub(r"<[^>]+>", "", x).strip() for x in re.findall(r"<td>(.*?)</td>", tr, re.S)]
        if len(tds) >= 6 and tds[0] and tds[0] != "Total" and tds[1]:
            try: out.append((tds[0], float(tds[1].replace(".", "")), float(tds[2].replace(",", ".")), float(tds[3])))
            except ValueError: pass
    return out
def fmt(v): return ("{:,.0f}".format(v)).replace(",", ".")
def block(title, rs):
    tot_s = sum(r[1] for r in rs); tot_c = sum(r[1] * r[2] * r[3] * 125 for r in rs)
    body = "".join("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>R$ %s</td><td>R$ %s</td></tr>" % (n, fmt(sa), ("%.1f" % (sa / 12)).replace(".", ","), ("%g" % d).replace(".", ","), "%g" % p, fmt(d * p * 125), fmt(sa * d * p * 125)) for n, sa, d, p in rs)
    body += "<tr><td><strong>Total</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td></td><td></td><td><strong>R$ %s</strong> (média)</td><td><strong>R$ %s</strong></td></tr>" % (fmt(tot_s), fmt(tot_s / 12), fmt(tot_c / tot_s), fmt(tot_c))
    return '<h3>%s</h3>\n<table>\n<thead><tr><th>Rito</th><th>Por ano</th><th>Por mês</th><th>Duração (h)</th><th>Pessoas</th><th>Custo por encontro</th><th>Custo por ano</th></tr></thead>\n<tbody>\n%s</tbody>\n</table>\n' % (title, body), tot_s, tot_c
mp, ma = table_after("Sistema proposto"), table_after("Sistema atual (estimado a partir das atas)")
if not (mp and ma): print("MISS tabelas antigas"); raise SystemExit
prop, atual = rows(mp.group(1)), rows(ma.group(1))
b1, s1, c1 = block("Sistema proposto: quantos encontros e quanto custa cada um", prop)
b2, s2, c2 = block("Sistema atual, estimado a partir das atas", atual)
new = ('<h3>Em números: quantas reuniões e quanto custa cada uma</h3>\n<p>Conta por cima, a R$ 125 a hora: custo do encontro é duração vezes pessoas vezes valor-hora; custo do ano é o custo do encontro vezes as vezes que ele acontece. A planilha anexa recalcula com outro valor-hora.</p>\n'
       + b1 + '<p>%s encontros por ano, cerca de %s por mês; R$ %s por ano; média de R$ %s por encontro. %s</p>\n' % (fmt(s1), fmt(s1 / 12), fmt(c1), fmt(c1 / s1), SP)
       + b2 + '<p>%s encontros por ano, cerca de %s por mês; R$ %s por ano; média de R$ %s por encontro. A cadência do S&amp;OP, do Diagnóstico e do Fórum de Gestão é estimativa deste documento. %s</p>\n' % (fmt(s2), fmt(s2 / 12), fmt(c2), fmt(c2 / s2), SE))
sec2 = sec.replace(mp.group(0), "", 1).replace(ma.group(0), "", 1)
sec2 = re.sub(r"<h3>O custo da sala</h3>", "<h3>O custo da sala</h3>\n" + new, sec2, count=1)
s = s.replace(sec, sec2); save("frag_H.html", s)
print("reunioes ok:", fmt(s1), fmt(c1), fmt(s2), fmt(c2))
b = load("build.py")
old = "body = re.sub(r'<h2>(.*?)</h2>" + chr(92) + "s*(<p class=" + chr(34) + "tese" + chr(34) + ">.*?</p>)', r'<h2>Estrutura: boas regras de convivência, quase nenhuma regra de decisão</h2>' + chr(10) + r'" + chr(92) + "2' + chr(10) + r'<h3>" + chr(92) + "1</h3>', body, count=1, flags=re.S)"
if old in b:
    new_b = "body = re.sub(r'<h2>(.*?)</h2>" + chr(92) + "s*(<p class=" + chr(34) + "tese" + chr(34) + ">.*?</p>)(" + chr(92) + "s*<p class=" + chr(34) + "gancho" + chr(34) + ">.*?</p>)?', r'<h2>Estrutura: boas regras de convivência, quase nenhuma regra de decisão</h2>' + chr(10) + r'" + chr(92) + "2" + chr(92) + "3' + chr(10) + r'<h3>" + chr(92) + "1</h3>', body, count=1, flags=re.S)"
    b = b.replace(old, new_b); save("build.py", b); print("build gancho ok")
else: print("MISS build regex")
