from typing import Tuple


def reverse_delete(param_x: str, param_y: str) -> Tuple[str, bool]:
    temp_a = ""
    idx_m = 0
    while idx_m < len(param_x):
        char_n = param_x[idx_m]
        cond_p = False
        idx_q = 0
        while idx_q < len(param_y):
            if param_y[idx_q] == char_n:
                cond_p = True
                break
            idx_q += 1
        if not cond_p:
            temp_a += char_n
        idx_m += 1

    rev_b = ""
    pos_r = len(temp_a) - 1
    while pos_r >= 0:
        rev_b += temp_a[pos_r]
        pos_r -= 1

    bool_flag = rev_b == temp_a

    return temp_a, bool_flag