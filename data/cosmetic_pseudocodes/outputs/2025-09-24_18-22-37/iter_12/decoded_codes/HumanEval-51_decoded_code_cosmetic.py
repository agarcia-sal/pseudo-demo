from typing import List

def remove_vowels(inputString: str) -> str:
    filteredChars: List[str] = []
    for idx in range(len(inputString)):
        currentChar: str = inputString[idx]
        lowerChar: str = currentChar.lower()
        if lowerChar not in {"a", "e", "i", "o", "u"}:
            filteredChars.append(currentChar)
    resultString: str = ""
    pos: int = 0
    while pos < len(filteredChars):
        resultString += filteredChars[pos]
        pos += 1
    return resultString