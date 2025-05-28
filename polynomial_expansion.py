import random
import os
from pylatex import Document, Enumerate, NoEscape, Command, Section, Center
from pylatex.utils import bold

problems = {
    r"$(a + b)^2 = $": r"$a^2 + 2ab + b^2$",
    r"$(a - b)^2 = $": r"$a^2 - 2ab + b^2$",
    r"$\text{(답 2개)} \; a^2 + b^2 = $": r"$(a+b)^2 - 2ab, (a-b)^2 + 2ab$",
    r"$(a + b)(a - b) = $": r"$a^2 - b^2$",
    r"$a^2 - b^2 = $": r"$(a+b)(a-b)$",
    r"$(x + a)(x + b) = $": r"$x^2 + (a+b)x + ab$",
    r"$(a + b + c)^2 = $": r"$a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$",
    r"$a^2 + b^2 + c^2 = $": r"$(a+b+c)^2 - 2(ab + bc + ca)$",
    r"$(x + a)(x + b)(x + c) = $": r"$x^3 + (a+b+c)x^2 + (ab+bc+ca)x + abc$",
    r"$(a + b)^3 = $": r"$a^3 + 3a^2b + 3ab^2 + b^3$",
    r"$(a - b)^3 = $": r"$a^3 - 3a^2b + 3ab^2 - b^3$",
    r"$(a + b)(a^2 - ab + b^2) = $": r"$a^3 + b^3$",
    r"$(a - b)(a^2 + ab + b^2) = $": r"$a^3 - b^3$",
    r"$\text{(답 2개)} \; a^3 + b^3 = $": r"$(a+b)(a^2 - ab + b^2), (a+b)^3 - 3ab(a+b)$",
    r"$\text{(답 2개)} \; a^3 - b^3 = $": r"$(a-b)(a^2 + ab + b^2), (a-b)^3 + 3ab(a-b)$",
    r"$(a + b + c)(a^2 + b^2 + c^2 - ab - ac - bc) = $": r"$a^3 + b^3 + c^3 - 3abc$",
    r"$(a^2 + ab + b^2)(a^2 - ab + b^2) = $": r"$a^4 + a^2b^2 + b^4$",
    r"$a^4 + a^2b^2 + b^4 = $": r"$(a^2 + ab + b^2)(a^2 - ab + b^2)$",
    r"$\text{(답 2개)} \; x^2 + \frac{1}{x^2} = $": r"$\left(x + \frac{1}{x}\right)^2 - 2, \left(x - \frac{1}{x}\right)^2 + 2$",
    r"$x^3 + \frac{1}{x^3} = $": r"$\left(x + \frac{1}{x}\right)^3 - 3\left(x + \frac{1}{x}\right)$",
    r"$x^3 - \frac{1}{x^3} = $": r"$\left(x - \frac{1}{x}\right)^3 + 3\left(x - \frac{1}{x}\right)$",
    r"$a^2 + b^2 + c^2 - ab - ac - bc = $": r"$\frac{1}{2}\left((a-b)^2 + (b-c)^2 + (c-a)^2\right)$",
    r"$a^3 + b^3 + c^3 = $": r"$(a+b+c)(a^2+b^2+c^2-ab-bc-ca) + 3abc$"
}

os.makedirs("output", exist_ok=True)
os.makedirs("answer", exist_ok=True)

problem_items = list(problems.items())
random.shuffle(problem_items)

def create_document():
    doc = Document(
        geometry_options={"tmargin": "2.5cm", "lmargin": "3cm", "rmargin": "3cm"},
        documentclass="article",
        fontenc="T1",
        inputenc="utf8"
    )
    
    doc.preamble.append(Command("usepackage", "kotex"))
    doc.preamble.append(Command("usepackage", "amsmath"))
    doc.preamble.append(Command("usepackage", "amssymb"))
    doc.preamble.append(Command("usepackage", "ulem"))
    
    doc.append(NoEscape(r"\large"))
    doc.append(NoEscape(r"\setlength{\itemsep}{2.5em}"))
    doc.append(NoEscape(r"\setlength{\parsep}{0.7em}"))
    
    return doc

problem_doc = create_document()

with problem_doc.create(Center()):
    problem_doc.append(Command("LARGE"))
    problem_doc.append(NoEscape(r"\textbf{곱셈 공식 테스트}"))
    problem_doc.append("\n\n")

with problem_doc.create(Enumerate()) as enum:
    for problem, _ in problem_items:
        enum.add_item(NoEscape(problem))

answer_doc = create_document()

with answer_doc.create(Center()):
    answer_doc.append(Command("LARGE"))
    answer_doc.append(NoEscape(r"\textbf{곱셈 공식 테스트 (정답)}"))
    answer_doc.append("\n\n")

with answer_doc.create(Enumerate()) as enum:
    for problem, answer in problem_items:
        enum.add_item(NoEscape(f"{problem} {answer}"))

problem_doc.generate_pdf(os.path.join("output", "polynomial_expansion"), compiler="xelatex", clean_tex=False)
answer_doc.generate_pdf(os.path.join("answer", "polynomial_expansion_answer"), compiler="xelatex", clean_tex=False)
