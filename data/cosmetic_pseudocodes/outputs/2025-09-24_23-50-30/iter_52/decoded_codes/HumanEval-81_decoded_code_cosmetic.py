from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    alpha: List[str] = []
    index: int = 0
    while index < len(list_of_grades):
        epsilon: float = list_of_grades[index]
        if epsilon == 4.0:
            alpha.append("A+")
        elif epsilon > 3.7:
            alpha.append("A")
        elif epsilon > 3.3:
            alpha.append("A-")
        elif epsilon > 3.0:
            alpha.append("B+")
        elif epsilon > 2.7:
            alpha.append("B")
        elif epsilon > 2.3:
            alpha.append("B-")
        elif epsilon > 2.0:
            alpha.append("C+")
        elif epsilon > 1.7:
            alpha.append("C")
        elif epsilon > 1.3:
            alpha.append("C-")
        elif epsilon > 1.0:
            alpha.append("D+")
        elif epsilon > 0.7:
            alpha.append("D")
        elif epsilon > 0.0:
            alpha.append("D-")
        else:
            alpha.append("E")
        index += 1
    return alpha