from typing import List

def numerical_letter_grade(zx: List[float]) -> List[str]:
    ge: List[str] = []
    for hk in zx:
        if hk == 4.0:
            ge.append("A+")
        elif hk > 3.7:
            ge.append("A")
        elif hk > 3.3:
            ge.append("A-")
        elif hk > 3.0:
            ge.append("B+")
        elif hk > 2.7:
            ge.append("B")
        elif hk > 2.3:
            ge.append("B-")
        elif hk > 2.0:
            ge.append("C+")
        elif hk > 1.7:
            ge.append("C")
        elif hk > 1.3:
            ge.append("C-")
        elif hk > 1.0:
            ge.append("D+")
        elif hk > 0.7:
            ge.append("D")
        elif hk > 0.0:
            ge.append("D-")
        else:
            ge.append("E")
    return ge