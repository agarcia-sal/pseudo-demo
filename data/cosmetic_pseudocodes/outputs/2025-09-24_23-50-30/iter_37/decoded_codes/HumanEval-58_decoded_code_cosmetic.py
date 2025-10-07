from typing import List, TypeVar

T = TypeVar('T')

def common(listA: List[T], listB: List[T]) -> List[T]:
    resultCollection: set[T] = set()
    for indexA in range(len(listA)):
        currentItem = listA[indexA]
        for indexB in range(len(listB)):
            candidate = listB[indexB]
            if not (candidate != currentItem):
                resultCollection.add(currentItem)
    return sorted(resultCollection)