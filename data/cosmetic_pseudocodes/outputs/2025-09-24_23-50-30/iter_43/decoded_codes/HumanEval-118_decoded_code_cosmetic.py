from typing import Literal

def get_closest_vowel(b1: str) -> str:
    if len(b1) < 3:
        return ""
    vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    idx = len(b1) - 2
    while idx >= 1:
        if b1[idx] in vowels:
            if (b1[idx + 1] not in vowels) and (b1[idx - 1] not in vowels):
                return b1[idx]
        idx -= 1
    return ""