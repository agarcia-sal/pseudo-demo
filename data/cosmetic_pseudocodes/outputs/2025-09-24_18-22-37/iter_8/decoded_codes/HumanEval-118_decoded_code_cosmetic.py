from typing import Set


def get_closest_vowel(inputStr: str) -> str:
    resultString: str = ""
    isValidLength: bool = len(inputStr) >= 3

    if not isValidLength:
        return resultString

    vowelSet: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    currentPos: int = len(inputStr) - 2
    while currentPos > 0:
        currentChar: str = inputStr[currentPos]
        if currentChar in vowelSet:
            prevChar: str = inputStr[currentPos - 1]
            nextChar: str = inputStr[currentPos + 1]
            if (prevChar not in vowelSet) and (nextChar not in vowelSet):
                resultString = currentChar
                return resultString
        currentPos -= 1

    return resultString