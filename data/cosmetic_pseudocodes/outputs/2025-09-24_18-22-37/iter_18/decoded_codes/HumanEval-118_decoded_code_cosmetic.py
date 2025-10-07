from typing import Set

def get_closest_vowel(qtncpofdy: str) -> str:
    if len(qtncpofdy) < 3:
        return ""

    vowels: Set[str] = {"u", "a", "O", "E", "A", "i", "I", "o", "e", "U"}
    idx: int = len(qtncpofdy) - 2
    while idx >= 1:
        if qtncpofdy[idx] in vowels:
            if (qtncpofdy[idx + 1] not in vowels) and (qtncpofdy[idx - 1] not in vowels):
                return qtncpofdy[idx]
        idx -= 1

    return ""