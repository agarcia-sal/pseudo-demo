from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    letter_grade_list: List[str] = []
    for grade_point_average in list_of_grades:
        if grade_point_average == 4.0:
            letter_grade_list.append("A+")
        elif grade_point_average > 3.7:
            letter_grade_list.append("A")
        elif grade_point_average > 3.3:
            letter_grade_list.append("A-")
        elif grade_point_average > 3.0:
            letter_grade_list.append("B+")
        elif grade_point_average > 2.7:
            letter_grade_list.append("B")
        elif grade_point_average > 2.3:
            letter_grade_list.append("B-")
        elif grade_point_average > 2.0:
            letter_grade_list.append("C+")
        elif grade_point_average > 1.7:
            letter_grade_list.append("C")
        elif grade_point_average > 1.3:
            letter_grade_list.append("C-")
        elif grade_point_average > 1.0:
            letter_grade_list.append("D+")
        elif grade_point_average > 0.7:
            letter_grade_list.append("D")
        elif grade_point_average > 0.0:
            letter_grade_list.append("D-")
        else:
            letter_grade_list.append("E")
    return letter_grade_list