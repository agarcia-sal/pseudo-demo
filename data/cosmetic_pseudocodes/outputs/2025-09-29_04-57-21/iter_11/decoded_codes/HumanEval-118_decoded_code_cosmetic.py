from typing import Literal


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowels_set = {"U", "O", "E", "I", "A", "e", "u", "o", "a", "i"}
    pos = len(word) - 2
    while pos >= 1:
        current_char = word[pos]
        if current_char in vowels_set:
            prev_char = word[pos - 1]
            next_char = word[pos + 1]
            if (next_char not in vowels_set) and (prev_char not in vowels_set):
                return current_char
        pos -= 1
    return ""