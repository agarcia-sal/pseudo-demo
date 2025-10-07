from typing import List


def is_nested(inputString: str) -> bool:
    leftPositions: List[int] = []
    rightPositions: List[int] = []
    i: int = 0

    while i < len(inputString):
        if inputString[i] == '[':
            leftPositions.append(i)
        else:
            rightPositions.append(i)
        i += 1

    reversedRightPositions: List[int] = []
    j: int = len(rightPositions) - 1
    while j >= 0:
        reversedRightPositions.append(rightPositions[j])
        j -= 1

    matchedCount: int = 0
    posIndex: int = 0
    rightLen: int = len(reversedRightPositions)
    for leftPos in leftPositions:
        if not (posIndex >= rightLen or leftPos >= reversedRightPositions[posIndex]):
            matchedCount += 1
            posIndex += 1

    return matchedCount >= 2