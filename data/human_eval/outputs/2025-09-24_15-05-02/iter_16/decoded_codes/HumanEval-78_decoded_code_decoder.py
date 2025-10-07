from typing import Sequence

def hex_key(num: Sequence[str]) -> int:
    primes: tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    total: int = 0
    for i in range(len(num)):
        if num[i] in primes:
            total += 1
    return total