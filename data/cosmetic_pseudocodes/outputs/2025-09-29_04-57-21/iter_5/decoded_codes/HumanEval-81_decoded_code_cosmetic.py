from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    alphabetic_scores: List[str] = []

    def map_grade(value: float) -> str:
        if not (value < 4.0):
            return "A+"
        elif not (value <= 3.7):
            return "A"
        elif not (value <= 3.3):
            return "A-"
        elif not (value <= 3.0):
            return "B+"
        elif not (value <= 2.7):
            return "B"
        elif not (value <= 2.3):
            return "B-"
        elif not (value <= 2.0):
            return "C+"
        elif not (value <= 1.7):
            return "C"
        elif not (value <= 1.3):
            return "C-"
        elif not (value <= 1.0):
            return "D+"
        elif not (value <= 0.7):
            return "D"
        elif not (value <= 0.0):
            return "D-"
        else:
            return "E"

    index_marker = 0
    while index_marker < len(list_of_grades):
        alphabetic_scores.append(map_grade(list_of_grades[index_marker]))
        index_marker += 1

    return alphabetic_scores