"""Gera docs/latex/plano-abnt.tex: abntex2 + equações nativas.
Uso: C:\\Python312\\python.exe code/build_abnt.py
"""
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eq_map import MAP

BASE = Path(r"C:\Users\danil\OneDrive\Documents\OpenScience\sessions\2026-10-07-0919\docs\latex")
SRC = BASE / "plano-v2.tex"
DST = BASE / "plano-abnt.tex"

INC = re.compile(r"\\includegraphics\[height=2\.2ex\]\{([^}]+)\}")

PRE = r"""% Plano SCX v1 — versão ABNT (abntex2) com equações em LaTeX nativo.
% Gerado por code/build_abnt.py a partir de plano-v2.tex + code/eq_map.py.
% Compilar (Overleaf ou TeX Live/MiKTeX com abntex2): pdflatex plano-abnt.tex
\documentclass[12pt,oneside,a4paper,brazil,sumario=tradicional]{abntex2}
\usepackage{amsmath,amssymb}
\usepackage{indentfirst}
\usepackage{booktabs,array,longtable}
\usepackage{graphicx}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
% abntex2 já carrega babel, hyperref, geometry e setspace
\graphicspath{{media/}}

% --- CAPA / FOLHA DE ROSTO ---
\instituicao{Universidade de São Paulo}
\autor{Danilo Lindemberg Amorim}
\titulo{Emergência de Redes Livres de Escala com Agentes Generativos de IA para Estudo de Popularidade de Repositórios GitHub}
\local{São Paulo, SP}
\data{2026}
\tipotrabalho{Plano de pesquisa (dissertação de mestrado)}
\preambulo{Plano de pesquisa apresentado ao Programa de Pós-Graduação em Modelagem em Sistemas Complexos da Universidade de São Paulo como requisito parcial de qualificação.}

\begin{document}
\selectlanguage{brazil}
\frenchspacing
\imprimircapa
\imprimirfolhaderosto
\tableofcontents
\clearpage
\textual
\markboth{}{}% seções com * não atualizam cabeçalhos; limpa "SUMÁRIO" das páginas do texto
"""

# Artefatos de conversão docx (frases duplicadas ao redor de equações-imagem).
# Cada par: (trecho com duplicação, forma limpa). Verificado contra o docx.
CLEANUPS = [
("onde cada um dos $n$ nó s se conecta aos seus $k$ vizinhos mais próximos.$n$ nó s se conecta aos seus $k$ vizinhos mais próximos.",
 "onde cada um dos $n$ nós se conecta aos seus $k$ vizinhos mais próximos."),
("e aplicam-se restrições mínimas como formações de arestas de um nó consigo mesmo, e arestas duplicadas entre dois nós.$0 < p < 1$, e aplicam-se restrições mínimas como formações de arestas de um nó consigo mesmo, e arestas duplicadas entre dois nós.",
 "e aplicam-se restrições mínimas como formações de arestas de um nó consigo mesmo e arestas duplicadas entre dois nós."),
("Iniciar com $m_{0}$ nós conectados entre si$m_{0}$ nós conectados entre si",
 "Iniciar com $m_{0}$ nós conectados entre si"),
("A cada passo temporal $t$, adicionar um novo nó$t$, adicionar um novo nó",
 "A cada passo temporal $t$, adicionar um novo nó"),
("conectando-se a $m$ nós existentes (com $m \\le m_{0}$)$n$ cria $m$ arestas, conectando-se a $m$ nós existentes (com $m \\le m_{0}$)",
 "conectando-se a $m$ nós existentes (com $m \\le m_{0}$)"),
("definida por: $\\Pi(k_{i}) = k_{i} / \\sum_{j} k_{j}$$n$",
 "definida por:\n\\[\\Pi(k_{i}) = k_{i} / \\sum_{j} k_{j}\\]"),
]

def convert_line(ln: str, missing: set) -> str:
    files = INC.findall(ln)
    for f in files:
        if f not in MAP:
            missing.add(f)
    stripped = INC.sub("", ln).strip()
    if files and not stripped:
        # linha só com imagem(ns): equação display
        cores = " \\quad ".join(MAP.get(f, r"\textbf{[EQ: %s]}" % f) for f in files)
        return "\\[" + cores + "\\]"
    def repl(m):
        f = m.group(1)
        return "$" + MAP.get(f, r"\textbf{[EQ: %s]}" % f) + "$"
    return INC.sub(repl, ln)

def main() -> None:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    # localiza \begin{document} do v2 e descarta preâmbulo/capa antigos
    try:
        bi = next(i for i, l in enumerate(lines) if l.strip() == r"\begin{document}")
    except StopIteration:
        raise SystemExit("plano-v2.tex sem \\begin{document}")
    body = lines[bi + 1:]
    # remove comandos de título do v2 (vão para capa/folha) e restos da 1ª página
    drop_exact = {r"\maketitle", r"\tableofcontents", r"\newpage", r"\end{document}",
                  r"\date{}", "Plano de Pesquisa"}
    body = [l for l in body
            if l.strip() not in drop_exact
            and not l.strip().startswith((r"\title{", r"\author{"))]
    # descarta linha de título repetida fora de comando (se houver)
    missing: set[str] = set()
    out = [PRE]
    # aceita section com ou sem * (a regen do v2 perde o *); sempre emite
    # starred + addcontentsline para preservar a numeração manual do Word
    secpat = re.compile(r"\\(sub)*section\*?\{(.+)\}")
    for ln in body:
        m = secpat.match(ln.strip())
        if m:
            depth = m.group(0).count("sub")
            level = ["section", "subsection", "subsubsection"][min(depth, 2)]
            title = m.group(2)
            out.append("\\%s*{%s}\\addcontentsline{toc}{%s}{%s}" % (level, title, level, title))
            continue
        out.append(convert_line(ln, missing))
    out.append("")
    out.append(r"\postextual")
    out.append(r"% Referências acima estão em texto corrido (seção Referências Bibliográficas).")
    out.append(r"% TODO: migrar para .bib + abntex2cite (altere para \bibliography{refs}).")
    out.append(r"\end{document}")
    text = "\n".join(out)
    text = unicodedata.normalize("NFC", text)
    text = text.replace("≈", "$\\approx$")
    nfix = 0
    for old, new in CLEANUPS:
        if old in text:
            text = text.replace(old, new)
            nfix += 1
        else:
            print("AVISO: cleanup não encontrado:", old[:60])
    print("cleanups aplicados:", nfix, "/", len(CLEANUPS))
    # display dentro de lista precisa de \item (docx numera a equação como item);
    # roda DEPOIS dos cleanups porque o cleanup 6 cria um display novo
    fixed, ldepth = [], 0
    for ln in text.splitlines():
        s = ln.strip()
        if s in (r"\begin{itemize}", r"\begin{enumerate}"):
            ldepth += 1
        elif s in (r"\end{itemize}", r"\end{enumerate}"):
            ldepth -= 1
        elif ldepth and s.startswith(r"\["):
            ln = "  \\item[] " + s
        fixed.append(ln)
    text = "\n".join(fixed)
    DST.write_text(text, encoding="utf-8")
    print("OK:", DST, DST.stat().st_size, "bytes")
    print("imagens sem mapeamento:", sorted(missing) if missing else "nenhuma")
    rest = INC.search(DST.read_text(encoding="utf-8"))
    print("includegraphics restantes:", "SIM — revisar" if rest else "zero")

if __name__ == "__main__":
    main()
