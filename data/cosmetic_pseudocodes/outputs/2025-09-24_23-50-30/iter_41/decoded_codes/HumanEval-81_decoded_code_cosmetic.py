from typing import List


def numerical_letter_grade(beta_list: List[float]) -> List[str]:
    letter_array: List[str] = []
    index_counter: int = 0
    while index_counter < len(beta_list):
        grade_value: float = beta_list[index_counter]
        if grade_value == 4.0:
            letter_array.append("A+")
        elif grade_value > 3.7:
            letter_array.append("A")
        elif grade_value > 3.3:
            letter_array.append("A-")
        elif grade_value > 3.0:
            letter_array.append("B+")
        elif grade_value > 2.7:
            letter_array.append("B")
        elif grade_value > 2.3:
            letter_array.append("B-")
        elif grade_value > 2.0:
            letter_array.append("C+")
        elif grade_value > 1.7:
            letter_array.append("C")
        elif grade_value > 1.3:
            letter_array.append("C-")
        elif grade_value > 1.0:
            letter_array.append("D+")
        elif grade_value > 0.7:
            letter_array.append("D")
        elif grade_value > 0.0:
            letter_array.append("D-")
        else:
            letter_array.append("E")
        index_counter += 1
    return letter_array