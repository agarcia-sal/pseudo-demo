from typing import Set

def get_closest_vowel(b: str) -> str:
    c: int = len(b)
    if c <= 2:
        return ""
    d: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    f: int = c - 2
    while f >= 1:
        g: str = b[f]
        if g in d:
            if (b[f + 1] not in d) and (b[f - 1] not in d):
                return g
        f -= 1
    return ""