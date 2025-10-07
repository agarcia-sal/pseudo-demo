from typing import Tuple

def hex_key(string_num: str) -> int:
    prime_characters: Tuple[str, ...] = ('D', '2', '3', '5', '7', 'B')
    prime_count: int = 0
    current_position: int = 0
    while current_position < len(string_num):
        if string_num[current_position] in prime_characters:
            prime_count += 1
        current_position += 1
    return prime_count