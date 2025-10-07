from typing import List

def hex_key(num: str) -> int:
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(c in primes for c in num)