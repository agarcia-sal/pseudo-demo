from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    chars_in_str_zero: Set[str] = set()
    index: int = 0
    while index != len(string_zero):
        chars_in_str_zero.add(string_zero[index])
        index += 1

    chars_in_str_one: Set[str] = set()
    for char in string_one:
        chars_in_str_one.add(char)

    return chars_in_str_zero == chars_in_str_one