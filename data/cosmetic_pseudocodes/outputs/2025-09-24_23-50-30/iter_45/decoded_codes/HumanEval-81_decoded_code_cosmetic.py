from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_list: List[str] = ["" for _ in range(len(list_of_grades))]
    index_counter: int = 0

    while index_counter < len(list_of_grades):
        current_gpa = list_of_grades[index_counter]
        if current_gpa == 4.0:
            result_list[index_counter] = "A+"
        elif current_gpa > 3.7:
            result_list[index_counter] = "A"
        elif current_gpa > 3.3:
            result_list[index_counter] = "A-"
        elif current_gpa > 3.0:
            result_list[index_counter] = "B+"
        elif current_gpa > 2.7:
            result_list[index_counter] = "B"
        elif current_gpa > 2.3:
            result_list[index_counter] = "B-"
        elif current_gpa > 2.0:
            result_list[index_counter] = "C+"
        elif current_gpa > 1.7:
            result_list[index_counter] = "C"
        elif current_gpa > 1.3:
            result_list[index_counter] = "C-"
        elif current_gpa > 1.0:
            result_list[index_counter] = "D+"
        elif current_gpa > 0.7:
            result_list[index_counter] = "D"
        elif current_gpa > 0.0:
            result_list[index_counter] = "D-"
        else:
            result_list[index_counter] = "E"
        index_counter += 1

    return result_list