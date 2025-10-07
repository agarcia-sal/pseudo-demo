from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    if integer_n <= 1:
        return None  # no divisor less than integer_n for 1 or less
    integer_j = integer_n - 1
    while integer_j > 0:
        if integer_n - (integer_j * (integer_n // integer_j)) == 0:
            return integer_j
        integer_j -= 1
    return None