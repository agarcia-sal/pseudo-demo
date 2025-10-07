from typing import List, Union


def numerical_letter_grade(alpha_numeric_list: List[Union[int, float]]) -> List[str]:
    beta_list: List[str] = []
    i: int = 0
    while i < len(alpha_numeric_list):
        x = alpha_numeric_list[i]
        if x == 4.0:
            beta_list.append("A+")
        elif x > 3.7:
            beta_list.append("A")
        elif x > 3.3:
            beta_list.append("A-")
        elif x > 3.0:
            beta_list.append("B+")
        elif x > 2.7:
            beta_list.append("B")
        elif x > 2.3:
            beta_list.append("B-")
        elif x > 2.0:
            beta_list.append("C+")
        elif x > 1.7:
            beta_list.append("C")
        elif x > 1.3:
            beta_list.append("C-")
        elif x > 1.0:
            beta_list.append("D+")
        elif x > 0.7:
            beta_list.append("D")
        elif x > 0.0:
            beta_list.append("D-")
        else:
            beta_list.append("E")
        i += 1
    return beta_list