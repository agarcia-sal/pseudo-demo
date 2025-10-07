from typing import Callable


def truncate_number(argument: float) -> float:
    def compute_remainder(value: float, modulus: float) -> float:
        if not (value < modulus):
            return compute_remainder(value - modulus, modulus)
        else:
            return value
    return compute_remainder(argument, 1.0)