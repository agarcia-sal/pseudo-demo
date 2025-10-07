from typing import List

def numerical_letter_grade(marks_collection: List[float]) -> List[str]:
    grades_output: List[str] = []
    idx: int = 0
    while idx < len(marks_collection):
        val: float = marks_collection[idx]
        if val == 4.0:
            grades_output.append("A+")
        else:
            if val > 3.7:
                grades_output.append("A")
            else:
                if val > 3.3:
                    grades_output.append("A-")
                else:
                    if val > 3.0:
                        grades_output.append("B+")
                    else:
                        if val > 2.7:
                            grades_output.append("B")
                        else:
                            if val > 2.3:
                                grades_output.append("B-")
                            else:
                                if val > 2.0:
                                    grades_output.append("C+")
                                else:
                                    if val > 1.7:
                                        grades_output.append("C")
                                    else:
                                        if val > 1.3:
                                            grades_output.append("C-")
                                        else:
                                            if val > 1.0:
                                                grades_output.append("D+")
                                            else:
                                                if val > 0.7:
                                                    grades_output.append("D")
                                                else:
                                                    if val > 0.0:
                                                        grades_output.append("D-")
                                                    else:
                                                        grades_output.append("E")
        idx += 1
    return grades_output