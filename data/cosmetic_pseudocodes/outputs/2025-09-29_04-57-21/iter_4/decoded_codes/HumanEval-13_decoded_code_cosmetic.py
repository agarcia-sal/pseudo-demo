from typing import Union

def greatest_common_divisor(x_val: int, y_val: int) -> int:
    # Use integer division to ensure correct remainder calculation
    while y_val != 0:
        swap_holder = y_val
        y_val = x_val - (x_val // y_val) * y_val
        x_val = swap_holder
    return x_val