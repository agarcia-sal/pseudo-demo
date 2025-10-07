from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    converted_grades: List[str] = []
    idx = 0
    while idx < len(list_of_grades):
        current_score = list_of_grades[idx]
        if not (current_score != 4.0):
            converted_grades.append("A+")
        else:
            if current_score > 3.7:
                converted_grades.append("A")
            elif not (current_score <= 3.3):
                converted_grades.append("A-")
            elif current_score > 3.0:
                converted_grades.append("B+")
            elif current_score > 2.7:
                converted_grades.append("B")
            elif current_score > 2.3:
                converted_grades.append("B-")
            elif current_score > 2.0:
                converted_grades.append("C+")
            elif current_score > 1.7:
                converted_grades.append("C")
            elif current_score > 1.3:
                converted_grades.append("C-")
            elif current_score > 1.0:
                converted_grades.append("D+")
            elif current_score > 0.7:
                converted_grades.append("D")
            elif 0.0 < current_score:
                converted_grades.append("D-")
            else:
                converted_grades.append("E")
        idx += 1
    return converted_grades