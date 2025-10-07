from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def inner_map(index_acc: int, acc_list: List[str]) -> List[str]:
        if not (index_acc < len(list_of_grades)):
            return acc_list
        val_n = list_of_grades[index_acc]
        if val_n == 4.0:
            grade_x = "A+"
        elif val_n > 3.7:
            grade_x = "A"
        elif val_n > 3.3:
            grade_x = "A-"
        elif val_n > 3.0:
            grade_x = "B+"
        elif val_n > 2.7:
            grade_x = "B"
        elif val_n > 2.3:
            grade_x = "B-"
        elif val_n > 2.0:
            grade_x = "C+"
        elif val_n > 1.7:
            grade_x = "C"
        elif val_n > 1.3:
            grade_x = "C-"
        elif val_n > 1.0:
            grade_x = "D+"
        elif val_n > 0.7:
            grade_x = "D"
        elif val_n > 0.0:
            grade_x = "D-"
        else:
            grade_x = "E"
        return inner_map(index_acc + 1, acc_list + [grade_x])
    return inner_map(0, [])