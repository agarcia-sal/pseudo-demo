from typing import Literal

def fibfib(param_x: int) -> int:
    if param_x == 0:
        return 0
    if param_x == 1:
        return 0
    if param_x == 2:
        return 1

    temp1: int = param_x - 1
    temp2: int = param_x - 2
    temp3: int = param_x - 3

    val1: int = fibfib(temp1)
    val2: int = fibfib(temp2)
    val3: int = fibfib(temp3)

    sum_result: int = val1 + val2 + val3

    return sum_result