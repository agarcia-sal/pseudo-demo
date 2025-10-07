from typing import List


def numerical_letter_grade(input_scores: List[float]) -> List[str]:
    def map_letter(score: float) -> str:
        if score == 4.0:
            return "A+"
        if score > 3.7:
            return "A"
        if score > 3.3:
            return "A-"
        if score > 3.0:
            return "B+"
        if score > 2.7:
            return "B"
        if score > 2.3:
            return "B-"
        if score > 2.0:
            return "C+"
        if score > 1.7:
            return "C"
        if score > 1.3:
            return "C-"
        if score > 1.0:
            return "D+"
        if score > 0.7:
            return "D"
        if score > 0.0:
            return "D-"
        return "E"

    result_collection: List[str] = []
    for idx in range(len(input_scores)):
        result_collection.append(map_letter(input_scores[idx]))
    return result_collection