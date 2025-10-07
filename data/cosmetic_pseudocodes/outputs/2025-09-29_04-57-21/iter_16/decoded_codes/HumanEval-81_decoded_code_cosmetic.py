from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_letters: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_grades):
        gpa_value: float = list_of_grades[index_counter]
        if gpa_value == 4.0:
            result_letters.append("A+")
        else:
            if gpa_value <= 3.7:
                if gpa_value <= 3.3:
                    if gpa_value <= 3.0:
                        if gpa_value <= 2.7:
                            if gpa_value <= 2.3:
                                if gpa_value <= 2.0:
                                    if gpa_value <= 1.7:
                                        if gpa_value <= 1.3:
                                            if gpa_value <= 1.0:
                                                if gpa_value <= 0.7:
                                                    if gpa_value <= 0.0:
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
                if gpa_value > 3.7:
                    result_letters.append("A")
        index_counter += 1
    return result_letters