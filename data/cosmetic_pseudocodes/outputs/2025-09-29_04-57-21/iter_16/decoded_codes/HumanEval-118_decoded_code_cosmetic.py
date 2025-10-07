from typing import Set


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    idx: int = len(word) - 2
    while idx >= 1:
        if word[idx] in vowel_set:
            if word[idx + 1] not in vowel_set and word[idx - 1] not in vowel_set:
                return word[idx]
        idx -= 1

    return ""