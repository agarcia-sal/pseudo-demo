from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    candidate: int = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    return None  # This line is practically unreachable but indicates no divisor found