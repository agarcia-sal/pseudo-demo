from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_list: List[str] = []
    for score in list_of_grades:
        if score == 4.0:
            result_list.append("A+")
        elif 3.7 < score < 4.0:
            result_list.append("A")
        elif 3.3 < score <= 3.7:
            result_list.append("A-")
        elif 3.0 < score <= 3.3:
            result_list.append("B+")
        elif 2.7 < score <= 3.0:
            result_list.append("B")
        elif 2.3 < score <= 2.7:
            result_list.append("B-")
        elif 2.0 < score <= 2.3:
            result_list.append("C+")
        elif 1.7 < score <= 2.0:
            result_list.append("C")
        elif 1.3 < score <= 1.7:
            result_list.append("C-")
        elif 1.0 < score <= 1.3:
            result_list.append("D+")
        elif 0.7 < score <= 1.0:
            result_list.append("D")
        elif 0.0 < score <= 0.7:
            result_list.append("D-")
        else:
            result_list.append("E")
    return result_list