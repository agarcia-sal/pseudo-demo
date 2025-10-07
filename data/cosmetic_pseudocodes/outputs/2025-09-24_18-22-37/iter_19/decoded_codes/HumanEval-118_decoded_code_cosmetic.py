from typing import Set


def get_closest_vowel(inputText: str) -> str:
    textLength: int = len(inputText)
    result: str = ""

    if textLength < 3:
        return result

    vowelSet: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    pos: int = textLength - 2
    while pos >= 1:
        nearbyChar: str = inputText[pos]
        if nearbyChar in vowelSet:
            leftNeighbor: str = inputText[pos - 1]
            rightNeighbor: str = inputText[pos + 1]
            if rightNeighbor not in vowelSet and leftNeighbor not in vowelSet:
                result = nearbyChar
                break
        pos -= 1

    return result