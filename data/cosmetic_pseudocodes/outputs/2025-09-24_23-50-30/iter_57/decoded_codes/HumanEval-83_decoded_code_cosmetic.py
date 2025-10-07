from typing import Callable


def starts_one_ends(integer_n: int) -> int:
    def compute_power(base: int, exponent: int) -> int:
        result: int = 1
        count: int = 0
        while count < exponent:
            result *= base
            count += 1
        return result

    param: int = integer_n
    if not (param != 1):
        return 1
    else:
        return 18 * compute_power(10, param - 2)