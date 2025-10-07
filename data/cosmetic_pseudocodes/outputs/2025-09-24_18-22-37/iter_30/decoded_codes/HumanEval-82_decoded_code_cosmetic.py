from typing import Any


def prime_length(input_string: str) -> bool:
    n: int = len(input_string)
    if n <= 1:
        return False
    d: int = 2
    while d <= n - 1:
        remainder: int = n % d
        if remainder == 0:
            return False
        d += 1
    return True