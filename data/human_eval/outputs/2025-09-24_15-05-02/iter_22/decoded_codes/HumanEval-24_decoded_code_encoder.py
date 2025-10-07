from typing import Optional

def largest_divisor(number: int) -> Optional[int]:
    for divisor in range(number - 1, 0, -1):
        if number % divisor == 0:
            return divisor
    return None