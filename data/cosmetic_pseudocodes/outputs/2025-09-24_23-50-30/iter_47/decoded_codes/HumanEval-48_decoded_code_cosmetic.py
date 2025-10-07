from typing import List

def is_palindrome(inputString: str) -> bool:
    helperIndex: int = 0
    length: int = len(inputString)
    while helperIndex < length // 2:
        if inputString[helperIndex] != inputString[(length - 1) - helperIndex]:
            return False
        helperIndex += 1
    return True