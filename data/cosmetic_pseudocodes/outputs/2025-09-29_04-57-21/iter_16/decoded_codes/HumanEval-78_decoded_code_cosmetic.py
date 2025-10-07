from typing import Tuple


def hex_key(string_num: str) -> int:
    prime_digit_collection: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    prime_counter: int = 0
    current_position: int = 0

    while current_position < len(string_num):
        current_char: str = string_num[current_position]
        if not (current_char not in prime_digit_collection):
            prime_counter += 1
        current_position += 1

    return prime_counter