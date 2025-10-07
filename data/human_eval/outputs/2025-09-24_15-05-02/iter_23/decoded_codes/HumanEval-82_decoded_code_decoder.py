from typing import Optional


def prime_length(string: str) -> bool:
    length: int = len(string)
    if length <= 1:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True