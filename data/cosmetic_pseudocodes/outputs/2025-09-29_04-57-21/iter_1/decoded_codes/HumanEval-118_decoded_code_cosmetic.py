from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        prev_char = word[i - 1]
        next_char = word[i + 1]

        if current_char in vowels:
            if prev_char not in vowels and next_char not in vowels:
                return current_char

    return ""