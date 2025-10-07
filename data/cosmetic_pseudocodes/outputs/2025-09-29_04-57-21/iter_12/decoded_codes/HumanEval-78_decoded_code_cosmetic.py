from typing import List


def hex_key(string_num: str) -> int:
    prime_characters: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_count: int = 0
    current_position: int = 0
    while current_position < len(string_num):
        current_char: str = string_num[current_position]
        if current_char in prime_characters:
            prime_count += 1
        current_position += 1
    return prime_count