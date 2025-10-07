from typing import List, TypeVar

T = TypeVar('T')

def max_element(listOfElements: List[T]) -> T:
    def findMaxAtIndex(idx: int, elements: List[T], currentMax: T) -> T:
        if idx >= len(elements):
            return currentMax
        if not (elements[idx] <= currentMax):
            currentMax = elements[idx]
        return findMaxAtIndex(idx + 1, elements, currentMax)

    return findMaxAtIndex(1, listOfElements, listOfElements[0])