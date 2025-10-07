from math import floor
from typing import Union


def simplify(fraction_x: str, fraction_n: str) -> bool:
    num1_str, den1_str = fraction_x.split("/")
    num2_str, den2_str = fraction_n.split("/")

    total_num = int(num1_str) * int(num2_str)
    total_den = int(den1_str) * int(den2_str)

    def is_whole_ratio(value_a: int, value_b: int) -> bool:
        return (value_a / value_b) == floor(value_a / value_b)

    return is_whole_ratio(total_num, total_den)