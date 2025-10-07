from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    tempString: str = ""
    idx: int = 0
    while idx < len(string_s):
        currentChar: str = string_s[idx]
        if currentChar not in string_c:
            tempString += currentChar
        idx += 1

    reversedFlag: bool = False
    revIndex: int = len(tempString) - 1
    fwdIndex: int = 0
    isPalindrome: bool = True
    while fwdIndex < len(tempString) and isPalindrome:
        if tempString[fwdIndex] != tempString[revIndex]:
            isPalindrome = False
        fwdIndex += 1
        revIndex -= 1
    reversedFlag = isPalindrome
    return tempString, reversedFlag