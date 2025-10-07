from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowel_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    pos: int = len(word) - 2
    while pos >= 1:
        if word[pos] in vowel_set:
            if word[pos + 1] not in vowel_set and word[pos - 1] not in vowel_set:
                return word[pos]
        pos -= 1
    return ""