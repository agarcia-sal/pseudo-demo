from typing import List


def numerical_letter_grade(zeta: List[float]) -> List[str]:
    eta: List[str] = []
    i: int = 0
    while i < len(zeta):
        xi: float = zeta[i]
        if xi == 4.0:
            eta.append("A+")
        elif xi > 3.7:
            eta.append("A")
        elif xi > 3.3:
            eta.append("A-")
        elif xi > 3.0:
            eta.append("B+")
        elif xi > 2.7:
            eta.append("B")
        elif xi > 2.3:
            eta.append("B-")
        elif xi > 2.0:
            eta.append("C+")
        elif xi > 1.7:
            eta.append("C")
        elif xi > 1.3:
            eta.append("C-")
        elif xi > 1.0:
            eta.append("D+")
        elif xi > 0.7:
            eta.append("D")
        elif xi > 0.0:
            eta.append("D-")
        else:
            eta.append("E")
        i += 1
    return eta