from typing import List

def numerical_letter_grade(array_of_scores: List[float]) -> List[str]:
    results: List[str] = []
    index: int = 0

    def assign_letter(score: float) -> str:
        if score == 4:
            return "A+"
        elif score > 3.7:
            return "A"
        elif score > 3.3:
            return "A-"
        elif score > 3:
            return "B+"
        elif score > 2.7:
            return "B"
        elif score > 2.3:
            return "B-"
        elif score > 2:
            return "C+"
        elif score > 1.7:
            return "C"
        elif score > 1.3:
            return "C-"
        elif score > 1:
            return "D+"
        elif score > 0.7:
            return "D"
        elif score > 0:
            return "D-"
        else:
            return "E"

    while index < len(array_of_scores):
        results.append(assign_letter(array_of_scores[index]))
        index += 1

    return results