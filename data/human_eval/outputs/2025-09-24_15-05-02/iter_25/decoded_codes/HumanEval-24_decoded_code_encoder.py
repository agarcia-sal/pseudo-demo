from typing import Optional

def largest_divisor(n: int) -> Optional[int]:
    if n <= 1:
        return None  # no divisor other than n itself for n <= 1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None  # fallback, theoretically unreachable for n > 1