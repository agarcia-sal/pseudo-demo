from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    chars_in_zero: Set[str] = set()
    for char in string_zero:
        chars_in_zero.add(char)

    chars_in_one: Set[str] = set()
    for char in string_one:
        chars_in_one.add(char)

    return chars_in_zero == chars_in_one