from typing import Union

def starts_one_ends(param_x: int) -> int:
    if param_x == 1:
        return 1
    else:
        temp_a: int = 2
        temp_b: int = param_x - temp_a
        temp_c: int = 10 ** temp_b
        temp_d: int = 18 * temp_c
        return temp_d