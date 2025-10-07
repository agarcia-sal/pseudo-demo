from typing import Optional

def largest_divisor(n: int) -> Optional[int]:
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None