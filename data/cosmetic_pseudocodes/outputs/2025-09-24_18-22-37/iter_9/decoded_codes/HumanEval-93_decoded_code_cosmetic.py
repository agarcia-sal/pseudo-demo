from typing import Dict

def encode(inputString: str) -> str:
    vowelChars: str = "aeiouAEIOU"
    mappingDict: Dict[str, str] = {}
    for char in vowelChars:
        newCharCode = ord(char) + 2
        mappingDict[char] = chr(newCharCode)

    toggledString = []
    for symbol in inputString:
        if symbol.isupper():
            toggledString.append(symbol.lower())
        elif symbol.islower():
            toggledString.append(symbol.upper())
        else:
            toggledString.append(symbol)
    toggledStringStr = ''.join(toggledString)

    resultString = []
    for elem in toggledStringStr:
        if elem in mappingDict:
            resultString.append(mappingDict[elem])
        else:
            resultString.append(elem)

    return ''.join(resultString)