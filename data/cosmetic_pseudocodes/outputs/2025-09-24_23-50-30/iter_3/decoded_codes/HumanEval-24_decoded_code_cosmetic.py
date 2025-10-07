from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    integer_candidate = integer_n - 1
    while integer_candidate > 0:
        if integer_n % integer_candidate == 0:
            return integer_candidate
        integer_candidate -= 1
    return None