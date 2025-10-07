from typing import List

def numerical_letter_grade(list_of_gpas: List[float]) -> List[str]:
    letter_grade_list: List[str] = []
    for gpa in list_of_gpas:
        if gpa == 4.0:
            letter_grade_list.append("A+")
        elif gpa > 3.7:
            letter_grade_list.append("A")
        elif gpa > 3.3:
            letter_grade_list.append("A-")
        elif gpa > 3.0:
            letter_grade_list.append("B+")
        elif gpa > 2.7:
            letter_grade_list.append("B")
        elif gpa > 2.3:
            letter_grade_list.append("B-")
        elif gpa > 2.0:
            letter_grade_list.append("C+")
        elif gpa > 1.7:
            letter_grade_list.append("C")
        elif gpa > 1.3:
            letter_grade_list.append("C-")
        elif gpa > 1.0:
            letter_grade_list.append("D+")
        elif gpa > 0.7:
            letter_grade_list.append("D")
        elif gpa > 0.0:
            letter_grade_list.append("D-")
        else:
            letter_grade_list.append("E")
    return letter_grade_list