from typing import List

def numerical_letter_grade(alpha: List[float]) -> List[str]:
    z: List[str] = []
    for m in alpha:
        if m == 4.0:
            z.append("A+")
        elif m > 3.7:
            z.append("A")
        elif m > 3.3:
            z.append("A-")
        elif m > 3.0:
            z.append("B+")
        elif m > 2.7:
            z.append("B")
        elif m > 2.3:
            z.append("B-")
        elif m > 2.0:
            z.append("C+")
        elif m > 1.7:
            z.append("C")
        elif m > 1.3:
            z.append("C-")
        elif m > 1.0:
            z.append("D+")
        elif m > 0.7:
            z.append("D")
        elif m > 0.0:
            z.append("D-")
        else:
            z.append("E")
    return z