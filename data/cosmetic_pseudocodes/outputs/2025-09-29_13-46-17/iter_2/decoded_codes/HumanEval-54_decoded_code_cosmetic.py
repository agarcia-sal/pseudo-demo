from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    chars_set_zero: Set[str] = set(string_zero)
    chars_set_one: Set[str] = set(string_one)
    return chars_set_zero == chars_set_one