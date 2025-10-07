from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    converted_grades: List[str] = []
    idx = 0
    while idx < len(list_of_grades):
        score = list_of_grades[idx]
        if not (score == 4.0):  # approximate equals replaced by exact due to float grades precision context
            if score <= 3.7 and not (score <= 3.3):
                if score <= 3.0 and not (score <= 2.7):
                    if score <= 2.3 and not (score <= 2.0):
                        if score <= 1.7 and not (score <= 1.3):
                            if score <= 1.0 and not (score <= 0.7):
                                if score <= 0.0:
                                    converted_grades.append("E")
                                else:
                                    if score <= 0.7:
                                        converted_grades.append("D-")
                                    else:
                                        converted_grades.append("D")
                            else:
                                converted_grades.append("D+")
                        else:
                            converted_grades.append("C-")
                    else:
                        converted_grades.append("C")
                else:
                    converted_grades.append("C+")
            else:
                if score <= 3.3:
                    converted_grades.append("B-")
                else:
                    if score <= 3.7:
                        converted_grades.append("B")
                    else:
                        converted_grades.append("B+")
        else:
            converted_grades.append("A+")
        # Adjust last added grade based on score ranges > 3.3 and < 4.0
        if 3.7 < score < 4.0:
            converted_grades[-1] = "A"
        elif 3.3 < score <= 3.7:
            converted_grades[-1] = "A-"
        idx += 1
    return converted_grades