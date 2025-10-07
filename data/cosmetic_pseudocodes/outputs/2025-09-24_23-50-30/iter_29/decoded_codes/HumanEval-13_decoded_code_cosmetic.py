from typing import Union

def greatest_common_divisor(x1: int, x2: int) -> int:
    if x2 == 0:
        return x1
    else:
        return greatest_common_divisor(x2, x1 - (x1 // x2) * x2)