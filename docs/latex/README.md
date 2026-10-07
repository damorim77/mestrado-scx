# LaTeX — Plano SCX v1

- `plano-abnt.tex` = **versão atual**: classe `abntex2` (capa + folha de rosto com campos `[PREENCHER]`, sumário, `\\textual`/`\\postextual`) e **133/133 imagens-equação convertidas em LaTeX nativo** (14 display `\\[...\\]`, resto inline `$...$`; zero `\\includegraphics`).
  - Geradores reproduzíveis: `code/docx_to_latex_v2.py` (docx→v2) → `code/build_abnt.py` + `code/eq_map.py` (v2→abnt).
  - Compilação: `pdflatex plano-abnt.tex` (Overleaf ou TeX Live/MiKTeX com `abntex2`); `media/` não é mais necessária.
- `plano-v2.tex` = versão fiel intermediária (com imagens em `media/`); `plano.tex` = v1 via txt (obsoleta).
- Conferir no PDF: Quadros 1–4 (largura `p{4cm}` pode precisar de ajuste),(labels `image192=u` — no Holme-Kim original o nó é `w`; `C_t` vs `c_t` em D'Souza; `P(k)` vs `\\Pi(k)` herdados do Word), 5 frases-duplicadas do docx já removidas (ver `CLEANUPS` em `build_abnt.py`), e preencher capa/folha de rosto.
- TODO: migrar referências para `.bib` + `abntex2cite`.
