from typing import Set


def get_closest_vowel(alpha: str) -> str:
    if len(alpha) < 3:
        return ""
    vowels_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    pos = len(alpha) - 2
    while pos >= 1:
        curr_char = alpha[pos]
        next_char = alpha[pos + 1]
        prev_char = alpha[pos - 1]
        if curr_char in vowels_set:
            if (next_char not in vowels_set) and (prev_char not in vowels_set):
                return curr_char
        pos -= 1
    return ""