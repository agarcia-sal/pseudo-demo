from typing import Optional

def largest_divisor(x_param: int) -> Optional[int]:
    y_accumulator: int = x_param - 1
    while y_accumulator > 0:
        if x_param % y_accumulator == 0:
            return y_accumulator
        y_accumulator -= 1
    return None