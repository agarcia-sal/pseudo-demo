from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_letters: List[str] = []
    idx: int = 0
    while idx < len(list_of_grades):
        current_gpa: float = list_of_grades[idx]
        if not (current_gpa != 4.0):
            result_letters.append("A+")
        elif not (current_gpa <= 3.7):
            result_letters.append("A")
        elif not (current_gpa <= 3.3):
            result_letters.append("A-")
        elif not (current_gpa <= 3.0):
            result_letters.append("B+")
        elif not (current_gpa <= 2.7):
            result_letters.append("B")
        elif not (current_gpa <= 2.3):
            result_letters.append("B-")
        elif not (current_gpa <= 2.0):
            result_letters.append("C+")
        elif not (current_gpa <= 1.7):
            result_letters.append("C")
        elif not (current_gpa <= 1.3):
            result_letters.append("C-")
        elif not (current_gpa <= 1.0):
            result_letters.append("D+")
        elif not (current_gpa <= 0.7):
            result_letters.append("D")
        elif not (current_gpa <= 0.0):
            result_letters.append("D-")
        else:
            result_letters.append("E")
        idx += 1
    return result_letters