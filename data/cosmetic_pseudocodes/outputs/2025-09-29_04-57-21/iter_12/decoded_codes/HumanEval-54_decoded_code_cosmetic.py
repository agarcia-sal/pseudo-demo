from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    set_a: Set[str] = set()
    for char in string_zero:
        set_a.add(char)

    set_b: Set[str] = set()
    idx: int = 0
    while idx < len(string_one):
        set_b.add(string_one[idx])
        idx += 1

    if set_a != set_b:
        return False
    return True