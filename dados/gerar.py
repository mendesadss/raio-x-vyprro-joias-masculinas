# -*- coding: utf-8 -*-
"""Gerador das páginas de loja do raio-x Vyprro / joias masculinas."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
dados = json.load(open(os.path.join(BASE, 'dados-brutos.json'), encoding='utf-8'))
reviews = json.load(open(os.path.join(BASE, 'reviews.json'), encoding='utf-8'))
try:
    trafego = json.load(open(os.path.join(BASE, 'trafego-similarweb.json'), encoding='utf-8'))
except Exception:
    trafego = {}

NAV = """<nav class="nav"><div class="wrap">
<a href="index.html" class="home{on_index}">◆ Painel</a>
<a href="estrategia.html"{on_estrategia}>★ Estratégia</a>
<a href="plano-de-acao.html"{on_plano}>🎯 Plano de Ação</a>
<a href="mercados.html"{on_mercados}>🌍 Mercados</a>
<a href="loja-vyprro.html"{on_vyprro}>Vyprro (referência)</a>
<a href="loja-luxujewelry.html"{on_luxujewelry}>Luxujewelry</a>
<a href="loja-storeedyta.html"{on_storeedyta}>Ed&amp;Ta / Storeedyta</a>
<a href="loja-alfredco.html"{on_alfredco}>Alfred &amp; Co. London</a>
<a href="loja-humbler.html"{on_humbler}>Humbler</a>
</div></nav>"""


def nav(active):
    keys = ['index', 'estrategia', 'plano', 'mercados', 'vyprro', 'luxujewelry', 'storeedyta', 'alfredco', 'humbler']
    kw = {}
    for k in keys:
        kw[f'on_{k}'] = ' class="on"' if k == active and k != 'index' else ('' if k != 'index' else '')
    if active == 'index':
        kw['on_index'] = ' on'
    else:
        kw['on_index'] = ''
    return NAV.format(**kw)


def head(title):
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Raio-X</title><link rel="stylesheet" href="estilo.css"></head><body>
"""


FOOT = """<footer><div class="wrap"><p><a href="index.html">← Voltar ao painel</a></p>
<p style="margin-top:12px">Meta Ad Library (3 chamadas/página: ACTIVE, ALL, amostra 50) · catálogo público Shopify · Tranco · Wayback · SimilarWeb · Judge.me/JSON-LD · Playwright. Mídia paga recoletada em 27 de julho de 2026.</p></div></footer>
</body></html>"""


def money(v):
    s = f"{v:,.2f}"
    intpart, dec = s.split('.')
    intpart = intpart.replace(',', '.')
    return f"${intpart},{dec}"


# ---------------------------------------------------------------- análise por loja
ANALISE = {
    'luxujewelry': {
        'nome': 'Luxujewelry', 'dominio': 'luxujewelry.shop', 'slug': 'luxujewelry',
        'page_id': '108930165625357', 'moeda': 'USD',
        'ativos': 212, 'historico': 2451,
        'unicos_amostra': 4, 'duplicacao': '12,5x', 'janela_dias': 3.29,
        'anuncios_dia': 15.2, 'unicos_semana': 8.5,
        'campeao_ad': '"Natural Tiger\'s Eye Bracelet For Men" (dezenas de cópias, maior volume da amostra)',
        'mix_formato': 'Imagem estática de produto isolado (fundo branco/estúdio), copy mínima — o próprio nome do produto é o hook ("Premium Leather Bracelet For Men"). Sofisticação nível 1 (produção quase nula).',
        'produto_campeao': {'titulo': 'Premium Leather Bracelet For Men', 'preco': 39.90, 'de': None},
        'top_produtos': [
            ('Aurelio Ruby Cuban Chain | 18K Gold Plated 316L Stainless Steel', 39.00),
            ('Premium Leather Bracelet For Men', 39.90),
            ('Natural Tiger\'s Eye Stone Bracelet', 39.90),
            ('Round Tiger\'s Eye Bracelet', 98.00),
            ('Trendy Tiger\'s Eye Bracelet', 89.00),
            ('Chunky Cuban Chain | Silver & Gold, 8mm & 12mm', 39.00),
            ('Natural Agarwood Jade Bracelet', 199.00),
            ('Romantic Agate Bracelet', 136.00),
        ],
        'anatomia': {
            'big_idea': 'Pedra natural (tiger\'s eye) e couro como marcador masculino discreto de status — "proteção/confiança" da pedra, sem apelo espiritual explícito.',
            'mecanismo': 'Nome do produto = o próprio anúncio. Sem storytelling, sem urgência, sem gatilho de escassez — a oferta é o produto em si, testado em volume industrial.',
            'hook': '"Natural Tiger\'s Eye Bracelet For Men" e "Premium Leather Bracelet For Men" repetidos em dezenas de variações de imagem/público.',
            'presell': 'PDP de catálogo padrão Shopify, foto de produto, sem página de vendas dedicada.',
            'objecao': '"É pedra de verdade ou resina pintada?" — a palavra "Natural" no próprio título do anúncio responde a isso antes do clique.',
        },
        'modelo': 'DROPSHIP PURO', 'modelo_pill': 'p-a',
        'veredito': 'MODELAR', 'veredito_pill': 'p-a',
        'nivel': 'MÉDIO', 'nivel_pill': 'p-b', 'scorecard_soma': 8,
        'defensabilidade': 'ARBITRAGEM', 'defensabilidade_pill': 'p-c',
        'momentum': 'ESCALANDO', 'momentum_pill': 'p-a',
        'scorecard': [
            ('Sourcing simples', 2, 'pedra/couro/aço genérico, disponível em qualquer fornecedor de AliExpress'),
            ('Ticket fecha sem escada', 1, 'ticket baixo ($42 mediano) puxado por dezenas de SKUs de $29-49, precisa de bundle pra AOV subir'),
            ('Criativo simples de produzir', 2, 'foto de produto isolado, zero produção'),
            ('Mecanismo com urgência', 0, 'nenhum gatilho de urgência/escassez identificado nos criativos amostrados'),
            ('Investimento de entrada baixo', 2, 'catálogo simples, sem necessidade de tooling caro'),
            ('Sem dependência de autoridade', 1, 'volume de teste (212 ativos) sugere operação grande, não replicável no primeiro mês por quem está começando'),
        ],
    },
    'storeedyta': {
        'nome': 'Ed&amp;Ta (Storeedyta)', 'dominio': 'storeedyta.com', 'slug': 'storeedyta',
        'page_id': '157335390804963', 'moeda': 'USD',
        'ativos': 19, 'historico': 19,
        'unicos_amostra': 8, 'duplicacao': '2,4x', 'janela_dias': 106.5,
        'anuncios_dia': 0.18, 'unicos_semana': 0.53,
        'campeao_ad': '"Real 316L Steel. Not a Knockoff" + linha de necklaces mitológicas (Celtic Cross, Archangel Michael, Thor\'s Hammer)',
        'mix_formato': 'Foto de produto em still + selo de material ("316L Stainless Steel") no próprio título. Sofisticação nível 1-2.',
        'produto_campeao': {'titulo': 'Celtic Cross Necklace for Men – 316L Stainless Steel | Irish Knotwork Pendant', 'preco': 45.99, 'de': None},
        'top_produtos': [
            ('Celtic Cross Necklace for Men – 316L Stainless Steel', 45.99),
            ('Yggdrasil Necklace with helm of awe', 45.99),
            ('Archangel Michael Shield Necklace for Men', 45.99),
            ('Archangel Michael Necklace – Sword & Wings', 45.99),
            ('Valknut Necklace – Norse Odin Symbol', 42.99),
            ('Thor\'s Hammer Mjolnir Necklace', 49.99),
            ('Celtic Trinity Knot Necklace', 39.99),
            ('Spartan Helmet Necklace', 45.99),
        ],
        'anatomia': {
            'big_idea': 'Identidade masculina via mitologia/herança (viking, celta, cristã, espartana) — a joia é símbolo de tribo/crença, não acessório de moda.',
            'mecanismo': 'Combate direto à objeção de qualidade do dropship genérico: "Real 316L Steel. Not a Knockoff" e "Packed by hand right in Miami" (operação com endereço/rosto real, não anônima).',
            'hook': '"Real 316L Steel. Not a Knockoff" e nomes de produto que já entregam a mitologia (Thor\'s Hammer, Archangel Michael, Celtic Cross).',
            'presell': 'PDP direta por produto/símbolo, sem funil de vendas elaborado; a venda é a identidade do símbolo escolhido.',
            'objecao': '"É bijuteria chinesa que enverdece?" — respondida com prova de material (316L) e origem (Miami) no próprio anúncio.',
        },
        'modelo': 'DROPSHIP DE MARCA', 'modelo_pill': 'p-a', 'modelo_estrela': True,
        'veredito': 'MODELAR', 'veredito_pill': 'p-a',
        'nivel': 'INICIANTE', 'nivel_pill': 'p-a', 'scorecard_soma': 10,
        'defensabilidade': 'CONSTRUÍVEL', 'defensabilidade_pill': 'p-a',
        'momentum': 'CRESCENDO', 'momentum_pill': 'p-a',
        'scorecard': [
            ('Sourcing simples', 2, 'aço inoxidável 316L com símbolo estampado, item padrão de fornecedor'),
            ('Ticket fecha sem escada', 2, 'ticket $35-46 já é o preço final, sem precisar de bundle'),
            ('Criativo simples de produzir', 2, 'foto still + selo de texto, produção mínima'),
            ('Mecanismo com urgência', 1, 'sem countdown/BOGO, mas a identidade do símbolo cria desejo específico (não é substituível por qualquer bracelete)'),
            ('Investimento de entrada baixo', 2, 'só 19 anúncios ativos: operação pequena e replicável, orçamento de teste baixo'),
            ('Sem dependência de autoridade', 1, 'presença social real (IG/TikTok/YouTube/Pinterest) ajuda, mas não é obrigatória pra replicar'),
        ],
    },
    'alfredco': {
        'nome': 'Alfred &amp; Co. London', 'dominio': 'alfredco.com', 'slug': 'alfredco',
        'page_id': '483344995061454', 'moeda': 'GBP',
        'ativos': 26, 'historico': 1422,
        'unicos_amostra': 8, 'duplicacao': '3,25x', 'janela_dias': 68.5,
        'anuncios_dia': 0.38, 'unicos_semana': 0.82,
        'campeao_ad': '"Designed To Be Worn Every Day!" / "★★★★★" (prova social)',
        'mix_formato': 'Não inspecionado visualmente (site bloqueado por Cloudflare para captura); pelo título dos anúncios, foco em "everyday wear" e prova social por estrelas.',
        'produto_campeao': None,
        'top_produtos': [],
        'anatomia': {
            'big_idea': '"Refined simplicity" — joia de prata de verdade (com selo de contraste do Goldsmith\'s Assay Office de Londres), não bijuteria disfarçada de luxo.',
            'mecanismo': 'Autenticidade material (prata 925 com selo oficial) como diferencial contra concorrência de aço inoxidável banhado.',
            'hook': '"Designed To Be Worn Every Day!" e avaliação por estrelas.',
            'presell': 'Não verificável (Cloudflare bloqueou a captura de página).',
            'objecao': 'Provavelmente preço vs. percepção de valor (prata de verdade custa mais que aço banhado) — não confirmado.',
        },
        'modelo': 'MARCA', 'modelo_pill': 'p-b',
        'veredito': 'OBSERVAR', 'veredito_pill': 'p-b',
        'nivel': '—', 'nivel_pill': 'p-n', 'scorecard_soma': None,
        'defensabilidade': 'CONSTRUÍVEL', 'defensabilidade_pill': 'p-a',
        'momentum': 'SINAIS DIVERGENTES', 'momentum_pill': 'p-i',
        'momentum_nota': 'Tranco (rank de domínio, 42 dias): piorou de 1.163.942 para 1.201.457 (caindo). SimilarWeb (rank de tráfego, 3 meses): melhorou de 738.951 para 675.083 (subindo). As duas fontes medem tráfego por métodos diferentes e divergem aqui — não force uma conclusão única: o dado real é 52,6 mil visitas/mês agora, com histórico recente de melhora pelo SimilarWeb mas piora pelo Tranco.',
        'scorecard': [],
    },
    'humbler': {
        'nome': 'Humbler', 'dominio': 'humbler.com', 'slug': 'humbler',
        'page_id': '104492180983999', 'moeda': 'USD',
        'ativos': 238, 'historico': 1728,
        'unicos_amostra': 2, 'duplicacao': '25x', 'janela_dias': 8.03,
        'anuncios_dia': 6.23, 'unicos_semana': 1.74,
        'campeao_ad': '"Your Daily Reminder is Now 30% Off." (dezenas de cópias, praticamente todo o volume ativo)',
        'mix_formato': 'Um único criativo de resposta direta escalado em massa + um criativo antigo de prova social ("Humbler™ - ⭐⭐⭐⭐⭐"). Sofisticação nível 1-2.',
        'produto_campeao': {'titulo': "Hard Work & God's Work Double Sided Pendant", 'preco': 75.00, 'de': None},
        'top_produtos': [
            ("Hard Work & God's Work Double Sided Pendant", 75.00),
            ('St. Michael Double Sided Pendant', 75.00),
            ('Death Smile Memento Mori Coin Pendant', 75.00),
            ('Essential Cross Pendant', 75.00),
            ('Icarus Double Sided Pendant', 75.00),
            ('Spartan Skull Veni Vidi Vici Coin Pendant', 75.00),
            ('Cuban 8mm Set', 94.00),
            ('Perseus vs. Medusa Coin Pendant', 75.00),
        ],
        'anatomia': {
            'big_idea': 'Pingente de mitologia/filosofia como "lembrete diário" de disciplina masculina (stoicismo, fé, memento mori) — a joia é mantra, não moda.',
            'mecanismo': 'Um único ângulo vencedor ("Your Daily Reminder") escalado em dezenas de cópias em vez de testar criativos novos — sofisticação de mídia madura, não de produto.',
            'hook': '"Your Daily Reminder is Now 30% Off."',
            'presell': 'Catálogo de pingentes de dupla face (Perseus vs Medusa, David vs Golias) — a narrativa mitológica está no próprio produto.',
            'objecao': 'Preço ($55-94) vs. bijuteria genérica — sustentado por 1.116 reviews declarados na home (não verificados) e stack de prova social (Judge.me).',
        },
        'modelo': 'DROPSHIP DE MARCA', 'modelo_pill': 'p-a', 'modelo_estrela': True,
        'veredito': 'MODELAR', 'veredito_pill': 'p-a',
        'nivel': 'AVANÇADO', 'nivel_pill': 'p-c', 'scorecard_soma': 5,
        'defensabilidade': 'CONSTRUÍVEL', 'defensabilidade_pill': 'p-a',
        'momentum': 'ESCALANDO', 'momentum_pill': 'p-a',
        'scorecard': [
            ('Sourcing simples', 1, 'pingente double-sided é mais complexo de fabricar que bracelete simples'),
            ('Ticket fecha sem escada', 2, 'ticket $55-94 já fecha sozinho, sem precisar de bundle'),
            ('Criativo simples de produzir', 0, 'catálogo de 108 SKUs com narrativa mitológica exige curadoria de conceito, não é "sobe foto e testa"'),
            ('Mecanismo com urgência', 1, 'desconto recorrente (30% off), mas sem escassez real'),
            ('Investimento de entrada baixo', 0, 'stack de Klaviyo + Postscript + Triple Whale + Gorgias é operação madura, não ponto de partida'),
            ('Sem dependência de autoridade', 1, 'marca com 7 anos de catálogo (produto mais antigo 2019) e 1.116 reviews alegados — vantagem de tempo de mercado que um iniciante não tem'),
        ],
    },
}


def bloco_midia(slug, a, d, r, t):
    sobrev = round(100 * a['ativos'] / a['historico'], 1) if a['historico'] else None
    out = []
    out.append(f'<h2><span class="n">02</span>Mídia paga</h2>')
    out.append('<div class="grid g4">')
    out.append(f'<div class="stat"><div class="v">{a["ativos"]}</div><div class="l">anúncios ativos hoje</div></div>')
    out.append(f'<div class="stat"><div class="v sm">{a["historico"]}</div><div class="l">histórico total</div></div>')
    if sobrev is not None:
        out.append(f'<div class="stat"><div class="v">{sobrev}%</div><div class="l">sobrevivência</div><div class="bar"><i style="width:{min(sobrev,100)}%"></i></div></div>')
    else:
        out.append('<div class="stat"><div class="v sm">—</div><div class="l">sobrevivência</div></div>')
    out.append(f'<div class="stat"><div class="v sm">{a["moeda"]}</div><div class="l">moeda de veiculação</div></div>')
    out.append('</div>')

    out.append('<h3>Ritmo de teste de criativo</h3>')
    if a['unicos_amostra']:
        out.append('<div class="tblwrap"><table><tbody>')
        out.append(f'<tr><td>Criativos únicos <span style="color:var(--dim2)">(amostra de 50 mais recentes)</span></td><td class="num"><b>{a["unicos_amostra"]}</b></td></tr>')
        out.append(f'<tr><td>Fator de duplicação</td><td class="num">{a["duplicacao"]} <span style="color:var(--dim2)">(mesmo criativo repetido)</span></td></tr>')
        if a['anuncios_dia']:
            nota = ' (rajada, não extrapolar)' if a['janela_dias'] and a['janela_dias'] < 0.5 else ''
            out.append(f'<tr><td>Anúncios por dia</td><td class="num">{a["anuncios_dia"]}/dia{nota}</td></tr>')
        if a['unicos_semana']:
            out.append(f'<tr><td>Criativos únicos por semana</td><td class="num"><b>{a["unicos_semana"]}</b></td></tr>')
        if a['janela_dias']:
            out.append(f'<tr><td>Janela da amostra</td><td class="num">{a["janela_dias"]} dias</td></tr>')
        out.append('</tbody></table></div>')
    else:
        out.append('<div class="note">Amostra insuficiente para cadência (menos de 20 anúncios no histórico total).</div>')

    out.append(f'<h3>Ranking de criativos vencedores <span class="pill p-a">modele</span></h3>')
    out.append(f'<div class="note"><b>Criativo campeão:</b> {a["campeao_ad"]}</div>')
    out.append(f'<div class="tblwrap"><table><tbody><tr><td style="white-space:nowrap;color:var(--acc);font-weight:600">Mix de formato e sofisticação</td><td>{a["mix_formato"]}</td></tr></tbody></table></div>')
    out.append(f'<div class="toplinks"><a class="adlib" href="https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id={a["page_id"]}" target="_blank">📓 Modele os criativos desta loja · biblioteca aberta ↗</a></div>')

    tr = t.get(a['dominio'])
    out.append('<h3>Tráfego real (SimilarWeb)</h3>')
    if tr and tr.get('status') == 'OK':
        out.append('<div class="grid g4">')
        out.append(f'<div class="stat"><div class="v sm">{tr["visitas"]}</div><div class="l">visitas/mês</div><div class="d">piso da versão pública, não precisão exata</div></div>')
        out.append(f'<div class="stat"><div class="v sm">{tr["bounce"]}</div><div class="l">taxa de rejeição</div><div class="d">{tr.get("pagesPerVisit","—")} págs/visita</div></div>')
        out.append('</div>')
        paises = ', '.join(f'{p["pais"]} {p["pct"]}' for p in tr.get('paises', []))
        out.append(f'<p style="color:var(--dim2);font-size:13px;margin-top:10px">Origem do tráfego: {paises}.</p>')
    else:
        out.append('<div class="note danger"><b>Dado não obtido.</b> SimilarWeb público não retornou (site protegido por Cloudflare / sem dados suficientes). Não invento número — ver seção de dados não obtidos.</div>')
    return '\n'.join(out), tr, sobrev


def bloco_financeiro(slug, a, tr):
    out = []
    out.append('<h3>Faturamento mensal estimado</h3>')
    if tr and tr.get('status') == 'OK':
        conv_setor = 0.0170
        bounce = float(tr['bounce'].replace('%', '')) if tr.get('bounce') else None
        ajuste = 0.70 if (bounce and bounce > 60) else (1.25 if (bounce and bounce < 45) else 1.00)
        conv = conv_setor * ajuste
        ticket_setor_usd = 108.0
        med = ANALISE[slug].get('_ticket_mediano', 40)
        ticket = max(med, 0.75 * ticket_setor_usd)
        vtxt = tr['visitas'].upper().replace(',', '.')
        mult = 1000 if 'K' in vtxt else (1000000 if 'M' in vtxt else 1)
        visitas_num = float(vtxt.replace('K', '').replace('M', '')) * mult
        if tr['visitas'] == '20K':
            # piso de exibicao da ferramenta gratuita: e categoria, nao medicao fina
            visitas_baixo, visitas_alto = 10000, 30000
        else:
            visitas_baixo, visitas_alto = round(visitas_num * 0.75), round(visitas_num * 1.25)
        ped_baixo = round(visitas_baixo * conv)
        ped_alto = round(visitas_alto * conv)
        fat_baixo = ped_baixo * ticket
        fat_alto = ped_alto * ticket
        fat_centro = (fat_baixo + fat_alto) / 2
        out.append('<div class="grid g4">')
        out.append(f'<div class="stat"><div class="v sm">{money(fat_baixo)} a {money(fat_alto)}</div><div class="l">receita bruta/mês</div><div class="d">SimilarWeb (piso) + triangulado</div></div>')
        out.append(f'<div class="stat"><div class="v sm">~{money(fat_centro)}</div><div class="l">cenário central</div><div class="d">receita, não lucro</div></div>')
        out.append('</div>')
        nota_visitas = (f'o "{tr["visitas"]}" do SimilarWeb público é o piso de exibição da ferramenta gratuita para lojas pequenas, não precisão exata — ordem de grandeza declarada, não medição fina'
                        if tr['visitas'] == '20K' else
                        f'{tr["visitas"]} medido pelo SimilarWeb, com margem de ±25% pela imprecisão inerente da ferramenta pública')
        out.append(f'<div class="note"><b>Como cheguei nesse número.</b> Visitas na faixa de {visitas_baixo/1000:.1f}K a {visitas_alto/1000:.1f}K/mês ({nota_visitas}) × conversão de {conv*100:.2f}% (benchmark do setor Fashion/Acessórios do IRP Commerce, {conv_setor*100:.2f}%, ajustada por {ajuste}x pelo bounce de {tr["bounce"]}) × ticket de <b>{money(ticket)}</b> (maior entre a mediana do catálogo e 75% do ticket do setor, £85,58 ≈ US$108) = faixa acima.</div>')
        out.append('<span class="pill p-b" style="margin-top:6px;display:inline-block">triangulado</span>')
    else:
        out.append('<div class="note danger"><b>Não estimado.</b> Sem tráfego real (SimilarWeb bloqueado) e sem contagem verificada de reviews suficiente para triangular. Estimar só pelo proxy de volume de anúncio erra até 2-9x (lição registrada na própria skill) — prefiro declarar a lacuna a entregar número inflado.</div>')
    return '\n'.join(out)


def bloco_investimento(a, tr):
    out = ['<h3>Custo de tráfego e investimento em mídia</h3>', '<div class="grid g4">']
    out.append('<div class="stat"><div class="v sm">$9,23</div><div class="l">CPM · benchmark</div><div class="d">Fashion/Apparel · EUA · 2026</div></div>')
    out.append('<div class="stat"><div class="v sm">$0,45</div><div class="l">CPC · benchmark</div></div>')
    out.append('<div class="stat"><div class="v sm">10,62%</div><div class="l">CPA · % da receita</div><div class="d">IRP Fashion, jun/2026</div></div>')
    if tr and tr.get('status') == 'OK':
        out.append('<div class="stat" style="border-color:var(--acc)"><div class="v sm">ver acima</div><div class="l">gasto em mídia/mês (est.)</div><div class="d">≈ receita × 10,62%</div></div>')
    else:
        out.append('<div class="stat" style="border-color:var(--warn)"><div class="v sm">—</div><div class="l">gasto em mídia/mês</div><div class="d">não estimável sem receita</div></div>')
    out.append('</div>')
    out.append('<div class="note">Gasto ≈ receita × 10,62% (o quanto o setor de Fashion/Acessórios gasta em mídia como fração da receita, benchmark IRP jun/2026). Não apresento ROAS: com o gasto derivado da receita por um percentual fixo, o ROAS seria sempre <code>1÷10,62%</code> por construção (tautologia), não um achado.</div>')
    return '\n'.join(out)


def bloco_topprodutos(a):
    if not a['top_produtos']:
        return '<div class="note">Catálogo não coletado (bloqueio de acesso ao domínio).</div>'
    rows = ''.join(f"<tr><td class='num'>{i+1}</td><td>{t}</td><td class='num'>${p:.2f}</td></tr>" for i, (t, p) in enumerate(a['top_produtos']))
    return f'<div class="tblwrap"><table><thead><tr><th>#</th><th>Produto</th><th>Preço</th></tr></thead><tbody>{rows}</tbody></table></div>'


def bloco_hero(slug, a):
    if not a['produto_campeao']:
        return '<div class="note danger">Produto campeão não identificado (catálogo bloqueado).</div>'
    p = a['produto_campeao']
    img = f'prints/{slug}-pdp.jpg'
    return f"""<div class="hero-prod">
<img src="{img}" alt="{a['nome']}" style="object-fit:cover;object-position:top;max-height:340px">
<div><div class="r">Best seller nº 1</div>
<h3>{p['titulo']}</h3>
<div class="preco">${p['preco']:.2f}</div>
<p style="color:var(--dim);margin:14px 0">Fonte: coleção de best sellers pública da loja.</p></div></div>"""


def bloco_scorecard(a):
    if not a['scorecard']:
        return ''
    rows = ''.join(f"<tr><td>{eixo}</td><td class='num'>{pts}/2</td><td style='color:var(--dim)'>{just}</td></tr>" for eixo, pts, just in a['scorecard'])
    return f"""<h3>Scorecard de nível de execução · soma {a['scorecard_soma']}/12 ({a['nivel']})</h3>
<div class="tblwrap"><table><thead><tr><th>Eixo</th><th>Pontos</th><th>Por quê</th></tr></thead><tbody>{rows}</tbody></table></div>
<p style="color:var(--dim2);font-size:13px;margin-top:10px">Nível é etiqueta de "pra quem serve", não nota de corte: 10-12 iniciante, 6-9 médio, 0-5 avançado. Toda oportunidade de dropshipping vale, muda só o perfil de operador."""


def gerar_loja(slug):
    a = ANALISE[slug]
    d = dados.get(a['dominio'], {})
    r = reviews.get(a['dominio'], {})
    cat = d.get('catalogo', {})
    a['_ticket_mediano'] = cat.get('preco_mediana', 40)
    ident = d.get('identificacao', {})
    wb = d.get('wayback', {})
    tc = d.get('tranco', {})
    sm = d.get('sitemap', {})
    social = d.get('social', {})

    midia_html, tr, sobrev = bloco_midia(slug, a, d, r, trafego)
    fin_html = bloco_financeiro(slug, a, tr)
    inv_html = bloco_investimento(a, tr)

    html = [head(a['nome']), nav(slug)]
    html.append(f"""<header><div class="wrap">
<div class="tag">Dossiê · {a['ativos']} anúncios ativos</div>
<h1>{a['nome']}</h1>
<p class="sub"><a href="https://{a['dominio']}" target="_blank">{a['dominio']}</a> · joia masculina · {a['moeda']}</p>
<div class="meta"><span>{a['ativos']} ativos</span><span>{a['historico']} no histórico</span>
<span>sobrevivência {sobrev if sobrev is not None else '—'}%</span>
<span class="pill {a['modelo_pill']}">{a['modelo']}{' ⭐' if a.get('modelo_estrela') else ''}</span>
<span class="pill {a['veredito_pill']}">{a['veredito']}</span>
<span class="pill {a['nivel_pill']}">NÍVEL {a['nivel']}</span></div>
<div class="toplinks">
<a class="adlib store" href="https://{a['dominio']}" target="_blank">🏬 Abrir loja · {a['dominio']} ↗</a>
<a class="adlib" href="https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id={a['page_id']}" target="_blank">📓 Biblioteca de anúncios · aberta, todos os países ↗</a>
</div></div></header>""")

    html.append(f'<section><div class="wrap"><h2><span class="n">01</span>Produto campeão</h2>{bloco_hero(slug, a)}{bloco_topprodutos(a)}</div></section>')

    html.append(f'<section><div class="wrap">{midia_html}{fin_html}{inv_html}</div></section>')

    prints_html = ''
    if os.path.exists(os.path.join(BASE, 'prints', f'{slug}-home.jpg')):
        prints_html = f"""<div class="shots">
<div class="shot"><div class="cap"><b>Home</b><a href="https://{a['dominio']}" target="_blank">abrir ↗</a></div><div class="frame"><img src="prints/{slug}-home.jpg"></div></div>
<div class="shot"><div class="cap"><b>PDP do campeão</b></div><div class="frame"><img src="prints/{slug}-pdp.jpg"></div></div>
</div>
<div class="shots"><div class="shot" style="grid-column:1/-1"><div class="cap"><b>Carrinho com item</b></div><div class="frame"><img src="prints/{slug}-carrinho.jpg"></div></div></div>"""
    else:
        prints_html = '<div class="note danger">Capturas não obtidas — domínio protegido por Cloudflare (bloqueou Playwright, curl e WebFetch igualmente).</div>'
    html.append(f'<section><div class="wrap"><h2><span class="n">03</span>Páginas capturadas</h2>{prints_html}</div></section>')

    an = a['anatomia']
    html.append(f"""<section><div class="wrap"><h2><span class="n">★</span>Anatomia do vencedor</h2>
<p class="lead">O que <b>faz o campeão vender</b>, decodificado dos criativos e do catálogo.</p>
<div class="tblwrap"><table><tbody>
<tr><td style='white-space:nowrap;color:var(--acc);font-weight:600'>Big idea / ângulo</td><td>{an['big_idea']}</td></tr>
<tr><td style='white-space:nowrap;color:var(--acc);font-weight:600'>Mecanismo único</td><td>{an['mecanismo']}</td></tr>
<tr><td style='white-space:nowrap;color:var(--acc);font-weight:600'>Formato de hook</td><td>{an['hook']}</td></tr>
<tr><td style='white-space:nowrap;color:var(--acc);font-weight:600'>Estrutura do presell</td><td>{an['presell']}</td></tr>
<tr><td style='white-space:nowrap;color:var(--acc);font-weight:600'>Objeção principal</td><td>{an['objecao']}</td></tr>
</tbody></table></div></div></section>""")

    if os.path.exists(os.path.join(BASE, 'prints', f'{slug}-home.jpg')):
        ref_home = f'Print da home ao lado (seção 03) + <a href="https://{a["dominio"]}" target="_blank" style="color:var(--acc)">🏬 abrir home ↗</a>. Modele esta home: {an["hook"]}'
        ref_pdp = f'Print da PDP ao lado (seção 03) — <a href="https://{a["dominio"]}" target="_blank" style="color:var(--acc)">🛍️ abrir PDP do campeão ↗</a>. PDP pra modelar: {an["presell"]}'
    else:
        ref_home = f'Não capturada (domínio bloqueado). Referência de home só por texto: {an["hook"]}'
        ref_pdp = f'Não capturada (domínio bloqueado). {an["presell"]}'
    html.append(f"""<section><div class="wrap"><h2><span class="n">★</span>Referência de home e PDP (pra modelar)</h2>
<p class="lead">O que copiar de cada página desta loja, pra levar ao <a href="plano-de-acao.html">Plano de Ação</a> da Vyprro.</p>
<div class="tblwrap"><table><tbody>
<tr><td style="white-space:nowrap;color:var(--acc);font-weight:600">Home — o que modelar</td><td>{ref_home}</td></tr>
<tr><td style="white-space:nowrap;color:var(--acc);font-weight:600">PDP — o que modelar</td><td>{ref_pdp}</td></tr>
</tbody></table></div></div></section>""")

    chips = ''.join(f"<span class=''>{ap}</span>" for ap in ident.get('apps', []))
    stack_html = f'<dd class="chips">{chips}</dd>' if chips else '<dd>não identificado (bloqueio de acesso)</dd>'
    socials = ', '.join(social.keys()) if social else ('nenhum perfil vinculado' if ident.get('nota_social') else 'não verificado')
    cat_line = f"{cat.get('n_produtos','—')} · {cat.get('n_variantes','—')} variantes" if cat.get('n_produtos') else 'catálogo bloqueado (Cloudflare)'
    ticket_line = f"<b>${cat.get('preco_mediana','—')}</b> · faixa ${cat.get('preco_min','—')} a ${cat.get('preco_max','—')}" if cat.get('preco_mediana') else '—'
    html.append(f"""<section><div class="wrap"><h2><span class="n">04</span>Catálogo, stack e identificação</h2>
<dl class="kv">
<dt>Plataforma</dt><dd>{ident.get('plataforma') or 'não identificada'}</dd>
<dt>Produtos</dt><dd>{cat_line}</dd>
<dt>Ticket mediano</dt><dd>{ticket_line}</dd>
<dt>Primeiro produto</dt><dd>{cat.get('primeiro_produto','—')}</dd>
<dt>Wayback</dt><dd>{wb.get('primeira_captura') or wb.get('erro','—')}</dd>
<dt>Tranco</dt><dd>{(str(tc.get('rank_atual')) + ' · ' + tc.get('tendencia','')) if tc.get('rank_atual') else tc.get('erro','—')}</dd>
<dt>Sitemap</dt><dd>{sm.get('total_urls','—')} URLs · {len(sm.get('possiveis_advertoriais',[]))} possíveis advertoriais</dd>
<dt>Tech stack</dt>{stack_html}
<dt>Redes sociais</dt><dd>{socials}</dd>
</dl></div></section>""")

    prova = '<div class="note">Nenhuma contagem pública encontrada (widget não expõe aggregateRating no HTML, ou loja recente demais).</div>'
    if r.get('loja_total'):
        lt = r['loja_total']
        prova = f"<div class='note good'><b>{lt['reviewCount']} reviews · nota {lt.get('ratingValue')}</b> · via {lt.get('fonte')}</div>"
    elif r.get('pedidos_estimados'):
        pe = r['pedidos_estimados']
        prova = f"<div class='note good'><b>Pedidos estimados (acumulado, não mensal):</b> {pe['a_3pct']:,} a {pe['a_1pct']:,} (base: {pe['base_reviews']} reviews de {pe.get('fonte_base','')})</div>".replace(',', '.')
    elif r.get('declarado_home'):
        prova = f"<div class='note danger'><b>Home declara {r['declarado_home']} reviews</b> — alegação de marketing, NÃO verificada por API. Cruzado com a idade do domínio na leitura final.</div>"
    html.append(f'<section><div class="wrap"><h2><span class="n">05</span>Prova social</h2>{prova}</div></section>')

    gaps = []
    if not cat.get('n_produtos'):
        gaps.append(('Catálogo completo', 'domínio protegido por Cloudflare', 'products.json via curl, WebFetch e Playwright — os três bloqueados'))
    if not (tr and tr.get('status') == 'OK'):
        gaps.append(('Tráfego real (SimilarWeb)', 'sem dados públicos suficientes ou site bloqueado', 'raspador público (trafego.js) com retry'))
    if not r.get('loja_total') and not r.get('pedidos_estimados'):
        gaps.append(('Contagem de reviews', 'widget não expõe aggregateRating no HTML ou loja não usa review pública', 'JSON-LD + Judge.me API'))
    gaps_html = ''.join(f'<tr><td><b>{g}</b></td><td>{m}</td><td>{t}</td></tr>' for g, m, t in gaps) or '<tr><td colspan="3">Nenhuma lacuna relevante nesta ficha.</td></tr>'
    html.append(f'<section><div class="wrap"><h2><span class="n">06</span>Dados não obtidos</h2><div class="tblwrap"><table><thead><tr><th>Dado</th><th>Motivo</th><th>Método tentado</th></tr></thead><tbody>{gaps_html}</tbody></table></div></div></section>')

    sc_html = bloco_scorecard(a)
    html.append(f"""<section><div class="wrap"><h2><span class="n">07</span>Veredito e classificação</h2>
<div class="grid g4" style="margin-bottom:18px">
<div class="stat"><div class="l">Modelo</div><div class="v sm"><span class="pill {a['modelo_pill']}">{a['modelo']}</span></div></div>
<div class="stat"><div class="l">Veredito de mercado</div><div class="v sm"><span class="pill {a['veredito_pill']}">{a['veredito']}</span></div></div>
<div class="stat"><div class="l">Nível de execução</div><div class="v sm"><span class="pill {a['nivel_pill']}">{a['nivel']}</span></div></div>
<div class="stat"><div class="l">Defensabilidade</div><div class="v sm"><span class="pill {a['defensabilidade_pill']}">{a['defensabilidade']}</span></div></div>
</div>
{sc_html}
<div class="note info" style="margin-top:14px"><b>Momentum da operação: <span class="pill {a['momentum_pill']}">{a['momentum']}</span></b>{'<br>' + a['momentum_nota'] if a.get('momentum_nota') else ''}</div>
<div class="op" style="margin-top:18px"><div class="r">Leitura final</div><h3>{a['veredito']} · {a['modelo']} · NÍVEL {a['nivel']}</h3>
<p style="color:var(--dim)">{an['mecanismo']}</p></div>
</div></section>""")

    html.append(FOOT)
    with open(os.path.join(BASE, f'loja-{slug}.html'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))
    print(f'gerado: loja-{slug}.html')


for slug in ['luxujewelry', 'storeedyta', 'alfredco', 'humbler']:
    gerar_loja(slug)
