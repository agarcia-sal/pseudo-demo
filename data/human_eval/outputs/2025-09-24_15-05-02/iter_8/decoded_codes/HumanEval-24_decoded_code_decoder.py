from typing import Optional

def largest_divisor(n: int) -> Optional[int]:
    for divisor in range(n - 1, 0, -1):
        if n % divisor == 0:
            return divisor
    return None