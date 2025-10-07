from typing import Union


def fibfib(param_x: int) -> int:
    if param_x == 0:
        return 0
    if param_x == 1:
        return 0
    if param_x == 2:
        return 1
    temp_val1: int = fibfib(param_x - 1)
    temp_val2: int = fibfib(param_x - 2)
    temp_val3: int = fibfib(param_x - 3)
    result_val: int = temp_val1 + temp_val2 + temp_val3
    return result_val