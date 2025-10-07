from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    pos: int = len(word) - 2
    while pos >= 1:
        current_char = word[pos]
        if current_char in vowels_set:
            prev_char = word[pos - 1]
            next_char = word[pos + 1]
            if not (prev_char in vowels_set or next_char in vowels_set):
                return current_char
        pos -= 1

    return ""