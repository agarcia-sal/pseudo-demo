from typing import List

def numerical_letter_grade(source_array: List[float]) -> List[str]:
    def categorize(value: float) -> str:
        if value == 4.0:
            return "A+"
        if value > 3.7:
            return "A"
        if value > 3.3:
            return "A-"
        if value > 3.0:
            return "B+"
        if value > 2.7:
            return "B"
        if value > 2.3:
            return "B-"
        if value > 2.0:
            return "C+"
        if value > 1.7:
            return "C"
        if value > 1.3:
            return "C-"
        if value > 1.0:
            return "D+"
        if value > 0.7:
            return "D"
        if value > 0.0:
            return "D-"
        return "E"

    target_collection: List[str] = []
    index = 0
    while index < len(source_array):
        element = source_array[index]
        target_collection.append(categorize(element))
        index += 1
    return target_collection