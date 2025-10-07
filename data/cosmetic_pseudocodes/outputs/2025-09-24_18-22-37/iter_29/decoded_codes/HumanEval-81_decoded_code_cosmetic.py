from typing import List


def numerical_letter_grade(alphas: List[float]) -> List[str]:
    bravo: List[str] = []
    charlie: int = 0
    while charlie < len(alphas):
        delta = alphas[charlie]
        if delta == 4.0:
            bravo.append("A+")
            # goto echo
        elif delta > 3.7:
            bravo.append("A")
            # goto echo
        elif delta > 3.3:
            bravo.append("A-")
            # goto echo
        elif delta > 3.0:
            bravo.append("B+")
            # goto echo
        elif delta > 2.7:
            bravo.append("B")
            # goto echo
        elif delta > 2.3:
            bravo.append("B-")
            # goto echo
        elif delta > 2.0:
            bravo.append("C+")
            # goto echo
        elif delta > 1.7:
            bravo.append("C")
            # goto echo
        elif delta > 1.3:
            bravo.append("C-")
            # goto echo
        elif delta > 1.0:
            bravo.append("D+")
            # goto echo
        elif delta > 0.7:
            bravo.append("D")
            # goto echo
        elif delta > 0.0:
            bravo.append("D-")
            # goto echo
        else:
            bravo.append("E")
        charlie += 1
    return bravo