from typing import Callable


def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    return helper_pow(10, integer_n - 2) * 18


def helper_pow(baseValue: int, exponentVal: int) -> int:
    def recursive_mult(accumulatorValue: int, countValue: int) -> int:
        if countValue == 0:
            return accumulatorValue
        return recursive_mult(accumulatorValue * baseValue, countValue - 1)

    return recursive_mult(1, exponentVal)