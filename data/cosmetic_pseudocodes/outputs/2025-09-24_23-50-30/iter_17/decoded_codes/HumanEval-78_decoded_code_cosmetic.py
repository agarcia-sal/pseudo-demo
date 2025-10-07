from typing import Set


def hex_key(input_str: str) -> int:
    prime_chars: Set[str] = {'2', '3', '5', '7', 'B', 'D'}
    counter: int = 0
    position: int = 0
    while position < len(input_str):
        if input_str[position] in prime_chars:
            counter += 1
        position += 1
    return counter