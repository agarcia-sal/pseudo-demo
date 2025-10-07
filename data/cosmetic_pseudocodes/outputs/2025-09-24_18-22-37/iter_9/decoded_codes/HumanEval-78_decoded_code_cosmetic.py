from typing import Tuple


def hex_key(input_text: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count_primes: int = 0
    pos: int = 0
    while pos <= len(input_text) - 1:
        current_char: str = input_text[pos]
        if current_char in prime_chars:
            count_primes += 1
        pos += 1
    return count_primes