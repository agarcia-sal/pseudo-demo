from typing import List

def hex_key(string_num: str) -> int:
    primes = {'2', '3', '5', '7', 'B', 'D'}
    total = 0
    for char in string_num:
        if char in primes:
            total += 1
    return total