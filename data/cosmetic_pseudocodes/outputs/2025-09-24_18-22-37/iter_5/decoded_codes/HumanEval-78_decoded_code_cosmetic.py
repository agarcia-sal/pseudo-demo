from typing import Tuple

def hex_key(input_string: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count_primes: int = 0
    position: int = 0
    while position < len(input_string):
        if input_string[position] in prime_chars:
            count_primes += 1
        position += 1
    return count_primes