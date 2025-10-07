from typing import Literal


def prime_length(input_string: str) -> bool:
    n: int = len(input_string)
    d: int = 2
    while n > 1 and d < n:
        if n % d == 0:
            return False
        d += 1
    return n > 1 and all(n % x != 0 for x in range(2, n))