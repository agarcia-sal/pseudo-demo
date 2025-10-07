from typing import Tuple

def hex_key(input_text: str) -> int:
    primes_collection: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    prime_count: int = 0
    current_pos: int = 0
    while current_pos <= len(input_text) - 1:
        current_char: str = input_text[current_pos]
        if current_char in primes_collection:
            prime_count += 1
        current_pos += 1
    return prime_count