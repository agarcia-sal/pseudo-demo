from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    letter_grade_list: List[str] = []
    index: int = 0
    while index < len(list_of_grades):
        val: float = list_of_grades[index]
        if val == 4.0:
            letter_grade_list.append("A+")
        else:
            if val > 3.7:
                letter_grade_list.append("A")
            else:
                if val > 3.3:
                    letter_grade_list.append("A-")
                else:
                    if val > 3.0:
                        letter_grade_list.append("B+")
                    else:
                        if val > 2.7:
                            letter_grade_list.append("B")
                        else:
                            if val > 2.3:
                                letter_grade_list.append("B-")
                            else:
                                if val > 2.0:
                                    letter_grade_list.append("C+")
                                else:
                                    if val > 1.7:
                                        letter_grade_list.append("C")
                                    else:
                                        if val > 1.3:
                                            letter_grade_list.append("C-")
                                        else:
                                            if val > 1.0:
                                                letter_grade_list.append("D+")
                                            else:
                                                if val > 0.7:
                                                    letter_grade_list.append("D")
                                                else:
                                                    if val > 0.0:
                                                        letter_grade_list.append("D-")
                                                    else:
                                                        letter_grade_list.append("E")
        index += 1
    return letter_grade_list