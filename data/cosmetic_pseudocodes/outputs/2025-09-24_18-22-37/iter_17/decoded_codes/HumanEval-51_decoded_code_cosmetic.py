from typing import List

def remove_vowels(originalString: str) -> str:
    filteredChars: List[str] = []
    iteratorIndex: int = 0
    while iteratorIndex < len(originalString):
        currentChar: str = originalString[iteratorIndex]
        loweredChar: str = currentChar.lower()
        if loweredChar not in {'a', 'e', 'i', 'o', 'u'}:
            filteredChars.append(currentChar)
        iteratorIndex += 1

    resultString: str = ""
    concatIndex: int = 0
    while concatIndex < len(filteredChars):
        resultString += filteredChars[concatIndex]
        concatIndex += 1
    return resultString