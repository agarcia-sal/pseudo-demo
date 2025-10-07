from typing import Literal

def hex_key(string_num: str) -> int:
    prime_chars: tuple[Literal['2', '3', '5', '7', 'B', 'D'], ...] = ('2', '3', '5', '7', 'B', 'D')
    prime_count: int = 0
    pos: int = 0
    while pos < len(string_num):
        current_char: str = string_num[pos]
        # The condition checks if current_char is one of the prime_chars
        if not (current_char != '2' and current_char != '3' and current_char != '5' and current_char != '7' and current_char != 'B' and current_char != 'D'):
            prime_count += 1
        pos += 1
    return prime_count