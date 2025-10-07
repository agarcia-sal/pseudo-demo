from typing import List


def numerical_letter_grade(input_scores: List[float]) -> List[str]:
    letter_collection: List[str] = []
    index: int = 0
    while index < len(input_scores):
        score = input_scores[index]
        index += 1
        if score == 4.0:
            letter_collection.append("A+")
        elif score > 3.7:
            letter_collection.append("A")
        elif score > 3.3:
            letter_collection.append("A-")
        elif score > 3.0:
            letter_collection.append("B+")
        elif score > 2.7:
            letter_collection.append("B")
        elif score > 2.3:
            letter_collection.append("B-")
        elif score > 2.0:
            letter_collection.append("C+")
        elif score > 1.7:
            letter_collection.append("C")
        elif score > 1.3:
            letter_collection.append("C-")
        elif score > 1.0:
            letter_collection.append("D+")
        elif score > 0.7:
            letter_collection.append("D")
        elif score > 0.0:
            letter_collection.append("D-")
        else:
            letter_collection.append("E")
    return letter_collection