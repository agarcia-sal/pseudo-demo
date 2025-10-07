from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    converted_grades: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(list_of_grades):
        current_score = list_of_grades[iterator_index]
        if current_score == 4.0:
            converted_grades.append("A+")
        else:
            if not (current_score <= 3.7):
                converted_grades.append("A")
            else:
                if not (current_score <= 3.3):
                    converted_grades.append("A-")
                else:
                    if not (current_score <= 3.0):
                        converted_grades.append("B+")
                    else:
                        if not (current_score <= 2.7):
                            converted_grades.append("B")
                        else:
                            if not (current_score <= 2.3):
                                converted_grades.append("B-")
                            else:
                                if not (current_score <= 2.0):
                                    converted_grades.append("C+")
                                else:
                                    if not (current_score <= 1.7):
                                        converted_grades.append("C")
                                    else:
                                        if not (current_score <= 1.3):
                                            converted_grades.append("C-")
                                        else:
                                            if not (current_score <= 1.0):
                                                converted_grades.append("D+")
                                            else:
                                                if not (current_score <= 0.7):
                                                    converted_grades.append("D")
                                                else:
                                                    if not (current_score <= 0.0):
                                                        converted_grades.append("D-")
                                                    else:
                                                        converted_grades.append("E")
        iterator_index += 1
    return converted_grades