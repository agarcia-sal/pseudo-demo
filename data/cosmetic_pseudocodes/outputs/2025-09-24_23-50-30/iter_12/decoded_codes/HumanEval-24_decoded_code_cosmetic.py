from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    variable_a: int = integer_n - 1
    while variable_a > 0:
        if integer_n % variable_a == 0:
            return variable_a
        variable_a -= 1
    return None