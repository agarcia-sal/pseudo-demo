from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    unique_chars_zero: Set[str] = set()
    unique_chars_one: Set[str] = set()

    idx: int = 0
    while idx < len(string_zero):
        unique_chars_zero.add(string_zero[idx])
        idx += 1

    idx = 0
    while idx < len(string_one):
        unique_chars_one.add(string_one[idx])
        idx += 1

    if len(unique_chars_zero) != len(unique_chars_one):
        return False

    iter_zero = iter(unique_chars_zero)
    for ch in iter_zero:
        if ch not in unique_chars_one:
            return False

    return True