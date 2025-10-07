from typing import Set


def get_closest_vowel(string: str) -> str:
    result: str = ""

    if len(string) < 3:
        return result

    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    pos: int = len(string) - 2
    while pos >= 1:
        if string[pos] in vowel_set:
            cond1: bool = string[pos + 1] not in vowel_set
            cond2: bool = string[pos - 1] not in vowel_set
            if cond1 and cond2:
                result = string[pos]
                return result
        pos -= 1

    return result