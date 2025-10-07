from typing import List

def numerical_letter_grade(x_list: List[float]) -> List[str]:
    y_list: List[str] = []
    z_idx: int = 0
    while z_idx < len(x_list):
        a_val: float = x_list[z_idx]
        if a_val == 4.0:
            b_str = "A+"
        elif a_val > 3.7:
            b_str = "A"
        elif a_val > 3.3:
            b_str = "A-"
        elif a_val > 3.0:
            b_str = "B+"
        elif a_val > 2.7:
            b_str = "B"
        elif a_val > 2.3:
            b_str = "B-"
        elif a_val > 2.0:
            b_str = "C+"
        elif a_val > 1.7:
            b_str = "C"
        elif a_val > 1.3:
            b_str = "C-"
        elif a_val > 1.0:
            b_str = "D+"
        elif a_val > 0.7:
            b_str = "D"
        elif a_val > 0.0:
            b_str = "D-"
        else:
            b_str = "E"
        y_list.append(b_str)
        z_idx += 1
    return y_list