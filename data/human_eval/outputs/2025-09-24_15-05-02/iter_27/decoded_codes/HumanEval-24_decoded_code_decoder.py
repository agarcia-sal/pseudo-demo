from typing import Optional

def largest_divisor(n: int) -> Optional[int]:
    if n <= 1:
        # No divisors for n <= 1 other than n itself,
        # but since function searches down from n-1, no valid divisor occurs.
        return None
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None  # logically unreachable since 1 divides every n >= 2