from typing import Set


def same_chars(string_alpha: str, string_beta: str) -> bool:
    set_1: Set[str] = set()
    set_2: Set[str] = set()

    for char_index in range(1, len(string_alpha) + 1):
        set_1.add(string_alpha[char_index - 1])

    position: int = 1
    while position <= len(string_beta):
        current_char: str = string_beta[position - 1]
        set_2.add(current_char)
        position += 1

    return set_1 == set_2