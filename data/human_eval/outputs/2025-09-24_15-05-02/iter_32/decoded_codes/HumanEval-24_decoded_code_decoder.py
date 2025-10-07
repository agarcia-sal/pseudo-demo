from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    if integer_n == 0:
        return None  # No divisors for zero
    for integer_i in range(integer_n - 1, 0, -1):
        if integer_n % integer_i == 0:
            return integer_i
    return None  # integer_n is 1 or -1, no divisor less than it