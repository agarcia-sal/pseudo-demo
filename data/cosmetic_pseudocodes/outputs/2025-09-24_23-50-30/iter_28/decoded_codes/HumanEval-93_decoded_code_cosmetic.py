from typing import Dict

def encode(inputStr: str) -> str:
    vowelCollection: list[str] = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    def shiftChar(c: str) -> str:
        return chr(ord(c) + 2)

    shiftedVowelsMap: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowelCollection):
        ch = vowelCollection[idx]
        shiftedVowelsMap[ch] = shiftChar(ch)
        idx += 1

    swappedStr: str = ""
    i: int = 0
    while i < len(inputStr):
        currChar = inputStr[i]
        isUpper: bool = "A" <= currChar <= "Z"
        isLower: bool = "a" <= currChar <= "z"
        if isUpper or isLower:
            swappedChar = currChar.lower() if isUpper else currChar.upper()
        else:
            swappedChar = currChar
        swappedStr += swappedChar
        i += 1

    result: str = ""
    j: int = 0
    while j < len(swappedStr):
        symbol = swappedStr[j]
        if symbol in shiftedVowelsMap:
            result += shiftedVowelsMap[symbol]
        else:
            result += symbol
        j += 1

    return result