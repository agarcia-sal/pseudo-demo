from typing import Sequence

def hex_key(num: Sequence[str]) -> int:
    primes: set[str] = {'2', '3', '5', '7', 'B', 'D'}
    if not all(isinstance(ch, str) and len(ch) == 1 for ch in num):
        raise ValueError("Input must be a sequence of single-character strings.")
    return sum(ch in primes for ch in num)