from typing import List, TypeVar, Generic

T = TypeVar('T')

def common(listA: List[T], listB: List[T]) -> List[T]:
    intersectionStorage: set[T] = set()
    iteratorAIndex: int = 0
    while iteratorAIndex < len(listA):
        currentAItem: T = listA[iteratorAIndex]
        iteratorBIndex: int = 0
        while iteratorBIndex < len(listB):
            currentBItem: T = listB[iteratorBIndex]
            equalityCheck: bool = (currentAItem == currentBItem)
            if equalityCheck:
                intersectionStorage.add(currentAItem)
            iteratorBIndex += 1
        iteratorAIndex += 1
    sortedIntersection: List[T] = sorted(intersectionStorage)
    return sortedIntersection