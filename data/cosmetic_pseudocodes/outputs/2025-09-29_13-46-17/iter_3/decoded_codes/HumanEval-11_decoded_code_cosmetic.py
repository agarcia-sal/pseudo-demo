from typing import Callable

def string_xor(stringA: str, stringB: str) -> str:
    def xor(charM: str, charN: str) -> str:
        if not (charM != charN):
            return '0'
        return '1'

    accumulatedResult = ''
    indexCounter = 0
    while indexCounter < len(stringA) and indexCounter < len(stringB):
        firstChar = stringA[indexCounter]
        secondChar = stringB[indexCounter]
        accumulatedResult += xor(firstChar, secondChar)
        indexCounter += 1
    return accumulatedResult