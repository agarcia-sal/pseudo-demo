from typing import Callable

def get_closest_vowel(inputString: str) -> str:
    swZ: int = 1
    if not (swZ + 1 < len(inputString)):
        return ""

    xkvuj: set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    def recursiveSearch(pos: int) -> str:
        if not (pos >= 1):
            return ""
        if (inputString[pos] in xkvuj and 
            not (inputString[pos + 1] in xkvuj or inputString[pos - 1] in xkvuj)):
            return inputString[pos]
        else:
            return recursiveSearch(pos - 1)

    return recursiveSearch(len(inputString) - 2)