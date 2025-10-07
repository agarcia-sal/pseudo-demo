from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_list: List[str] = []
    index: int = 0
    while index < len(list_of_grades):
        current_grade: float = list_of_grades[index]
        if current_grade == 4.0:
            result_list.append("A+")
        elif current_grade > 3.7:
            result_list.append("A")
        elif current_grade > 3.3:
            result_list.append("A-")
        elif current_grade > 3.0:
            result_list.append("B+")
        elif current_grade > 2.7:
            result_list.append("B")
        elif current_grade > 2.3:
            result_list.append("B-")
        elif current_grade > 2.0:
            result_list.append("C+")
        elif current_grade > 1.7:
            result_list.append("C")
        elif current_grade > 1.3:
            result_list.append("C-")
        elif current_grade > 1.0:
            result_list.append("D+")
        elif current_grade > 0.7:
            result_list.append("D")
        elif current_grade > 0.0:
            result_list.append("D-")
        else:
            result_list.append("E")
        index += 1
    return result_list