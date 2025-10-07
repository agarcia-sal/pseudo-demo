from typing import Set


def same_chars(str_a: str, str_b: str) -> bool:
    set_a: Set[str] = set()
    set_b: Set[str] = set()

    for char_x in str_a:
        set_a.add(char_x)

    for char_y in str_b:
        set_b.add(char_y)

    return not (set_a != set_b)