from typing import Set


def get_closest_vowel(input_string: str) -> str:
    if len(input_string) < 3:
        return ""

    vowel_set: Set[str] = {"u", "E", "i", "O", "A", "a", "e", "U", "I", "o"}
    pos: int = len(input_string) - 2

    while pos >= 1:
        current_char = input_string[pos]
        if current_char in vowel_set:
            next_char = input_string[pos + 1]
            prev_char = input_string[pos - 1]
            if next_char not in vowel_set and prev_char not in vowel_set:
                return current_char
        pos -= 1

    return ""