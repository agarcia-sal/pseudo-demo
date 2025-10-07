from typing import Dict

def encode(text: str) -> str:
    vowelCollection: str = "aeiouAEIOU"
    shiftedMapping: Dict[str, str] = {}
    posIndex: int = 0

    while posIndex < len(vowelCollection):
        currentChar: str = vowelCollection[posIndex]
        asciiValue: int = ord(currentChar)
        incrementedValue: int = asciiValue + 2
        mappedChar: str = chr(incrementedValue)
        shiftedMapping[currentChar] = mappedChar
        posIndex += 1

    transformedText: str = ""
    idx: int = 0
    while idx < len(text):
        letter: str = text[idx]
        flippedLetter: str = letter.upper() if letter.islower() else letter.lower()
        transformedText += flippedLetter
        idx += 1

    outputString: str = ""
    i: int = 0
    while i < len(transformedText):
        currentChar: str = transformedText[i]
        if currentChar in vowelCollection:
            replacementChar: str = shiftedMapping[currentChar]
            outputString += replacementChar
        else:
            outputString += currentChar
        i += 1

    return outputString