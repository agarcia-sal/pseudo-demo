from math import floor, ceil
from typing import List


def rounded_avg(x_start: int, x_end: int) -> str:
    if x_end < x_start:
        return "-1"

    def accumulate(current: int, terminal: int, total: int) -> int:
        if current > terminal:
            return total
        return accumulate(current + 1, terminal, total + current)

    total_sum: int = accumulate(x_start, x_end, 0)
    count_elements: int = x_end - x_start + 1
    mean_val: float = total_sum / count_elements

    def integer_round(val: float) -> int:
        return ceil(val) if val - floor(val) >= 0.5 else floor(val)

    rounded_val: int = integer_round(mean_val)

    def convert_to_binary(num: int) -> str:
        if num == 0:
            return "0"
        digits: List[str] = []
        n: int = num
        while n > 0:
            digits.append(str(n % 2))
            n //= 2
        return "".join(reversed(digits))

    bin_str: str = convert_to_binary(rounded_val)
    return bin_str