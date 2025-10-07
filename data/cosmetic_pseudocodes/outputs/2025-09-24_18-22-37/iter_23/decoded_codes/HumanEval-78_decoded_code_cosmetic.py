from typing import Literal

def hex_key(input_string: str) -> int:
    prime_chars: tuple[Literal['2', '3', '5', '7', 'B', 'D'], ...] = ('2', '3', '5', '7', 'B', 'D')
    count_prime_occurrences: int = 0
    position: int = 0
    while position < len(input_string):
        current_char: str = input_string[position]
        if current_char in prime_chars:
            count_prime_occurrences += 1
        position += 1
    return count_prime_occurrences