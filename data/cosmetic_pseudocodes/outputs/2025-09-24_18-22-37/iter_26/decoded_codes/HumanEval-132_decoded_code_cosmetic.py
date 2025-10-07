from typing import List

def is_nested(inputString: str) -> bool:
    leftIndices: List[int] = []
    rightIndices: List[int] = []

    pointer: int = 0
    strLen: int = len(inputString)
    while pointer < strLen:
        currentChar: str = inputString[pointer]
        if currentChar == '[':
            leftIndices.append(pointer)
        else:
            rightIndices.append(pointer)
        pointer += 1

    rightIndices.reverse()

    leftCount: int = 0
    rightPos: int = 0
    rightLen: int = len(rightIndices)

    idxIter: int = 0
    while idxIter < len(leftIndices):
        leftVal: int = leftIndices[idxIter]

        if rightPos < rightLen and leftVal < rightIndices[rightPos]:
            leftCount += 1
            rightPos += 1

        idxIter += 1

    return leftCount >= 2