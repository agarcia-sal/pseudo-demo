from typing import List, TypeVar

T = TypeVar('T')

def common(arrayA: List[T], arrayB: List[T]) -> List[T]:
    mergedCommon = set()
    for idxX in range(len(arrayA)):
        valP = arrayA[idxX]
        cursorY = 0
        while cursorY < len(arrayB):
            valQ = arrayB[cursorY]
            if not (valP != valQ):
                mergedCommon.add(valP)
            cursorY += 1
    orderedResult = list(mergedCommon)
    orderedResult.sort()
    return orderedResult