from typing import Dict

def encode(inputString: str) -> str:
    vowelsList: str = "aeiouAEIOU"
    vowelShiftMap: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowelsList):
        currentChar: str = vowelsList[idx]
        asciiVal: int = ord(currentChar)
        incrementedAscii: int = asciiVal + 2
        mappedChar: str = chr(incrementedAscii)
        vowelShiftMap[currentChar] = mappedChar
        idx += 1

    alteredString: str = ""
    i: int = 0
    while i < len(inputString):
        originalChar: str = inputString[i]
        asciiVal = ord(originalChar)
        if 65 <= asciiVal <= 90:
            swapChar = chr(asciiVal + 32)
        elif 97 <= asciiVal <= 122:
            swapChar = chr(asciiVal - 32)
        else:
            swapChar = originalChar
        alteredString += swapChar
        i += 1

    resultString: str = ""
    j: int = 0
    while j < len(alteredString):
        chr_ = alteredString[j]
        if chr_ in vowelShiftMap:
            resultString += vowelShiftMap[chr_]
        else:
            resultString += chr_
        j += 1

    return resultString