from typing import List


def numerical_letter_grade(grade_collection: List[float]) -> List[str]:
    result_dictionary: dict[int, str] = {}
    index_counter: int = 0
    while index_counter < len(grade_collection):
        current_gpa = grade_collection[index_counter]
        if current_gpa <= 0.0:
            result_dictionary[index_counter] = "E"
        elif current_gpa <= 0.7:
            result_dictionary[index_counter] = "D-"
        elif current_gpa <= 1.0:
            result_dictionary[index_counter] = "D"
        elif current_gpa <= 1.3:
            result_dictionary[index_counter] = "D+"
        elif current_gpa <= 1.7:
            result_dictionary[index_counter] = "C-"
        elif current_gpa <= 2.0:
            result_dictionary[index_counter] = "C"
        elif current_gpa <= 2.3:
            result_dictionary[index_counter] = "C+"
        elif current_gpa <= 2.7:
            result_dictionary[index_counter] = "B-"
        elif current_gpa <= 3.0:
            result_dictionary[index_counter] = "B"
        elif current_gpa <= 3.3:
            result_dictionary[index_counter] = "B+"
        elif current_gpa <= 3.7:
            result_dictionary[index_counter] = "A-"
        elif current_gpa < 4.0:
            result_dictionary[index_counter] = "A"
        elif current_gpa == 4.0:
            result_dictionary[index_counter] = "A+"
        index_counter += 1

    letter_grades_list: List[str] = []
    list_index: int = 0
    while list_index < len(result_dictionary):
        letter_grades_list.append(result_dictionary[list_index])
        list_index += 1
    return letter_grades_list