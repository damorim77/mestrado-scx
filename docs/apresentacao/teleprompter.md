# Teleprompter completo. 11 slides para vídeo gravado

Leitura a 130 palavras por minuto. Total alvo: 18 a 20 min. Tela final parada por 10 segundos.
Regras: PTC leve. Nenhum travessão. Acentos corretos. Sigla GABM só a partir do slide 5. Sigla ABM com expansão no slide 4.

## Slide 1 (1:00, cerca de 110 palavras)

[TELA] Título, nome e programa em duas linhas, centralizados.
[FALA]
Olá. Eu sou Danilo Amorim, do PPG Modelagem em Sistemas Complexos da USP. Este vídeo apresenta meu projeto de mestrado em até 20 minutos. O título é este: Emergência de Redes Livres de Escala com Agentes Semânticos. Hoje eu mostro a visão geral em 9 slides. A hipótese da pesquisa vem a seguir, e depois eu apresento o problema, a ideia, o laboratório empírico e a forma de comparação. Os detalhes metodológicos ficam para a próxima etapa.
[PAUSA 2s]

## Slide 2 (1:30, cerca de 150 palavras)

[TELA] Título mais hipótese centralizada na vertical e na horizontal.
[FALA]
A hipótese desta pesquisa é esta: agentes semânticos de IA podem reproduzir padrões livres de escala observados em redes complexas sem imposição de um mecanismo formativo? Repare nos dois lados da frase. De um lado, o padrão: concentração em poucos hubs, cauda pesada, lei de potência. Do outro, a condição: nenhuma regra que force os agentes a preferir os populares. Se a curva emerge mesmo assim, a explicação é comportamental. Cada agente escolhe por afinidade, qualidade e contexto, e a macroestrutura nasce dessas microdecisões. Se a curva não emerge, descobrimos o limite dos agentes atuais. Nos dois casos, o resultado informa a metodologia. O teste usa o GitHub como laboratório e compara três mundos: o real, o simulado e o modelo clássico. Guarde a hipótese, pois ela organiza todo o resto da apresentação.
[PAUSA 2s]

## Slide 3 (2:30, cerca de 320 palavras)

[TELA] Conceito, mecanismo com animação da regra e limite.
[FALA]
Vamos ao conceito. Uma rede livre de escala é uma rede onde poucos hubs concentram a maioria das ligações. A maioria dos nós tem poucas conexões. Poucos têm muitíssimas. Essa desigualdade segue lei de potência na distribuição de grau, com expoente 3 no modelo. O modelo Barabási Albert, de 1999, propõe um mecanismo formativo com dois ingredientes. Primeiro, crescimento: a rede ganha um nó por vez. Segundo, anexação preferencial: cada nó novo cria ligações com chance proporcional ao grau atual. Quem tem mais, recebe mais. Na animação, a rede cresce diante dos olhos até 800 nós: cada ponto novo cria 2 ligações, com chance proporcional ao grau de quem já está na rede. Repare nos pontos que incham e esquentam de cor: são os hubs se formando, e repare como a rede adensa ao redor deles. À esquerda, o gráfico da distribuição acompanha ao vivo em escala log-log: muitos pontos à esquerda em cima, poucos à direita embaixo. A maioria continua pequena. A construção segue durante todo o slide. O modelo é elegante e influente. O limite também é claro, e vale separar dois níveis. No nível macro, o modelo gera a curva. No nível micro, a regra é um como se: estipulada para produzir o padrão, não observada em decisões reais. Nenhum desenvolvedor decide dar star porque calculou probabilidade proporcional ao grau. A decisão real envolve leitura do README, afinidade com a linguagem, reputação do mantenedor e momento do projeto. A pergunta que sobra é de mecanismo. Decisões humanas reais, tomadas uma a uma, produzem a mesma curva sem ninguém impor a regra? Esse é o ponto de partida do projeto. Não proponho mais um gerador de curva. Proponho um teste de mecanismo com dados observáveis. E o caminho para esse teste é modelar os nós como agentes que decidem. É o próximo slide.
[PAUSA 2s]

## Slide 4 (2:30, cerca de 320 palavras)

[TELA] Grafo bipartido, stars como proxy e caixa com a pergunta do crescimento.
[FALA]
Para quem nunca usou: GitHub é a maior plataforma de hospedagem de código aberto. Desenvolvedores publicam projetos chamados repositórios, e qualquer pessoa acompanha um projeto dando star, um curtir com registro público. Mas o GitHub não é uma rede social comum, nem um arquivo morto. Ele é uma rede sociotécnica: um grafo com dois tipos de nós, desenvolvedores de um lado e repositórios do outro, como mostra o diagrama. A colaboração acontece exatamente no encontro entre atores e artefatos. E a aresta que nos interessa é a de popularidade: o star. Cada star é um endosso público que liga o mundo social ao mundo técnico, e é por essa aresta que a atenção flui. Ela flui de forma concentrada: só o Linux soma cerca de 250 mil stars, seguido de VS Code, curl e repositórios ilustrativos com uma dezena. As arestas descem em cascata: quanto menor o repositório, menos desenvolvedores chegam. A distribuição é compatível com lei de potência, então é plausível tratar o GitHub como rede livre de escala. É exatamente o padrão que queremos ver emergir da simulação. Dar star é ainda uma decisão simples, pública e reversível. Cada decisão vem com contexto rico. O agente lê README, linguagem, tópicos, commits e atividade do mantenedor. Os dados são públicos e longitudinais, de 2024 a 2026. Filtros removem o ruído: sem repositórios vazios, sem forks, sem bots, sem material que não é software e com atividade mínima. O resultado é uma base tratada onde comparação entre real e simulado faz sentido. E fica a pergunta da caixa em destaque: como modelar o crescimento de popularidade dos repositórios GitHub, se a qualidade do README pesa na decisão de dar star?
[PAUSA 2s]

## Slide 5 (2:00, cerca de 200 palavras)

[TELA] Conceito, 4 tópicos e diagrama de decisões individuais a padrão global.
[FALA]
Como modelar esse crescimento? Tratando cada desenvolvedor como um agente. A resposta clássica é a modelagem baseada em agentes: um fenômeno representado em termos de seus agentes individuais e das interações entre eles. Cada agente tem um perfil heterogêneo e toma decisões no nível micro. Desenvolvedores têm gostos, repertórios e critérios distintos, e a ABM representa essa diversidade sem média. Da auto-organização desses agentes emergem fenômenos no nível macro, sem nenhum coordenador central. Ninguém decreta o padrão. Ele nasce das interações, como mostra o diagrama. Por isso a ABM é amplamente aplicada na Ciência de Redes, tanto para entender a dinâmica nas redes quanto das redes. Mas o limite aparece rápido. Codificar em regras os processos mentais que determinam a decisão pode ser extremamente desafiador e tornar o modelo mais complexo que o desejado. Falta um cérebro pronto para escolher com contexto, memória e nuance. E veja no próximo slide o tamanho desse desafio.
[PAUSA 2s]

## Slide 6 (1:00, cerca de 110 palavras)

[TELA] Captura real do README com legenda do agravante.
[FALA]
Este é o README real do VS Code, capturado da página do repositório. Badges, capturas de tela, tabelas, links. Cada desenvolvedor lê isso de um jeito: um repara na documentação, outro na atividade recente, outro na reputação. Para regra fixa, essa riqueza é ruído indomável. Para um agente com modelo de linguagem, é texto legível. Eis o agravante que decide o método: se a escolha depende de interpretar um README, o modelo precisa ler. A resposta é o próximo slide.
[PAUSA 2s]

## Slide 7 (2:30, cerca de 270 palavras)

[TELA] Dois painéis: o que ela entrega (7 itens) e o que ela cobra (3 custos).
[FALA]
A resposta amadureceu em duas etapas. A primeira alternativa tem sigla GABM, que significa Modelagem Baseada em Agentes Generativos. A proposta é direta: manter a ABM e trocar o motor de decisão por um modelo de linguagem. Cada agente percebe o repositório, recupera memória, avalia afinidade e reputação, e então decide. Na prática, o agente lê o README, cruza o conteúdo com o perfil do desenvolvedor e escolhe com motivo declarado, como afinidade com o tema ou reputação do mantenedor. O painel da esquerda mostra o que essa troca entrega. São sete necessidades vindas da literatura. Primeira, avaliação semântica do texto de entrada, como o README. Segunda, agentes críveis, que decidem pelo contexto em vez de obedecer regra fixa. Terceira, senso comum e decisão próxima da humana, com racionalidade limitada, vieses e heurísticas. Quarta, memória entre decisões, que carrega o histórico para o julgamento. Quinta, reflexão e planejamento. Sexta, deliberação explícita em linguagem natural. Sétima, regras flexíveis, que aliviam o viés do modelador embutido em se isso, faça aquilo. O painel da direita mostra o que ela cobra. Cada decisão consome múltiplas inferências autoregressivas, pois o modelo gera texto token a token, e a conta chega em três moedas. Custo computacional, porque milhares de decisões por rodada exigem máquina forte ou API. Custo financeiro, porque inferência paga se cobra por token. E tempo, porque rodadas de horas travam iteração e calibração. Some-se a fragilidade da reprodutibilidade externa, pois o mesmo prompt pode gerar respostas distintas. Em escala de milhares de agentes e rodadas, esses custos se multiplicam e definem o teto do experimento. A primeira alternativa funciona, mas cobra caro por decisão.
[PAUSA 2s]

## Slide 8 (1:00, cerca de 120 palavras)

[TELA] Dois painéis: LLMs e DS1 em 5 traços cada, com par Retorna. Faixa de definição no topo.
[FALA]
A proposta tem sigla SABM, Modelagem Baseada em Agentes Semânticos. A faixa acima define a classe DS1 e já adianta a diferença: adapta o julgamento pelo contexto. Os painéis contrastam os motores em cinco traços. O LLM é generativo, retorna sequência de tokens, e é autoregressivo: cada token custa uma inferência dependente das anteriores, com maior latência, custo e amostragem que dificulta reprodução. O DS1 é classificador, retorna escore ou escolha discreta, e não é autoregressivo: uma única inferência devolve a resposta, com baixa latência, menor custo e alta reprodutibilidade sem amostragem. Um modelo mais enxuto para direcionar a decisão do agente. No próximo slide, o que essa troca mantém e o que ela deixa pelo caminho.
[PAUSA 2s]

## Slide 9 (1:30, cerca de 130 palavras)

[TELA] SABM com animação da transição: 4 itens atravessam para mantém, 3 ficam em abre mão, medidor de custo despenca. Botão Rever repete.
[FALA]
A troca é pontual e aparece em movimento. Manter a ABM e substituir o modelo de linguagem por modelos DS1. O DS1 não gera texto, apenas decide: recebe atributos, devolve tipo e escore. E a passagem aparece em movimento. À esquerda estão as sete entregas da GABM. Quatro delas atravessam: avaliação semântica, agentes críveis, julgamento próximo do humano e regras flexíveis. Três ficam pelo caminho: memória entre decisões, reflexão e planejamento, e deliberação explícita em linguagem natural. Por isso os custos caem nas três moedas, como mostra o medidor: cada decisão consome uma passada direta, sem gerar token a token. Em troca, as rodadas duram minutos e se repetem idênticas. A aposta em um gesto: manter o julgamento e aposentar a deliberação, para ganhar escala com reprodutibilidade externa.
[PAUSA 2s]

## Slide 10 (1:30, cerca de 140 palavras)

[TELA] Três caixas numeradas, parágrafo da mecânica e barra da hipótese.
[FALA]
A metodologia tem três movimentos. Primeiro, similar o crescimento da rede: o método Barabási Albert bipartido como baseline contra a SABM, nas mesmas condições. Segundo, comparar contra dados empíricos: verificar o ajuste com medidas estatísticas entre simulado e observado, na curva da distribuição e no mecanismo de formação. Terceiro, avaliar os resultados: qual modelo melhor se assemelha aos dados empíricos, e onde cada um erra. O baseline impõe a regra e a SABM decide por contexto, então a comparação isola o efeito do julgamento semântico. A mecânica imita desenvolvedores usando a busca do GitHub para encontrar repositórios e decidir se dão estrela ou não. E a hipótese que organiza tudo: o componente semântico pode ajudar a explicar por que alguns projetos se tornam mais populares. Se a SABM reproduzir melhor a concentração observada, o mecanismo ganha evidência.
[PAUSA 2s]

## Slide 11 (1:00 mais tela final de 10s, cerca de 80 palavras)

[TELA] Agradecimento com nome. Tela final estática.
[FALA]
Para concluir, retomo a pergunta em forma simples. Agentes semânticos de IA que decidem sozinhos reproduzem padrões livres de escala de modo verossímil a dados reais? Vimos o caminho da resposta. Os modelos clássicos explicam a curva impondo a regra. A SABM propõe trocar a regra por decisões com julgamento semântico e motor barato. O GitHub oferece o teste empírico pelos dois critérios: curva e mecanismo. Se a concentração emergir das decisões, o mecanismo ganha evidência sem premissa imposta. Obrigado por assistir.
[PAUSA 5s. Manter tela final parada por 10s para corte]
Tela final: Danilo Lindemberg Amorim.
