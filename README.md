# mestrado-scx

Dissertação de mestrado (PPG Modelagem em Sistemas Complexos, USP): reproduzir a formação de redes livres de escala com agentes semânticos, usando a rede de estrelas do GitHub.

Este repositório começou a partir da versão 2 do plano de pesquisa. O histórico anterior, do open-science, não foi trazido.

## Layout

| Caminho | Conteúdo |
| --- | --- |
| `plano/` | tudo que se refere ao plano de pesquisa |
| `plano/latex/` | fonte do plano (`plano-abnt.tex`), bibliografia (`refs.bib`) e compilação (`plano-abnt.bat`) |

## Compilação

Dentro de `plano/latex/`: `plano-abnt.bat`, ou `pdflatex`, `biber`, `pdflatex`, `pdflatex`. Requer MiKTeX ou TeX Live com `abntex2` e `biblatex-abnt`.
