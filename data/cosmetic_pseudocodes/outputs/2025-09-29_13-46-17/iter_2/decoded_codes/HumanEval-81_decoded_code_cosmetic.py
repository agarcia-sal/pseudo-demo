from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def inner_convert(index: int, results: List[str]) -> List[str]:
        if index >= len(list_of_grades):
            return results
        current_grade = list_of_grades[index]
        if current_grade == 4.0:
            grade_symbol = "A+"
        elif 3.7 < current_grade < 4.0:
            grade_symbol = "A"
        elif 3.3 < current_grade <= 3.7:
            grade_symbol = "A-"
        elif 3.0 < current_grade <= 3.3:
            grade_symbol = "B+"
        elif 2.7 < current_grade <= 3.0:
            grade_symbol = "B"
        elif 2.3 < current_grade <= 2.7:
            grade_symbol = "B-"
        elif 2.0 < current_grade <= 2.3:
            grade_symbol = "C+"
        elif 1.7 < current_grade <= 2.0:
            grade_symbol = "C"
        elif 1.3 < current_grade <= 1.7:
            grade_symbol = "C-"
        elif 1.0 < current_grade <= 1.3:
            grade_symbol = "D+"
        elif 0.7 < current_grade <= 1.0:
            grade_symbol = "D"
        elif 0.0 < current_grade <= 0.7:
            grade_symbol = "D-"
        else:
            grade_symbol = "E"
        return inner_convert(index + 1, results + [grade_symbol])
    return inner_convert(0, [])