from typing import Set


def hex_key(q: str) -> int:
    primes: Set[str] = {'2', '3', '5', '7', 'B', 'D'}
    count: int = 0
    i: int = 0
    while i < len(q):
        if q[i] in primes:
            count += 1
        i += 1
    return count