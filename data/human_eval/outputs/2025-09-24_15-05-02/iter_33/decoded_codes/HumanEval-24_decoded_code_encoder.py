from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    if integer_n <= 1:
        return None  # no divisor in range for n <= 1
    for integer_i in range(integer_n - 1, 0, -1):
        if integer_n % integer_i == 0:
            return integer_i
    return None