from typing import Set


def same_chars(string_alpha: str, string_beta: str) -> bool:
    set_x: Set[str] = set()
    set_y: Set[str] = set()

    for char_p in string_alpha:
        set_x.add(char_p)
    for char_q in string_beta:
        set_y.add(char_q)

    return not (set_x - set_y) and not (set_y - set_x)