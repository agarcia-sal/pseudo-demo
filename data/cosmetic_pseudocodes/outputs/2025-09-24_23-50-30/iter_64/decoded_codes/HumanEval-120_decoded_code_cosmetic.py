from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')


class Comparable:
    def __lt__(self, other: 'Comparable') -> bool:
        return NotImplemented

    def __gt__(self, other: 'Comparable') -> bool:
        return NotImplemented


def SortNonDecreasing(lst: List[T]) -> None:
    lengthVar: int = len(lst)
    indexVar: int = 0

    while indexVar < lengthVar - 1:
        innerIndex: int = 0
        while innerIndex < lengthVar - indexVar - 1:
            if lst[innerIndex] > lst[innerIndex + 1]:
                tempVal: T = lst[innerIndex]
                lst[innerIndex] = lst[innerIndex + 1]
                lst[innerIndex + 1] = tempVal
            innerIndex += 1
        indexVar += 1


def maximum(freshVarA: List[T], freshVarB: int) -> List[T]:
    if freshVarB == 0:
        return []

    SortNonDecreasing(freshVarA)

    def SliceFromEnd(collection: List[T], count: int) -> List[T]:
        return collection[len(collection) - count : len(collection)]

    freshVarC: List[T] = SliceFromEnd(freshVarA, freshVarB)
    return freshVarC