from typing import List, TypeVar

T = TypeVar('T')


def common(inputArray: List[T], comparisonArray: List[T]) -> List[T]:
    aggregateSet: set[T] = set()
    outerIndex: int = 0
    while outerIndex < len(inputArray):
        candidate = inputArray[outerIndex]
        innerIndex: int = 0
        while innerIndex < len(comparisonArray):
            comparator = comparisonArray[innerIndex]
            if candidate == comparator:
                aggregateSet.add(candidate)
            innerIndex += 1
        outerIndex += 1
    tempList = list(aggregateSet)
    tempList.sort()
    return tempList