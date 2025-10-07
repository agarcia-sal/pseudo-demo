from typing import Set


def get_closest_vowel(inputstr: str) -> str:
    if len(inputstr) < 3:
        return ""

    charset: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    # Iterate from length-2 down to 1 inclusive
    for pointer in range(len(inputstr) - 2, 0, -1):
        if inputstr[pointer] in charset:
            if (inputstr[pointer + 1] not in charset) and (inputstr[pointer - 1] not in charset):
                return inputstr[pointer]

    return ""