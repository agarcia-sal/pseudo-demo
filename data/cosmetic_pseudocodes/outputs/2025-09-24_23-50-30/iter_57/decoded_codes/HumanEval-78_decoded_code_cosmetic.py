from typing import Literal

def hex_key(input_string: str) -> int:
    prime_chars: tuple[Literal['2', '3', '5', '7', 'B', 'D'], ...] = ('2', '3', '5', '7', 'B', 'D')
    count_prime: int = 0
    position: int = 0
    length: int = len(input_string)
    while position < length:
        char = input_string[position]
        if char in prime_chars:
            count_prime += 1
        position += 1
    return count_prime