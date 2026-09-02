# -*- coding: utf-8 -*-
"""Varredura de palavras perigosas (tom agressivo, acusatório ou expositivo) no HTML montado. Uso: python perigosas.py"""
import io, re, sys
HTML = r"A:\_01 Projetos\Estrategia\Pesquisas\Anatomia Profunda - GT Susep Vida e RE - 26-09-01\Anatomia Profunda - GT Susep Vida e RE - 26-09-01.html"
LEX = [r"\bningu[ée]m (sabe|consegue|explica|escreveu|decide|responde)", r"\bn[ãa]o consegue[m]?\b", r"\bincompet", r"\bculpa", r"\bfalh(a|ou|am|aram)\b", r"\bfracass", r"\bdesespera", r"\bomiss", r"\bnegligen",
       r"\bdescr[ée]dito", r"\bsem saber\b", r"\bsem perceber\b", r"\bdesmistifica", r"\bconfus[ao]s?\b", r"\batropel", r"\bdisput", r"\bmedo\b", r"\breceio\b", r"\bdesabafo", r"\bmuro das lamenta",
       r"\bvil[ãa]o", r"\berr(o|ou|am|ada|ado)\b", r"\bpior\b", r"\bgargalo\b", r"\btrav(a|am|ou|ada|ado)\b", r"\besquec", r"\bignor", r"\bsumi(u|ram)\b", r"\bà força\b", r"\bexp[oõ]e", r"\bacus", r"\bexig(e|em|iu)\b",
       r"\bdeveria[m]?\b", r"\bpromet", r"\bsozinh[ao]", r"\bnão sabe[m]?\b", r"\bsem dono\b", r"\bsem regra\b", r"\bem vão\b", r"\bperd(e|em|eu|ida)\b"]
html = io.open(HTML, encoding="utf-8").read()
hits = {}
for m in re.finditer(r'<section id="p-([a-z0-9]+)" class="pane">(.*?)</section>', html, re.S):
    pid, body = m.group(1), m.group(2)
    txt = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S); txt = re.sub(r"<[^>]+>", " ", txt); txt = re.sub(r"\s+", " ", txt)
    noq = '"'.join(p for i, p in enumerate(txt.split('"')) if i % 2 == 0)
    for pat in LEX:
        for mm in re.finditer(pat, noq, re.I):
            hits.setdefault(pid, []).append((pat, noq[max(0, mm.start() - 70):mm.end() + 50].strip()))
tot = sum(len(v) for v in hits.values())
print("ocorrências fora de aspas:", tot)
for pid, v in hits.items():
    print("\n==", pid, len(v))
    for pat, ctx in v[:40]: print("  [%s] %s" % (pat, ctx))
