from typing import List

def numerical_letter_grade(alpha_list: List[float]) -> List[str]:
    def classify(beta: float) -> str:
        if beta == 4.0:
            return "A+"
        if beta > 3.7:
            return "A"
        if beta > 3.3:
            return "A-"
        if beta > 3.0:
            return "B+"
        if beta > 2.7:
            return "B"
        if beta > 2.3:
            return "B-"
        if beta > 2.0:
            return "C+"
        if beta > 1.7:
            return "C"
        if beta > 1.3:
            return "C-"
        if beta > 1.0:
            return "D+"
        if beta > 0.7:
            return "D"
        if beta > 0.0:
            return "D-"
        return "E"

    def helper(gamma: List[float], delta: int) -> List[str]:
        if delta == len(gamma):
            return []
        return [classify(gamma[delta])] + helper(gamma, delta + 1)

    return helper(alpha_list, 0)