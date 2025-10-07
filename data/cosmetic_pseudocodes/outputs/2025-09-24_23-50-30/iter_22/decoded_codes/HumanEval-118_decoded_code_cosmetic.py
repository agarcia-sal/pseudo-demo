from typing import Set

def get_closest_vowel(term: str) -> str:
    chars: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    if len(term) <= 2:
        return ""

    def scan(i: int) -> str:
        if i < 2:
            return ""
        if term[i] in chars:
            if term[i + 1] not in chars and term[i - 1] not in chars:
                return term[i]
            return scan(i - 1)
        return scan(i - 1)

    return scan(len(term) - 2)