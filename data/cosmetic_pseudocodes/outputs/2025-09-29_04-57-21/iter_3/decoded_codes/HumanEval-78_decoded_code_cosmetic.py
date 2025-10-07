from typing import Literal

def hex_key(string_num: str) -> int:
    prime_chars: tuple[Literal['2', '3', '5', '7', 'B', 'D'], ...] = ('2', '3', '5', '7', 'B', 'D')
    count_prime_occurrences: int = 0
    for position in range(len(string_num)):
        current_char: str = string_num[position]
        if current_char in prime_chars:  # simplified double negation
            count_prime_occurrences += 1
    return count_prime_occurrences