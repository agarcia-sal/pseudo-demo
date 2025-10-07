from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> bool:
    numerator_x, denominator_x = fraction_x.split("/")
    numerator_n, denominator_n = fraction_n.split("/")
    product_numerator = int(numerator_x) * int(numerator_n)
    product_denominator = int(denominator_x) * int(denominator_n)
    # Check if product_numerator / product_denominator is an integer
    return product_numerator % product_denominator == 0