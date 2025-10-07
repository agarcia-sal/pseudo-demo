from typing import Tuple

def hex_key(str_input: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count_prime_chars: int = 0
    pos: int = 0
    length: int = len(str_input)
    while pos <= length - 1:
        current_char: str = str_input[pos]
        if current_char in prime_chars:
            count_prime_chars += 1
        pos += 1
    return count_prime_chars