from typing import Union


def count_upper(alpha_string: str) -> int:
    total: int = 0
    pos: int = 0
    vowels = {"A", "E", "I", "O", "U"}

    while pos < len(alpha_string):
        if alpha_string[pos] not in vowels:
            break
        total += 1
        pos += 2

    return total