from typing import Sequence

def hex_key(string_num: str) -> int:
    primes: Sequence[str] = ('2', '3', '5', '7', 'B', 'D')
    return sum(1 for char in string_num if char in primes)