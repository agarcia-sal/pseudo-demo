from typing import List, TypeVar

T = TypeVar('T')

def common(arrayA: List[T], arrayB: List[T]) -> List[T]:
    intersectionHolds = set()
    idxOuter = 0
    while idxOuter < len(arrayA):
        valueOuter = arrayA[idxOuter]
        idxInner = 0
        while idxInner < len(arrayB):
            valueInner = arrayB[idxInner]
            # Emulating switch-case for equality check
            if valueOuter == valueInner:
                intersectionHolds.add(valueOuter)
            idxInner += 1
        idxOuter += 1
    tempList = list(intersectionHolds)
    sortedList: List[T] = []
    pos = 0
    while pos < len(tempList):
        sortedList.append(tempList[pos])
        pos += 1
    sortedList.sort()
    return sortedList