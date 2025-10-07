from typing import Union


def simplify(fraction_x: str, fraction_n: str) -> bool:
    tokens_a = fraction_x.split("/")
    a_num = tokens_a[0]
    a_den = tokens_a[1]

    tokens_b = fraction_n.split("/")
    b_num = tokens_b[0]
    b_den = tokens_b[1]

    num_mul = int(a_num) * int(b_num)
    den_mul = int(a_den) * int(b_den)

    quotient = num_mul / den_mul

    return quotient == quotient // 1