from typing import List

def remove_vowels(inputString: str) -> str:
    resultString: str = ""
    positionIndex: int = 0
    lengthOfInput: int = len(inputString)
    vowelsSet: List[str] = ["a", "e", "i", "o", "u"]

    while positionIndex < lengthOfInput:
        currentCharacter: str = inputString[positionIndex]
        currentLower: str = currentCharacter.lower()

        if currentLower not in vowelsSet:
            resultString += currentCharacter

        positionIndex += 1

    return resultString