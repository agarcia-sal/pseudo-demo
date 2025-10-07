from typing import Callable


def fix_spaces(text: str) -> str:
    def processTrailingSpaces(pendingStart: int, pendingEnd: int, outputAcc: str) -> str:
        length = pendingEnd - pendingStart
        if length > 2:
            outputAcc += "-"
        elif length > 0:
            outputAcc += "_" * length
        return outputAcc

    positionCounter: int = 0
    segmentStart: int = 0
    segmentEnd: int = 0
    transformedResult: str = ""

    while positionCounter < len(text):
        if text[positionCounter] == " ":
            segmentEnd += 1
        else:
            length = segmentEnd - segmentStart
            if length > 2:
                transformedResult += "-" + text[positionCounter]
            elif length > 0:
                transformedResult += ("_" * length) + text[positionCounter]
            else:
                transformedResult += text[positionCounter]
            segmentStart = positionCounter + 1
            segmentEnd = positionCounter + 1
        positionCounter += 1

    transformedResult = processTrailingSpaces(segmentStart, segmentEnd, transformedResult)
    return transformedResult