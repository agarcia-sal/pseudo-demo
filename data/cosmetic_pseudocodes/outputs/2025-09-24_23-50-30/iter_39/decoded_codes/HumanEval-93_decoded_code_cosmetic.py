from typing import Dict, List

def encode(inputText: str) -> str:
    letterSet: str = "AEIOUaeiou"
    translationMap: Dict[str, str] = {}
    for char in letterSet:
        asciiVal = ord(char)
        translationMap[char] = chr(asciiVal + 2)

    def applyTranslation(items: List[str], ix: int, acc: str) -> str:
        if ix == len(items):
            return acc
        currChar = items[ix]
        swappedChar = currChar.lower() if currChar.isupper() else currChar.upper()
        replacementChar = translationMap.get(swappedChar, swappedChar)
        return applyTranslation(items, ix + 1, acc + replacementChar)

    return applyTranslation(list(inputText), 0, "")