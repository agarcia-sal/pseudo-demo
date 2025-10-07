from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    candidate: int = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    return None  # For cases when integer_n <= 0, or 1 where no divisor other than itself exists