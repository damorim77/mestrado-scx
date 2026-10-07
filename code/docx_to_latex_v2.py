"""Converte o docx do Plano SCX v1 em LaTeX v2 fiel.
Preserva: Title/Heading1-3, negrito/italico, links, listas, 4 tabelas (Quadros)
e 133 imagens (equacoes como PNG/GIF) extraidas para docs/latex/media/.
Uso: C:\\Python312\\python.exe code/docx_to_latex_v2.py
"""
import re
import shutil
import zipfile
from pathlib import Path
from lxml import etree

SRC = Path(r"C:\Users\danil\Downloads\Plano de Pesquisa SCX v1.docx")
DST = Path(r"C:\Users\danil\OneDrive\Documents\OpenScience\sessions\2026-10-07-0919\docs\latex\plano-v2.tex")
MEDIA_DST = DST.parent / "media"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "a": A, "wp": WP, "r": R}


def esc(s: str) -> str:
    s = s.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                 ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciircum{}")]:
        s = s.replace(a, b)
    return s


def main() -> None:
    z = zipfile.ZipFile(SRC)
    doc_xml = z.read("word/document.xml")
    rels_xml = z.read("word/_rels/document.xml.rels")
    root = etree.fromstring(doc_xml)
    rels = etree.fromstring(rels_xml)
    rid_to_media = {}
    for rel in rels:
        rid = rel.get("Id")
        tgt = rel.get("Target", "")
        if tgt.startswith("media/"):
            rid_to_media[rid] = tgt.split("/")[-1]

    # extrai midias
    MEDIA_DST.mkdir(parents=True, exist_ok=True)
    for name in z.namelist():
        if name.startswith("word/media/"):
            dest = MEDIA_DST / Path(name).name
            if not dest.exists():
                dest.write_bytes(z.read(name))

    body = root.find("w:body", NS)
    out: list[str] = [
        "% Plano SCX v1 — conversao fiel do docx (v2).",
        "% Tabelas e imagens (equacoes) preservadas; revisar numeracao e ABNT.",
        r"\documentclass[12pt,a4paper]{article}",
        r"\usepackage[brazil]{babel}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{lmodern}",
        r"\usepackage{csquotes}",
        r"\usepackage{hyperref}",
        r"\usepackage{graphicx}",
        r"\usepackage{booktabs}",
        r"\usepackage{array}",
        r"\usepackage{longtable}",
        r"\usepackage{geometry}",
        r"\geometry{margin=3cm}",
        r"\usepackage{setspace}",
        r"\onehalfspacing",
        r"\graphicspath{{media/}}",
        r"\begin{document}",
    ]

    # mapa numId -> formato (bullet/decimal) via numbering.xml (listas do Word
    # usam numPr direto, sem estilo nomeado — por isso os bullets se perderam na v2)
    numid_fmt: dict[str, str] = {}
    try:
        numbering = etree.fromstring(z.read("word/numbering.xml"))
        absfmt: dict[str, dict[str, str]] = {}
        for absn in numbering.findall("w:abstractNum", NS):
            aid = absn.get(f"{{{W}}}abstractNumId")
            for lvl in absn.findall("w:lvl", NS):
                il = lvl.get(f"{{{W}}}ilvl", "0")
                f = lvl.find("w:numFmt", NS)
                absfmt.setdefault(aid, {})[il] = f.get(f"{{{W}}}val") if f is not None else "bullet"
        for num in numbering.findall("w:num", NS):
            nid = num.get(f"{{{W}}}numId")
            aid = num.find("w:abstractNumId", NS).get(f"{{{W}}}val")
            numid_fmt[nid] = absfmt.get(aid, {}).get("0", "bullet")
    except KeyError:
        pass

    in_itemize = False
    in_enumerate = False
    open_numid: str | None = None
    title_done = False

    def close_lists():
        nonlocal in_itemize, in_enumerate, open_numid
        if in_itemize:
            out.append(r"\end{itemize}")
            in_itemize = False
        if in_enumerate:
            out.append(r"\end{enumerate}")
            in_enumerate = False
        open_numid = None

    def push_item(env: str, numid: str, txt: str):
        nonlocal in_itemize, in_enumerate, open_numid
        want_itemize = (env == "itemize")
        if open_numid != numid or in_itemize != want_itemize:
            close_lists()
            out.append(r"\begin{%s}" % env)
            if want_itemize:
                in_itemize = True
            else:
                in_enumerate = True
            open_numid = numid
        out.append(r"  \item " + txt)

    def run_text(run) -> str:
        """Texto de um w:r com b/i/link/imagem."""
        parts: list[str] = []
        rpr = run.find("w:rPr", NS)
        b = rpr.find("w:b", NS) is not None if rpr is not None else False
        i = rpr.find("w:i", NS) is not None if rpr is not None else False
        # imagem inline?
        for blip in run.findall(".//a:blip", NS):
            rid = blip.get(f"{{{R}}}embed")
            fname = rid_to_media.get(rid)
            if fname:
                parts.append(r"\includegraphics[height=2.2ex]{%s}" % esc(fname))
        for t in run.findall("w:t", NS):
            txt = esc(t.text or "")
            if not txt:
                continue
            if b and i:
                txt = r"\textbf{\textit{%s}}" % txt
            elif b:
                txt = r"\textbf{%s}" % txt
            elif i:
                txt = r"\textit{%s}" % txt
            parts.append(txt)
        for br in run.findall("w:br", NS):
            parts.append(r"\\")
        return "".join(parts)

    def para_text(p) -> str:
        chunks: list[str] = []
        for child in p:
            tag = etree.QName(child).localname
            if tag == "r":
                chunks.append(run_text(child))
            elif tag == "hyperlink":
                inner = "".join(run_text(r) for r in child.findall("w:r", NS))
                href = child.get(f"{{{R}}}id", "")
                chunks.append(inner)  # URLs do texto preservadas como texto
            elif tag == "drawing":
                for blip in child.findall(".//a:blip", NS):
                    rid = blip.get(f"{{{R}}}embed")
                    fname = rid_to_media.get(rid)
                    if fname:
                        chunks.append(r"\includegraphics[height=2.2ex]{%s}" % esc(fname))
        return "".join(chunks).strip()

    def table_to_latex(tbl) -> list[str]:
        rows = tbl.findall("w:tr", NS)
        grid: list[list[str]] = []
        for tr in rows:
            cells = []
            for tc in tr.findall("w:tc", NS):
                ps = tc.findall("w:p", NS)
                cells.append(" ".join(para_text(p) for p in ps))
            grid.append(cells)
        if not grid:
            return []
        ncols = max(len(r) for r in grid)
        lines = [r"\begin{center}", r"\begin{tabular}{%s}" % ("|".join(["p{4cm}"] * ncols)),
                 r"\toprule"]
        for ri, row in enumerate(grid):
            row += [""] * (ncols - len(row))
            lines.append(" & ".join(c or "---" for c in row) + r" \\")
            if ri == 0:
                lines.append(r"\midrule")
        lines += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
        return lines

    for child in body:
        tag = etree.QName(child).localname
        if tag == "p":
            style_el = child.find("w:pPr/w:pStyle", NS)
            style = style_el.get(f"{{{W}}}val", "normal") if style_el is not None else "normal"
            txt = para_text(child)
            if not txt and child.findall(".//a:blip", NS) == []:
                close_lists()
                out.append("")
                continue
            slow = style.lower()
            if "title" in slow:
                if not title_done:
                    # primeiro Title = titulo principal
                    out.append(r"\title{%s}" % txt)
                    out.append(r"\author{Plano de Pesquisa SCX v1 — convertido do docx}")
                    out.append(r"\date{}")
                    out.append(r"\maketitle")
                    out.append(r"\tableofcontents")
                    out.append(r"\newpage")
                    title_done = True
                else:
                    close_lists()
                    out.append(r"\begin{center}\Large %s\end{center}" % txt)
            elif "heading1" in slow:
                close_lists()
                out.append(r"\section{%s}" % txt)
            elif "heading2" in slow:
                close_lists()
                out.append(r"\subsection{%s}" % txt)
            elif "heading3" in slow:
                close_lists()
                out.append(r"\subsubsection{%s}" % txt)
            elif "listbullet" in slow or "list bullet" in slow:
                push_item("itemize", "style", txt)
            elif "listnumber" in slow or "list number" in slow:
                push_item("enumerate", "style", txt)
            else:
                npr = child.find("w:pPr/w:numPr", NS)
                if npr is not None:
                    nid = npr.find("w:numId", NS).get(f"{{{W}}}val")
                    fmt = numid_fmt.get(nid, "bullet")
                    push_item("itemize" if fmt == "bullet" else "enumerate", nid, txt)
                    continue
                close_lists()
                out.append(txt + "\n")
        elif tag == "tbl":
            close_lists()
            out.append(r"% [tabela original do docx]")
            out.extend(table_to_latex(child))
        # sectPr ignorado

    close_lists()
    out.append(r"\end{document}")
    DST.write_text("\n".join(out), encoding="utf-8")
    print(f"OK: {DST} ({DST.stat().st_size} bytes)")
    inc = "\n".join(out).count("includegraphics")
    print(f"imagens incluidas: {inc} | midias extraidas: {len(list(MEDIA_DST.glob('*')))}")


if __name__ == "__main__":
    try:
        from lxml import etree  # noqa
    except ImportError:
        raise SystemExit("Falta lxml: C:\\Python312\\python.exe -m pip install lxml python-docx")
    main()
