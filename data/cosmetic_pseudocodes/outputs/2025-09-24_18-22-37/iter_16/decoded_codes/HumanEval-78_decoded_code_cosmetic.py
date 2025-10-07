from typing import Sequence


def hex_key(beta: Sequence[str]) -> int:
    primes_collection = {'2', '3', '5', '7', 'B', 'D'}
    prime_counter = 0
    pos = 0
    while pos <= len(beta) - 1:
        current_char = beta[pos]
        if current_char in primes_collection:
            prime_counter += 1
        pos += 1
    return prime_counter