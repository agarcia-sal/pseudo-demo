from math import floor
from typing import Union


def simplify(fraction_x: str, fraction_n: str) -> bool:
    n_digits: str = ""
    d_digits: str = ""
    p_digits: str = ""
    q_digits: str = ""
    index_x: int = 0

    # Parse numerator of fraction_x
    while True:
        char_x = fraction_x[index_x]
        if char_x == "/":
            break
        n_digits += char_x
        index_x += 1

    index_x += 1  # skip '/'

    # Parse denominator of fraction_x
    while index_x < len(fraction_x):
        d_digits += fraction_x[index_x]
        index_x += 1

    index_n: int = 0

    # Parse numerator of fraction_n
    while True:
        char_n = fraction_n[index_n]
        if char_n == "/":
            break
        p_digits += char_n
        index_n += 1

    index_n += 1  # skip '/'

    # Parse denominator of fraction_n
    while index_n < len(fraction_n):
        q_digits += fraction_n[index_n]
        index_n += 1

    num_product = int(n_digits) * int(p_digits)
    den_product = int(d_digits) * int(q_digits)

    quotient: float = num_product / den_product

    # Check if quotient is integer (no fractional part)
    return not (quotient > floor(quotient))