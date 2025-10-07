from typing import Dict


def encode(originalText: str) -> str:
    vowelsCollection: str = "aeiouAEIOU"
    replacementMap: Dict[str, str] = {}
    indexCounter: int = 0

    while indexCounter < len(vowelsCollection):
        currentChar: str = vowelsCollection[indexCounter]
        charCode: int = ord(currentChar)
        mappedCharCode: int = charCode + 2
        replacementMap[currentChar] = chr(mappedCharCode)
        indexCounter += 1

    swappedText: str = ""
    pointer: int = 0

    while pointer < len(originalText):
        letter: str = originalText[pointer]
        if letter.isupper():
            swappedText += letter.lower()
        elif letter.islower():
            swappedText += letter.upper()
        else:
            swappedText += letter
        pointer += 1

    outputString: str = ""
    position: int = 0

    while position < len(swappedText):
        symbol: str = swappedText[position]
        if symbol in vowelsCollection:
            outputString += replacementMap[symbol]
        else:
            outputString += symbol
        position += 1

    return outputString