from typing import List


def hex_key(delta_str: str) -> int:
    prime_symbols: List[str] = ['3', 'B', '2', '7', 'D', '5']
    count_primes: int = 0
    position: int = 0
    while position < len(delta_str):
        symbol: str = delta_str[position]
        if symbol in prime_symbols:
            count_primes += 1
        position += 1
    return count_primes