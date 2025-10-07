from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def translate(score: float) -> str:
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

    index = 0
    converted_list: List[str] = []
    while index < len(list_of_grades):
        current_grade = list_of_grades[index]
        mapped_value = translate(current_grade)
        converted_list = converted_list + [mapped_value]
        index += 1

    return converted_list