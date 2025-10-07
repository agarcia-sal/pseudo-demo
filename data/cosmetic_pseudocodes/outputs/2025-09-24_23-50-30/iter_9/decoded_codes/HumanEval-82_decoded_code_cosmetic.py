from typing import Union


def prime_length(input_string: str) -> bool:
    n: int = len(input_string)
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True