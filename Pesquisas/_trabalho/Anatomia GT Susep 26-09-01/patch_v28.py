# -*- coding: utf-8 -*-
"""v28: como destravar e começar pequeno: três grupos de ação na Proposta; Laços no menu."""
import io, os, re
W = r"A:\_01 Projetos\Estrategia\Pesquisas\_trabalho\Anatomia GT Susep 26-09-01"
def load(n): return io.open(os.path.join(W, n), encoding="utf-8").read()
def save(n, s): io.open(os.path.join(W, n), "w", encoding="utf-8", newline="\n").write(s)
SP = '<span class="sel sel-p">Proposta</span>'
SEC = '''
<h3>Como destravar o movimento: começar pequeno, em três grupos de ação</h3>
<p>O desenho inteiro não precisa estar pronto para o primeiro passo. As ações se separam por quem precisa autorizar: o que a Estratégia começa amanhã, o que depende de mentores e líderes, e o que só a diretoria e a TI decidem. Cada grupo anda no seu ritmo; nenhum espera o outro.</p>
<table>
<thead><tr><th>Grupo de ação</th><th>O que se faz</th><th>Quem autoriza</th><th>Primeiro passo</th></tr></thead>
<tbody>
<tr><td><strong>1. Começa amanhã, sem pedir nada</strong></td><td>Ficha única de demanda; lista dos problemas escrita pelas áreas; a planilha extensa vira fila carimbada; medir o tempo entre entrada e decisão dos itens abertos; publicar o painel com a linha de base das atas; registrar os não-ganhos.</td><td>A própria Estratégia, com a facilitação e o líder da esteira.</td><td>O primeiro encontro, só de problemas, com a parede dos 72 sintomas.</td></tr>
<tr><td><strong>2. Depende de mentores e líderes</strong></td><td>Tabela de alçadas assinada; duas esteiras com dono e indicador; uma sala de guerra por tema crítico (prestamista de prêmio único em Vida; esgotamento de comissão em RE); dedicação declarada por pessoa; agilista de melhoria contínua com tempo protegido.</td><td>Mentores e líderes de esteira, no encontro de alçadas e no de papéis.</td><td>Uma hora de mentoria por tema, com a recomendação única do prestamista na mão.</td></tr>
<tr><td><strong>3. Depende da diretoria e da TI</strong></td><td>Número-base da meta assinado e aberto por ramo; cota de TI reservada à SUSEP e critério de despriorização; orçamento de reposição de consultores; fronteira entre Fórum de Negócio e Fórum de Gestão.</td><td>Diretoria Comercial, Controladoria e diretoria de TI.</td><td>Uma página com as três decisões e o custo de cada mês de espera, levada pelo mentor.</td></tr>
</tbody>
</table>
<p>A regra do começo pequeno: um tema por esteira, uma porta, um indicador. O grupo 1 prova que o método funciona antes de pedir alçada; o grupo 2 dá alçada ao que já provou; o grupo 3 remove o que só a diretoria pode remover. Se o grupo 1 não andar em um mês, o problema é de método e se corrige nos encontros; se o grupo 3 não responder em 45 dias, o item entra no PIE como parado por falta de decisão. ''' + SP + '''</p>
'''
H = load("frag_H.html")
if "<h3>Como: criar significado antes de criar estrutura</h3>" in H:
    H = H.replace("<h3>Como: criar significado antes de criar estrutura</h3>", SEC + "<h3>Como: criar significado antes de criar estrutura</h3>", 1); print("proposta ok")
else: print("MISS proposta")
save("frag_H.html", H)
b = load("build.py"); b = b.replace('("loops", "Loops")', '("loops", "Laços")')
K = "Diagnóstico Rápido &middot; SU GT Evoluir Modelo de Negócio SUSEP Vida e RE &middot; 2026-09-01 &middot; Uso interno &middot; Material sensível"
b = re.sub(r'<p class="lbl">GT Evoluir Modelo de Negócio SUSEP Vida e RE, Seguros Unimed &middot; Diagnóstico funcional em 1º de setembro de 2026 &middot; Uso interno &middot; Material sensível</p>', '<p class="lbl">' + K + '</p>', b)
b = re.sub(r'GT Evoluir Modelo de Negócio SUSEP Vida e RE, Seguros Unimed &middot; Diagnóstico de 1º de setembro de 2026 &middot; Uso interno &middot; Material sensível: não circular fora da área de Estratégia', K + ' &middot; Não circular fora da área de Estratégia', b)
save("build.py", b); print("kicker:", K in b)
