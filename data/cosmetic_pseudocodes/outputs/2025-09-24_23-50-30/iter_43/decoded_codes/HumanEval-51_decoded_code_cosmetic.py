from typing import Set


def remove_vowels(text: str) -> str:
    vowelsSet: Set[str] = {"a", "e", "i", "o", "u"}
    newString = []
    for index in range(len(text)):
        charVar = text[index]
        normalizedChar = charVar.lower()
        if normalizedChar not in vowelsSet:
            newString.append(charVar)
    return ''.join(newString)