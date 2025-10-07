from typing import Callable

def is_happy(inputString: str) -> bool:
    if len(inputString) < 3:
        return False

    def checkPair(position: int) -> bool:
        if position > len(inputString) - 3:
            return True

        firstChar = inputString[position]
        secondChar = inputString[position + 1]
        thirdChar = inputString[position + 2]

        if firstChar == secondChar or secondChar == thirdChar or firstChar == thirdChar:
            return False

        return checkPair(position + 1)

    return checkPair(0)