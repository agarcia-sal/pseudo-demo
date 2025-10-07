from typing import List

def get_closest_vowel(inputString: str) -> str:
    if len(inputString) < 3:
        return ""

    vowelSet: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    i: int = len(inputString) - 2
    while i >= 1:
        currentChar: str = inputString[i]
        if currentChar in vowelSet:
            nextChar: str = inputString[i + 1]
            prevChar: str = inputString[i - 1]
            if (nextChar not in vowelSet) and (prevChar not in vowelSet):
                return currentChar
        i -= 1

    return ""