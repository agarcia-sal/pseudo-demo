from typing import Literal

def hex_key(string_num: str) -> int:
    prime_collection: tuple[Literal['2'], Literal['3'], Literal['5'], Literal['7'], Literal['B'], Literal['D']] = ('2', '3', '5', '7', 'B', 'D')
    sum_prime_chars: int = 0
    pos: int = 0
    while pos <= len(string_num) - 1:
        current_char: str = string_num[pos]
        if current_char in prime_collection:
            sum_prime_chars += 1
        pos += 1
    return sum_prime_chars