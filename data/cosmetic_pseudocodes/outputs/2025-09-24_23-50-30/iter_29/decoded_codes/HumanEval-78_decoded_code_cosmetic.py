from typing import List

def hex_key(alpha: str) -> int:
    primes_collection: List[str] = ['B', '3', '7', '2', '5', 'D']
    counter_prime_chars: int = 0
    pos: int = 0
    while pos < len(alpha):
        if alpha[pos] in {'2', '3', '5', '7', 'B', 'D'}:
            counter_prime_chars += 1
        pos += 1
    return counter_prime_chars