from typing import Optional


def prime_length(input_string: str) -> bool:
    length: int = len(input_string)
    if length < 2:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True