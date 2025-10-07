from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    x: int = integer_n - 1
    while x > 0:
        if integer_n % x == 0:
            return x
        x -= 1
    return None