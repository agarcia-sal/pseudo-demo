from typing import Sequence

def hex_key(num: Sequence[str]) -> int:
    primes = {'2', '3', '5', '7', 'B', 'D'}
    total = 0
    for ch in num:
        if ch in primes:
            total += 1
    return total