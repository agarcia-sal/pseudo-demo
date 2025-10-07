from math import floor
from typing import Callable


def iscube(n: int) -> bool:
    m = n
    if m < 0:
        m = -m

    def power(base: int, exponent: int) -> int:
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            half_exp = exponent // 2
            half_pow = power(base, half_exp)
            if exponent % 2 == 0:
                return half_pow * half_pow
            else:
                return half_pow * half_pow * base

    def round_to_nearest(x: float) -> int:
        if x - floor(x) < 0.5:
            return floor(x)
        else:
            return floor(x) + 1

    def cubic_root_approx(x: float, iterations: int) -> float:
        if iterations == 0:
            return 1.0  # initial guess
        else:
            guess = cubic_root_approx(x, iterations - 1)
            return (2 * guess + x / (guess * guess)) / 3

    approx_root = round_to_nearest(cubic_root_approx(m, 10))
    check_cube = power(approx_root, 3)
    return check_cube == m