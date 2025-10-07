from typing import List


def numerical_letter_grade(magnitude_values: List[float]) -> List[str]:
    marks: List[str] = []
    for curr_val in magnitude_values:
        if curr_val == 4.0:
            marks.append("A+")
        elif curr_val > 3.7:
            marks.append("A")
        elif curr_val > 3.3:
            marks.append("A-")
        elif curr_val > 3.0:
            marks.append("B+")
        elif curr_val > 2.7:
            marks.append("B")
        elif curr_val > 2.3:
            marks.append("B-")
        elif curr_val > 2.0:
            marks.append("C+")
        elif curr_val > 1.7:
            marks.append("C")
        elif curr_val > 1.3:
            marks.append("C-")
        elif curr_val > 1.0:
            marks.append("D+")
        elif curr_val > 0.7:
            marks.append("D")
        elif curr_val > 0.0:
            marks.append("D-")
        else:
            marks.append("E")
    return marks