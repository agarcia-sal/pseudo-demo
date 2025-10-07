from typing import Literal


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels_collection = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    pos = len(word) - 2
    while pos >= 1:
        current_char = word[pos]
        if current_char in vowels_collection:
            next_char = word[pos + 1]
            prev_char = word[pos - 1]
            if not (next_char in vowels_collection or prev_char in vowels_collection):
                return current_char
        pos -= 1

    return ""