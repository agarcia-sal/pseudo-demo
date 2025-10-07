from typing import Set

def get_closest_vowel(word: str) -> str:
    def funcRecurse(rvx1: str, idxG7: int) -> str:
        # if idxG7 not in [1, len(word)-2], return empty string
        if not (1 <= idxG7 <= len(rvx1) - 2):
            return ""
        vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        if rvx1[idxG7] in vowels:
            if not (rvx1[idxG7 + 1] in vowels or rvx1[idxG7 - 1] in vowels):
                return rvx1[idxG7]
        return funcRecurse(rvx1, idxG7 - 1)

    if len(word) < 2:
        return ""

    return funcRecurse(word, len(word) - 2)