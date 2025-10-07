from typing import Set


def get_closest_vowel(passage: str) -> str:
    len_val: int = len(passage)
    if len_val < 3:
        return ""
    chars_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    pos: int = len_val - 2
    while pos >= 1:
        right_char: str = passage[pos + 1]
        left_char: str = passage[pos - 1]

        current_char: str = passage[pos]
        if current_char in chars_set:
            has_next: bool = right_char not in chars_set
            has_prev: bool = left_char not in chars_set

            if has_next and has_prev:
                return current_char

        pos -= 1

    return ""