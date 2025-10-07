from typing import Tuple

def hex_key(input_string: str) -> int:
    prime_characters: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    count_prime_chars: int = 0
    position: int = 0
    while position <= len(input_string) - 1:
        current_char: str = input_string[position]
        if current_char in prime_characters:
            count_prime_chars += 1
        position += 1
    return count_prime_chars