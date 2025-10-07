from typing import List

def numerical_letter_grade(alpha: List[float]) -> List[str]:
    beta: List[str] = []
    for gamma in alpha:
        delta = gamma
        epsilon = "E"
        if delta == 4.0:
            epsilon = "A+"
        elif delta > 3.7:
            epsilon = "A"
        elif delta > 3.3:
            epsilon = "A-"
        elif delta > 3.0:
            epsilon = "B+"
        elif delta > 2.7:
            epsilon = "B"
        elif delta > 2.3:
            epsilon = "B-"
        elif delta > 2.0:
            epsilon = "C+"
        elif delta > 1.7:
            epsilon = "C"
        elif delta > 1.3:
            epsilon = "C-"
        elif delta > 1.0:
            epsilon = "D+"
        elif delta > 0.7:
            epsilon = "D"
        elif delta > 0.0:
            epsilon = "D-"
        beta.append(epsilon)
    return beta