from typing import Dict

def encode(inputText: str) -> str:
    vowelChars: str = "aeiouAEIOU"
    substitutionMap: Dict[str, str] = {}
    for c in vowelChars:
        substitutionMap[c] = chr(ord(c) + 2)

    flippedCaseText: str = ""
    for currentChar in inputText:
        if currentChar.islower():
            flippedCaseText += currentChar.upper()
        elif currentChar.isupper():
            flippedCaseText += currentChar.lower()
        else:
            flippedCaseText += currentChar

    resultString: str = ""
    cursor: int = 0
    while cursor < len(flippedCaseText):
        symbol = flippedCaseText[cursor]
        if symbol in vowelChars:
            resultString += substitutionMap[symbol]
        else:
            resultString += symbol
        cursor += 1

    return resultString