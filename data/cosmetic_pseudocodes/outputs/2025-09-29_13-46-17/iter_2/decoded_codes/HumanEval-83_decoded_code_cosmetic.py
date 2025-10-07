from typing import Union


def starts_one_ends(integer_n: int) -> int:
    def power_recursive(b: int, e: int) -> int:
        if e <= 0:
            return 1
        else:
            return b * power_recursive(b, e - 1)

    if integer_n == 1:
        return 1
    else:
        base = 10
        exponent = integer_n - 2
        power_result = power_recursive(base, exponent)
        product = 18 * power_result
        return product