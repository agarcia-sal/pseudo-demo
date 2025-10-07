from typing import Set


def get_closest_vowel(strng: str) -> str:
    if len(strng) < 3:
        return ""

    chars: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    pos: int = len(strng) - 2
    while pos >= 1:
        c = strng[pos]
        if c in chars:
            if strng[pos + 1] not in chars and strng[pos - 1] not in chars:
                return c
        pos -= 1

    return ""