import random
import os
from pylatex import Document, Enumerate, NoEscape, Command, Section, Center
from pylatex.utils import bold

problems = [
    r"$(a + b)^2 = $",
    r"$(a - b)^2 = $",
    r"$\text{(답 2개)} \; a^2 + b^2 = $",
    r"$(a + b)(a - b) = $",
    r"$a^2 - b^2 = $",
    r"$(x + a)(x + b) = $",
    r"$(a + b + c)^2 = $",
    r"$a^2 + b^2 + c^2 = $",
    r"$(x + a)(x + b)(x + c) = $",
    r"$(a + b)^3 = $",
    r"$(a - b)^3 = $",
    r"$(a + b)(a^2 - ab + b^2) = $",
    r"$(a - b)(a^2 + ab + b^2) = $",
    r"$\text{(답 2개)} \; a^3 + b^3 = $",
    r"$\text{(답 2개)} \; a^3 - b^3 = $",
    r"$(a + b + c)(a^2 + b^2 + c^2 - ab - ac - bc) = $",
    r"$(a^2 + ab + b^2)(a^2 - ab + b^2) = $",
    r"$a^4 + a^2b^2 + b^4 = $",
    r"$\text{(답 2개)} \; x^2 + \frac{1}{x^2} = $",
    r"$x^3 + \frac{1}{x^3} = $",
    r"$x^3 - \frac{1}{x^3} = $",
    r"$a^2 + b^2 + c^2 - ab - ac - bc = $",
    r"$(a + b + c)^3 = $",
    r"$a^3 + b^3 + c^3 = $",
]

random.shuffle(problems)

# 문서 설정
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

# 제목
with doc.create(Center()):
    doc.append(Command("LARGE"))
    doc.append(NoEscape(r"\textbf{다항식의 곱셈 공식 테스트}"))
    doc.append("\n\n")

doc.append(NoEscape(r"\large"))
doc.append(NoEscape(r"\setlength{\itemsep}{2.5em}"))
doc.append(NoEscape(r"\setlength{\parsep}{0.7em}"))

# 문제 목록
with doc.create(Enumerate()) as enum:
    for problem in problems:
        enum.add_item(NoEscape(problem))

output_path = os.path.join("output", "polynomial_expansion")
doc.generate_pdf(output_path, compiler="xelatex", clean_tex=False)
