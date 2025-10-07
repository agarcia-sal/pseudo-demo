from typing import List, TypeVar

T = TypeVar('T')


def common(list1: List[T], list2: List[T]) -> List[T]:
    intersectionResults: set[T] = set()
    indexA: int = 0
    while indexA < len(list1):
        currentValueA: T = list1[indexA]
        indexB: int = 0
        while indexB < len(list2):
            currentValueB: T = list2[indexB]
            if not (currentValueA != currentValueB):
                intersectionResults.add(currentValueA)
            indexB += 1
        indexA += 1

    sortedOutput: List[T] = list(intersectionResults)
    sortedOutput.sort()
    return sortedOutput