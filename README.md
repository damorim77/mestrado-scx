# mestrado-scx

Dissertação de mestrado (PPG Modelagem em Sistemas Complexos, USP): reproduzir a formação de redes livres de escala com agentes semânticos, usando a rede de estrelas do GitHub.

Base: versão 2 do plano de pesquisa (`latex/plano-abnt-v2.tex`), usada como ponto de partida deste repositório. O histórico anterior (open-science) não foi trazido.

## Layout

| Caminho | Conteúdo |
| --- | --- |
| `latex/` | fonte do plano v2 (`plano-abnt-v2.tex`), bibliografia (`refs.bib`) e compilação (`plano-abnt-v2.bat`) |
| `plano-v2.md` | roteiro da v2 (2026-10-19), defasado em relação ao `.tex` |
| `knowledge/current-state.md` | objetivo, estágio e próxima ação |
| `notes/` | diário por data (uma entrada por dia de trabalho) |

## Compilação

Dentro de `latex/`: `plano-abnt-v2.bat`, ou `pdflatex`, `biber`, `pdflatex`, `pdflatex`. Requer MiKTeX ou TeX Live com `abntex2` e `biblatex-abnt`.
