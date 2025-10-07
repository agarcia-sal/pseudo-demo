from typing import List


def is_nested(inputStr: str) -> bool:
    openIndices: List[int] = []
    closeIndices: List[int] = []
    iterCount: int = 0

    while iterCount < len(inputStr):
        char = inputStr[iterCount]
        if char == '[':
            openIndices.append(iterCount)
        else:
            closeIndices.append(iterCount)
        iterCount += 1

    closeIndices.reverse()
    score: int = 0
    cursor: int = 0
    closeLen: int = len(closeIndices)

    for element in openIndices:
        if cursor < closeLen and element < closeIndices[cursor]:
            score += 1
            cursor += 1

    return score >= 2