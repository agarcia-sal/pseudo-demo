from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    chars_in_zero: Set[str] = set()
    index: int = 0
    while index < len(string_zero):
        chars_in_zero.add(string_zero[index])
        index += 1

    chars_in_one: Set[str] = set()
    position: int = 0
    while position < len(string_one):
        chars_in_one.add(string_one[position])
        position += 1

    if chars_in_zero.issuperset(chars_in_one) and chars_in_one.issuperset(chars_in_zero):
        return True
    else:
        return False