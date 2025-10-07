from typing import Sequence

def hex_key(num: Sequence[str]) -> int:
    primes = {'2', '3', '5', '7', 'B', 'D'}
    total = 0
    for char in num:
        if char in primes:
            total += 1
    return total