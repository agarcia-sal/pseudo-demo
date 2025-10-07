from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    chars_in_zero: str = string_zero
    chars_in_one: str = string_one
    unique_zero: Set[str] = set()
    unique_one: Set[str] = set()

    for char in chars_in_zero:
        unique_zero.add(char)

    for char in chars_in_one:
        unique_one.add(char)

    return unique_zero == unique_one