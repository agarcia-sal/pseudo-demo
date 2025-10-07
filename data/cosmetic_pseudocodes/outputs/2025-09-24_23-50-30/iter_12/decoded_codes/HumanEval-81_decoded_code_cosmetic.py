from typing import Iterable, List

def numerical_letter_grade(numbers_collection: Iterable[float]) -> List[str]:
    results_array: List[str] = []

    def map_grade(score: float) -> str:
        # Since the pseudocode uses "score NOT LESS THAN x" in descending order:
        if score >= 4.0:
            return "A+"
        if score >= 3.7:
            return "A"
        if score >= 3.3:
            return "A-"
        if score >= 3.0:
            return "B+"
        if score >= 2.7:
            return "B"
        if score >= 2.3:
            return "B-"
        if score >= 2.0:
            return "C+"
        if score >= 1.7:
            return "C"
        if score >= 1.3:
            return "C-"
        if score >= 1.0:
            return "D+"
        if score >= 0.7:
            return "D"
        if score >= 0.0:
            return "D-"
        return "E"

    for element in numbers_collection:
        results_array.append(map_grade(element))

    return results_array