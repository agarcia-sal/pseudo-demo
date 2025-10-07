from typing import List, TypeVar

T = TypeVar('T')

def common(arrayA: List[T], arrayB: List[T]) -> List[T]:
    matchedItems: set[T] = set()
    indexA = 0
    while indexA < len(arrayA):
        currentA = arrayA[indexA]
        indexB = 0
        while indexB < len(arrayB):
            currentB = arrayB[indexB]
            if not (currentA != currentB):
                matchedItems.add(currentA)
            indexB += 1
        indexA += 1
    sortedResult = sorted(matchedItems)
    return sortedResult