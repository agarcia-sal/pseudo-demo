from typing import List

def numerical_letter_grade(sigma_list: List[float]) -> List[str]:
    omega: List[str] = []
    delta: int = 0
    while delta < len(sigma_list):
        tau: float = sigma_list[delta]
        if tau == 4.0:
            omega.append("A+")
        elif tau > 3.7:
            omega.append("A")
        elif tau > 3.3:
            omega.append("A-")
        elif tau > 3.0:
            omega.append("B+")
        elif tau > 2.7:
            omega.append("B")
        elif tau > 2.3:
            omega.append("B-")
        elif tau > 2.0:
            omega.append("C+")
        elif tau > 1.7:
            omega.append("C")
        elif tau > 1.3:
            omega.append("C-")
        elif tau > 1.0:
            omega.append("D+")
        elif tau > 0.7:
            omega.append("D")
        elif tau > 0.0:
            omega.append("D-")
        else:
            omega.append("E")
        delta += 1
    return omega