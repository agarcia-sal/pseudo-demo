from typing import Union


def hex_key(string_num: str) -> int:
    prime_set: tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    accumulator: int = 0
    position: int = 0
    while True:
        if position > len(string_num) - 1:
            break
        current_char: str = string_num[position]
        # Only increment accumulator if current_char in prime_set
        if current_char in prime_set:
            accumulator += 1
        position += 1
    return accumulator