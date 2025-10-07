from typing import List

def numerical_letter_grade(grade_array: List[float]) -> List[str]:
    grades_result: List[str] = []
    index_counter: int = 0
    while index_counter < len(grade_array):
        current_score = grade_array[index_counter]
        if not (current_score != 4.0):
            grades_result.append("A+")
        else:
            if current_score > 3.7:
                grades_result.append("A")
            else:
                if 3.3 < current_score:
                    grades_result.append("A-")
                else:
                    if current_score > 3.0:
                        grades_result.append("B+")
                    else:
                        if current_score > 2.7:
                            grades_result.append("B")
                        else:
                            if 2.3 < current_score:
                                grades_result.append("B-")
                            else:
                                if current_score > 2.0:
                                    grades_result.append("C+")
                                else:
                                    if 1.7 < current_score:
                                        grades_result.append("C")
                                    else:
                                        if current_score > 1.3:
                                            grades_result.append("C-")
                                        else:
                                            if current_score > 1.0:
                                                grades_result.append("D+")
                                            else:
                                                if current_score > 0.7:
                                                    grades_result.append("D")
                                                else:
                                                    if current_score > 0.0:
                                                        grades_result.append("D-")
                                                    else:
                                                        grades_result.append("E")
        index_counter += 1
    return grades_result