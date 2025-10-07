from typing import List, Set


def get_closest_vowel(term: str) -> str:
    if len(term) < 3:
        return ""

    chars: List[str] = list(term)
    entries: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    for pos in range(len(chars) - 2, 0, -1):
        if chars[pos] in entries:
            if chars[pos + 1] in entries or chars[pos - 1] in entries:
                continue
            return chars[pos]

    return ""