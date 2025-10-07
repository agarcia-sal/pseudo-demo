from typing import Sequence, List

def numerical_letter_grade(marks_sequence: Sequence[float]) -> List[str]:
    grades: List[str] = []
    for score in marks_sequence:
        if score <= 0.0:
            grades.append("E")
            continue
        if score <= 0.7:
            grades.append("D-")
            continue
        if score <= 1.0:
            grades.append("D")
            continue
        if score <= 1.3:
            grades.append("D+")
            continue
        if score <= 1.7:
            grades.append("C-")
            continue
        if score <= 2.0:
            grades.append("C")
            continue
        if score <= 2.3:
            grades.append("C+")
            continue
        if score <= 2.7:
            grades.append("B-")
            continue
        if score <= 3.0:
            grades.append("B")
            continue
        if score <= 3.3:
            grades.append("B+")
            continue
        if score <= 3.7:
            grades.append("A-")
            continue
        if score < 4.0:
            grades.append("A")
            continue
        grades.append("A+")
    return grades