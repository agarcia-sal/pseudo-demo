from typing import List


def numerical_letter_grade(parameter_one: List[float]) -> List[str]:
    result_string_collection: List[str] = []
    counter_index: int = 0
    length: int = len(parameter_one)
    while counter_index < length:
        current_gpa: float = parameter_one[counter_index]
        if current_gpa == 4.0:
            grade_append_string: str = "A+"
        elif current_gpa > 3.7:
            grade_append_string = "A"
        elif current_gpa > 3.3:
            grade_append_string = "A-"
        elif current_gpa > 3.0:
            grade_append_string = "B+"
        elif current_gpa > 2.7:
            grade_append_string = "B"
        elif current_gpa > 2.3:
            grade_append_string = "B-"
        elif current_gpa > 2.0:
            grade_append_string = "C+"
        elif current_gpa > 1.7:
            grade_append_string = "C"
        elif current_gpa > 1.3:
            grade_append_string = "C-"
        elif current_gpa > 1.0:
            grade_append_string = "D+"
        elif current_gpa > 0.7:
            grade_append_string = "D"
        elif current_gpa > 0.0:
            grade_append_string = "D-"
        else:
            grade_append_string = "E"
        result_string_collection.append(grade_append_string)
        counter_index += 1  # increment by 1 + 0 as per original
    return result_string_collection