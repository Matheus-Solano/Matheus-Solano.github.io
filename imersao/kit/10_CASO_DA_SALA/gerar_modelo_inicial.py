r"""
Gera modelo_inicial_consumidor.docx a partir de
pedagogia\03_CASO_linha\02_MODELO_PECA\modelo_inicial_consumidor.md,
para quem chegar na imersao sem modelo de peca proprio.

Titulos (#, ##) viram Heading. Paragrafos normais ficam em Times New Roman 12.
Reexecutavel: rode de novo sempre que o .md de origem mudar.
"""

import re
from pathlib import Path

from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

BASE = Path(__file__).resolve().parents[3]  # 07_IMERSAO_2026-09-19
FONTE_MD = BASE / "pedagogia" / "03_CASO_linha" / "02_MODELO_PECA" / "modelo_inicial_consumidor.md"
SAIDA_DOCX = Path(__file__).resolve().parent / "modelo_inicial_consumidor.docx"

FONTE_NOME = "Times New Roman"
FONTE_TAMANHO = Pt(12)


def set_font(run, bold=False, italic=False):
    run.font.name = FONTE_NOME
    run.font.size = FONTE_TAMANHO
    run.bold = bold
    run.italic = italic
    # garante a fonte tambem para caracteres do alfabeto latino estendido (acentos)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    rfonts.set(qn("w:eastAsia"), FONTE_NOME)


def add_runs_with_markdown_bold(paragraph, text):
    """Divide o texto em trechos **negrito** e normais, preservando itens entre colchetes."""
    parts = re.split(r"(\*\*.*?\*\*)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            set_font(run, bold=True)
        else:
            run = paragraph.add_run(part)
            set_font(run)


def set_default_style(doc):
    style = doc.styles["Normal"]
    style.font.name = FONTE_NOME
    style.font.size = FONTE_TAMANHO
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    rfonts.set(qn("w:eastAsia"), FONTE_NOME)


def style_heading_font(paragraph):
    for run in paragraph.runs:
        run.font.name = FONTE_NOME
        rpr = run._element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = rpr.makeelement(qn("w:rFonts"), {})
            rpr.append(rfonts)
        rfonts.set(qn("w:eastAsia"), FONTE_NOME)


def main():
    linhas = FONTE_MD.read_text(encoding="utf-8").splitlines()

    doc = Document()
    set_default_style(doc)

    dentro_tabela = False
    tabela_linhas = []
    dentro_checklist = False

    def fechar_tabela():
        nonlocal dentro_tabela, tabela_linhas
        if not tabela_linhas:
            dentro_tabela = False
            return
        linhas_dados = [l for l in tabela_linhas if not re.match(r"^\|[\s:|-]+\|$", l)]
        celulas = [
            [c.strip() for c in l.strip().strip("|").split("|")]
            for l in linhas_dados
        ]
        if celulas:
            n_cols = len(celulas[0])
            tabela = doc.add_table(rows=len(celulas), cols=n_cols)
            tabela.style = "Table Grid"
            for i, linha in enumerate(celulas):
                for j, valor in enumerate(linha):
                    if j < n_cols:
                        cell_par = tabela.cell(i, j).paragraphs[0]
                        run = cell_par.add_run(valor)
                        set_font(run, bold=(i == 0))
        tabela_linhas = []
        dentro_tabela = False

    for linha in linhas:
        bruta = linha.rstrip("\n")
        texto = bruta.strip()

        # linhas de tabela markdown
        if texto.startswith("|"):
            dentro_tabela = True
            tabela_linhas.append(texto)
            continue
        elif dentro_tabela:
            fechar_tabela()

        if not texto:
            continue

        if texto == "---":
            continue

        if texto == "<br>":
            doc.add_paragraph()
            continue

        m = re.match(r"^(#{1,3})\s+(.*)$", texto)
        if m:
            nivel = len(m.group(1))
            titulo = re.sub(r"\*\*(.*?)\*\*", r"\1", m.group(2))
            p = doc.add_heading(titulo, level=nivel)
            style_heading_font(p)
            continue

        if texto.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Pt(18)
            add_runs_with_markdown_bold(p, texto.lstrip("> ").strip())
            for run in p.runs:
                run.italic = True
            continue

        if texto.startswith("- [ ]"):
            p = doc.add_paragraph(style="List Bullet")
            add_runs_with_markdown_bold(p, "[ ] " + texto[5:].strip())
            continue

        if texto.startswith(("- ", "* ")) and not texto.startswith("**"):
            p = doc.add_paragraph(style="List Bullet")
            add_runs_with_markdown_bold(p, texto[2:].strip())
            continue

        m_num = re.match(r"^(\d+)\.\s+(.*)$", texto)
        if m_num:
            p = doc.add_paragraph(style="List Number")
            add_runs_with_markdown_bold(p, m_num.group(2))
            continue

        p = doc.add_paragraph()
        p.alignment = 3  # justificado
        add_runs_with_markdown_bold(p, texto)

    if dentro_tabela:
        fechar_tabela()

    doc.save(SAIDA_DOCX)
    print(f"Gerado: {SAIDA_DOCX}")


if __name__ == "__main__":
    main()
