# MASTER: GABM Scales (apresentação de mestrado em vídeo)

Fonte: ui-ux-pro-max, query "academic presentation minimal content-first", dials variance 3, motion 2, density 3.
Uso: deck HTML 16:9 para gravação em 1080p, sem interação ao vivo.

## Tokens

Cores (modo claro, fundo papel):
background #F8FAFC, foreground #0F172A, card #FFFFFF, card foreground #0F172A
primary (azul marinho acadêmico) #1E3A5F, on primary #FFFFFF
secondary #334155, on secondary #FFFFFF
accent (dourado de citação, só detalhes) #B45309, on accent #FFFFFF
Acentos vibrantes sobre o dark (ui-ux-pro-max, domínios color/style): ciano #22D3EE, violeta #A78BFA, esmeralda #34D399, céu #38BDF8. Uso restrito a elementos gráficos grandes (números de passo, marcadores, barra de título em gradiente). Texto corrido permanece em foreground/muted para contraste.
muted #E9EEF5, muted foreground #475569, border #CBD5E1, ring #1E3A5F

Tipografia:
Títulos: Crimson Pro, 600 a 700, caixa alta só em rótulos curtos.
Corpo: Atkinson Hyperlegible, 400 e 700. Corpo mínimo 24px no slide. Notas 18px.
Import: Google Fonts Atkinson Hyperlegible mais Crimson Pro.

Espaçamento (density 3, generoso para vídeo comprimido):
Base 8px. Seções com 24, 32 ou 48px. Gutter lateral mínimo 64px em 1920px, 40px em 1280px. Largura de texto até 28 palavras por linha.

Movimento (motion 2, sutil):
Transição entre slides com fade de 250ms. Sem slide lateral. Sem autoplay. Sem parallax.
Respeitar prefers reduced motion: pular qualquer animação e mostrar o estado final.

## Regras de slide

1. Um conceito por slide. Título até 12 palavras. Até 4 bullets por slide. Cada bullet até 20 palavras.
2. Contraste mínimo 4.5:1 para texto. Texto secundário usa #475569 sobre #F8FAFC ou #FFFFFF.
3. Ícones só vetoriais SVG em 1 estilo por nível. Nenhum emoji como ícone.
4. Gráficos em SVG com texto alternativo. Nenhum PNG de texto.
5. Foco visível para navegação por teclado. Setas alternam slides. Tecla F ativa tela cheia. Tecla N mostra ou oculta notas.
6. Barra de progresso fina em azul marinho. Contador “2 de 7”. Tempo alvo por slide indicado no canto.
7. Tela final do slide 7 fica parada por 10 segundos para corte do vídeo.

## Anti padrões proibidos

Lista corrida sem hierarquia. Fundo com textura. Mais de 2 fontes. Dourado como fundo de texto. Animação com som. Vídeo em autoplay. Tabela com mais de 4 linhas por slide.

## Hierarquia de consulta

Este arquivo é a fonte de verdade visual do deck em `docs/apresentacao/`.
