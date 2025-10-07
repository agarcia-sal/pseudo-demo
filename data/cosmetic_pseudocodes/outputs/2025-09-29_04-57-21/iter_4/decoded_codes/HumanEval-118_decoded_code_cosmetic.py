from typing import Set


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    position = len(word) - 2
    while position >= 1:
        current_char = word[position]
        if current_char in vowels_set:
            next_char = word[position + 1]
            prev_char = word[position - 1]
            if (next_char not in vowels_set) and (prev_char not in vowels_set):
                return current_char
        position -= 1

    return ""