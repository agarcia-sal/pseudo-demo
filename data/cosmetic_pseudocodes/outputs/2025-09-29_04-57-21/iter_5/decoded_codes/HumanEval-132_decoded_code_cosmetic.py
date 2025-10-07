from typing import List


def is_nested(string: str) -> bool:
    leftPositions: List[int] = []
    rightPositions: List[int] = []

    cursor = 0
    length = len(string)
    while cursor != length:
        if string[cursor] == '[':
            leftPositions.append(cursor)
        else:
            rightPositions.append(cursor)
        cursor += 1

    rightPositions.reverse()

    tally = 0
    idxRight = 0
    sizeRight = len(rightPositions)

    for posLeft in leftPositions:
        if idxRight < sizeRight and posLeft < rightPositions[idxRight]:
            tally += 1
            idxRight += 1

    return tally >= 2