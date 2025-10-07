from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    chars_in_first: Set[str] = set(string_zero)
    chars_in_second: Set[str] = set(string_one)
    return chars_in_first == chars_in_second