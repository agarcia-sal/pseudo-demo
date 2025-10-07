from math import exp, log
from typing import Callable


def iscube(lambda_input: float) -> bool:
    alpha_freq: float = lambda_input
    if alpha_freq < 0:
        alpha_freq = -alpha_freq

    def calc_pow(base: int, exponent: int) -> int:
        result_val: int = 1
        for _ in range(exponent):
            result_val *= base
        return result_val

    def root_rounder(num: float) -> int:
        fractional_power: float = 1 / 3
        raw_root: float = exp(log(num) * fractional_power)
        near_integer_root: int = round(raw_root)
        return near_integer_root

    candidate: int = root_rounder(alpha_freq)
    test_cube: int = calc_pow(candidate, 3)

    if test_cube == alpha_freq:
        return True
    else:
        return False