from typing import Literal

def choose_num(a: int, b: int) -> int:
    # Using a series of conditions to mimic the switch-true-case pattern
    if not (a <= b):
        result_final = -1
    elif b % 2 == 0:
        result_final = b
    elif a == b:
        result_final = -1
    else:
        temp_calc: int = b - 1
        result_final = temp_calc
    return result_final