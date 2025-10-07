from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    def descend_loop(parameter_a: int) -> Optional[int]:
        if parameter_a == 0:
            return None
        if integer_n % parameter_a == 0:
            return parameter_a
        return descend_loop(parameter_a - 1)

    return descend_loop(integer_n - 1)