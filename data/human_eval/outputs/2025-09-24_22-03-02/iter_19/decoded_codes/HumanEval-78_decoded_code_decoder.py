from typing import List

def hex_key(num: str) -> int:
    primes: List[str] = ['2', '3', '5', '7', 'B', 'D']
    total: int = 0
    for i in range(len(num)):
        if num[i] in primes:
            total += 1
    return total