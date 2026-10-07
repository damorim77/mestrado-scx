# LaTeX — Plano SCX

- `plano-abnt.tex` = **versão atual**: classe `abntex2`, 133 equações em LaTeX nativo
  (zero `\includegraphics`), citações via `\cite`/`\citeonline` (`abntex2cite alf`).
- `refs.bib` = **bibliografia** (133 entradas; 4 reconstruídas e marcadas no cabeçalho —
  confirmar: `vasquez2003`, `song2005`, `boccara2004`, `wolfram2022`).
- `plano-abnt.pdf` = saída compilada (pdflatex + bibtex + pdflatex + pdflatex).
- Geradores reproduzíveis: `code/docx_to_latex_v2.py` (docx→v2) → `code/build_abnt.py` +
  `code/eq_map.py` (v2→abnt). Intermediários (`plano.tex`, `plano-v2.tex`, `media/`) removidos;
  o conversor reextrai do docx se preciso.
- Detalhes de compilação e capa/folha: ver cabeçalho do `.tex` e `notes/2026-10-07.md`.
