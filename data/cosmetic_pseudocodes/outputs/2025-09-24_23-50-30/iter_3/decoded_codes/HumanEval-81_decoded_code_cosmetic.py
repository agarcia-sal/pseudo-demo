from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    results: List[str] = []
    for gpa in list_of_grades:
        if gpa == 4.0:
            results.append("A+")
        elif gpa > 3.7:
            results.append("A")
        elif gpa > 3.3:
            results.append("A-")
        elif gpa > 3.0:
            results.append("B+")
        elif gpa > 2.7:
            results.append("B")
        elif gpa > 2.3:
            results.append("B-")
        elif gpa > 2.0:
            results.append("C+")
        elif gpa > 1.7:
            results.append("C")
        elif gpa > 1.3:
            results.append("C-")
        elif gpa > 1.0:
            results.append("D+")
        elif gpa > 0.7:
            results.append("D")
        elif gpa > 0.0:
            results.append("D-")
        else:
            results.append("E")
    return results