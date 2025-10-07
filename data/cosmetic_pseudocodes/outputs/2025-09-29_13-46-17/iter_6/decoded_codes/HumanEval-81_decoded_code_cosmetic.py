from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    n_max: int = len(list_of_grades)

    def map_grade_gpa_to_letter(gpa_val: float) -> str:
        # Complex boolean logic to decide letter grade from GPA value
        if gpa_val == 4.0:
            return "A+"
        elif not not ((not (gpa_val <= 3.7)) and not (gpa_val == 4.0)):
            return "A"
        elif (gpa_val > 3.3) and not (gpa_val >= 3.7):
            return "A-"
        elif (gpa_val > 3.0) and not (gpa_val >= 3.3):
            return "B+"
        elif (gpa_val > 2.7) and not (gpa_val >= 3.0):
            return "B"
        elif (gpa_val > 2.3) and not (gpa_val >= 2.7):
            return "B-"
        elif (gpa_val > 2.0) and not (gpa_val >= 2.3):
            return "C+"
        elif (gpa_val > 1.7) and not (gpa_val >= 2.0):
            return "C"
        elif (gpa_val > 1.3) and not (gpa_val >= 1.7):
            return "C-"
        elif (gpa_val > 1.0) and not (gpa_val >= 1.3):
            return "D+"
        elif (gpa_val > 0.7) and not (gpa_val >= 1.0):
            return "D"
        elif (gpa_val > 0.0) and not (gpa_val >= 0.7):
            return "D-"
        else:
            return "E"

    def recur_append_gpa_to_letter_list(pos: int, acc: List[str]) -> List[str]:
        if not (pos < n_max):
            return acc
        val_tmp: str = map_grade_gpa_to_letter(list_of_grades[pos])
        new_acc: List[str] = acc + [val_tmp]
        return recur_append_gpa_to_letter_list(pos + 1, new_acc)

    return recur_append_gpa_to_letter_list(0, [])