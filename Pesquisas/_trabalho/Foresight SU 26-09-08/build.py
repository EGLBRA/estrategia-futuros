# -*- coding: utf-8 -*-
"""Monta uma Anatomia Profunda (casca .tabs/.pane da AnatomiaProfundaForesight) a partir de fragmentos.
Uso: python build.py A  |  python build.py B
- fragmentos: frag_<X>_*.html (concatenados em ordem de nome), cada um com <section id="p-xxx" class="pane">
- fontes: fontes_<X>.py define SOURCES = [(chave, html_da_fonte), ...], GRUPOS = [(titulo, [chaves])] e NOTA
- citacao no texto: <sup>{{chave,chave2}}</sup> -> links numerados
- selos: [[V]] [[I]] [[E]] [[P]] -> span por extenso
- meta: meta_<X>.py define TITLE, LBL, H1, META, TABS = [(id, rotulo)], FOOTER, OUT_HTML, OUT_MD, NCOLS
"""
import re, io, sys, glob, html, importlib, os

X = sys.argv[1]
base = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, base)
meta = importlib.import_module("meta_" + X)
fon = importlib.import_module("fontes_" + X)

CASCA = io.open(r"A:\_01 Projetos\Estrategia\AnatomiaProfundaForesight.html", encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", CASCA, re.S).group(1)
css = re.sub(r"#r-dest:checked~#p-dest[^\n]*\n", "", css)
css = re.sub(r"#r-dest:checked~\.tabs[^\n]*\n", "", css)
ncols = getattr(meta, "NCOLS", 9)
css = css.replace("grid-template-columns:repeat(9,max-content)", "grid-template-columns:repeat(%d,max-content)" % ncols)
extra_css = """
.tese{font-size:16px;font-style:italic;color:#333;margin:-4px 0 14px;padding-bottom:10px;border-bottom:1px solid #e0e0e0}
.pratica{background:#fbfaf7;border:1px solid #e8e4d8;border-radius:4px;padding:12px 16px;margin:18px 0 4px}
.pratica h3{margin-top:2px}
.pratica p{margin-bottom:8px}
.pratica p:last-child{margin-top:8px;font-weight:700}
.apex{background:#1a1a1a;color:#fff;border-radius:6px;padding:14px 18px;margin:16px 0}
.apex .lbl{color:#bbb}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0}
@media(max-width:700px){.g3{grid-template-columns:1fr}}
.sel-p{background:#efe9f7;color:#4b2a7a}
.tag{display:inline-block;font-family:system-ui,sans-serif;font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;padding:1px 7px;border-radius:3px;background:#eee;color:#444;margin-right:4px}
p{margin-bottom:10px}
"""
css = css + extra_css

tabs = meta.TABS
ids = [t[0] for t in tabs]
rule_pane = ",".join("#r-%s:checked~#p-%s" % (i, i) for i in ids) + "{display:block}"
rule_lab = ",".join("#r-%s:checked~.tabs [for=r-%s]" % (i, i) for i in ids) + "{color:#1a1a1a;border-bottom-color:#b71c1c;font-weight:700}"
css = css.replace(".pane{display:none}", ".pane{display:none}\n" + rule_pane + "\n" + rule_lab)

SOURCES = fon.SOURCES
keys = [k for k, _ in SOURCES]
num = {k: i + 1 for i, k in enumerate(keys)}
assert len(keys) == len(set(keys)), "chave de fonte duplicada"

frags = sorted(glob.glob(os.path.join(base, "frag_%s_*.html" % X)))
body = "\n".join(io.open(f, encoding="utf-8").read() for f in frags)

used = {}


def cit(m):
    ks = [k.strip() for k in m.group(1).split(",") if k.strip()]
    out = []
    for k in ks:
        if k not in num:
            raise SystemExit("FONTE DESCONHECIDA: " + k)
        used[k] = used.get(k, 0) + 1
        out.append('<a class="cit" href="#f%d">%d</a>' % (num[k], num[k]))
    return "<sup>" + ", ".join(out) + "</sup>"


body = re.sub(r"<sup>\{\{([^}]+)\}\}</sup>", cit, body)
if "{{" in body:
    i = body.find("{{")
    raise SystemExit("citacao fora de <sup>: " + body[i - 80:i + 80])
body = (body.replace("[[V]]", '<span class="sel sel-v">Verificado</span>')
            .replace("[[I]]", '<span class="sel sel-i">Inferência</span>')
            .replace("[[E]]", '<span class="sel sel-e">Especulativo</span>')
            .replace("[[P]]", '<span class="sel sel-p">Proposta</span>'))

fontes_html = ['<section id="p-fontes" class="pane">', "<h2>Fontes</h2>", fon.NOTA]
n = 1
src = dict(SOURCES)
for titulo, ks in fon.GRUPOS:
    fontes_html.append("<h3>%s</h3>" % titulo)
    fontes_html.append('<ol start="%d">' % n if n > 1 else "<ol>")
    for k in ks:
        assert num[k] == n, "ordem das fontes quebrada em %s: esperado %d, tem %d" % (k, n, num[k])
        fontes_html.append('<li id="f%d">%s</li>' % (n, src[k]))
        n += 1
    fontes_html.append("</ol>")
fontes_html.append("</section>")
assert n - 1 == len(keys), "GRUPOS nao cobre todas as fontes"
body += "\n" + "\n".join(fontes_html)

orfas = [k for k in keys if k not in used]
if orfas:
    print("AVISO fontes orfas (nao citadas):", orfas)

panes = re.findall(r'<section id="p-([^"]+)" class="pane">', body)
missing = [i for i in ids if i not in panes]
extra = [p for p in panes if p not in ids]
if missing or extra:
    raise SystemExit("abas x paineis: faltam %s, sobram %s" % (missing, extra))
for ch, nome in [("\u2014", "travessao"), ("\u2013", "en-dash"), ("\u2192", "seta"), ("\u2190", "seta"), ("\u2794", "seta"), ("\u21d2", "seta"), ("\u25ba", "seta")]:
    if ch in body:
        i = body.find(ch)
        raise SystemExit("%s encontrado: ...%s..." % (nome, body[i - 60:i + 60]))
for pat in [r"\bIA\b", r"intelig[êe]ncia artificial", r"\bagente\b", r"HackMarket", r"HackNews"]:
    for m in re.finditer(pat, body):
        ctx = body[max(0, m.start() - 70):m.end() + 70].replace("\n", " ")
        print("AVISO termo sensivel:", pat, "::", ctx)

radios = "\n".join('<input class="tabr" type="radio" name="tab" id="r-%s"%s>' % (i, " checked" if k == 0 else "") for k, i in enumerate(ids))
labels = "\n".join('<label class="tab" for="r-%s">%s</label>' % (i, lab) for i, lab in tabs)

page = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<style>%s</style>
</head>
<body>
<div class="W">
<div class="lbl">%s</div>
<h1>%s</h1>
<div class="meta">%s</div>
%s
<nav class="tabs">
%s
</nav>
%s
<footer>%s</footer>
</div>
<script>
document.addEventListener("click",function(e){
 var a=e.target.closest?e.target.closest("a.cit"):null;
 if(!a)return;
 var r=document.getElementById("r-fontes");
 if(r)r.checked=true;
});
</script>
</body>
</html>
""" % (meta.TITLE, css, meta.LBL, meta.H1, meta.META, radios, labels, body, meta.FOOTER)

os.makedirs(os.path.dirname(meta.OUT_HTML), exist_ok=True)
io.open(meta.OUT_HTML, "w", encoding="utf-8", newline="").write(page)


def md_of(s):
    s = re.sub(r"<sup>(.*?)</sup>", lambda m: " [" + re.sub(r"<[^>]+>", "", m.group(1)) + "]", s)
    s = re.sub(r'<span class="sel sel-\w">(\w+)</span>', r"[\1]", s)
    s = re.sub(r"<h2>(.*?)</h2>", r"\n## \1\n", s)
    s = re.sub(r"<h3>(.*?)</h3>", r"\n### \1\n", s)
    s = re.sub(r"<h4>(.*?)</h4>", r"\n#### \1\n", s)
    s = re.sub(r"<li[^>]*>", "- ", s)
    s = re.sub(r"</(p|li|tr|div|h\d|table|ul|ol)>", "\n", s)
    s = re.sub(r"</t[dh]>", " | ", s)
    s = re.sub(r"<(br|/?thead|/?tbody)[^>]*>", "\n", s)
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


md = "# %s\n\n%s\n\nDocumento espelho do HTML. Selos [Verificado] / [Inferência] / [Especulativo] em cada afirmação; citações entre colchetes apontam para a lista única de Fontes.\n\n%s" % (
    html.unescape(re.sub("<[^>]+>", "", meta.H1)), md_of(meta.META), md_of(body))
io.open(meta.OUT_MD, "w", encoding="utf-8", newline="").write(md)

nrad = len(re.findall(r'<input class="tabr"', page))
nlab = len(re.findall(r'<label class="tab"', page))
npan = len(re.findall(r'class="pane"', page))
print("OK %s: radios=%d labels=%d paineis=%d fontes=%d citacoes=%d bytes=%d" % (X, nrad, nlab, npan, len(keys), sum(used.values()), len(page.encode("utf-8"))))
