from typing import Set


def get_closest_vowel(text: str) -> str:
    result_string: str = ""
    chars: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    total_length: int = len(text)

    if total_length < 3:
        return result_string

    pos = total_length - 2
    while pos > 0:
        current_char = text[pos]
        if current_char in chars:
            next_char = text[pos + 1]
            prev_char = text[pos - 1]
            if (next_char not in chars) and (prev_char not in chars):
                result_string = current_char
                return result_string
        pos -= 1

    return result_string