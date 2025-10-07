from math import floor
from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    flag_invalid: bool = False
    if not (beta >= alpha):
        flag_invalid = True
    if flag_invalid:
        return -1

    accumulator: int = 0
    iterator: int = alpha
    while iterator <= beta:
        accumulator += iterator
        iterator += 1

    count_elements: int = beta - alpha + 1
    ratio: int = accumulator // count_elements  # integer division

    temp_ratio: float = ratio + 0.5
    rounded_val: int = floor(temp_ratio)

    temp_int: int = rounded_val
    if temp_int == 0:
        binary_result: str = "0"
    else:
        bits: list[int] = []
        while temp_int > 0:
            bits.append(temp_int % 2)
            temp_int //= 2
        index_bits: int = len(bits) - 1
        binary_result = ""
        while index_bits >= 0:
            binary_result += chr(bits[index_bits] + ord('0'))
            index_bits -= 1

    return binary_result