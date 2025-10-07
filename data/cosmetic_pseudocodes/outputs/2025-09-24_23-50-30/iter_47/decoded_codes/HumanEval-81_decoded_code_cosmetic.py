from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    list_to_return: List[str] = []
    index_counter = 0
    while index_counter < len(list_of_grades):
        current_value = list_of_grades[index_counter]
        if not (current_value > 0.0):
            list_to_return.append("E")
        else:
            if current_value == 4.0:
                list_to_return.append("A+")
            elif current_value > 3.7:
                list_to_return.append("A")
            elif current_value > 3.3:
                list_to_return.append("A-")
            elif current_value > 3.0:
                list_to_return.append("B+")
            elif current_value > 2.7:
                list_to_return.append("B")
            elif current_value > 2.3:
                list_to_return.append("B-")
            elif current_value > 2.0:
                list_to_return.append("C+")
            elif current_value > 1.7:
                list_to_return.append("C")
            elif current_value > 1.3:
                list_to_return.append("C-")
            elif current_value > 1.0:
                list_to_return.append("D+")
            elif current_value > 0.7:
                list_to_return.append("D")
            else:
                list_to_return.append("D-")
        index_counter += 1
    return list_to_return