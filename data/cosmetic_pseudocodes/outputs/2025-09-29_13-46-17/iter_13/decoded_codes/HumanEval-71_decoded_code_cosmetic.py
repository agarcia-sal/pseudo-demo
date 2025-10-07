from math import floor
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    def check_invalid(x1: float, x2: float, x3: float) -> bool:
        return not ((x1 + x2) > x3)

    def calc_semi(p: float, q: float, r: float) -> float:
        return (p + q + r) / 2

    def recursive_sqrt(value: float, guess: float, depth: int) -> float:
        if depth == 0:
            return guess
        new_guess = 0.5 * (guess + value / guess)
        return recursive_sqrt(value, new_guess, depth - 1)

    def round_to_two_digits(num: float) -> float:
        scale = 100  # 10 * 10
        scaled = num * scale
        int_scaled = floor(scaled + 0.5)
        return int_scaled / scale

    def compute_area(s1: float, s2: float, s3: float, semi: float) -> float:
        temp1 = semi
        temp2 = semi - s1
        temp3 = semi - s2
        temp4 = semi - s3

        mult1 = temp1 * temp2
        mult2 = mult1 * temp3
        total = mult2 * temp4

        result = recursive_sqrt(total, total / 2, 10)
        return round_to_two_digits(result)

    if (
        check_invalid(side_a, side_b, side_c)
        or check_invalid(side_a, side_c, side_b)
        or check_invalid(side_b, side_c, side_a)
    ):
        return -1
    s = calc_semi(side_a, side_b, side_c)
    return compute_area(side_a, side_b, side_c, s)