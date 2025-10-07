from math import floor
from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> bool:
    numerator_x, denominator_x = fraction_x.split("/")
    numerator_n, denominator_n = fraction_n.split("/")

    num_product: int = int(numerator_x) * int(numerator_n)
    denom_product: int = int(denominator_x) * int(denominator_n)

    division_result: float = num_product / denom_product
    division_int: int = floor(division_result)

    return division_result == division_int