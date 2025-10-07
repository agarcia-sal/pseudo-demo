from typing import List

def numerical_letter_grade(zeta: List[float]) -> List[str]:
    def helper(xi: float, omega: List[str]) -> List[str]:
        if xi == 4.0:
            return omega + ["A+"]
        elif xi > 3.7:
            return omega + ["A"]
        elif xi > 3.3:
            return omega + ["A-"]
        elif xi > 3.0:
            return omega + ["B+"]
        elif xi > 2.7:
            return omega + ["B"]
        elif xi > 2.3:
            return omega + ["B-"]
        elif xi > 2.0:
            return omega + ["C+"]
        elif xi > 1.7:
            return omega + ["C"]
        elif xi > 1.3:
            return omega + ["C-"]
        elif xi > 1.0:
            return omega + ["D+"]
        elif xi > 0.7:
            return omega + ["D"]
        elif xi > 0.0:
            return omega + ["D-"]
        else:
            return omega + ["E"]

    def recur(delta: int, gamma: List[str]) -> List[str]:
        if delta == 0:
            return gamma
        return recur(delta - 1, helper(zeta[len(zeta) - delta], gamma))

    return recur(len(zeta), [])