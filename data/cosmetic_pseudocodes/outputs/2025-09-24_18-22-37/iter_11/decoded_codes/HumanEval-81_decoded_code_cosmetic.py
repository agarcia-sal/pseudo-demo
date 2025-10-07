from typing import List


def numerical_letter_grade(array_of_scores: List[float]) -> List[str]:
    result_letters: List[str] = []
    index_counter: int = 0
    length: int = len(array_of_scores)
    while index_counter < length:
        current_gpa: float = array_of_scores[index_counter]
        temp_flag: bool = False

        if current_gpa == 4.0:
            result_letters.append("A+")
            temp_flag = True
        elif current_gpa > 3.7:
            result_letters.append("A")
            temp_flag = True
        elif current_gpa > 3.3:
            result_letters.append("A-")
            temp_flag = True
        elif current_gpa > 3.0:
            result_letters.append("B+")
            temp_flag = True
        elif current_gpa > 2.7:
            result_letters.append("B")
            temp_flag = True
        elif current_gpa > 2.3:
            result_letters.append("B-")
            temp_flag = True
        elif current_gpa > 2.0:
            result_letters.append("C+")
            temp_flag = True
        elif current_gpa > 1.7:
            result_letters.append("C")
            temp_flag = True
        elif current_gpa > 1.3:
            result_letters.append("C-")
            temp_flag = True
        elif current_gpa > 1.0:
            result_letters.append("D+")
            temp_flag = True
        elif current_gpa > 0.7:
            result_letters.append("D")
            temp_flag = True
        elif current_gpa > 0.0:
            result_letters.append("D-")
            temp_flag = True

        if not temp_flag:
            result_letters.append("E")

        index_counter += 1

    return result_letters