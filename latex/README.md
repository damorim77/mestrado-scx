# LaTeX — Plano SCX

- `plano-abnt-v2.tex` = **versão 2 em produção**: conteúdo completo (Introdução,
  Objetivos, Referencial com Quadro 1, DS1 em 3.3, GitHub sociotécnica em 3.4,
  Metodologia com motor DS1); compilação limpa de 19 páginas (10 de texto + 9 de
  referências, 86 chaves); bat `plano-abnt-v2.bat`.
  Orçamento de 10 páginas ao todo pendente de decisão de corte.
- `plano-abnt.tex` = versão atual: classe `abntex2`, 133 equações em LaTeX nativo
  (zero `\includegraphics`), citações via `\cite`/`\citeonline` (`abntex2cite alf`).
- `refs.bib` = **bibliografia** (133 entradas; 4 reconstruídas e marcadas no cabeçalho —
  confirmar: `vasquez2003`, `song2005`, `boccara2004`, `wolfram2022`).
- `plano-abnt.pdf` = saída compilada (pdflatex + biber + pdflatex + pdflatex).
- `plano-abnt.bat` = compila tudo com duplo-clique (configura o PATH do MiKTeX sozinho).
- Citações: `\textcite` (narrativa "Sobrenome (ano)") vs `\parencite` (parentética
  "(SOBRENOME, ano)"); a diferença exige a opção `accite` do biblatex — ver regra no README raiz.
- Geradores reproduzíveis: `code/docx_to_latex_v2.py` (docx→v2) → `code/build_abnt.py` +
  `code/eq_map.py` (v2→abnt). Intermediários (`plano.tex`, `plano-v2.tex`, `media/`) removidos;
  o conversor reextrai do docx se preciso.
- Detalhes de compilação e capa/folha: ver cabeçalho do `.tex` e `notes/2026-10-07.md`.
