from typing import List

def numerical_letter_grade(alpha_list: List[float]) -> List[str]:
    beta_list: List[str] = []

    def process_element(gamma: float) -> str:
        if gamma == 4.0:
            return "A+"
        if gamma > 3.7:
            return "A"
        if gamma > 3.3:
            return "A-"
        if gamma > 3.0:
            return "B+"
        if gamma > 2.7:
            return "B"
        if gamma > 2.3:
            return "B-"
        if gamma > 2.0:
            return "C+"
        if gamma > 1.7:
            return "C"
        if gamma > 1.3:
            return "C-"
        if gamma > 1.0:
            return "D+"
        if gamma > 0.7:
            return "D"
        if gamma > 0.0:
            return "D-"
        return "E"

    delta = beta_list
    for epsilon in alpha_list:
        delta.append(process_element(epsilon))
    return delta