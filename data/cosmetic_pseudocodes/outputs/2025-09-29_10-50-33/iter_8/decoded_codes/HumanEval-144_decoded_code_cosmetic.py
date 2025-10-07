from math import floor
from typing import Tuple


def parseFraction(fraction: str) -> Tuple[int, int]:
    parts = fraction.split("/")
    return int(parts[0]), int(parts[1])


def isIntegerDivision(num: int, den: int) -> bool:
    division_result = num / den
    return (division_result - floor(division_result)) == 0


def simplify(dividend_str: str, divisor_str: str) -> None:
    top_val, bottom_val = parseFraction(dividend_str)
    top_factor, bottom_factor = parseFraction(divisor_str)

    numerator_product = top_val * top_factor
    denominator_product = bottom_val * bottom_factor

    if isIntegerDivision(numerator_product, denominator_product):
        raise Exception(True)
    else:
        raise Exception(False)