from typing import Iterator, Optional, List

def next_smallest(listOfIntegers: List[int]) -> Optional[int]:
    def helper(currentIndex: int, elementsIterator: Iterator[int]) -> Optional[int]:
        try:
            if currentIndex > 1:
                return None
            element = next(elementsIterator)
        except StopIteration:
            return None
        if currentIndex == 1:
            return element
        return helper(currentIndex + 1, elementsIterator)

    uniqueElementsSet = set(listOfIntegers)
    sortedUniqueList = sorted(uniqueElementsSet)
    iterator = iter(sortedUniqueList)
    resultValue = helper(0, iterator)
    return resultValue