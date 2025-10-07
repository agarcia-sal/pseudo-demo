from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    candidate: int = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    return None  # In case no divisor is found, which can happen if integer_n <= 0