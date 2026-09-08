# -*- coding: utf-8 -*-
# Fontes da Anatomia B (A visão contrária). Ordem = numeracao.
from fontes_A import SOURCES as A_SOURCES

def L(u, t=None):
    return '<a href="%s">%s</a>' % (u, t or u.replace("https://", "").replace("http://", "").split("/")[0])

A = dict(A_SOURCES)

NOTA = """<div class="card">
<p><strong>Nota de método.</strong> Este documento defende a tese contrária à do plano de instalação da função de futuros e usa, de propósito, as mesmas fontes internas e regulatórias daquele documento, para que a divergência esteja na leitura e não no dado. <span class="sel sel-v">Verificado</span> indica afirmação apoiada em documento publicado e identificado, acessado em 8 de setembro de 2026 salvo indicação. <span class="sel sel-i">Inferência</span> indica raciocínio sobre fontes verificadas sem afirmação direta nelas; toda a tese e todo o desenho alternativo estão nesta categoria. <span class="sel sel-e">Especulativo</span> indica hipótese sem base direta. <span class="sel sel-p">Proposta</span> marca desenho a validar.</p>
<p><strong>Sobre as fontes internas.</strong> As atas do grupo de trabalho SUSEP Vida e Ramos Elementares são citadas pelo documento interno que as consolidou, por função e em tom de diagnóstico. O que aqui se chama de "gargalo de decisão" é leitura deste documento sobre aquele material, não conclusão dele.</p>
<p><strong>Sobre a evidência acadêmica.</strong> Os estudos de previsão e de capacidade de absorção são citados nos seus resultados principais; os limites de cada um estão declarados no texto e na aba Check.</p>
</div>"""

SOURCES = [
 # A. Seguros Unimed e documentos do projeto
 ("su_rs2025", A["su_rs2025"]),
 ("su_c666", A["su_c666"]),
 ("su_result", A["su_result"]),
 ("su_sobre", A["su_sobre"]),
 ("gt_susep", A["gt_susep"]),
 ("anat1", A["anat1"]),
 ("plano", 'Projeto Estratégia (documento irmão). <em>A Anatomia Profunda: Foresight na Seguros Unimed, o plano</em>, 8 de setembro de 2026, 50 fontes: a proposta de célula de duas pessoas, cinco encaixes no calendário, carteira de opções e custo de cerca de R$ 715 mil no ano 1. Mesma pasta deste documento.'),
 ("ampla", A["ampla"]),
 ("exame_unimed", A["exame_unimed"]),
 # B. Regulacao e demografia
 ("susep_plano", A["susep_plano"]),
 ("ans_agenda", A["ans_agenda"]),
 ("lei15040", A["lei15040"]),
 ("lc213", A["lc213"]),
 ("orsa", A["orsa"]),
 ("seg388", A["seg388"]),
 ("ans_cbr", A["ans_cbr"]),
 ("ibge", A["ibge"]),
 ("iess", A["iess"]),
 ("cnseg_pdms", A["cnseg_pdms"]),
 # C. Radar pronto e precedentes
 ("axa", A["axa"]),
 ("sonar", A["sonar"]),
 ("sicredi", A["sicredi"]),
 ("ftsg", A["ftsg"]),
 ("facunimed", A["facunimed"]),
 # D. A ciencia da previsao e da decisao
 ("tetlock", 'Good Judgment. <em>The Superforecasters\' Track Record</em>: no torneio de previsão da IARPA, o projeto liderado por Philip Tetlock e Barbara Mellers na Universidade da Pensilvânia foi mais de 30% mais preciso que analistas de inteligência com acesso a informação sigilosa; os melhores previsores amadores receberam o nome de superprevisores. ' + L("https://goodjudgment.com/resources/the-superforecasters-track-record/", "goodjudgment.com")),
 ("bain", A["bain"]),
 ("rohrbeck", A["rohrbeck"]),
 ("klein", A["klein"]),
 ("cohen", 'Cohen, W. M.; Levinthal, D. A. <em>Absorptive Capacity: A New Perspective on Learning and Innovation</em>. Administrative Science Quarterly, v. 35, n. 1, 1990, p. 128-152: a capacidade de uma organização reconhecer o valor de informação nova, assimilá-la e aplicá-la depende do conhecimento prévio relacionado e é cumulativa. ' + L("https://www.jstor.org/stable/2393553", "jstor.org")),
 ("luehrman", 'Luehrman, T. A. <em>Strategy as a Portfolio of Real Options</em>. Harvard Business Review, setembro e outubro de 1998: a estratégia como sequência de opções que se compram, se mantêm ou se abandonam conforme a incerteza se resolve. ' + L("https://hbr.org/1998/09/strategy-as-a-portfolio-of-real-options", "hbr.org")),
 ("rand", 'Lempert, R. J.; Popper, S. W.; Bankes, S. C. <em>Shaping the Next One Hundred Years: New Methods for Quantitative, Long-Term Policy Analysis</em>. RAND, 2003 (MR-1626): decisões robustas, que se saem razoavelmente bem em muitos futuros, em vez de decisões ótimas para um futuro previsto. ' + L("https://www.rand.org/pubs/monograph_reports/MR1626.html", "rand.org")),
 ("scoblic", A["scoblic"]),
]

GRUPOS = [
 ("A Seguros Unimed, o Sistema e os documentos do projeto", ["su_rs2025","su_c666","su_result","su_sobre","gt_susep","anat1","plano","ampla","exame_unimed"]),
 ("Regulação e demografia: o futuro que já tem data", ["susep_plano","ans_agenda","lei15040","lc213","orsa","seg388","ans_cbr","ibge","iess","cnseg_pdms"]),
 ("O radar pronto e os precedentes", ["axa","sonar","sicredi","ftsg","facunimed"]),
 ("A ciência da previsão e da decisão", ["tetlock","bain","rohrbeck","klein","cohen","luehrman","rand","scoblic"]),
]
