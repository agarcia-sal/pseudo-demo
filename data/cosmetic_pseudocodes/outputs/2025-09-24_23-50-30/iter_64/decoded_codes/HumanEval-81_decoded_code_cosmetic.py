from typing import List


def numerical_letter_grade(alpha: List[float]) -> List[str]:
    beta: List[str] = []
    delta: int = 0
    length_alpha: int = len(alpha)
    while delta < length_alpha:
        epsilon: float = alpha[delta]
        if epsilon == 4.0:
            beta.append("A+")
        elif epsilon > 3.7:
            beta.append("A")
        elif epsilon > 3.3:
            beta.append("A-")
        elif epsilon > 3.0:
            beta.append("B+")
        elif epsilon > 2.7:
            beta.append("B")
        elif epsilon > 2.3:
            beta.append("B-")
        elif epsilon > 2.0:
            beta.append("C+")
        elif epsilon > 1.7:
            beta.append("C")
        elif epsilon > 1.3:
            beta.append("C-")
        elif epsilon > 1.0:
            beta.append("D+")
        elif epsilon > 0.7:
            beta.append("D")
        elif epsilon > 0.0:
            beta.append("D-")
        else:
            beta.append("E")
        delta += 1
    return beta