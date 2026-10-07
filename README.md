# mestrado-scx — GABM para Redes Livres de Escala (GitHub Stars)

Dissertação de mestrado (PPG Modelagem em Sistemas Complexos, USP): validar empiricamente a
metodologia GABM como ferramenta para simular a emergência de redes livres de escala,
comparando resultados e mecanismos com os modelos clássicos (sobretudo Barabási–Albert 1999).

**Pergunta:** a GABM reproduz propriedades macroscópicas livres de escala a partir de decisões
microscópicas autônomas, com verossimilhança a dados reais vs. modelos clássicos?

## Fases do plano (`docs/plano.md`)

- **Fase I** — extração (GH Archive + API GitHub + temas)
- **Fase II** — pós-processamento + enriquecimento semântico (embeddings, ChromaDB/LanceDB)
- **Fase III** — simulação GABM (Concordia, descoberta em 2 etapas + cascata)
- **Fase IV** — validação (Clauset et al. 2009, P(conectar|grau), KS + TOST, sensibilidade)

Ver `docs/revisao-metodologia.md` (3 bloqueadores: grafo bipartido, circularidade do ranking,
critérios de validação).

## Layout

| Caminho | Conteúdo |
| --- | --- |
| `docs/plano.md` | resumo do plano e pergunta |
| `docs/revisao-metodologia.md` | revisão com bloqueadores e recomendações |
| `docs/latex/plano-abnt.tex` | **versão atual do texto** (abntex2) |
| `docs/latex/refs.bib` | **bibliografia BibTeX** (133 entradas, estilo `abntex2cite alf`) |
| `docs/latex/plano-abnt.pdf` | PDF compilado |
| `code/` | pipeline: `docx_to_latex_v2.py`, `eq_map.py`, `build_abnt.py`, `convert_docs_to_latex.py` |
| `data/raw/`, `data/processed/` | dados GH Archive / base filtrada (não commitar arquivos grandes) |
| `results/figures/`, `results/tables/` | saídas verificáveis |
| `knowledge/` | fatos atuais (`current-state.md` = objetivo e próximos passos) |
| `notes/` | diário por data |

## Escrevendo e citando (biblatex-abnt + biber)

- Texto em `docs/latex/plano-abnt.tex`; referências em `docs/latex/refs.bib`.
- **Regra de ouro (ABNT): só o ano entre parênteses → narrativa; autores também entre
  parênteses → MAIÚSCULAS** (`et al.` sempre minúsculo e itálico, automático):
  - Narrativa: `\textcite{chave}` → "Sobrenome (ano)". Ex.: `\textcite{barabasi1999}`
  - Parentética: `\parencite{chave}` → "(SOBRENOME, ano)". Ex.: `\parencite{newman2003}`
  - Múltiplas: `\parencite{chave1, chave2}`. Com página: `\textcite[p.~25]{chave}`
- A distinção maiúscula/minúscula depende da opção `accite` no preâmbulo
  (`\usepackage[...,accite]{biblatex}`) — não remover.
- Nova entrada mínima no `.bib` (chave única `sobrenomeano`, **sobrenome em Title Case** —
  o estilo põe maiúscula sozinho onde a ABNT exige):
  `@misc{sobrenome2026, author = {Nome Sobrenome and others}, title = {...}, year = {2026}, url = {...}, urldate = {2026-10-07}}`
- Autor corporativo: `author = {{ORG}}` (chaves duplas); sem data: `year = {s.d.}` (sem colchetes);
  `urldate` sempre ISO (`aaaa-mm-dd`).
- Toda chave citada precisa existir no `.bib`, senão sai `[?]` no PDF.

## Compilando (em `docs/latex/`)

```sh
pdflatex plano-abnt.tex; biber plano-abnt; pdflatex plano-abnt.tex; pdflatex plano-abnt.tex
```

Requer MiKTeX/TeX Live com `abntex2` (no Windows: `AppData/Local/Programs/MiKTeX/miktex/bin/x64` no PATH).

## Agente (`AGENTS.md`)

Este repo usa o loop `evolve-agent`: declarar objetivo, checar estado, menor mudança
verificável, registrar lição em `notes/` a cada ciclo.
