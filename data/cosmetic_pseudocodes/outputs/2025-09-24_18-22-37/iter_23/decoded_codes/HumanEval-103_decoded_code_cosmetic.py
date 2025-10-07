from math import floor
from typing import Union


def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"

    total_sum: int = 0
    current_index: int = alpha
    while current_index <= beta:
        total_sum += current_index
        current_index += 1

    count: int = beta - alpha + 1
    raw_average: float = total_sum / count

    decimal_part: float = raw_average - floor(raw_average)
    if decimal_part >= 0.5:
        nearest_int: int = floor(raw_average) + 1
    else:
        nearest_int = floor(raw_average)

    binary_form: str = ""
    if nearest_int == 0:
        binary_form = "0"
    else:
        temp_num: int = nearest_int
        bits_stack: list[int] = []
        while temp_num > 0:
            bits_stack.append(temp_num % 2)
            temp_num //= 2
        # build binary string from bits_stack in reverse order
        for idx in range(len(bits_stack) - 1, -1, -1):
            binary_form += str(bits_stack[idx])

    return binary_form