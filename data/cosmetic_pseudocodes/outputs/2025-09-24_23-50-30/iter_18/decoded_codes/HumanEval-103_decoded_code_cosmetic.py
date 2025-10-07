from math import floor, ceil
from typing import Union

def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"
    accumulator: int = 0
    index: int = alpha
    while index <= beta:
        accumulator += index
        index += 1
    total_count: int = (beta - alpha) + 1
    quotient: float = accumulator / total_count

    # Compute rounded_result as the nearest integer with tie rounding up
    if quotient >= 0.5 + floor(quotient):
        rounded_result: int = ceil(quotient)
    else:
        rounded_result = floor(quotient)

    bin_str: str = ""
    temp_val: int = rounded_result

    if temp_val == 0:
        bin_str = "0"
    while temp_val > 0:
        bit_val: int = temp_val - 2 * (temp_val // 2)
        # char of '0' + bit_val
        bin_str = chr(bit_val + 48) + bin_str
        temp_val = temp_val // 2

    return bin_str