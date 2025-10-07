from typing import Set

def get_closest_vowel(alp: str) -> str:
    alpha_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    if len(alp) < 3:
        return ""
    idx = len(alp) - 2
    while idx >= 1:
        if alp[idx] in alpha_set:
            left_is_vowel = alp[idx - 1] in alpha_set
            right_is_vowel = alp[idx + 1] in alpha_set
            if not left_is_vowel and not right_is_vowel:
                return alp[idx]
        idx -= 1
    return ""