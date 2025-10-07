from typing import List


def prime_length(word: str) -> bool:
    length: int = len(word)
    if length < 2:
        return False
    return not any(length % divisor == 0 for divisor in range(2, length))