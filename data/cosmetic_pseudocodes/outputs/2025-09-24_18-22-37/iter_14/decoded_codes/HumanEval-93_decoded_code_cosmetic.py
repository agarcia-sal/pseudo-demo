from typing import Dict

def encode(inputStr: str) -> str:
    vowelSet: str = "AEIOUa e i o u"
    cipherMap: Dict[str, str] = {}
    indexCounter: int = 0
    while indexCounter < len(vowelSet):
        currentChar: str = vowelSet[indexCounter]
        charCode: int = ord(currentChar)
        shiftedCharCode: int = charCode + 2
        cipherMap[currentChar] = chr(shiftedCharCode)
        indexCounter += 1

    swappedStr: str = ""
    pos: int = 0
    while pos < len(inputStr):
        ch: str = inputStr[pos]
        if ch.islower():
            tempChar: str = ch.upper()
        elif ch.isupper():
            tempChar = ch.lower()
        else:
            tempChar = ch
        swappedStr += tempChar
        pos += 1

    resultStr: str = ""
    idx: int = 0
    while idx < len(swappedStr):
        currentChar = swappedStr[idx]
        if currentChar in cipherMap:
            resultStr += cipherMap[currentChar]
        else:
            resultStr += currentChar
        idx += 1

    return resultStr