from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    collected = set()
    outerIndex = 0
    while outerIndex < len(list1):
        outerItem = list1[outerIndex]
        innerIndex = 0
        while innerIndex < len(list2):
            innerItem = list2[innerIndex]
            if outerItem == innerItem:
                collected.add(outerItem)
            innerIndex += 1
        outerIndex += 1
    sortedOutput = sorted(collected)
    return sortedOutput