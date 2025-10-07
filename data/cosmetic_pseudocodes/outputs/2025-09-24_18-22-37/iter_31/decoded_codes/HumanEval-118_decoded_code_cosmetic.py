from typing import Set


def get_closest_vowel(inputStr: str) -> str:
    resultStr: str = ""
    alphaSet: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    lenVal: int = len(inputStr)

    if lenVal < 3:
        resultStr = ""
    else:
        pos: int = 1
        while pos < lenVal - 1:
            currChar: str = inputStr[pos]
            if currChar in alphaSet:
                nextChar: str = inputStr[pos + 1]
                prevChar: str = inputStr[pos - 1]
                if (nextChar not in alphaSet) and (prevChar not in alphaSet):
                    resultStr = currChar
                    break
            pos += 1

    return resultStr