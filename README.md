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

## Escrevendo e citando

- Texto em `docs/latex/plano-abnt.tex`; referências em `docs/latex/refs.bib`.
- Citação parentética: `\cite{chave}` → "(SOBRENOME, ano)".
  Narrativa: `\citeonline{chave}` → "Sobrenome (ano)". Múltiplas: `\cite{chave1, chave2}`.
- Nova entrada mínima no `.bib` (chave única `sobrenomeano`):
  `@misc{sobrenome2026, author = {Nome SOBRENOME and others}, title = {...}, year = {2026}, url = {...}, urldate = {...}}`
- Autor corporativo: `author = {{ORG}}`; sem data: `year = {s.d.}` (sem colchetes).
- Toda `\cite{chave}` precisa existir no `.bib`, senão sai `[?]` no PDF.

## Compilando (em `docs/latex/`)

```sh
pdflatex plano-abnt.tex; bibtex plano-abnt; pdflatex plano-abnt.tex; pdflatex plano-abnt.tex
```

Requer MiKTeX/TeX Live com `abntex2` (no Windows: `AppData/Local/Programs/MiKTeX/miktex/bin/x64` no PATH).

## Agente (`AGENTS.md`)

Este repo usa o loop `evolve-agent`: declarar objetivo, checar estado, menor mudança
verificável, registrar lição em `notes/` a cada ciclo.
