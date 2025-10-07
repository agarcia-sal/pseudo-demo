from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_letters: List[str] = []
    iterator: int = 0
    while iterator < len(list_of_grades):
        current_value: float = list_of_grades[iterator]

        if current_value != 4.0:
            if not (current_value > 3.7):
                if not (current_value > 3.3):
                    if not (current_value > 3.0):
                        if not (current_value > 2.7):
                            if not (current_value > 2.3):
                                if not (current_value > 2.0):
                                    if not (current_value > 1.7):
                                        if not (current_value > 1.3):
                                            if not (current_value > 1.0):
                                                if not (current_value > 0.7):
                                                    if not (current_value > 0.0):
                                                        result_letters.append("E")
                                                    else:
                                                        result_letters.append("D-")
                                                else:
                                                    result_letters.append("D")
                                            else:
                                                result_letters.append("D+")
                                        else:
                                            result_letters.append("C-")
                                    else:
                                        result_letters.append("C")
                                else:
                                    result_letters.append("C+")
                            else:
                                result_letters.append("B-")
                        else:
                            result_letters.append("B")
                    else:
                        result_letters.append("B+")
                else:
                    result_letters.append("A-")
            else:
                result_letters.append("A")
        else:
            result_letters.append("A+")

        iterator += 1
    return result_letters