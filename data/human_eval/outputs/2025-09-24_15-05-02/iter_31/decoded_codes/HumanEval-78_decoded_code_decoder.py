from typing import Tuple


def hex_key(string_num: str) -> int:
    primes: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    return sum(ch in primes for ch in string_num)