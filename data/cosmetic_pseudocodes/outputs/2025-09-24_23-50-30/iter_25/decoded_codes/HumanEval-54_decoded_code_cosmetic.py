from typing import Set

def same_chars(str_a: str, str_b: str) -> bool:
    set_x: Set[str] = set(str_a)
    set_y: Set[str] = set(str_b)
    return set_x == set_y