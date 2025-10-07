from typing import List


def solve(string_input: str) -> str:
    negateCaseFlag: int = 0
    positionCounter: int = 0
    transformedChars: List[str] = [char for char in string_input]

    while positionCounter < len(string_input):
        currentChar: str = string_input[positionCounter]

        if ('A' <= currentChar <= 'Z') or ('a' <= currentChar <= 'z'):
            if 'a' <= currentChar <= 'z':
                transformedChars[positionCounter] = currentChar.upper()
            else:
                transformedChars[positionCounter] = currentChar.lower()
            negateCaseFlag = 1

        positionCounter += 1

    assembledResult: str = ""
    arrIndex: int = 0
    while arrIndex < len(transformedChars):
        assembledResult += transformedChars[arrIndex]
        arrIndex += 1

    if negateCaseFlag == 0:
        assembledResult = assembledResult[::-1]

    return assembledResult