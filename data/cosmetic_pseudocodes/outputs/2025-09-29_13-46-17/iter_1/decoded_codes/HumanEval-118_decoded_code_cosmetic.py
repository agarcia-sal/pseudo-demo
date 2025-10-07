from typing import Set


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    for pos in range(len(word) - 2, 0, -1):
        current_char = word[pos]
        if current_char in vowels:
            left_char = word[pos - 1]
            right_char = word[pos + 1]
            if left_char not in vowels and right_char not in vowels:
                return current_char

    return ""