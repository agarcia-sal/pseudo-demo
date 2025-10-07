from typing import Set

def same_chars(s0: str, s1: str) -> bool:
    set_s0: Set[str] = set()
    for character in s0:
        set_s0.add(character)
    set_s1: Set[str] = set()
    for character in s1:
        set_s1.add(character)
    if set_s0 == set_s1:
        return True
    else:
        return False