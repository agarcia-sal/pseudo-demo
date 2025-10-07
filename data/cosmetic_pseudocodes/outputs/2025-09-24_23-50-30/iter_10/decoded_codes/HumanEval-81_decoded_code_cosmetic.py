from typing import List


def numerical_letter_grade(xyz: List[float]) -> List[str]:
    qrs: List[str] = []
    for val in xyz:
        if val == 4.0:
            qrs.append("A+")
        elif val > 3.7:
            qrs.append("A")
        elif val > 3.3:
            qrs.append("A-")
        elif val > 3.0:
            qrs.append("B+")
        elif val > 2.7:
            qrs.append("B")
        elif val > 2.3:
            qrs.append("B-")
        elif val > 2.0:
            qrs.append("C+")
        elif val > 1.7:
            qrs.append("C")
        elif val > 1.3:
            qrs.append("C-")
        elif val > 1.0:
            qrs.append("D+")
        elif val > 0.7:
            qrs.append("D")
        elif val > 0.0:
            qrs.append("D-")
        else:
            qrs.append("E")
    return qrs