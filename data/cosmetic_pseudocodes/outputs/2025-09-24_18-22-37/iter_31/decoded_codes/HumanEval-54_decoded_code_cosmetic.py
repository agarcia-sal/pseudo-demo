from typing import Set

def same_chars(str_a: str, str_b: str) -> bool:
    set_x: Set[str] = set()
    set_y: Set[str] = set()

    for each_char in str_a:
        set_x.add(each_char)

    for each_char in str_b:
        set_y.add(each_char)

    return set_x == set_y