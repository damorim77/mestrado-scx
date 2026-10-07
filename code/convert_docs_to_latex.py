"""Converte o export txt do Google Docs (SCX v1) em um .tex inicial.
Uso: C:\\Python312\\python.exe code/convert_docs_to_latex.py
Entrada: tool-output do webfetch (640 linhas); Saida: docs/latex/plano.tex
Limitacoes conhecidas: formulas/equacoes e tabelas (Quadros) se perderam no
export txt e viram placeholders [EQUACAO]/[QUADRO] para conferir no Docs.
"""
import re
from pathlib import Path

SRC = Path(r"C:\Users\danil\AppData\Roaming\com.ai4s.workbench\runtime\xdg-data\opencode\tool-output\tool_11650ce7b001F5RRV2G5727snP")
DST = Path(r"C:\Users\danil\OneDrive\Documents\OpenScience\sessions\2026-10-07-0919\docs\latex\plano.tex")

SECTION_EXACT = {
    "Introdução e Justificativa": "section",
    "Objetivos": "section",
    "Revisão Bibliográfica": "section",
    "Metodologia": "section",
    "Referências Bibliográficas": "section",
}

def escape(s: str) -> str:
    s = s.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                 ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciircum{}")]:
        s = s.replace(a, b)
    return s

def convert() -> None:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    # remove linha 1 vazia/lixo se houver; mantem a partir de "Plano de Pesquisa"
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "Plano de Pesquisa")
        lines = lines[start:]
    except StopIteration:
        pass

    out: list[str] = []
    out.append("% Gerado automaticamente a partir do Google Docs (export txt) — v1 inicial.")
    out.append("% ATENCAO: equacoes e Quadros se perderam no txt; conferir no Docs original.")
    out.append("% Compilar com: xelatex plano.tex (ou pdflatex com \\usepackage[utf8]{inputenc}).")
    out.append(r"\documentclass[12pt,a4paper]{article}")
    out.append(r"\usepackage[brazil]{babel}")
    out.append(r"\usepackage{fontspec}")
    out.append(r"\usepackage{csquotes}")
    out.append(r"\usepackage{hyperref}")
    out.append(r"\usepackage{graphicx}")
    out.append(r"\usepackage{booktabs}")
    out.append(r"\usepackage{geometry}")
    out.append(r"\geometry{margin=3cm}")
    out.append(r"\usepackage{setspace}")
    out.append(r"\onehalfspacing")
    out.append(r"\title{Emergência de Redes Livres de Escala com Agentes Generativos de IA\\ Para Estudo de Popularidade de Repositórios GitHub}")
    out.append(r"\author{Plano de Pesquisa SCX v1 — convertido do Google Docs}")
    out.append(r"\date{}")
    out.append(r"\begin{document}")
    out.append(r"\maketitle")
    out.append(r"\tableofcontents")
    out.append(r"\newpage")

    in_itemize = False
    in_refs = False

    def close_items():
        nonlocal in_itemize
        if in_itemize:
            out.append(r"\end{itemize}")
            in_itemize = False

    num_sec = re.compile(r"^(\d+(?:\.\d+){0,2})\.?\s+(.+)$")

    for raw in lines[2:]:  # pula "Plano de Pesquisa" + titulo
        s = raw.strip()
        if not s:
            close_items()
            out.append("")
            continue
        if s in ("Plano de Pesquisa", lines[1].strip() if len(lines) > 1 else ""):
            continue
        # secao exata
        if s in SECTION_EXACT and len(s) < 60:
            close_items()
            if s == "Referências Bibliográficas":
                in_refs = True
                out.append(r"\section{Referências Bibliográficas}")
                out.append(r"{\footnotesize")
            else:
                out.append(r"\section{" + escape(s) + "}")
            continue
        # numeradas tipo "1. Conceitos", "2.1.3. Modelo ..."
        m = num_sec.match(s)
        if m and len(s) < 120 and not in_refs:
            close_items()
            num, title = m.group(1), m.group(2)
            depth = num.count(".")
            cmd = "section" if depth == 0 else ("subsection" if depth == 1 else "subsubsection")
            out.append(r"\%s{%s — %s}" % (cmd, escape(num), escape(title)))
            continue
        # bullets "* ..." (objetivos, listas)
        if s.startswith("* ") or s.startswith("• "):
            item = escape(s[2:].strip())
            if not in_itemize:
                out.append(r"\begin{itemize}")
                in_itemize = True
            out.append(r"  \item " + item)
            continue
        # itens numerados internos da metodologia ("1. Conectar-se...", "1. Grafo em estrela")
        if re.match(r"^\d+\.\s+\S+", s) and len(s) < 300 and not in_refs:
            close_items()
            out.append(r"\paragraph{" + escape(s.split(".", 1)[0]) + ".} " + escape(s.split(".", 1)[1].strip()))
            continue
        # quadros
        if s.startswith("Quadro ") or s.startswith("Quado "):
            close_items()
            out.append(r"\begin{center}\textbf{" + escape(s) + r"}\\[0.3em]{\small [QUADRO — tabela original no Google Docs; reconstruir com tabular/booktabs]}\end{center}")
            continue
        if s.startswith("Fonte:"):
            out.append(r"{\small \textit{" + escape(s) + "}}")
            continue
        # referencias: cada linha vira paragrafo pequeno pendente
        if in_refs:
            out.append(r"\hangindent=1.5em " + escape(s) + r"\\[0.3em]")
            continue
        # marca provavel formula perdida: parenteses vazios ou simbolos isolados
        mark = s
        if re.search(r"\(\s*\)|\(\s*[a-zA-Z]\s*\)|\b\d*\s*[mMpPkK]\b.*\(.*\)", s) and len(s) < 80:
            pass
        # paragrafo normal; sinaliza trechos com lacunas de simbolos
        if re.search(r"\(\s{2,}\)|Modelo [AB] \(\s*\)|dada por:\s*$", s):
            out.append(escape(s) + " " + r"\textbf{[EQUAÇÃO — verificar no Docs original]}")
        else:
            out.append(escape(s) + "\n")
            out.append("")

    close_items()
    if in_refs:
        out.append("}")
    out.append(r"\end{document}")

    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text("\n".join(out), encoding="utf-8")
    print(f"OK: {DST} ({DST.stat().st_size} bytes, {len(out)} linhas latex)")

if __name__ == "__main__":
    convert()
