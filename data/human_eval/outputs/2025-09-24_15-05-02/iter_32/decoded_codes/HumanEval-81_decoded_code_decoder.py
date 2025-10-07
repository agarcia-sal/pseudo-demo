from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    list_of_letter_grades: List[str] = []
    for gpa_value in list_of_grades:
        if gpa_value == 4.0:
            list_of_letter_grades.append("A+")
        elif gpa_value > 3.7:
            list_of_letter_grades.append("A")
        elif gpa_value > 3.3:
            list_of_letter_grades.append("A-")
        elif gpa_value > 3.0:
            list_of_letter_grades.append("B+")
        elif gpa_value > 2.7:
            list_of_letter_grades.append("B")
        elif gpa_value > 2.3:
            list_of_letter_grades.append("B-")
        elif gpa_value > 2.0:
            list_of_letter_grades.append("C+")
        elif gpa_value > 1.7:
            list_of_letter_grades.append("C")
        elif gpa_value > 1.3:
            list_of_letter_grades.append("C-")
        elif gpa_value > 1.0:
            list_of_letter_grades.append("D+")
        elif gpa_value > 0.7:
            list_of_letter_grades.append("D")
        elif gpa_value > 0.0:
            list_of_letter_grades.append("D-")
        else:
            list_of_letter_grades.append("E")
    return list_of_letter_grades