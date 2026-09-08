# -*- coding: utf-8 -*-
"""QA de forma e de voz sobre o HTML gerado. Uso: python qa.py <caminho.html>"""
import re, io, sys, html, collections

p = sys.argv[1]
h = io.open(p, encoding="utf-8").read()
body = re.search(r"<body>(.*)</body>", h, re.S).group(1)
vis = re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S)
vis = html.unescape(re.sub(r"<[^>]+>", " ", vis))

# 1. travessao / setas
for ch, nome in [("—", "travessao"), ("–", "en-dash"), ("→", "seta"), ("►", "seta")]:
    print(nome, vis.count(ch))

# 2. palavras sem acento (armadilhas)
arm = ["nao", "numero", "orgao", "decisao", "previdencia", "voce", "publico", "confianca", "relacao", "proprio", "gestao", "servico", "adesao", "tambem", "inferencia", "consequencia", "atencao", "saude", "medico", "estrategia", "cenario", "cenarios", "orcamento", "tres", "mes", "ja", "so", "ate", "apos", "analise", "codigo", "politica", "economica", "juridico", "tecnologica", "demografica", "etica", "logica", "pratica", "historico", "periodo", "minimo", "maximo", "unico", "unica", "proxima", "proximo", "necessario", "obrigatorio", "obrigatoria", "regulatorio", "regulatoria", "atuaria", "atuario", "diretoria", "matriz", "premio", "premios", "beneficiario", "beneficiarios", "cooperativa", "referencia", "experiencia", "ciencia", "conselheiro", "conteudo", "residencia", "possivel", "possiveis", "responsavel", "variavel", "nivel", "disponivel", "sustentavel", "familia", "area", "areas", "media", "credito", "debito", "titulo", "capitulo", "artigo"]
words = re.findall(r"[A-Za-zÀ-ÿ]+", vis)
low = collections.Counter(w.lower() for w in words)
bad = {w: low[w] for w in arm if low.get(w)}
# 'so', 'ja', 'ate', 'apos', 'mes', 'tres', 'area', 'media', 'matriz', 'diretoria' sao ambiguos; listar so os claros
claros = {k: v for k, v in bad.items() if k not in ("so", "ja", "ate", "apos", "mes", "tres", "area", "areas", "media", "matriz", "diretoria", "artigo", "codigo")}
print("sem acento (claros):", claros)
print("sem acento (ambiguos):", {k: v for k, v in bad.items() if k not in claros})

# 3. anglicismos fora de aspas
ang = ["discovery", "squad", "BAU", "assessment", "backlog", "checklist", "kick-off", "kickoff", "churn", "cross-sell", "front-end", "lead time", "onboarding", "scrum", "dashboard", "roadmap", "sprint", "insight", "stakeholder", "compliance", "feedback", "mindset", "workshop", "briefing", "deadline", "budget", "core", "know-how", "framework", "gap", "trade-off", "player", "driver", "expertise", "report", "outlook", "toolkit", "hub", "sandbox", "open insurance", "benchmark"]
for a in ang:
    n = len(re.findall(r"(?i)\b" + re.escape(a) + r"s?\b", vis))
    if n:
        print("anglicismo:", a, n)

# 4. menções sensíveis
for pat in [r"\bIA\b", r"intelig[êe]ncia artificial", r"\bagente\b", r"HackMarket", r"HackNews", r"\bskill\b"]:
    n = len(re.findall(pat, vis))
    if n:
        print("sensivel:", pat, n)

# 5. selos: paragrafos com numero mas sem selo (amostra)
secs = re.findall(r'<section id="p-([^"]+)" class="pane">(.*?)</section>', body, re.S)
for sid, s in secs:
    t = html.unescape(re.sub(r"<[^>]+>", " ", s))
    n_sel = len(re.findall(r"Verificado|Inferência|Especulativo|Proposta", t))
    n_cit = len(re.findall(r'class="cit"', s))
    w = len(re.findall(r"\w+", t))
    print("%-10s palavras=%5d selos=%3d citacoes=%3d" % (sid, w, n_sel, n_cit))
print("total palavras:", len(re.findall(r"\w+", vis)))
