from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    set_alpha: Set[str] = set()
    set_beta: Set[str] = set()
    index_x: int = 0
    while index_x < len(string_zero):
        set_alpha.add(string_zero[index_x])
        index_x += 1
    index_y: int = 0
    while index_y < len(string_one):
        set_beta.add(string_one[index_y])
        index_y += 1
    if set_alpha == set_beta:
        return True
    else:
        return False