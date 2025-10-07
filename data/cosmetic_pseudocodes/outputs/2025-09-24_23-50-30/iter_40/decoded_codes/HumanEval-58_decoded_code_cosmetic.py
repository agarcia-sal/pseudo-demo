from typing import Iterable, List, TypeVar

T = TypeVar('T')

def common(containerA: Iterable[T], containerB: Iterable[T]) -> List[T]:
    uniqueElements: dict[T, bool] = {}
    listA = list(containerA)
    listB = list(containerB)
    idxA = 0
    while idxA < len(listA):
        idxB = 0
        while idxB < len(listB):
            if listA[idxA] == listB[idxB]:
                uniqueElements[listA[idxA]] = True
            idxB += 1
        idxA += 1
    resultList = list(uniqueElements.keys())
    resultList.sort()
    return resultList