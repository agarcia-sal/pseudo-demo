from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    reversed_candidates = list(range(1, integer_n))[::-1]
    for candidate in reversed_candidates:
        if candidate % integer_n == 0 or integer_n % candidate == 0:
            return candidate
    return None