from typing import Dict


def encode(inputStr: str) -> str:
    vowelsCollection: str = "aeiouAEIOU"
    mappingDict: Dict[str, str] = {}
    idx: int = 1
    while True:
        if idx > len(vowelsCollection):
            break
        currentChar: str = vowelsCollection[idx - 1]
        replacementChar: str = chr(ord(currentChar) + 2)
        mappingDict[currentChar] = replacementChar
        idx += 1

    toggledStr: str = ""
    position: int = 0
    strLength: int = len(inputStr)

    while position < strLength:
        currentChar: str = inputStr[position]
        if 'a' <= currentChar <= 'z':
            toggledStr += currentChar.upper()
        elif 'A' <= currentChar <= 'Z':
            toggledStr += currentChar.lower()
        else:
            toggledStr += currentChar
        position += 1

    finalResult: str = ""
    for letter in toggledStr:
        if letter in mappingDict:
            finalResult += mappingDict[letter]
        else:
            finalResult += letter

    return finalResult