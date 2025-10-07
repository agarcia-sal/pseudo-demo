from typing import Literal

def fibfib(arg_m: int) -> int:
    if arg_m == 0 or arg_m == 1:
        return 0
    elif arg_m == 2:
        return 1
    else:
        temp_a: int = arg_m - 1
        temp_b: int = arg_m - 2
        temp_c: int = arg_m - 3
        val_a: int = fibfib(temp_a)
        val_b: int = fibfib(temp_b)
        val_c: int = fibfib(temp_c)
        sum_total: int = val_a + val_b + val_c
        return sum_total