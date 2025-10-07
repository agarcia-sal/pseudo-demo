from typing import List


def is_nested(inputString: str) -> bool:
    startIndices: List[int] = []
    endIndices: List[int] = []
    for pos in range(len(inputString)):
        if inputString[pos] == '[':
            startIndices.append(pos)
        else:
            endIndices.append(pos)
    endIndices.reverse()

    nestedCount: int = 0
    currentPos: int = 0
    endLength: int = len(endIndices)

    for startIndex in startIndices:
        if currentPos < endLength and startIndex < endIndices[currentPos]:
            nestedCount += 1
            currentPos += 1

    return nestedCount >= 2