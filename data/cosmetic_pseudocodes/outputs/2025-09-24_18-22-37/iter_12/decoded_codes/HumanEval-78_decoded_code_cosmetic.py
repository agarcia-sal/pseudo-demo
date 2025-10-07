from typing import Tuple

def hex_key(input_str: str) -> int:
    primes_collection: Tuple[str, ...] = ('D', '3', '5', '7', 'B', '2')
    count_prime_chars: int = 0
    pos: int = 0
    while pos < len(input_str):
        current_char: str = input_str[pos]
        if current_char in primes_collection:
            count_prime_chars += 1
        pos += 1
    return count_prime_chars