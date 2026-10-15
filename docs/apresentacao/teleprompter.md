# Teleprompter completo. 9 slides para vídeo gravado

Leitura a 130 palavras por minuto. Total alvo: 17 a 19 min. Tela final parada por 10 segundos.
Regras: PTC leve. Nenhum travessão. Acentos corretos. Sigla GABM só a partir do slide 5. Sigla ABM com expansão no slide 4.

## Slide 1 (1:00, cerca de 110 palavras)

[TELA] Título, nome e programa em duas linhas, centralizados.
[FALA]
Olá. Eu sou Danilo Amorim, do PPG Modelagem em Sistemas Complexos da USP. Este vídeo apresenta meu projeto de mestrado em até 20 minutos. O título é este: Emergência de Redes Livres de Escala com Agentes Generativos de IA para Estudo de Popularidade de Repositórios GitHub. Hoje eu mostro a visão geral em 8 slides. A hipótese da pesquisa vem a seguir, e depois eu apresento o problema, a ideia, o laboratório empírico e a forma de comparação. Os detalhes metodológicos ficam para a próxima etapa.
[PAUSA 2s]

## Slide 2 (1:30, cerca de 150 palavras)

[TELA] Título mais hipótese centralizada na vertical e na horizontal.
[FALA]
A hipótese desta pesquisa é esta: agentes generativos de IA podem reproduzir padrões livres de escala observados em redes complexas sem imposição de um mecanismo formativo? Repare nos dois lados da frase. De um lado, o padrão: concentração em poucos hubs, cauda pesada, lei de potência. Do outro, a condição: nenhuma regra que force os agentes a preferir os populares. Se a curva emerge mesmo assim, a explicação é comportamental. Cada agente escolhe por afinidade, qualidade e contexto, e a macroestrutura nasce dessas microdecisões. Se a curva não emerge, descobrimos o limite dos agentes atuais. Nos dois casos, o resultado informa a metodologia. O teste usa o GitHub como laboratório e compara três mundos: o real, o simulado e o modelo clássico. Guarde a hipótese, pois ela organiza todo o resto da apresentação.
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

## Slide 7 (2:30, cerca de 300 palavras)

[TELA] Três cartões: cérebro, micro verossímil, aposta. Primeira definição de GABM.
[FALA]
De um lado, agentes sem cérebro para processos mentais. Do outro, um laboratório onde cada decisão exige ler e julgar. A resposta é acoplar os dois: a sigla do método deste projeto é GABM, que significa Modelagem Baseada em Agentes Generativos. Nesse enfoque, cada agente usa um modelo de linguagem como cérebro. Cada agente percebe o repositório, recupera memória, avalia afinidade temática, pondera qualidade percebida e reputação, e então decide. A arquitetura segue o padrão Percepção, Cérebro e Ação, com memória e planejamento explícitos. Com isso, cada escolha carrega motivo: afinidade com o tema, qualidade do código, reputação do mantenedor. Por que GABM e não a ABM tradicional, que já produziu modelos úteis? Porque a ABM clássica vence quando a regra de decisão é simples e conhecida: segregação, trânsito, contágio. Dar star é outra classe de decisão: exige ler documentação, interpretar qualidade, ponderar reputação. Comportamento semanticamente denso demais para caber em se isso, faça aquilo sem caricatura. Quando a decisão é o próprio fenômeno, o modelo precisa decidir de verdade. É exatamente o nosso caso. A aposta do projeto é direta. Se cada agente escolhe como um desenvolvedor, os hubs emergem sem regra imposta. Ninguém programa que os agentes se conectem aos populares. A concentração emerge das decisões. Essa troca muda o status da anexação preferencial. Ela deixa de ser premissa e passa a ser hipótese a testar. A literatura recente motiva esse teste. Estudos de 2025 e 2026 relatam anexação preferencial emergente em enxames de agentes de linguagem e discutem validação como desafio central da simulação generativa. O teste usa o GitHub como laboratório, que apresento a seguir.
[PAUSA 2s]

## Slide 8 (2:30, cerca de 320 palavras)

[TELA] Três caixas: Observar o real. Simular com agentes. Comparar mundos.
[FALA]
A abordagem tem três passos, sem jargão. Primeiro, observar o real. Coletamos eventos de star e o contexto de cada repositório no período. Organizamos os dados em janelas mensais para acompanhar a dinâmica. Enriquecemos cada repositório com representação semântica para similaridade mensurável. Segundo, simular com agentes. Os agentes generativos exploram um catálogo com as mesmas informações que um desenvolvedor veria. Cada agente monta uma lista curta, avalia e escolhe onde dar star. Prompts, versão do modelo, temperatura e sementes ficam registrados para reprodução. Terceiro, comparar mundos. Comparamos três mundos: o real observado, o simulado pelos agentes e o modelo clássico como referência. A comparação usa dois critérios. Primeiro, a curva. A distribuição simulada se aproxima da real? O expoente é próximo? A cauda aparece sem imposição? Segundo, o mecanismo. A chance de star cresce com o grau como no real? Pesa mais afinidade ou popularidade? A validação usa o método de Clauset, com alternativa log normal e testes com margens pré definidas. Em vídeo high level, o ponto essencial é este: não basta acertar a forma da curva. É preciso acertar por motivos parecidos com os humanos. Esse duplo critério protege o projeto contra vitória vazia, onde a curva bate por acidente.
[PAUSA 2s]

## Slide 9 (2:30, cerca de 320 palavras)

[TELA] Quatro ganhos em grade simples.
[FALA]
Por que isso importa? Primeiro, o ganho científico. Este projeto testa mecanismo, não só ajuste de curva. Muitos trabalhos mostram que tal modelo gera tal distribuição. Poucos mostram que agentes que leem, comparam e escolhem geram a distribuição pelos mesmos motivos que pessoas. Segundo, o ganho metodológico. O projeto mostra se o modelo de linguagem decide de forma verossímil ou apenas imita padrões vistos no treino. Se o agente só repete “popular é bom”, o teste revela. Se o agente pondera tema, qualidade e contexto, o teste também revela. Terceiro, o ganho prático. Poucos repositórios capturam quase toda a atenção em plataformas abertas. Entender essa concentração ajuda a discutir descoberta justa, diversidade de projetos, sustentabilidade de mantenedores e risco de monocultura de dependências. Quarto, a atualidade. A literatura de 2025 e 2026 coloca a validação como desafio central da simulação generativa com agentes. Há entusiasmo com demonstrações vívidas e há ceticismo saudável sobre realismo comportamental. Este projeto responde com protocolo explícito, dados públicos e baselines clássicos. O escopo foi reduzido de propósito para caber no mestrado: pipeline de dados com embeddings, simulação mínima com controle e comparação com método estabelecido mais análise de mecanismo. Três entregáveis verificáveis valem mais que uma promessa ampla.
[PAUSA 2s]

## Slide 10 (1:30 mais tela final de 10s, cerca de 190 palavras)

[TELA] Três takeaways mais tela final estática com nome e contato.
[FALA]
Para concluir, retomo a pergunta em forma simples. Agentes generativos de IA que decidem sozinhos reproduzem padrões livres de escala de modo verossímil a dados reais? Vimos o caminho da resposta. Os modelos clássicos explicam a curva impondo a regra. A GABM propõe trocar a regra por decisões. O GitHub oferece o teste empírico para comparar os dois mundos pelos dois critérios: curva e mecanismo. Os detalhes metodológicos e o cronograma ficam para a próxima etapa. Obrigado por assistir.
[PAUSA 5s. Manter tela final parada por 10s para corte]
Tela final: Danilo Lindemberg Amorim. PPG Modelagem em Sistemas Complexos, USP. Plano completo e referências disponíveis sob solicitação.
