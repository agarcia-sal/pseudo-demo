from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    letter_collection: List[str] = []
    index_tracker: int = 0
    length: int = len(list_of_grades)

    while index_tracker < length:
        current_score: float = list_of_grades[index_tracker]
        index_tracker += 1

        if current_score == 4.0:
            letter_collection.append("A+")
            continue
        if current_score > 3.7:
            letter_collection.append("A")
            continue
        if current_score > 3.3:
            letter_collection.append("A-")
            continue
        if current_score > 3.0:
            letter_collection.append("B+")
            continue
        if current_score > 2.7:
            letter_collection.append("B")
            continue
        if current_score > 2.3:
            letter_collection.append("B-")
            continue
        if current_score > 2.0:
            letter_collection.append("C+")
            continue
        if current_score > 1.7:
            letter_collection.append("C")
            continue
        if current_score > 1.3:
            letter_collection.append("C-")
            continue
        if current_score > 1.0:
            letter_collection.append("D+")
            continue
        if current_score > 0.7:
            letter_collection.append("D")
            continue
        if current_score > 0.0:
            letter_collection.append("D-")
            continue

        letter_collection.append("E")

    return letter_collection