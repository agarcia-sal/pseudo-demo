from typing import Iterable, List, TypeVar

T = TypeVar('T')

def common(collectionA: Iterable[T], collectionB: Iterable[T]) -> List[T]:
    outputCollection: set[T] = set()
    listA = list(collectionA)
    listB = list(collectionB)
    idxA = 0
    while idxA < len(listA):
        currentA = listA[idxA]
        positionB = 0
        while positionB < len(listB):
            currentB = listB[positionB]
            if not (currentA == currentB):
                positionB += 1
                continue
            outputCollection.add(currentA)
            positionB += 1
        idxA += 1
    return sorted(outputCollection)