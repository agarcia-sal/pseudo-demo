from typing import Literal


def get_closest_vowel(input_word: str) -> str:
    if len(input_word) < 3:
        return ""

    vowels_set: set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    pos: int = len(input_word) - 2

    while pos >= 1:
        current_char = input_word[pos]
        if current_char in vowels_set:
            next_char = input_word[pos + 1]
            prev_char = input_word[pos - 1]
            if next_char not in vowels_set and prev_char not in vowels_set:
                return current_char
        pos -= 1

    return ""