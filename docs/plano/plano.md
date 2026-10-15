# Dissertação — GABM para Redes Livres de Escala (GitHub Stars)

Título: Emergência de Redes Livres de Escala com Agentes Generativos de IA para Estudo de Popularidade de Repositórios GitHub

Documento-fonte: https://docs.google.com/document/d/1V1k3MfRpjuXqxRWYStj0OAKlSZ9q4n5IYPRUTWH0ZmA/edit?usp=sharing (Plano de Pesquisa SCX v1)
Estágio: proposta inicial | Foco de revisão: metodologia e análise

## Pergunta
GABM reproduz propriedades macroscópicas livres de escala a partir de decisões microscópicas autônomas, com verossimilhança a dados reais vs. modelos clássicos (sobretudo Barabási-Albert 1999)?

## Estrutura deste workspace
- `docs/` — plano resumido, revisão de metodologia, decisões
- `data/raw/` — GH Archive / API GitHub (não commitar arquivos grandes)
- `data/processed/` — base filtrada, embeddings, vetores
- `code/` — coleta, pós-processamento, simulação Concordia, validação
- `results/figures/`, `results/tables/` — saídas verificáveis
- `notes/` — diário; `knowledge/` — fatos atuais

## Fases (conforme plano)
- Fase I: extração (GH Archive + API + temas)
- Fase II: pós-processamento + enriquecimento semântico (jina-code-embeddings, ChromaDB/LanceDB)
- Fase III: simulação GABM (Concordia, descoberta em 2 etapas + cascata)
- Fase IV: validação (Clauset et al. 2009, P(conectar|grau), KS + TOST, sensibilidade)

## 3 bloqueadores (ver docs/revisao-metodologia.md)
1. Formalizar grafo bipartido desenvolvedor→repositório vs. BA unipartite.
2. Controle sem ranking por estrelas para evitar circularidade.
3. Hierarquizar critérios de validação (margem TOST, alternativa log-normal).
