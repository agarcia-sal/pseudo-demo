from typing import Tuple

def hex_key(input_str: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    accumulator: int = 0
    cursor: int = 0
    while True:
        if cursor > len(input_str) - 1:
            break
        current_char: str = input_str[cursor]
        if current_char in prime_chars:
            accumulator += 1
        cursor += 1
    return accumulator