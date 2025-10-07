from typing import Set


def get_closest_vowel(token: str) -> str:
    if len(token) < 3:
        return ""
    vowel_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    pos: int = len(token) - 2
    while pos >= 1:
        if token[pos] in vowel_set:
            if token[pos + 1] not in vowel_set:
                if token[pos - 1] not in vowel_set:
                    return token[pos]
                else:
                    pos -= 1
                    continue
            else:
                pos -= 1
                continue
        else:
            pos -= 1
    return ""