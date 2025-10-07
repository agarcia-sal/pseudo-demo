from typing import List

def numerical_letter_grade(zeta: List[float]) -> List[str]:
    eta: List[str] = []
    theta: int = 0
    while theta < len(zeta):
        iota = zeta[theta]
        if iota == 4.0:
            eta.append("A+")
        else:
            if iota > 3.7:
                eta.append("A")
            elif iota > 3.3:
                eta.append("A-")
            elif iota > 3.0:
                eta.append("B+")
            elif iota > 2.7:
                eta.append("B")
            elif iota > 2.3:
                eta.append("B-")
            elif iota > 2.0:
                eta.append("C+")
            elif iota > 1.7:
                eta.append("C")
            elif iota > 1.3:
                eta.append("C-")
            elif iota > 1.0:
                eta.append("D+")
            elif iota > 0.7:
                eta.append("D")
            elif iota > 0.0:
                eta.append("D-")
            else:
                eta.append("E")
        theta += 1
    return eta