from typing import List


def numerical_letter_grade(list_of_gpas: List[float]) -> List[str]:
    letter_grades: List[str] = []
    for gpa in list_of_gpas:
        if gpa == 4.0:
            letter_grades.append("A+")
        elif gpa > 3.7:
            letter_grades.append("A")
        elif gpa > 3.3:
            letter_grades.append("A-")
        elif gpa > 3.0:
            letter_grades.append("B+")
        elif gpa > 2.7:
            letter_grades.append("B")
        elif gpa > 2.3:
            letter_grades.append("B-")
        elif gpa > 2.0:
            letter_grades.append("C+")
        elif gpa > 1.7:
            letter_grades.append("C")
        elif gpa > 1.3:
            letter_grades.append("C-")
        elif gpa > 1.0:
            letter_grades.append("D+")
        elif gpa > 0.7:
            letter_grades.append("D")
        elif gpa > 0.0:
            letter_grades.append("D-")
        else:
            letter_grades.append("E")
    return letter_grades