# Roteiro da Versão 2 do Plano de Pesquisa (SCX)

Data: 2026-10-19
Estado: roteiro pronto, aguardando início da execução
Base verificada: `latex/plano-abnt.tex` (808 linhas, texto na página 3 a 54 do PDF), `revisao-metodologia.md`, notas de 2026-10-10 a 2026-10-17.

## 1. Objetivo da v2

Compactar o plano de pesquisa de 52 páginas de texto (v1) para 10 páginas, contando Introdução até Metodologia mais a lista de referências, sem capa e sem folha de rosto. Dois tópicos entram nesta versão: um tópico novo discutindo Modelos de Decisão Sistema 1 (DS1) e a redação do tópico GitHub como rede sociotécnica, hoje apenas com o título no tex. A coerência com o pivô GABM para DS1, já concluído na introdução, se estende à metodologia, que será reescrita com motor DS1.

## 2. Decisões registradas com o autor (2026-10-19)

1. Contagem das 10 páginas: texto (Introdução a Metodologia) mais referências; sem folha de rosto. Capa fica de fora da proposta. Recomendo também sem sumário: em 10 páginas o sumário só ocupa espaço. Se o programa exigir sumário, o referencial recua 0,5 página.
2. Metodologia reescrita para motor DS1: modelo local open weight tipo Jebadiah 4B v2 em temperatura 0 com seed fixa. Plataformas GABM (Concordia) aparecem só como contexto histórico da literatura.
3. Âncora sociotécnica: com referência conceitual E com argumentação empírica. Entrada que proponho registrar no bib: Orlikowski e Scott (2008), sociomaterialidade. Trist (1981), origem do termo sociotécnico, como segunda entrada opcional.

## 3. Estado de partida verificado

- v1 como base de corte: seções 1 e 2 (redes e mecanismos, 7 modelos, páginas 6 a 31), seções 3 e 4 (ABM e GABM, 32 a 46), seção 5 GitHub vazia, Metodologia 47 a 54.
- Revisão de metodologia (2026-10-07) com 3 achados críticos pendentes: representação do grafo indefinida, circularidade do ranking por estrelas e critérios conjuntos de validação inviáveis.
- Pendência anterior que entra na v2: citar `krakauer2026` e `wei2022` na introdução do tex (`kaplan2020` já citada na 4.3).
- Seção 4 tem stub pendente "Usos em redes complexas; Limitações e crítica" (linhas 720 a 722 do tex), que a v2 absorve dentro da síntese.
- Correções de texto da v1 a carregar: objetivo 3 diz "GABM" onde deve dizer DS1; Quadro 3 com artefatos de edição ($L(p)$$L(p)$ duplicado); "Quado 4"; dois parágrafos de fecho duplicados na seção 3.3 (linhas 592 e 594).
- Bib: todas as chaves planejadas para os dois tópicos novos conferidas em `refs.bib` (48 chaves, 2026-10-19). Nenhuma obra de sistemas sociotécnicos.
- Restrições permanentes do autor aplicam-se a toda escrita da v2: zero travessões (padrão de AI slop), acentuação correta, vocabulário já introduzido antes de uso em cada seção e terminologia congelada da introdução (roteador, triagem, assessor, primeiros estágios da cascata, DS1).

## 4. Estrutura e orçamento de páginas

| Seção | Páginas | Palavras | Derivada de | Operação |
|---|---|---|---|---|
| Introdução e Justificativa | 1,25 | 420 | v1 p. 3 a 4 | condensar; citar krakauer2026 e wei2022; aproximar DS1 sem duplicar 3.3; mover GitHub da intro para 3.4 |
| Objetivos | 0,50 | 170 | v1 p. 5 | parágrafo geral + 5 itens enxutos; corrigir GABM para DS1 |
| 3.1 Redes complexas e mecanismos de formação | 2,00 | 660 | v1 seções 1 e 2 | síntese com quadro comparativo único |
| 3.2 Da ABM aos agentes semânticos | 1,00 | 330 | v1 seções 3 e 4 + stub | fusão; fecha o stub |
| 3.3 Modelos de Decisão Sistema 1 | 1,00 | 340 | intro par. DS1 + bloco t_system1 do bib | NOVO |
| 3.4 GitHub como rede sociotécnica | 1,00 | 340 | intro par. GitHub + slides da apresentação | NOVO em redação |
| Metodologia | 1,25 | 420 | v1 metodologia + revisão | reescrita DS1 |
| Total de texto | 8,00 | ~2.700 | | |
| Referências | 2,00 | 45 a 65 chaves | | |
| Total | 10,00 | | | |

Calibração: estimativa de 350 palavras por página em 12pt com espaçamento 1,5 da abntex2. Confirmar na primeira compilação e redistribuir cortes se desviar.

## 5. Operação de compressão por seção

- 3.1 (a maior compressão da v2, de 26 para 2 páginas): prosa foca em ligação preferencial como mecanismo formativo central: Price (crescimento e vantagem cumulativa), Barabási-Albert (rigidez de $\alpha$, Vantagem do Pioneiro via $k_{i}(t)$, limites de agrupamento) e os mecanismos alternativos que sustentam a hipótese de decisão semântica: aptidão e otimização. Os 7 modelos passam para um quadro comparativo único com quatro colunas (modelo, premissa da formação, resultado, limitação), ocupando cerca de 0,5 página. Mantém-se obrigatoriamente: o modelo aleatório como referencial nulo; o debate da Lei da Potência contra log-normal de Broido e Clauset (fundamenta a validação); os desvios de cauda discutidos por Newman. Cortam-se: descrições passo a passo das simulações, equações de otimização estrutural (D'Souza e Cancho-Solé contam em um parágrafo cada, sem fórmula), gás de Bose em uma frase. Máximo de 3 equações: $\Pi(k)$, $P(k) \sim k^{-\gamma}$ e $k_{i}(t)$.
- 3.2: ABM em 1 parágrafo (definição e a distinção baixo para cima contra o campo médio); robustez em 1 parágrafo (dedução por Epstein, irredutibilidade computacional e equifinalidade como cautela validativa); limitações em bullets de 1 linha (regras se então, escolha racional irrealista, dupla filtragem dependente de ordenação, alto custo por chamada), fechando com a demanda da GABM. GABM e LLMs em 2 parágrafos: definição, capacidades emergentes (Lei da Escala, instrução, contexto) e as limitações que motivam o DS1: estocasticidade, alucinação, memória, custo e latência por decisão. Citações de formação de redes por GABM (demarzo2023, piao2025, papachristou2025, ji2025, ji2025b) ficam em 1 parágrafo introdutório do item.
- Cortes totais fora da v2: histórico da IA generativa (v1 4.1); arquitetura completa de agente (percepção, cérebro, ação com sub-listas); classes de Wolfram e teoremas de Azadi (1 frase cada se couber); percolação do componente gigante (2 frases).

## 6. Tópico novo 3.3: Modelos de Decisão Sistema 1

Cinco parágrafos, chaves já conferidas no bib:

1. Origem cognitiva: dualidade Sistema 1 e Sistema 2 na decisão humana \parencite{kahneman2003} e a analogia formal em IA \parencite{bengio2019, booch2021, goyal2022}.
2. Demanda técnica: LLMs caros, lentos e estocásticos como motor de micro-decisões tipificadas; economia por cascata de inferência \parencite{chen2023}; roteamento \parencite{ong2025} e papéis de triagem e assessor \parencite{nandakishore2026}.
3. Definição e mecânica da classe: modelos pequenos (1 a 4B de parâmetros) treinados para decisão tipificada sobre entrada semântica compacta, saída rápida e estável em temperatura 0; exemplos: Jev \parencite{typesafe2026} e Laya \parencite{laya2026}; adoção por Microsoft, Cloudflare e OpenAI \parencite{microsoft2026, cloudflare2026, openai2026}.
4. Consolidação da nomenclatura pós-Jev e reflexo na academia \parencite{santos2026}; fronteira da classe: modelos de decisão rápida não são LLMs juízes nem verificadores.
5. Fechamento argumentativo: a decisão de dar estrela é micro-decisão frequente, semântica e de baixa complexidade; requisitos de determinismo, custo e reprodutibilidade externa apontam DS1 como motor mais aderente que um LLM generativo; diferenças em relação à GABM declaradas e remetidas à metodologia.

Cuidado editorial: a introdução mantém apenas a história do rótulo (2 a 3 frases) com remessa para 3.3; o aprofundamento mecânico mora em 3.3. Nenhum travessão; vírgula no lugar.

## 7. Tópico redigido 3.4: GitHub como rede sociotécnica

Cinco parágrafos, chaves já conferidas no bib:

1. Objeto: GitHub como maior plataforma de hospedagem de código aberto \parencite{github2025, stackoverflow2025}: repositórios, colaboração e o mecanismo de estrela como expressão de apreciação.
2. A rede observável: grafo bipartido desenvolvedor x repositório com arestas de estrela; distribuição de grau seguindo Lei da Potência \parencite{borges2016, borges2018, gu2026}; efeito Mateus \parencite{merton1968}.
3. Defesa sociotécnica: nem fator social puro nem infraestrutura técnica pura explicam o formato. Lado social: curadoria humana, marketing técnico, comunidades e reputação. Lado técnico: busca, ordenação de resultados, README, forks \parencite{jiang2017}, API e automações \parencite{he2025b}. Âncora conceitual: sociomaterialidade, prática social e tecnologia como mutuamente constitutivas \parencite{orlikowski2008}. Evidência do acoplamento: hubs e a fragilidade em ataques de cadeia de suprimento \parencite{saayman2026, dholakia2026} e esquemas fraudulentos de estrelas \parencite{he2025b}.
4. Observabilidade: registros públicos longitudinalmente completos via GH Archive \parencite{grigorik_gharchive}; estrelas como proxy de popularidade consolidada na literatura \parencite{borges2018}.
5. Ponte metodológica: a dimensão social demanda semântica (personas, temas, README); a dimensão técnica demanda motor determinístico e replicável (DS1); fecha preparando a hipótese: ligação preferencial pode emergir da combinação, ou mecanismos alternativos socialmente fundados.

Registro no bib: entrada de Orlikowski e Scott (2008) (Academy of Management Annals, 2(1), 433 a 474) com nota de reconstrução no cabeçalho até passagem completa pela biblioteca, como já praticado com outras chaves (vasquez2003, song2005, boccara2004). Trist (1981) como segunda entrada opcional.

## 8. Metodologia reescrita com motor DS1

1. Objetivo observacional: grafo bipartido desenvolvedor x repositório com arestas dirigidas de estrela; popularidade como projeção unipartida; decisão modelada: WatchEvent diante de conjuntos descobertos (trata o achado 1 da revisão: sem essa definição, comparar com Barabási-Albert unipartido não se sustenta).
2. Recorte (1 parágrafo): repositórios públicos criados de janeiro/2024 a abril/2026; exclusões de vazios, forks, bots, não-software (classificação semântica com precisão e recall reportados) e atividade mínima (2 commits em 30 dias) tratada como hipótese de corte a testar em sensibilidade; README versionado contra viés de sobrevivência.
3. Motor: DS1 local (Jebadiah 4B v2, quantização Q8, hash travado, temperatura 0, seed fixa), justificado por redundância triângular: restrição de hardware, benchmark independente e medição própria na biblioteca (90,3% de acordo, determinismo total, robustez à inversão de ordem), com ressalvas declaradas (verdade de referência = banco curado; ordens de referência do teste).
4. Simulação em 2 etapas: descoberta por similaridade semântica no banco vetorial (top m); avaliação em cascata \parencite{craswell2008}; decisão de estrela pelo motor DS1. Controle para o achado 2: condição comparativa sem sinal de popularidade (ordenação só por similaridade, contagem de estrelas escondida) contra a condição com contagem visível, isolando se o padrão vem da decisão semântica ou da exposição de popularidade.
5. Validação hierarquizada (achado 3): critério primário: $P(\text{conectar} | \text{grau relativo})$ proporcional ao grau relativo; critérios secundários: ajuste de Lei da Potência pela proposta Clauset e comparativa log-normal \parencite{broido2019}; KS como teste descritivo, não como prova de equivalência; TOST com margem pré-registrada antes da execução; sensibilidade (agentes, top m, corte de atividade).
6. Reprodutibilidade: protocolo ODD \parencite{grimm2006}, versão e hash do modelo, temperatura, seed, prompts versionados e repositório com logs de decisão.
7. Estabilidade do motor, herdando o lembrete de 2026-10-15: decisões repetidas N vezes sob condições idênticas, ordem embaralhada e opções A e B invertidas, medindo taxa de troca e variação máxima de probabilidade; sustenta que o critério primário herda estabilidade do motor.
8. Viabilidade: execução local em uma RTX 3050 6GB (Jebadiah Q8 cabe na VRAM), custo nulo de API, fase IV reprodutível off-line.

Regras de escrita: prosa curta unificada, sem sub-listas de 3 níveis como na v1; cada fase em 2 a 4 frases; plataformas BigQuery, ClickHouse e Snowflake comprimidas em 1 frase.

## 9. Pendências carregadas da v1

- Citar krakauer2026 e wei2022 na introdução (ação posterior registrada em 2026-10-17).
- Corrigir objetivo 3: trocar GABM por DS1 (ou por a abordagem, se a redação pedir).
- Zerar os dois fechos duplicados da 3.3 da v1 (a v2 mantém um).
- Não reusar o Quadro 3 com artefatos e corrigir depois "Quado 4".
- Concretizar o stub "Usos em redes complexas; Limitações e crítica" dentro da 3.2 compactada.

## 10. Arquitetura de arquivos

- Novo documento: `latex/plano-abnt-v2.tex`, derivado do preâmbulo da v1, sem \imprimircapa, sem \imprimirfolhaderosto e sem \tableofcontents.
- `refs.bib` único compartilhado; biber imprime só o citado; entradas novas recebem marcador de reconstrução no cabeçalho.
- `plano-abnt-v2.bat` espelhando o bat da v1.
- v1 permanece intocado como referência; o README do latex recebe uma linha sobre a v2 após a primeira compilação bem-sucedida.
- Pipeline docx fica para depois: o mestre da v2 é o tex até nova decisão; se o Google Doc voltar a ser mestre, ajusta-se `code/build_abnt.py` para a variante sem capa.

## 11. Critérios de verificação

1. Compilação: pdflatex, biber, pdflatex, pdflatex; zero chaves perdidas e zero erros.
2. Página: páginas até o fim da metodologia mais referências somam 10 ou menos, medida no PDF final.
3. Travessões: zero ocorrências dos caracteres de travessão em e en no tex v2, incluindo sequências de hífen do LaTeX, que contam como violação do padrão também.
4. Referências impressas entre 45 e 70.
5. Achados críticos da revisão endereçados nominalmente na metodologia (grafo bipartido, controle de popularidade, hierarquia de validação com margem TOST e alternativa log-normal).
6. Terminologia consistente: DS1 com expansão única na primeira ocorrência; GABM apenas nos parágrafos históricos; nenhuma duplicação entre intro e 3.3; vocabulário de cada seção introduzido antes de uso.

## 12. Ordem de execução

1. Esqueleto do plano-abnt-v2.tex (preâmbulo, título, seções vazias).
2. Redação do tópico novo 3.3 (DS1): o de maior risco editorial e sem dependências, por isso começa.
3. Redação de 3.4 (GitHub sociotécnica) com entrada de `orlikowski2008` no bib.
4. Redação da introdução e dos objetivos citando krakauer2026 e wei2022.
5. Compressão de 3.1 e 3.2 (v1 vira matéria-prima).
6. Reescrita da metodologia com motor e controles já decididos; conferir viabilidade de custo antes do fechamento.
7. Scans de travessões, compilação, contagem de páginas e ajuste de orçamento; atualização de README; relatório das notas do dia.

## 13. Riscos e mitigação

- Estouro de página: cortar nessa ordem: parágrafos de otimização de 3.1, detalhes de robustez da 3.2, operacionalização da coleta na metodologia; quadro comparativo é a última coisa a crescer.
- Introdução e 3.3 duplicados: compor a introdução com apenas 2 a 3 frases de história do rótulo DS1.
- Chave nova sem conferência: nenhuma chave entra nos tópicos novos antes de conferência no refs.bib; fontes técnicas de blog (benchmark do Jebadiah) entram só como evidência de apoio triangulada, nunca como autoridade única.
- Chave reconstruída sem PDF (orlikowski2008): marcar no cabeçalho do bib como reconstruída e verificar pelo DOI assim que possível.
- Classificação software ou não-software operada por LLM na v1 contradiz a coerência do motor: na v2, a tarefa vai para o próprio DS1, com precisão e recall reportados em amostra de validação.
