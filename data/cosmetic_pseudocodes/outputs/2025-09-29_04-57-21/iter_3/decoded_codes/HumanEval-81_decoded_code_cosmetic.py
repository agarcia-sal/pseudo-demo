from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def map_to_letter(score: float) -> str:
        if score == 4.0:
            return "A+"
        if not (score <= 3.7):
            return "A"
        if 3.3 < score:
            return "A-"
        if 3.0 < score:
            return "B+"
        if 2.7 < score:
            return "B"
        if 2.3 < score:
            return "B-"
        if 2.0 < score:
            return "C+"
        if 1.7 < score:
            return "C"
        if 1.3 < score:
            return "C-"
        if 1.0 < score:
            return "D+"
        if 0.7 < score:
            return "D"
        if 0.0 < score:
            return "D-"
        return "E"

    result_letters: List[str] = []
    for idx in range(len(list_of_grades)):
        current_value = list_of_grades[idx]
        grade_label = map_to_letter(current_value)
        result_letters.append(grade_label)
    return result_letters