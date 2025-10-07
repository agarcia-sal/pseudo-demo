from typing import Dict


def get_closest_vowel(word: str) -> str:
    vowels_map: Dict[str, bool] = {
        "a": True, "e": True, "i": True, "o": True, "u": True,
        "A": True, "E": True, "I": True, "O": True, "U": True,
    }

    if len(word) < 3:
        return ""

    idx: int = len(word) - 2

    while idx >= 1:
        if vowels_map.get(word[idx], False):
            if not vowels_map.get(word[idx + 1], False) and not vowels_map.get(word[idx - 1], False):
                return word[idx]
        idx -= 1

    return ""