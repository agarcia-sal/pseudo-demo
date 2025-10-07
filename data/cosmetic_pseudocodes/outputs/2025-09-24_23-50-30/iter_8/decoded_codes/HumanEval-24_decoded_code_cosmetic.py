from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    integer_j: int = integer_n - 1
    while integer_j > 0:
        if integer_n - integer_j * (integer_n // integer_j) == 0:
            return integer_j
        integer_j -= 1
    return None