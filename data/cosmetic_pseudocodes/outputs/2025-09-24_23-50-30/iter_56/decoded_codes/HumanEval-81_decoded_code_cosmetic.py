from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_list: List[str] = []

    def compute_letter(index: int) -> None:
        if not (index < len(list_of_grades)):
            return
        current_val: float = list_of_grades[index]
        if current_val == 4.0:
            grade_char = "A+"
        elif current_val > 3.7:
            grade_char = "A"
        elif current_val > 3.3:
            grade_char = "A-"
        elif current_val > 3.0:
            grade_char = "B+"
        elif current_val > 2.7:
            grade_char = "B"
        elif current_val > 2.3:
            grade_char = "B-"
        elif current_val > 2.0:
            grade_char = "C+"
        elif current_val > 1.7:
            grade_char = "C"
        elif current_val > 1.3:
            grade_char = "C-"
        elif current_val > 1.0:
            grade_char = "D+"
        elif current_val > 0.7:
            grade_char = "D"
        elif current_val > 0.0:
            grade_char = "D-"
        else:
            grade_char = "E"
        result_list.append(grade_char)
        compute_letter(index + 1)

    compute_letter(0)
    return result_list