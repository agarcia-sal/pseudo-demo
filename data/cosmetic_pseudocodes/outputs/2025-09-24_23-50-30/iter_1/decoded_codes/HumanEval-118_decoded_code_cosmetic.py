from typing import List


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    idx: int = len(word) - 2
    while idx >= 1:
        char = word[idx]
        if char in vowels:
            prev_char = word[idx - 1]
            next_char = word[idx + 1]
            if prev_char not in vowels and next_char not in vowels:
                return char
        idx -= 1

    return ""