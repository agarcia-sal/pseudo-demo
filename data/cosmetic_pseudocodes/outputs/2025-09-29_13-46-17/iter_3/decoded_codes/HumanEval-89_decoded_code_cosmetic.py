from typing import Callable

def encrypt(inputString: str) -> str:
    resultString: str = ""
    alpha: str = "abcdefghijklmnopqrstuvwxyz"

    def process(index: int) -> str:
        nonlocal resultString
        if index >= len(inputString):
            return resultString

        currentChar: str = inputString[index]
        position: int = alpha.find(currentChar)

        if position != -1:
            newPos: int = ((position + 2) * 2) % 26
            resultString += alpha[newPos]
        else:
            resultString += currentChar

        return process(index + 1)

    return process(0)