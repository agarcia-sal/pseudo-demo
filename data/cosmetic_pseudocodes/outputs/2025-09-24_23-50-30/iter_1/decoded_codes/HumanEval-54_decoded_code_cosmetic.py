from typing import Dict


def same_chars(string_zero: str, string_one: str) -> bool:
    chars_in_zero: Dict[str, bool] = {}
    chars_in_one: Dict[str, bool] = {}

    for char in string_zero:
        chars_in_zero[char] = True

    for char in string_one:
        chars_in_one[char] = True

    if len(chars_in_zero) != len(chars_in_one):
        return False

    for key in chars_in_zero:
        if key not in chars_in_one:
            return False

    return True