from typing import Any


def fibfib(num_x: int) -> int:
    if num_x == 0:
        return 0
    if num_x == 1:
        return 0
    if num_x == 2:
        return 1
    val_a = num_x - 1
    val_b = num_x - 2
    val_c = num_x - 3
    res1 = fibfib(val_a)
    res2 = fibfib(val_b)
    res3 = fibfib(val_c)
    total = res1 + res2 + res3
    return total