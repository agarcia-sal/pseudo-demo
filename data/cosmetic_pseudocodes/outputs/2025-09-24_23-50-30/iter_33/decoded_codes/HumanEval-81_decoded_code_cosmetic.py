from typing import List

def numerical_letter_grade(grade_collection: List[float]) -> List[str]:
    def map_grades(grades: List[float], index: int, result_accum: List[str]) -> List[str]:
        if index == len(grades):
            return result_accum
        current_value = grades[index]
        if current_value == 4.0:
            code_map = "A+"
        elif current_value > 3.7:
            code_map = "A"
        elif current_value > 3.3:
            code_map = "A-"
        elif current_value > 3.0:
            code_map = "B+"
        elif current_value > 2.7:
            code_map = "B"
        elif current_value > 2.3:
            code_map = "B-"
        elif current_value > 2.0:
            code_map = "C+"
        elif current_value > 1.7:
            code_map = "C"
        elif current_value > 1.3:
            code_map = "C-"
        elif current_value > 1.0:
            code_map = "D+"
        elif current_value > 0.7:
            code_map = "D"
        elif current_value > 0.0:
            code_map = "D-"
        else:
            code_map = "E"
        return map_grades(grades, index + 1, result_accum + [code_map])

    return map_grades(grade_collection, 0, [])