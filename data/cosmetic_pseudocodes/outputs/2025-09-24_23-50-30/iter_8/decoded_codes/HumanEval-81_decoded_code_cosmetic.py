from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    output_sequence: List[str] = ["" for _ in range(len(list_of_grades))]
    index_counter: int = 0
    while index_counter < len(list_of_grades):
        mark_value = list_of_grades[index_counter]
        if mark_value == 4.0:
            output_sequence[index_counter] = "A+"
        elif mark_value > 3.7:
            output_sequence[index_counter] = "A"
        elif mark_value > 3.3:
            output_sequence[index_counter] = "A-"
        elif mark_value > 3.0:
            output_sequence[index_counter] = "B+"
        elif mark_value > 2.7:
            output_sequence[index_counter] = "B"
        elif mark_value > 2.3:
            output_sequence[index_counter] = "B-"
        elif mark_value > 2.0:
            output_sequence[index_counter] = "C+"
        elif mark_value > 1.7:
            output_sequence[index_counter] = "C"
        elif mark_value > 1.3:
            output_sequence[index_counter] = "C-"
        elif mark_value > 1.0:
            output_sequence[index_counter] = "D+"
        elif mark_value > 0.7:
            output_sequence[index_counter] = "D"
        elif mark_value > 0.0:
            output_sequence[index_counter] = "D-"
        else:
            output_sequence[index_counter] = "E"
        index_counter += 1
    return output_sequence