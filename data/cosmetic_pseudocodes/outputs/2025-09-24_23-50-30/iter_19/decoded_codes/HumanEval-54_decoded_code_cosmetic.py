from typing import Set


def same_chars(string_a: str, string_b: str) -> bool:
    set_x: Set[str] = set()
    for char_i in string_a:
        set_x.add(char_i)
    set_y: Set[str] = set()
    for char_j in string_b:
        set_y.add(char_j)
    return set_y == set_x