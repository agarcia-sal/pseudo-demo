from typing import Set


def get_closest_vowel(param1: str) -> str:
    if len(param1) < 3:
        return ""

    vowels: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    param3 = len(param1) - 2

    while param3 >= 1:
        if param1[param3] in vowels:
            if (param1[param3 + 1] not in vowels) and (param1[param3 - 1] not in vowels):
                return param1[param3]
        param3 -= 1

    return ""