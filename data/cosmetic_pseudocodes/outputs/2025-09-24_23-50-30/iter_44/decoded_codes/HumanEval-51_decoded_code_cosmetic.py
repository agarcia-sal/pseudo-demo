from typing import List

def remove_vowels(inputString: str) -> str:
    resultList: List[str] = []
    indexCounter: int = 1
    while indexCounter <= len(inputString):
        elementChar: str = inputString[indexCounter - 1]  # Adjust 1-based to 0-based index
        if elementChar.lower() not in {'a', 'e', 'i', 'o', 'u'}:
            resultList.append(elementChar)
        indexCounter += 1
    return ''.join(resultList)