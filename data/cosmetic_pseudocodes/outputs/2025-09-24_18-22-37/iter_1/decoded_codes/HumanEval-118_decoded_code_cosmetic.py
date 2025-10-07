from typing import Set


def get_closest_vowel(word: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    if len(word) < 3:
        return ""

    # Iterate backward from second last to index 1 (inclusive)
    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        if current_char in vowels:
            left_char = word[i - 1]
            right_char = word[i + 1]
            if left_char not in vowels and right_char not in vowels:
                return current_char

    return ""