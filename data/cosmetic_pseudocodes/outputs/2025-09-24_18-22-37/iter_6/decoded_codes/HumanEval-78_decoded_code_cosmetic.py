from typing import Tuple

def hex_key(input_str: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count_primes: int = 0
    pos: int = 0
    while pos < len(input_str):
        current_char: str = input_str[pos]
        if current_char not in prime_chars:
            pos += 1
            continue
        else:
            count_primes += 1
        pos += 1
    return count_primes