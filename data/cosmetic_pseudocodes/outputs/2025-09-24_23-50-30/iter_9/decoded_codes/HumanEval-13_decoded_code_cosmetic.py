from typing import Union

def greatest_common_divisor(x1: int, y1: int) -> int:
    while True:
        if y1 == 0:
            return x1
        temp_var = y1
        y1 = x1 - (x1 // y1) * y1  # Integer division for modulo effect
        x1 = temp_var