# Revisão de Metodologia — 2026-10-07

Fonte: Plano de Pesquisa SCX v1 (Google Docs, export txt).

## Pontos fortes
- Pergunta coerente pergunta→método→análise; comparativos empírico / BA puro / aleatório.
- Recorte temporal 01/2024–04/2026 e filtros (vazios, forks, bots `[bot]`, não-software via LLM, atividade mínima 2 commits/30d) mostram cuidado com vieses.
- Atenção a viés de sobrevivência do README e anonimização contra memorização da LLM.

## Achados críticos
1. **Representação do grafo indefinida.** BA = nó novo + m arestas a existentes. Stars = arestas novas entre nós já existentes (ambos os lados crescem + reativação). Definir: nós, arestas, crescimento, projeção. Sem isso, "Lei da Potência de estrelas" não é comparável a "distribuição de graus BA".
2. **Circularidade do ranking.** Reordenar top-m por estrelas + modelo cascata injeta ligação preferencial e depois testa sua emergência. Exigir controle: sem contagem visível / ordem aleatória / só similaridade.
3. **Critérios conjuntos impossíveis.** Clauset + gama em IC95% + KS não-rejeita + TOST rejeita + sensibilidade. KS não-rejeitar ≠ equivalência; TOST sem margem pré-registrada é vago. Hierarquizar primário/secundário e incluir alternativa log-normal (Broido-Clauset 2019, citado na própria revisão).

## Recomendações priorizadas
- [ ] Formalizar modelo bipartido temporal (schemas de WatchEvent/CreateEvent, janela mensal, 28 passos).
- [ ] Desenhar experimento controle com/sem sinal de popularidade.
- [ ] Estimar viabilidade: N agentes, chamadas LLM/mês, custo Concordia, amostragem estratificada.
- [ ] Fixar protocolo reprodutibilidade: modelo/versão, temperatura, seeds, prompts versionados, ODD, logs de raciocínio.
- [ ] Validar classificador software/não-software (precisão/recall) e filtros (sensibilidade a 2 commits/30d).
- [ ] Reduzir escopo para 3 entregáveis de mestrado: pipeline dados+embeddings, simulação mínima com controle, comparação Clauset+mecanismo.

## Seções a completar no Doc
Usos em redes complexas; Limitações e crítica; 5. GitHub e Redes Sociotécnicas.
