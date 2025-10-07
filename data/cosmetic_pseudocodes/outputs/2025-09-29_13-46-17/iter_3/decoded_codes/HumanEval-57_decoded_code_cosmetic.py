from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...

def monotonic(listOfElements: List[T]) -> bool:
    def checkAscending(elements: List[T], index: int) -> bool:
        if index >= len(elements) - 1:
            return True
        if elements[index] > elements[index + 1]:
            return False
        return checkAscending(elements, index + 1)

    def checkDescending(elements: List[T], idx: int) -> bool:
        if idx >= len(elements) - 1:
            return True
        if elements[idx] < elements[idx + 1]:
            return False
        return checkDescending(elements, idx + 1)

    return checkAscending(listOfElements, 0) or checkDescending(listOfElements, 0)