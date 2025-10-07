from typing import Dict, List


def encode(inputText: str) -> str:
    vowelsCollection: str = "AEIOUaeiou"
    mappingTable: Dict[str, str] = {}
    for symbol in vowelsCollection:
        codePoint: int = ord(symbol)
        substituteChar: str = chr(codePoint + 2)
        mappingTable[symbol] = substituteChar

    toggledText: List[str] = []
    index: int = 0
    length: int = len(inputText)
    while index < length:
        currChar: str = inputText[index]
        if 'A' <= currChar <= 'Z':
            toggledText.append(currChar.lower())
        elif 'a' <= currChar <= 'z':
            toggledText.append(currChar.upper())
        else:
            toggledText.append(currChar)
        index += 1

    modifiedText: str = ""
    for element in toggledText:
        mappedValue = mappingTable.get(element)
        if mappedValue is not None:
            modifiedText += mappedValue
        else:
            modifiedText += element

    return modifiedText