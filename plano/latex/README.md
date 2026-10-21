# LaTeX do plano

- `plano-abnt.tex`: fonte do plano de pesquisa.
- `refs.bib`: bibliografia (uma única base para o plano).
- `plano-abnt.bat`: compila tudo com duplo-clique (configura o PATH do MiKTeX).
- `plano-abnt.pdf`: saída compilada; regenerada pelo `.bat` após edições.

Citações: `\textcite` (narrativa, "Sobrenome (ano)") e `\parencite` (parentética, "(SOBRENOME, ano)"). Exige a opção `accite` do biblatex.
Nova entrada no `.bib`: chave `sobrenome ano`, sobrenome em Title Case, `year = {s.d.}` (sem colchetes) quando não houver ano.
