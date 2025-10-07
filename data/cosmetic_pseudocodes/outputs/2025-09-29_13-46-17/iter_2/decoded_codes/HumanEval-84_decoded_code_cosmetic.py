from typing import Callable


def solve(integer_N: int) -> str:
    def accumulate_digits(digits_str: str, idx: int, total: int) -> int:
        if idx > len(digits_str):
            return total
        return accumulate_digits(digits_str, idx + 1, total + int(digits_str[idx - 1]))

    digits_string: str = str(integer_N)
    sum_val: int = accumulate_digits(digits_string, 1, 0)
    bin_str: str = bin(sum_val)
    return bin_str[3:]