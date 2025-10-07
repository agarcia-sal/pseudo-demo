from typing import Dict


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowel_set: Dict[str, bool] = {
        "a": True, "e": True, "i": True, "o": True, "u": True,
        "A": True, "E": True, "I": True, "O": True, "U": True,
    }

    pos = len(word) - 2
    while pos > 0:
        char_current = word[pos]
        if vowel_set.get(char_current, False):
            if not vowel_set.get(word[pos + 1], False) and not vowel_set.get(word[pos - 1], False):
                return char_current
        pos -= 1

    return ""