from typing import Set

def same_chars(zero_str: str, one_str: str) -> bool:
    set_zero: Set[str] = set()
    set_one: Set[str] = set()

    for char in zero_str:
        set_zero.add(char)

    for char in one_str:
        set_one.add(char)

    return (set_zero - set_one) | (set_one - set_zero) == set()