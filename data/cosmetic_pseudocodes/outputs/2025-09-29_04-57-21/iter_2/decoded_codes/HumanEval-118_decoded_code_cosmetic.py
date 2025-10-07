from typing import Set

def get_closest_vowel(term: str) -> str:
    if len(term) < 3:
        return ""
    vowel_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    pos: int = len(term) - 2
    while pos >= 1:
        if term[pos] in vowel_set:
            if term[pos + 1] not in vowel_set and term[pos - 1] not in vowel_set:
                return term[pos]
        pos -= 1
    return ""