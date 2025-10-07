from typing import Dict, Set


def encode(inputText: str) -> str:
    vowelSet: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    replacementMap: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in vowelSet}

    swappedText = []
    for currentChar in inputText:
        if currentChar.islower():
            flippedChar = currentChar.upper()
        elif currentChar.isupper():
            flippedChar = currentChar.lower()
        else:
            flippedChar = currentChar
        swappedText.append(flippedChar)

    transformedText = []
    for sym in swappedText:
        if sym in vowelSet:
            transformedText.append(replacementMap[sym])
        else:
            transformedText.append(sym)

    return ''.join(transformedText)