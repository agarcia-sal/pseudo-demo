from typing import List


def numerical_letter_grade(scores_collection: List[float]) -> List[str]:
    results_collection: List[str] = []
    index: int = 0
    length: int = len(scores_collection)
    while index < length:
        current_score: float = scores_collection[index]
        if current_score == 4.0:
            results_collection.append("A+")
        elif current_score > 3.7:
            results_collection.append("A")
        elif current_score > 3.3:
            results_collection.append("A-")
        elif current_score > 3.0:
            results_collection.append("B+")
        elif current_score > 2.7:
            results_collection.append("B")
        elif current_score > 2.3:
            results_collection.append("B-")
        elif current_score > 2.0:
            results_collection.append("C+")
        elif current_score > 1.7:
            results_collection.append("C")
        elif current_score > 1.3:
            results_collection.append("C-")
        elif current_score > 1.0:
            results_collection.append("D+")
        elif current_score > 0.7:
            results_collection.append("D")
        elif current_score > 0.0:
            results_collection.append("D-")
        else:
            results_collection.append("E")
        index += 1
    return results_collection