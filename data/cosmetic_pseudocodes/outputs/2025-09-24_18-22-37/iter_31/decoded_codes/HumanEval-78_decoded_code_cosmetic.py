from typing import Tuple

def hex_key(code_str: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count_prime_occurrences: int = 0
    pos: int = 0
    length: int = len(code_str)
    while pos < length:
        current_c: str = code_str[pos]
        if current_c in prime_chars:
            count_prime_occurrences += 1
        pos += 1
    return count_prime_occurrences