from typing import List


def numerical_letter_grade(alpha_list: List[float]) -> List[str]:
    beta: List[str] = []
    gamma = 0
    while gamma < len(alpha_list):
        delta = alpha_list[gamma]
        if delta == 4.0:
            beta.append("A+")
        elif delta > 3.7:
            beta.append("A")
        elif delta > 3.3:
            beta.append("A-")
        elif delta > 3.0:
            beta.append("B+")
        elif delta > 2.7:
            beta.append("B")
        elif delta > 2.3:
            beta.append("B-")
        elif delta > 2.0:
            beta.append("C+")
        elif delta > 1.7:
            beta.append("C")
        elif delta > 1.3:
            beta.append("C-")
        elif delta > 1.0:
            beta.append("D+")
        elif delta > 0.7:
            beta.append("D")
        elif delta > 0:
            beta.append("D-")
        else:
            beta.append("E")
        gamma += 1
    return beta